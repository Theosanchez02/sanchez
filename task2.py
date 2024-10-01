#STEP 1: CREATE A PROGRAM THAT A LIST OF YOUR FAV FRUITTS
#STEP 2: USE LOOP
#STEP 3: APPEND ALL THE LIST OF  YOUR FAV FRUIT 
        #IF YOUR LIST CONTAIN "BANANA" THE PROGRAM WILL BREAK 
        #IF YOUR LIST COANTAIN "APPLE" THE PROGRAM WILL PRINT "HAPPY EATING"

myfavfruitnum = int(input("enter num of myfavfruits: "))


myfavfruits = []

for i in range(myfavfruitnum):
    fruit = input("enter  my favfruit")
    myfavfruits.append(fruit)
    if fruit == "banana":
        break 
    elif fruit == "apple":
        print("happy eating")


print(myfavfruits)

