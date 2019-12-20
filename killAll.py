import os
import time
import re

w = open("log.txt", "w").close()
os.system('call tasklist > log.txt')

f = open("log.txt","r")

content = f.readlines()
a = content[4].split("  ")
print(content[5])
for i in range(4,220):
    try:
        os.system('call taskkill /F /T /PID '+re.search(r'\d+', content[i]).group() )
        #time.sleep(2)
    except Exception:
        print(re.search(r'\d+', content[i]).group())

'''

\Users\kevs_\OneDrive\Documents\AMD
filename = 'log,txt'
filehandle = open(filename, 'r')
while True:
    # read a single line
    counter++
    line = filehandle.readline()
    if not line:
        break
    print(line)

# close the pointer to that file
filehandle.close()
'''
