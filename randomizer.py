from pathlib import Path
import json
import random
import os

file = Path().absolute()
historyPath = str(file) + "/history"
historyJson = historyPath + "/history.json"


def readhistory(historyFile):
    with open(historyFile, "r") as readFile:
        data = json.load(readFile)
    return data


def writeHistory(oldHistory, appendEvents, outcome, historyFile):
    newHistory = {}
    newHistory["events"] = {}

    currentEvent = 1
    for x in appendEvents:
        newHistory["events"]["event " + str(currentEvent)] = x
        currentEvent += 1

    newHistory["outcome"] = "event " + str(outcome + 1)

    oldHistory["history"].append(newHistory)

    with open(historyFile, "w") as writeFile:
        json.dump(oldHistory, writeFile, indent=4,
                  separators=(", ", ": "), sort_keys=False)


def event(amountEvents):
    runningIndex = 0
    eventArray = []
    while runningIndex < amountEvents:
        event = input(str(runningIndex + 1) + ". Event: ")
        while event == "":
            print("Event " + str(runningIndex + 1) +
                  " is not allowed to be empty!")
            event = input(str(runningIndex + 1) + ". Fall: ")
        eventArray.append(event)
        runningIndex += 1
    return(eventArray)


def randomizer(amountRandom):
    randomnum = random.randrange(0, amountRandom, 1)
    return randomnum


def inputs():
    amountStr = input("Amount of Events: ")
    while not amountStr.isdigit():
        amountStr = input("The amount must be an integer: ")
    amountInt = int(amountStr)
    return amountInt


amount = inputs()
events = event(amount)

randomEvent = randomizer(amount)

print("Result: " + str(events[randomEvent]))

history = readhistory(historyJson)
writeHistory(history, events, randomEvent, historyJson)

os.system("pause")
