"""Randomises and assigns Latin squares"""
import random
import glob
import csv
import os
import subprocess
from pydub import AudioSegment
from latinSquareGenerator import LatinSquare

latinSquare = []

audioList = ["Videos/AudioInput/A.wav", "Videos/AudioInput/B.wav", "Videos/AudioInput/C.wav", \
    "Videos/AudioInput/D.wav", "Videos/AudioInput/E.wav", "Videos/AudioInput/F.wav",\
    "Videos/AudioInput/G.wav", "Videos/AudioInput/H.wav", "Videos/AudioInput/I.wav", \
    "Videos/AudioInput/J.wav", "Videos/AudioInput/K.wav", "Videos/AudioInput/L.wav"\
    , "Videos/AudioInput/M.wav", "Videos/AudioInput/N.wav", "Videos/AudioInput/O.wav"]

fillerList = ["Videos/AudioInput/aa.wav", "Videos/AudioInput/bb.wav", "Videos/AudioInput/cc.wav", \
    "Videos/AudioInput/dd.wav", "Videos/AudioInput/ee.wav", "Videos/AudioInput/ff.wav", \
    "Videos/AudioInput/gg.wav", "Videos/AudioInput/hh.wav", "Videos/AudioInput/ii.wav", \
    "Videos/AudioInput/jj.wav", "Videos/AudioInput/kk.wav", "Videos/AudioInput/ll.wav" \
    , "Videos/AudioInput/mm.wav", "Videos/AudioInput/nn.wav", "Videos/AudioInput/oo.wav", \
    "Videos/AudioInput/pp.wav"]

order = list(range(16))

""" Writes generated Latin square to CSV file """

def writeLatinSquareToFile(square, name):
    with open("CSV/" + name + ".csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(square)


""" Takes mp4 files, extracts the audio and compiles them into a single
    file, currently named output.mp3 """

def combineAudiofiles(audioList, order, name):
    combined = AudioSegment.empty()
    for i in range(len(audioList)):
        j = order[i]
        filler = AudioSegment.from_file(fillerList[i], format="wav")
        item = AudioSegment.from_file(audioList[j], format="wav")
        combined += filler
        combined += item
    filler = AudioSegment.from_file(fillerList[15], format="wav")
    combined += filler
    with open("Videos/" + name, 'wb') as out_f:
        combined.export(out_f, format="wav")


""" Generates Latin square of specified size """

def createLatinSquare():
    ls = LatinSquare.generate_latin_square(15)
    return(ls.square)


""" Asks what to name the output file """
def outputFileName(type):
    name = input("Write name of " + type + " file here: \n")
    return(name)


def main():
    result = createLatinSquare()
    name = outputFileName("CSV")
    writeLatinSquareToFile(result, name)
    for i in range(len(audioList)):
        name = outputFileName("output audio")
        combineAudiofiles(audioList, result[i], name)
if __name__ == "__main__":
    main()
