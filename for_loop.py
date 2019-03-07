fileBuffRead = open("text.txt", "r")

details = fileBuffRead.readlines()

print(type(details))

for lines in details:
    var = lines.split("=")[0].strip('\n')
    val = lines.split("=")[1].strip('\n')
    print("Value of "+var+" is:"+" "+str(val))
