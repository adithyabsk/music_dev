from abjad import *
from math import *
import time
from analyze import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
import sys
import threading
"""
def getfreq(lens):
    now = time.time()
    rec = Recorder(out_fname='test_{}.wav'.format(now), durations=lens, debug=True)

    data_queue = rec.get_queue()

    threading.Thread(target=rec.record).start()

    while True:
        print('Enter')
        data = data_queue.get()
        return data
"""

note_count = 0
# @profile
def main():
    # @profile
    def rightnote(obs, exp):
        return abs(obs - exp) < 20

    def preload_display(path, length):
        return ([mpimg.imread('{}/{}right.png'.format(path, i))[30:120,:,:] for i in range(length)],
                [mpimg.imread('{}/{}wrong.png'.format(path, i))[30:120,:,:] for i in range(length)])

    # Setup args from commandline
    numnotes = int(sys.argv[2])
    image_path = sys.argv[1]
    plt.rcParams["figure.figsize"] = [20.0,9.0]
    datafile = open(sys.argv[1] + '/data.csv','r')
    lens = []
    freqs = []
    fname = 'nolanmary.wav'
    try:
        os.remove(fname)
    except OSError:
        pass

    for line in datafile:
        lens.append(float(line.split(',')[0]))
        freqs.append(float(line.split(',')[1]))

    # Setup plot
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)

    # Pre-fetch images
    rimages, wimages = preload_display(image_path, numnotes)

    # Setup animation counter

    def animate(i):
        obs_note = data_queue.get()

        if obs_note == -1:
            time.sleep(2)
            quit()

        global note_count

        if(not rightnote(obs_note, freqs[note_count])):
            image = wimages[note_count]
        else:
            image = rimages[note_count]

        note_count+=1

        ax1.clear()
        ax1.imshow(image)

    def init_func():
        # Set up ground image
        image = mpimg.imread(sys.argv[1] + '/ground.png')[30:120,:,:]
        ax1.imshow(image)

    # Setup recorder
    rec = Recorder(out_fname=fname, durations=lens, debug=True)
    data_queue = rec.get_queue()

    # # Play "metronome"
    # for i in range(4):
    #     print("\7")
    #     time.sleep(.5)

    # Start animation and recording
    ani = animation.FuncAnimation(fig, animate, init_func=init_func, interval=100)
    threading.Thread(target=rec.record).start()
    plt.show()

if __name__ == '__main__':
    main()
     