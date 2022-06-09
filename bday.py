import time as q
import pygame
import os
os.system('color F4')
pygame.mixer.init()
pygame.mixer.music.load("blablabla.mp3")
pygame.mixer.music.play()
print('wait 10 seconds')
y=q.sleep(10)
x="My Amal"
 
b=len(x)
def cake(): 
    print(" "*23,"i  i  i  i")
    y=q.sleep(0.5)
    print(" "*23,"i  i  i  i")
    y=q.sleep(0.5)
    print(" "*21,"__i__i__i__i__")
    y=q.sleep(0.5)
    print(" "*20,"|"," "*12,"|")
    y=q.sleep(0.5)
    print(" "*20,"|"," "*12,"|")
    y=q.sleep(0.5)
    print(" "*20,"|"," "*12,"|")
    y=q.sleep(0.5)
    print(" "*16,"-"*24)
    y=q.sleep(0.75)
    print(" "*16,"|"," "*20,"|")
    y=q.sleep(0.75)
    print(" "*16,"|"," "*int((20-b)/2),x," "*int((20-b)/2-2)," |")
    y=q.sleep(0.75)
    print(" "*16,"|"," "*20,"|")
    y=q.sleep(0.75)
    print(" "*16,"-"*24)
    y=q.sleep(1)
 
 
def menu():
    print()
    for i in range(4):
        if i==3:
            print(" "*13,"HAPPY HAPPY BIRTHDAY TO YOU")
        elif i==0 or i==1:
            print(" "*15,"HAPPY BIRTHDAY TO YOU")
        elif i==2:
            print(" "*15,"HAPPY BIRTHDAY","*",x.upper(),"*","\n")
        q.sleep(1.5)
        print()
    
def heart():
    for row in range(6):
        print(" "*25,end="")
        for col in range(7):
            if (row==0 and col %3 != 0)or(row==1 and col %3==0) or(row-col==2) or(row+col==8):
                print("❤",end=" ")
            else:
                print(end="  ")
        print() 
print("#"*9,"BIRTHDAY WISHES FOR MY LOVELY","*"+"AMAL"+"*","#"*9)
q.sleep(1.25)
menu()
cake()
 
print(" "*12,"thank god for having uu darling\n \n\n".upper())
q.sleep(2)
x="Happy, healthy, exceptional, rocking birthday to the love of my life"
a=x.split()
for i in a:
    print("\t\t",i.title())
    q.sleep(0.5)
print("")
q.sleep(1)
print(" "*18,"I love you to the moon and back".upper())
q.sleep(1)
print(" "*18,"my only and my special amal <3".upper())
q.sleep(1)
print()
heart()
y = q.sleep(260)
#I love you amal for real n7ebek
