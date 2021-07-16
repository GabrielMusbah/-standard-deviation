import numpy  # https://numpy.org/
import math  # https://docs.python.org/3.8/library/math.html


print("Enter numbers in  line: ")
listNumber = input().split()



def convertList(listNumber):
    listNumber = list(map(int, listNumber))  # convert list string in int

    return listNumber


def lengthList(listNumber):
    lengthList = len(listNumber)

    return lengthList


def averageList(listNumber):
    averageList = numpy.mean(listNumber)

    return averageList


def listAverage(averageList, lengthList): # this creat a list with only average
    listAverage = []

    while lengthList > 0:
        listAverage.append(averageList)
        lengthList = lengthList - 1

    return listAverage


def listNumberMinusAverage(listNumber, listAverage):  # code use this list to creat a list with: (number(n) - average)
    listNumberMinusAverage = []

    listNumberMinusAverage = [(a - b) for a, b in zip(listNumber, listAverage)]

    return listNumberMinusAverage


def listNumberMinusAverageSquared(listNumberMinusAverage):
    listNumberMinusAverageSquared = []

    listNumberMinusAverageSquared = [(a * b) for a, b in zip(listNumberMinusAverage, listNumberMinusAverage)]

    return listNumberMinusAverageSquared


def sumList(listNumberMinusAverageSquared):
    sumList = sum(listNumberMinusAverageSquared)

    return sumList


def sumListDividedAverage(sumList, averageList):
    sumListDividedAverage = sumList / (averageList - 1)

    return sumListDividedAverage


def standardDeviation(sumListDividedAverage):
    standardDeviation = math.pow(sumListDividedAverage, 1 / 2)

    return standardDeviation



listNumber = convertList(listNumber)

lengthList = lengthList(listNumber)

averageList = averageList(listNumber)

listAverage = listAverage(averageList, lengthList)

listNumberMinusAverage = listNumberMinusAverage(listNumber, listAverage)

listNumberMinusAverageSquared = listNumberMinusAverageSquared(listNumberMinusAverage)

sumList = sumList(listNumberMinusAverageSquared)

sumListDividedAverage = sumListDividedAverage(sumList, averageList)

standardDeviation = standardDeviation(sumListDividedAverage)

print("The standard deviation: %0.5f" % standardDeviation)
