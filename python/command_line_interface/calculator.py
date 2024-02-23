import argparse

def add_numbers(args):
    result = args.num1 + args.num2
    print(f"The sum of {args.num1} and {args.num2} is: {result}")

def subtract_numbers(args):
    result = args.num1 - args.num2
    print(f"The difference between {args.num1} and {args.num2} is: {result}")

def main():
    parser = argparse.ArgumentParser(description="Simple CLI for basic arithmetic operations.")
    parser.add_argument('num1', type=int, help='First number')
    parser.add_argument('num2', type=int, help='Second number')
    parser.add_argument('--add', action='store_true', help='Add the two numbers')
    parser.add_argument('--subtract', action='store_true', help='Subtract the second number from the first')

    args = parser.parse_args()

    if args.add:
        add_numbers(args)
    elif args.subtract:
        subtract_numbers(args)
    else:
        print("Please specify an operation with --add or --subtract.")

if __name__ == "__main__":
    main()
