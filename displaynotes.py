from abjad import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
numnotes = 29
plt.rcParams["figure.figsize"] = [20.0,9.0]
def rightnote():
        print("WAS THE NOTE RIGHT?")
        return int(input())
for i in range(numnotes):
        while(not rightnote()):
                image = mpimg.imread('possibleframes/' + str(i) + 'wrong.png')
                image = image[30:120,:,:]
                plt.imshow(image,aspect = 'auto')
                #print(type(image))
                plt.imshow(image)
                plt.show()
        image = mpimg.imread('possibleframes/' + str(i) + 'right.png')
        image = image[30:120,:,:]
        plt.imshow(image)
        plt.pause(.001)
        plt.ion()
        plt.show()
 
