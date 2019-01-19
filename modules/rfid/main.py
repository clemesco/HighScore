import readRFID
import creditor as cd
import subprocess


rfidR = readRFID.RfidReader()

print("Starting RFID Card Reader")     

#Opening terminal process
task = subprocess.Popen(
    ['sudo', 'cat', '/dev/ttyUSB0'], stdout=subprocess.PIPE)
print("Beginning Reading")
print("Please, do a blank credit")


for idCard in task.stdout:
    idCard = str(idCard)
    table = str.maketrans(dict.fromkeys("\\nb' "))
    idCard = idCard.translate(table)


    if idCard != "" and len(idCard) >= 10:
        rfidR.addToDatabase(idCard)
        cd.processCard(idCard)
    print("\n"*3)


# task.wait()