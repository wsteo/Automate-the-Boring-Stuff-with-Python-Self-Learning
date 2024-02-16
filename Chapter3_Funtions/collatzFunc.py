import sys

def collatz(number): 
    try:
        if number % 2 == 0:
            return number // 2
        elif number % 2 == 1:
            return 3 * number + 1
    except TypeError:
        print('You need to enter an integer')

print('Enter number:')
userInputNumber = input()
try:
    output = collatz(int(userInputNumber))
except ValueError:
    print('You entered a string. You need to enter an integer')
    sys.exit()
    
print(output)
while output != 1:
    output = collatz(int(output))
    print(output)