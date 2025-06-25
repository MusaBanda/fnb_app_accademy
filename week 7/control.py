import time

name = input("what is your username? ")
print("hello ", name)

place = input("where are you from " + name +"? ")

age = int(input("so "+ name + " how old are you "))
time.sleep(0.5)

print("please check if the following information is corret ")
time.sleep(1.5)
print("your name is ", name + " ,your from ", place + " ,you are ", age ,"old")
time.sleep(1.5)
print("if correct enter yes and if not enter no ")

answer = input("? ")
if answer == "yes":
    print("ok lets proceed ", name)

if answer == "no":
    print("re-run")
    
print(" welcome to my survey ")
time.sleep(3)
print("today i'll be asking you a few qeustion please only answer using the number's provided in multiple qeustions")
time.sleep(5)
print("NOTE THE FOLLOWING QEUSTIONS ARE BASED ON FOOTBALL")
time.sleep(4)

print("Question 1")
time.sleep(0.5)

print("who is the best player(goat) betweem; ")
time.sleep(1.5)
print("1.cristiano ronaldo")
print("2.leo messi")
print("3.benzema")
answer = input("? ")

if answer == "1":
    print("your answer is ,ronaldo is the best")
if answer == "2":
    print("your answer is ,leo messi is the best")
if answer == "3":
    print("your answer is ,benzema is the best")
else:
    print("your answer is invalid please re-run the program and try again")
    exit()