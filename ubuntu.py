import paramiko, time

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='ip', username='username', password='password', look_for_keys=True, allow_agent=False)


while True:
    cmd1 = input('>>')
    stdin, stdout, stderr = ssh_client.exec_command(cmd1)
    out, error = stdout.readlines(), stderr.readlines()
    
    if error != []:
        print('>', error)
    elif cmd1 == 'exit':
        print('Çıkış Yapılıyor')
        break
    else:
        for i in out:
            print('>', i)
    time.sleep(1)