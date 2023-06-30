print("MINI Caluculator")
print("We are Here to peform below Functions:")
s={1:"Addition",2:"Subtraction",3:"Division",4:"Multiplication"}
print(s)
count=0
ad=0
mu=1
su=0
ttl=0
a=int(input("Selcet the number b/w 1 t0 4:"))
while True:
    if a==1:
        z=int(input("How many numbers I need to add for you :"))
        i=0
        while i<z:
            h=int(input("Enter a number:"))
            i+=1
            ad=ad+h
            print("The result is:",ad)
            break
    elif a==4:
        z=int(input("How many numbers I need to multiply for you :"))
        i=0
        while i<z:
            h=int(input("Enter a number:"))
            i+=1
            mu=mu*h
        print("The result is:",mu)
        break
    elif a==2:
        z=int(input("How many times I need to subtract for you :"))
        i=0
        while i<z:
            h=int(input("Enter a number:"))
            if not i:
                su=h
            else:
                su-=h
            i+=1
        print("The result is:",su)
        break
    elif a==3:
        z=int(input("How many times I need to do division for you :"))
        i=0
        while i<z:
            h=int(input("Enter a number:"))
            if not i:
                su=h
            else:
                su=su/h
            i+=1
        print("The result is:",su)
        break
    else:
        
        if count:
            print('enter a valid number b/w 1-4 or type 0 to exit')
        else:
            print("invalid number enter a valid number b/w between 1 and 4")
            
        a = int(input('enter a number b/w 1-4 >> '))
        if count and a == 0:
            print('dhobey')
            break
        count +=1
