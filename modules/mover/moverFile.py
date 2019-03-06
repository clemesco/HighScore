import os
import datetime
import time
import shutil

from os import listdir
from os.path import isfile, join

class mover():

    def __init__(self):
        self.tempList = ['mslug3.zip', 'nbbatman.zip', 'rampage.zip']
        self.moveFile = 'mover/movedGame.txt'
        self.permaRomPath = 'mover/permaRom/'
        self.tempRomPath = 'mover/tempRom/'

    def moveToTemp(self, gameFile):
        shutil.move(os.path.abspath(self.permaRomPath) + '/' + gameFile,
                    os.path.abspath(self.tempRomPath) + '/' + gameFile)

    def moveToPerm(self, gameFile):
        shutil.move(os.path.abspath(self.tempRomPath) + '/' + gameFile,
                    os.path.abspath(self.permaRomPath) + '/' + gameFile)

    def directoryToList(self, romPath):
        onlyfiles = [f for f in listdir(romPath) if isfile(join(romPath, f))]
        return onlyfiles

    def saveMovedGame(self, gameFile, i):
        with open(self.moveFile, 'w') as f:
            f.write(str(i) + gameFile)

    def getGameId(self):
        with open(self.moveFile, 'r') as f:
            id = f.read(1)
        return id

    def changeGame(self):
        i = int(self.getGameId())
        previousGame = self.tempList[i]
        self.moveToTemp(previousGame)

        nextGameId = i+1

        if nextGameId > len(self.directoryToList(self.tempRomPath))-1:
            nextGameId = 0

        self.saveMovedGame(self.tempList[nextGameId], nextGameId)

        self.moveToPerm(self.tempList[nextGameId])
        nextGame = self.tempList[int(self.getGameId())]
        #os.system('killall attract')
        os.system('attract --build-romlist mame -o mame')
        # os.system('attract')
