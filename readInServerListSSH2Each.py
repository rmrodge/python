import base64
import paramiko

array = []

fh = open('my_text_file.txt')

for line in fh:
     print(line)
     #Need to add these two items to clean up the extra items added for line items.
     line=line.strip('\n')
     line=line.strip('\t')
     array.append(line)   
fh.close()

print("List of array items")
print(array[0])
print(array[1])

for x in array:
     print("List of array items in for loop") 
     print(x)
     client = paramiko.SSHClient()
     client.load_system_host_keys()
     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     client.connect(x, username='username', password='password')
     stdin, stdout, stderr = client.exec_command('cat /proc/meminfo')
     for line in stdout:
       print('... ' + line.strip('\n'))
     client.close() 
