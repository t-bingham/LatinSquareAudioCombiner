"""Randomises and assigns Latin squares"""
import random
import glob
import csv
import os
from pydub import AudioSegment
from latinSquareGenerator import LatinSquare

latinSquare = []

Ki = AudioSegment.from_file("Videos/K_Original.wav", format="wav")
Li = AudioSegment.from_file("Videos/L_Original.wav", format="wav")

K = Ki[12000 : 22000]
with open("Videos/" + "K" + ".wav", 'wb') as out_f:
    K.export(out_f, format="wav")
L = Li[12000 : 22000]
with open("Videos/" + "L" + ".wav", 'wb') as out_f:
    L.export(out_f, format="wav")
