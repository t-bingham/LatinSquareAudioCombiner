"""Randomises and assigns Latin squares"""
import random
import glob
import csv
import os
from pydub import AudioSegment
from latinSquareGenerator import LatinSquare

latinSquare = []
audioList = ["Videos/A.mp4", "Videos/B.mp4", "Videos/C.mp4", \
    "Videos/D.mp4", "Videos/E.mp4", "Videos/F.mp4", "Videos/G.mp4", \
    "Videos/H.mp4", "Videos/I.mp4"]


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
        item = AudioSegment.from_file(audioList[j], format="mp4")
        combined += item
    with open("Videos/" + name, 'wb') as out_f:
        combined.export(out_f, format="mp3")


""" Generates Latin square of specified size """

def createLatinSquare():
    ls = LatinSquare.generate_latin_square(9)
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
