#STEP 1: CREATE A PROGRAM THAT A LIST OF YOUR FAV FRUITTS
#STEP 2: USE LOOP
#STEP 3: APPEND ALL THE LIST OF  YOUR FAV FRUIT 
        #IF YOUR LIST CONTAIN "BANANA" THE PROGRAM WILL BREAK 
        #IF YOUR LIST COANTAIN "APPLE" THE PROGRAM WILL PRINT "HAPPY EATING"

myfavfruit = int ( input("enter num of my fav fruit  :"))


myfavfruit = []

for i in range(myfavfruit):
    fruit = input("enter  my favfruit")
    myfavfruit.append(myfavfruit)


print(myfavfruit)


for data in myfavfruit:
 if data == "banana":
    break
 elif data == "apple":
    print("happy eating")