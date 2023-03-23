### Excersice 2: Good Morning Sir

'''Create a python program capable of greeting you with Good Morning, Good Afternoon 
and Good Evening. Your program should use time module to get the current hour. 
Here is a sample program and documentation link for you:'''

import time
t= time.strftime('%I:%M:%S %p')
print(f"The time is {t}")

hour= int(time.strftime('%I'))

min = int(time.strftime('%M'))

sec = int(time.strftime('%S'))

period=time.strftime('%p')

if (hour>=00 and hour<12 and period=='AM') or (hour==11 and min<60):
    print("Good Morning")


elif (hour>=12 and hour<5 and period=='PM') or (hour==4 and min<60 and period=='PM'):
    print("Good Afternoon")

else:
    print("Good Evening")

