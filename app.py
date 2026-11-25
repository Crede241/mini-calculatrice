import sys

from calculatrice import addition, division, multiplication


def main():
    if len(sys.argv) != 4:
        print("Usage : python app.py <a> <+|x|/> <b>")
        return
    a, op, b = float(sys.argv[1]), sys.argv[2], float(sys.argv[3])
    if op == "+":
        print(addition(a, b))
    elif op == "x":
        print(multiplication(a, b))
    elif op == "/":
        print(division(a, b))
    else:
        print("Opérateur inconnu")


if __name__ == "__main__":
    main()