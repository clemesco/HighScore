import subprocess
import creditor as cd
import csv
import datetime
import time
import os


class RfidReader:

    # Add RFID tag to database if not already present
    def addToDatabase(self, idCard):

        t = datetime.datetime.now()

        #table = str.maketrans(dict.fromkeys("\\nb'"))

        isAlready = False
        #idCard = idCard.translate(table)
        if idCard != "":
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'IDs.csv')), 'r+') as f:
                csv_reader = csv.reader(f, delimiter=',')
                for row in csv_reader:
                    if row[0] == idCard:
                        isAlready = True
                        print(idCard +
                              " is already in the database. Skipping adding it")
                        break
                    else:
                        isAlready = False
            if isAlready == False:

                with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'IDs.csv')), 'a+', newline='') as f:
                    csv_writer = csv.writer(f, delimiter=',')
                    csv_writer.writerow(
                        [idCard, cd.creditsPerCycle, time.mktime(t.timetuple())])
                    print(idCard + " added to the database.")

                # Update the database for conversion to list
            cd.userList = cd.updateUserList()
