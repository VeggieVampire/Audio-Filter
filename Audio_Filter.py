#This script cleans up audio files.
#To displayed the audio plot you must have matplotlib installed.
#For processing the audio you will need to install scipy
#To Get updates go to https://github.com/VeggieVampire


import scipy.io.wavfile
import math

rate, data = scipy.io.wavfile.read('input.wav')


import matplotlib.pyplot as plt
plt.plot(data)
plt.show()



UpClip = eval(raw_input("What upper value do you want to Clipping?: "))
BottomClip = eval(raw_input("What bottom value do you want to Clipping?: "))

#cut all values below user's value
for n,i in enumerate(data):
    if i<= BottomClip:
        data[n]= BottomClip + 1

#cut all values above user's value
for n,i in enumerate(data):
    if i >= UpClip:
        data[n]= UpClip + 1


#Amplify all upper values
for n,i in enumerate(data):
    if i >= UpClip + 5:
        data[n]= 800000

#Make all BottomClips 0
for n,i in enumerate(data):
    if i <= BottomClip + 5:
        data[n]= 0


#Show changed plot
plt.plot(data)
plt.show()

#output a wave file
from scipy.io.wavfile import write
scipy.io.wavfile.write('output.wav',rate,data)



