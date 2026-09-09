"""hi there,

We'll learn today -
- taking input on the variable
- showing typecasting
- Converting one format to another format
"""


money = input("Enter your Money : ")
print(f"Here is your money", money)

money2 = input("Enter your Money again : ")
print(f"Here is your amount", money2)

total = money + money2

print("Total amaont ", total)

print(type(money))
print(type(total))

# taking Integer type data
int_money = int(input("Enter u r input : "))
int_money_ = int(input("Enter u r input again : "))

total_int = int_money + int_money_

print("Total amount integer : ", total_int)
print(type(total_int))


# taking float data
Age = float(input("what's ur age? : "))
print("My age is ", Age)


# converting String to Integer
money_int = int(money)
print("Converted from string into Integer is ", money_int, " which was a string")

# converting Integer to String
money_str = str(int_money)
print("Converted from Integer into string is ", money_str, " which was an Integer")

'''
same coverting process can be applied for -
- String to Integer
- Integer to String
- Integer to Float
- Float to Integer
- String to Float
- Float to String
'''