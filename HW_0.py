import random
#16 A
E16a = 15 * 38
print(E16a)

#16 B
E16b = (3 + 4) * (5 + 6)
print(E16b)

#16 C
E16C = 7 / 2
print(int(E16C))

#16 D
E16D = 48 // 5
print(E16D)

#16 E
E16E = (8 + 7 + 4 + 2) / 4
print(E16E)

#16 F
E16F = 2 ** 10
print(int(E16F))

#16 G
E16G = 49 ** 0.5
print(E16G)

#16 H
E16H = 80 * 0.25
print(int(E16H))





#18
#I am 170cm tall, i.e. 5 feet and 7 inches.
l = 179
l2 = l % 30.48
print("I am ", l, "cm tall, i.e. ", (int(l2)), "feet,", "6", "inches.")



#19
#The length of the sides of the triangle is a, b and c. Write a program 
#that calculates the area of the triangle using the Heron formula.
#Read the values of the sides of the triangle from the keyboard. Using the
#program, calculate the area of the triangle for the sides 3, 4 and 5.

a = 3
b = 4
c = 5
p = (a + b + c) // 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(int(S))

'''
#20
h = float(input("Enter your heigh: "))
w = int(input("Enter your weight: "))
BMI = (w / (h ** 2))
print("Your BMI index is ", BMI)
'''

#21
roll1 = random.randint(1, 6)
roll2 = random.randint(1, 6)
roll3 = random.randint(1, 6)
s1 = roll3 + roll2 + roll1
r = f"The 1 roll is: {roll1};\nThe 2 roll is: {roll2};\nThe 3 roll is: {roll3}."
s = f"The sum of 3 rolls is: {s1}."
print(r)
print(s)


#23
#23% VAT was paid from the amount of PLN 15.84. Calculate and display VAT.
# Apply formatting with decimal places. Sample result:
#Amount  : 15.84 zł
#VAT 23% :  3.64 zł
a = int(input("Enter your full amount: "))
v = a * 0.23
print("Amount : ", a)
print("VAT 23% : ", v)








