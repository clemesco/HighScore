import csv
import datetime
import time
from pynput.keyboard import Key, Controller

creditsPerCycle = 2
numberOfHours = 2

#Initiate keyboard for credit input once in-game
keyboard = Controller()

#Get user database as list
def updateUserList():
    with open('IDs.csv', 'r+') as f:
        reader = csv.reader(f, delimiter=',')
        userList = list(reader)
    return userList


userList = updateUserList()

#Get the csv row for specific user
def getRow(idCard):
    for row in userList:
        # print(row[0])
        if row[0] == idCard:
            return row

#Reload account if x amount of seconds went by
def reloadAccount(idCard, timeInSceonds, creditCount):
    row = getRow(idCard)
    t1 = datetime.datetime.now()
    t1 = time.mktime(t1.timetuple())
    diff = t1-float(row[2])
    if diff >= timeInSceonds:
        row[1] = creditCount
        row[2] = t1
        print('Reloaded account !')

#Approve credit request if user has enough credits
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

#Rewrite database
def updateCSV():
    with open("IDs.csv", 'w') as f:
        wr = csv.writer(f, lineterminator='\n', delimiter=',')
        for val in userList:
            wr.writerow(val)
        print('Updated CSV')

#Press key to credit once in-game
def creditGame():
    keyboard.press(Key.space)
    time.sleep(0.5)
    keyboard.release(Key.space)

#Main process function
def processCard(idCard):
    reloadAccount(idCard, numberOfHours*3600, creditsPerCycle)
    okForCredit = approve(idCard)
    if okForCredit:
        creditGame()
    updateCSV()
    return okForCredit
