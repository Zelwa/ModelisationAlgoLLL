from fractions import Fraction
import  numpy as  np
from numpy import long


def parser(file_name):
    f = open(file_name,"r")
    basis = f.read().splitlines()
    base_vector = []
    for line in basis:
        line = line.replace("[", " ")
        line = line.replace("]", " ")
        line = line.rsplit()
        vector = [ ]
        for i in range(len(line)):
            vector.append(Fraction(line[i]))
        base_vector.append(vector)
    array = np.array(base_vector)
    f.close()
    return array

def parser2(file_name):
    f = open(file_name,"r")
    basis = f.read().split("], [")
    base_vector = []
    for line in basis:
        line = line.replace(",", "")
        line = line.replace("[", " ")
        line = line.replace("]", " ")
        line = line.rsplit()
        vector = []
        for i in range(len(line)):
            vector.append(Fraction(long(line[i])))

        base_vector.append(vector)
    array = np.array(base_vector)
    f.close()
    return array






