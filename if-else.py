import requests

r = requests.get('http://10.211.203.91:3001/util')
result = r.json()
print(result)

print(type(result))

cpuUtil = result['CPU']
memUtil = result['MEM']

CRITICAL = 100
WARNING = 80
OK = 50

if cpuUtil <= OK:
    print("CPU is OK | Utilization: "+ str(cpuUtil))
elif (cpuUtil > OK and cpuUtil <= WARNING):
    print("CPU is in WARNING | Utilization: "+ str(cpuUtil))
elif (cpuUtil > WARNING and cpuUtil <= CRITICAL):
    print("CPU is in CRITICAL | Utilization: "+ str(cpuUtil))
