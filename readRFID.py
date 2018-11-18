import subprocess
import creditor as cd
import csv
import datetime, time



def addToDatabase(idCard):

        t = datetime.datetime.now()

        isAlready = False
        output = idCard.translate(table)
        if output != "":
            with open('IDs.csv', 'r+') as f:
                csv_reader = csv.reader(f, delimiter=',')
                for row in csv_reader:
                    if row[0] == output:
                        isAlready = True
                        print(output +
                            " is already in the database. Skipping")
                        break
                    else:
                        isAlready = False
            if isAlready == False:
                
                with open('IDs.csv', 'a+', newline='') as f:
                    csv_writer = csv.writer(f, delimiter=',')
                    csv_writer.writerow([output, 2, time.mktime(t.timetuple())])
                    print(output + " added to the database.") 

                #Update the database for conversion to list
                cd.userList = cd.updateUserList()

print("Starting RFID Card Reader")

task = subprocess.Popen(
    ['sudo', 'cat', '/dev/ttyUSB0'], stdout=subprocess.PIPE)
print("Beginning Reading")
print("Please, do a blank credit")


for idCard in task.stdout:
    idCard = str(idCard)
    table = str.maketrans(dict.fromkeys("\\nb'"))
    idCard = idCard.translate(table)

    print(idCard)

    if idCard.translate(table) != "":
        addToDatabase(idCard)
        cd.processCard(idCard)
        
        

#task.wait()
