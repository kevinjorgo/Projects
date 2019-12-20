#! python3

print('what is your name')
name = raw_input()
print(name)
if 'kevin' == name:
    print('hi kevin')
else:
    print('done')

spam=0
while spam<3:
    print('ctrl+c will interrupy program')
    spam=spam+1
    if spam == 2:
        break

for i in range(0, 6, 2):
    print(i)


import random
print(random.randint(1,100))


def hello(name):
    print('this is a function '+ name)

hello('kev')
hello('kev')



    
