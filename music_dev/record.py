import argparse
import tempfile
from queue import Queue
import sys

# import sounddevice as sd
# import soundfile as sf
import numpy as np


from threading import Thread
import traceback
import pickle
import time


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
parser.add_argument(
    '-c', '--channels', type=int, default=1, help='number of input channels')
parser.add_argument(
    'filename', nargs='?', metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
args = parser.parse_args()

try:
    import sounddevice as sd
    import soundfile as sf
    import numpy  # Make sure NumPy is loaded before it is used in the callback
    assert numpy  # avoid "imported but unused" message (W0611)

    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, 'input')
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info['default_samplerate'])
    if args.filename is None:
        args.filename = tempfile.mktemp(prefix='delme_rec_unlimited_',
                                        suffix='.wav', dir='')
    q = Queue()
    full_arr = np.array([])
    # duration = [0.5, 0.5, 0.5, 0.5, 
    #             0.5, 0.5, 1, 
    #             0.5, 0.5, 1, 
    #             0.5, 0.5, 1, 
    #             0.5, 0.5, 0.5, 0.5, 
    #             0.5, 0.5, 0.5, 0.5,
    #             0.5, 0.5, 0.5, 0.5,
    #             2]
    duration = [1, 1, 1]

    ret_arr = []

    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put((indata.copy(), time.inputBufferAdcTime))

    # Make sure the file is opened before recording anything:
    print('Start')

    with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
                      channels=args.channels, subtype=args.subtype) as file:
        with sd.InputStream(samplerate=args.samplerate, device=args.device,
                            channels=args.channels, callback=callback) as ss:
            start_time = ss.time
            next_slice_start = None
            dur_count = 0
            while True:
                np_arr, buff_time = q.get()
                # if next_slice_start is None:
                #     next_slice_start = int((buff_time-start_time)*args.samplerate)
                #     print(next_slice_start)
                file.write(np_arr)
                full_arr = np.append(full_arr, np_arr)
                # full_arr = np.append(full_arr, np_arr)
                # if full_arr.size >= int(next_slice_start+duration[dur_count]*args.samplerate+1):
                #     print()
                #     print(next_slice_start)
                #     print(int(next_slice_start+duration[dur_count]*args.samplerate))
                #     print(full_arr.size)
                #     print()
                #     ret_arr.append(full_arr[next_slice_start:int(next_slice_start+duration[dur_count]*args.samplerate)])
                #     next_slice_start = int(next_slice_start+duration[dur_count]*args.samplerate)+1
                #     dur_count+=1
                #     if dur_count == len(duration):
                #         raise KeyboardInterrupt

except KeyboardInterrupt:
    print('\nRecording finished: ' + repr(args.filename))
    with open('data.pkl', 'wb') as fopen:
        pickle.dump(full_arr, fopen)
    parser.exit(0)
except Exception as e:
    traceback.print_exc()
    parser.exit(type(e).__name__ + ': ' + str(e))


# def record(sample_rate=44100, device=None, channels=1, durations):
# 
#     def callback():
# 
#         pass
# 
#     sound_arr = np.array([])
# 
#     with sd.InputStream(samplerate=sample_rate, device=device,
#                         channels=args.channels, callback=callback,
#                         latency='low'):
#         # start recording: 3, 2, 1, Go...
#         # Mark that starting point and send blocks based on that
#         s_time = time.time()
#         while True:
#             temp_arr = q.get()
# 
#             sound_arr = np.append(q.get())
#         