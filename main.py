#inputing value a
a = input("enter the first number in the pattern?")
a = int(a)

#inputing value d(difference)
d = input("what is the difference between each of the consecutive numbers in the pattern?")
d = int(d)

#inputting n(nth term)
n = input("what the nth term you want to find?")
n = int(n)

#constant value of U to caluculate the nth term
U = a + (n - 1) * d

#printing the value of U
print(U)
