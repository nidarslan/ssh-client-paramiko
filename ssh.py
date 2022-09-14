import sys
from time import sleep
import paramiko
switch="ip"

conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect(switch, username="user", password="pass",  look_for_keys=True, allow_agent=False)
switch_conn = conn.invoke_shell()
print('Successfully connected to %s' % switch)
sleep(1)        

while True:
    cmd1 = input('>>')
    stdin, stdout, stderr = conn.exec_command(cmd1)
    out, error = stdout.readlines(), stderr.readlines()
    
    if error != []:
        print('>', error)
    elif cmd1 == 'exit':
        print('Çıkış Yapılıyor')
        break
    else:
        for i in out:
            print('>', i)
print(switch_conn.recv(5000).decode("utf-8"))