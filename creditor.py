import csv
import datetime
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()


def updateUserList():
    with open('IDs.csv', 'r+') as f:
        reader = csv.reader(f, delimiter=',')
        userList = list(reader)
    return userList


userList = updateUserList()


def getRow(idCard):
    for row in userList:
        # print(row[0])
        if row[0] == idCard:
            return row


def reloadAccount(idCard, timeInSceonds, creditCount):
    row = getRow(idCard)
    t1 = datetime.datetime.now()
    t1 = time.mktime(t1.timetuple())
    diff = t1-float(row[2])
    if diff >= timeInSceonds:
        row[1] = creditCount
        row[2] = t1
        print('Reloaded account !')


def approve(idCard):
    row = getRow(idCard)
    creditNumber = int(row[1])
    if creditNumber > 0:
        row[1] = creditNumber - 1
        print("Credits left:", row[1])
        return True
    else:
        print("You are out of credits. Please wait until your credits are back !")
        return False


def updateCSV():
    with open("IDs.csv", 'w') as f:
        wr = csv.writer(f, lineterminator='\n', delimiter=',')
        for val in userList:
            wr.writerow(val)


def creditGame():
    keyboard.press(Key.space)
    keyboard.release(Key.space)


def processCard(idCard):
    reloadAccount(idCard, 3600, 2)
    okForCredit = approve(idCard)
    if okForCredit:
        creditGame()
    updateCSV()
    return okForCredit
