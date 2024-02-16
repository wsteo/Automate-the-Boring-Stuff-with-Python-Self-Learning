def collatz(number):
    try:
        if number % 2 == 0:
            return number // 2
        elif number % 2 == 1:
            return 3 * number + 1
    except ValueError:
        raise ValueError('You need to enter an integer')

def main():
    try:
        user_input = int(input("Enter an integer for the Collatz sequence: "))
        result = collatz(user_input)
        print(result)

        while result != 1:
            result = collatz(result)
            print(result)

    except ValueError as e:
        print(f'Error: {e}. Please enter a valid integer.')

if __name__ == "__main__":
    main()
