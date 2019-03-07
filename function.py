import os

def createFile(fileName, entry):
    os.chdir("/tmp")
    fileBuffWrite = open(fileName, "w")
    fileBuffWrite.write(entry)
    fileBuffWrite.close()

    fileBuffRead = open(fileName, "r")
    fileBuffRead.readlines()
    fileBuffRead.close()

strInput = """{
'Name':'Arnab Kumar Nandy',
'ID':'arnab.nandy',
'Location':'BLR',
'Project':'DC'
}
"""

fName = "empDetails.json"

createFile(fName, strInput)
