# Create a FizzBuzz
# Print the number from 1 to 100 but if it's a multiple of 3 print Fizz, of 5 print Buzz, if it's both print FizzBuzz
# Extra credit; create one that also handles 7 (Balls) and 11 (Booze)


for i in range(50):
    output = ""
    if (i % 3 == 0):
        output = "Fizz"
    if (i%5 == 0):
        output += "Buzz"
    if (i%7==0):
        output += "Balls"
    if (i%11==0):
        output += "Booze"
    if (output == ""):
        output = i
    print(output)



print("5 delen door 3 rest: ", 5%3)
print("6 delen door 3 rest: ", 6%3)
print("7 delen door 3 rest: ", 7%3)
