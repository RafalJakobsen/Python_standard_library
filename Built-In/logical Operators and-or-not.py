# Python Logical Operators: And, Or, Not:

# What is a boolean?

isRaining=True
isSunny=True

# Logical Operators ==> Special Operators for Booleans

# AND
# True and True ==> True
# False and True ==> False
# True and False ==> False
# False and False ==> False

if isRaining and isSunny:
    print("We might see a rainbow")

# OR
# True and True ==> True
# False and True ==> True
# True and False ==> True
# False and False ==> False

if isRaining or isSunny:
    print("It might be rainy or it might be sunny")

#NOT
# True ==> False
# False ==> True

if not isRaining:
    print("It must be raining")

ages = [12,18,38,87,7,2]
for age in ages:
    isAdult = age > 17;
    if not isAdult:
        print("Being " + str(age) + " does not make you an adult.")

for age in ages:
    isAdult = age < 17;
    if not isAdult:
        print("Being " + str(age) + " make you an adult.")

