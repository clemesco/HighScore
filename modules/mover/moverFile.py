import os
import datetime
import time
import shutil

from os import listdir
from os.path import isfile, join

permaRomPath = 'mover/permaRom/'
tempRomPath = 'mover/tempRom/'


def moveToTemp(gameFile):
    shutil.move(os.path.abspath(permaRomPath) + '/' + gameFile,
                os.path.abspath(tempRomPath) + '/' + gameFile)
    print('Moved game to temp folder')


def moveToPerm(gameFile):
    shutil.move(os.path.abspath(tempRomPath) + '/' + gameFile,
                os.path.abspath(permaRomPath) + '/' + gameFile)
    print('Moved game to perm folder')


def directoryToList(romPath):
    onlyfiles = [f for f in listdir(romPath) if isfile(join(romPath, f))]
    return onlyfiles


tempList = ['mslug3.zip', 'nbbatman.zip', 'rampage.zip']


def saveMovedGame(gameFile, i):
    with open('mover/movedGame.txt', 'w') as f:
        f.write(str(i) + gameFile)
    print('Saved Game in text file')


def getGameId():
    with open('mover/movedGame.txt', 'r') as f:
        id = f.read(1)
    return id


def changeGame():
    i = int(getGameId())
    previousGame = tempList[i]
    print('Previous game is:', previousGame)
    moveToTemp(previousGame)

    nextGameId = i+1

    if nextGameId > len(directoryToList(tempRomPath))-1:
        nextGameId = 0

    saveMovedGame(tempList[nextGameId], nextGameId)

    moveToPerm(tempList[nextGameId])
    nextGame = tempList[int(getGameId())]
    print('Next game is:', nextGame)
    #os.system('killall attract')
    os.system('attract --build-romlist mame -o mame')
    #os.system('attract')

    

changeGame()
