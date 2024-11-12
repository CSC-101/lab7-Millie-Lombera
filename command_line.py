import sys
from convert import str_to_float

def main():
    total = 0.0
    for arg in sys.argv[1:]:
        result = str_to_float(arg)
        if result is not None:
            total += result
    print("Sum of command-line numbers:", total)


if __name__ == '__main__':
    main()