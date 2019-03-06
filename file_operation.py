#path = input("Enter the full path of the file to be created...")
path="/tmp/details.json"
print("Entered PATH is "+ path)

fileBufferWrite = open(path, "w")

entry = """{
'hostname':'server1.UCSBANG6.com',
'cpu':3,
'mem':'2GB',
'filesystems':
  {
  '/boot':'512MB',
  '/opt':'20GB',
  '/':'16GB'
  },
'ip':'10.211.203.123'
}
"""

fileBufferWrite.write(entry)

fileBufferWrite.close()

fileBufferRead = open(path, "r")

output = fileBufferRead.read().strip()

print(output)
