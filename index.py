import argparse

def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to your project."

def add_numbers(a: int, b: int) -> int:
    return a + b

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Tool")
    
    parser.add_argument("--name", type=str, help="Your name")
    parser.add_argument("--add", nargs=2, type=int, metavar=('A', 'B'), help="Add two numbers")
    
    args = parser.parse_args()

    if args.name:
        print(greet(args.name))

    if args.add:
        result = add_numbers(args.add[0], args.add[1])
        print(f"Result: {result}")

if __name__ == "__main__":
    main()