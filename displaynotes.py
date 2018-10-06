from abjad import *
import time
from analyze import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
def getfreq(lens):
    import threading
    now = time.time()
    rec = Recorder(out_fname='test_{}.wav'.format(now), durations=lens, debug=True)

    data_queue = rec.get_queue()

    threading.Thread(target=rec.record).start()

    while True:
        print('Enter')
        data = data_queue.get()
        return data
numnotes = int(sys.argv[2])
plt.rcParams["figure.figsize"] = [20.0,9.0]
datafile = open(sys.argv[1] + '/data.csv','r')
lens = []
freqs = []
for line in datafile:
        lens.append(float(line.split(',')[0]))
        freqs.append(float(line.split(',')[1]))
def rightnote():
        print(getfreq(lens))
        print("WAS THE NOTE RIGHT?")
        return int(input())
image = mpimg.imread(sys.argv[1] + '/ground.png')
image = image[30:120,:,:]
plt.imshow(image)
plt.ion()
plt.show()
for i in range(numnotes):
        while(not rightnote()):
                image = mpimg.imread(sys.argv[1] + '/' + str(i) + 'wrong.png')
                image = image[30:120,:,:]
                #plt.imshow(image,aspect = 'auto')
                plt.imshow(image)
                plt.ion()
                plt.show()
        image = mpimg.imread(sys.argv[1] + '/' + str(i) + 'right.png')
        image = image[30:120,:,:]
        plt.imshow(image)
        plt.pause(.001)
        plt.ion()
        plt.show()
 
