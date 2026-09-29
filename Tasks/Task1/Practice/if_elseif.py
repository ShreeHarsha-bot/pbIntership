name=input("Enter your name :")
totalPercent=int(input("Enter your percentage :")) 
if(totalPercent<=100):
   
    if(totalPercent>=85 ):
     print(f"{name} is secured {totalPercent}%, and he got grade A")
    elif(totalPercent>=75):
     print(f"{name} is secured {totalPercent}%, and he got grade B")
    elif(totalPercent>=60):
     print(f"{name} is secured {totalPercent}%, and he got grade C")
    elif(totalPercent>=55):
     print(f"{name} is secured {totalPercent}%, and he got grade D")
    elif(totalPercent>=35):
     print(f"{name} is secured {totalPercent}%, and he got grade E")
    else:
     print(f"{name} is secured {totalPercent}%, and he got grade F")


