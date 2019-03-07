import paramiko
import sys

command = sys.argv[1]
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.211.203.60", username='oss', password='root123')
stdin, stdout, stderr = ssh.exec_command(command)

print(str(stdout.read().decode('ascii').strip()))
