## your chappi chaiwala
print(".........chappi chaiwala..........")
print("..................................")
print(".............  menu   ............")

print("1. chai: ")
print("2. coffee: ")
bill = 0
drink = input("what do you want? :") 


if drink == "chai" or drink == "1":
    bill += 20
elif drink == "coffee"or drink == "2":
    bill += 30

sugar = input("do you need extra sugar: ")
if sugar == 'y' or sugar == 'yes':
    bill += 2
rusk = input("do you need rusk: ")
if rusk == 'y' or rusk == 'yes':
    bill += 5


bread = input("do you need bread: ")
if bread == 'y' or bread == 'yes':
    bill += 5

print("Bill =",bill)
 