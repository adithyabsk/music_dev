import argparse
import tempfile
from queue import Queue
import sys

import threading
import os
import pickle
import time

import sounddevice as sd
import soundfile as sf
import numpy as np

def device_list():
    return sd.query_devices()

class Recorder():
    def __init__(self, out_fname, durations, sample_rate=44100, device=None, channels=1, debug=False):
        self.out_fname = out_fname
        self.durations = durations
        self.sample_rate = sample_rate
        self.device = device
        self.channels = channels
        self.debug = debug

        self.data_queue = Queue()

    def get_queue(self):
        return self.data_queue

    def fft_analyze(self, data, rate):
        spectre = np.fft.fft(data)
        freq = np.fft.fftfreq(data.size, 1/rate)
        mask = freq > 0
        return freq[np.argmax(np.abs(spectre[mask]))]

    def record(self):
        raw_queue = Queue()
        full_arr = np.array([])
        ret_arr = []

        def callback(indata, frames, time, status):
            """Audio callback"""
            # if status:
            #     print(status, file=sys.stderr)
            raw_queue.put((indata.copy(), time.inputBufferAdcTime))

        try:
            os.remove(self.out_fname)
        except OSError:
            pass

        with sf.SoundFile(self.out_fname, mode='x', samplerate=self.sample_rate,
                          channels=self.channels, subtype=None) as file:
            with sd.InputStream(samplerate=self.sample_rate, device=self.device,
                                channels=self.channels, callback=callback) as ss:
                start_time = ss.time
                next_slice_start = None
                dur_count = 0
                while True:
                    np_arr, buff_time = raw_queue.get()
                    if next_slice_start is None:
                        next_slice_start = int((buff_time-start_time)*self.sample_rate)
                    file.write(np_arr)
                    full_arr = np.append(full_arr, np_arr)
                    if full_arr.size >= int(next_slice_start+self.durations[dur_count]*self.sample_rate+1):
                        slice_end = int(next_slice_start+self.durations[dur_count]*self.sample_rate)
                        raw_slice = full_arr[next_slice_start:slice_end]
                        freq = self.fft_analyze(raw_slice, self.sample_rate)
                        self.data_queue.put(freq)
                        if self.debug:
                            print('Note Info: ({} num) ({} dur) ({} freq)'.format(dur_count, 
                                self.durations[dur_count], freq))
                        if self.debug:
                            ret_arr.append(raw_slice)
                        next_slice_start = slice_end+1
                        dur_count+=1
                        if dur_count == len(self.durations):
                            # if self.debug:
                            #     now = time.time()
                            #     debug_file = tempfile.mktemp(prefix='debug_slices_{}_'.format(now), suffix='.pkl', dir='')
                            #     with open(debug_file, 'wb') as fopen:
                            #         pickle.dump(debug_file, fopen)
                            self.data_queue.put(-1)
                            return

if __name__ == '__main__':
    import threading

    durations = [0.5, 0.5, 0.5, 0.5, 
                0.5, 0.5, 1, 
                0.5, 0.5, 1, 
                0.5, 0.5, 1, 
                0.5, 0.5, 0.5, 0.5, 
                0.5, 0.5, 0.5, 0.5,
                0.5, 0.5, 0.5, 0.5,
                2]
    fname = 'testing.wav'
    rec = Recorder(out_fname=fname, durations=[3], debug=True)

    data_queue = rec.get_queue()

    threading.Thread(target=rec.record).start()

    while True:
        data = data_queue.get()
        print(data)
        if data == -1:
            break