from sys import *
from sympy.parsing.sympy_parser import parse_expr as pe
import sympy as sp
import re

x = sp.symbols("x")


def main():
    global x
    y = input("f(x) = ").replace(" ", "")
    validate(y)

    print("Type the initial letter:")
    print("1. Indefinite Integral                     (I)")
    print("2. Differentiate                           (D)")
    print("3. Expand/Simplify                         (E)")
    print("4. Factorise                               (F)")
    print("5. Area under the curve (Integration)      (A)")
    print("6. Minima and maxima (Critical Points)     (M)")
    print("7. Solve for x when f(x) = 0               (S)")

    id = input("Command: ").upper()
    id_set = ["I", "D", "E", "F", "A", "M", "S", "1", "2", "3", "4", "5", "6", "7"]
    if not id in id_set:
        exit("Error: Invalid command")
    if id == "I" or id == "1" or id == "D" or id == "2":
        try:
            t = int(
                input(
                    f"How many times to {'integrate' if id == 'I' else ''}{'differentiate' if id == 'D' else ''} =>"
                )
            )
            if t != int(t):
                raise ValueError
        except ValueError:
            exit("Error: Number must be an integer")

    if id == "I" or id == "1":
        tSub = sub(t)
        y = f"{tSub}∫ f(x) dx = {intgrt(y, t) + c(t)}"
    elif id == "D" or id == "2":
        tSup = to_super(str(t))
        y = (f"f{tSup}(x) = {dfrnt(y, t)}").replace("log", "ln")
    elif id == "E" or id == "3":
        output = f"f(x) = {smplfy(y)}"
    elif id == "F" or id == "4":
        y = f"f(x) = {factor(y)}"
    elif id == "A" or id == "5":
        y = Area(y)
    elif id == "M" or id == "6":
        output = ""
        critical_points = minmaxima(y)
        results = (
            super(critical_points)
            .replace("I", "i")
            .replace("]", "}")
            .replace("[", "{")
            .replace("*", "·")
        )

        print(f"Critical Points:{results}\n")


    elif id == "S" or id == "7":
        output = ""
        print(root(y))
        results = (
            super(str(root(y)))
            .replace("I", "i")
            .replace("]", "")
            .replace("[", "")
            .split(",")
        )
        for i in range(len(results)):
            output = output + "x" + sub(i + 1) + "=" + results[i] + "\n"

    if id != "E" and id != "5" and id != "M" and id != "6" and id != "S" and id != "7":
        output = f"\n{super(y)}"
    print(output.replace("*", "·"))


def intgrt(y, t=1):
    y = symper(y)
    for _ in range(t):
        y = sp.integrate(y)
    return str(y)


def dfrnt(y, t=1):
    y = symper(y)
    for _ in range(t):
        y = sp.diff(y)
    return str(y)


def replacer(y):
    g = re.findall(r"([+-]?\d+x)", y)
    f = re.findall(
        r"\((?:\d*(?:x\^\d*)?)(?:[+-]?\d*(?:x\^\d*)?)*x?(?:[+-]?\d*(?:x\^\d*)?)?\)",
        y,
    )
    if f != []:
        if y.startswith(f[0]):
            f.remove(f[0])
        k = str(f)
    for _ in range(len(f)):
        y = y.replace(f[_], f[_].replace("(", "*("))
    for _ in range(len(g)):
        y = y.replace(g[_], g[_].replace("x", "*x"))
    t = y.replace("^", "**").replace("***", "**")

    return t


def symper(y: str):
    t = replacer(y)
    return pe(t)


def super(y: str):
    y = y.replace("**", "^")
    y = re.sub(r"\^x", "^(x)", y)
    out = re.sub(r"^\(?([0-9x]+(?:[./][0-9x]+)?)\)?", lambda m: to_super(m[1]), y)
    return out


def to_super(num: str):
    transl = str.maketrans("1234567890.x/()", "¹²³⁴⁵⁶⁷⁸⁹⁰ᐧˣ′⁽⁾")
    return num.translate(transl)


def sub(num: int):
    subscripts = "₀₁₂₃₄₅₆₇₈₉"
    result = ""
    for char in str(num):
        result += subscripts[int(char)]
    return result


def factor(y: str):
    y = symper(y)
    return str(sp.factor(y))


def c(t):
    z = t
    out = ""
    for i in range(t):
        if i != t - 1:
            out = out + " + C" + sub(i) + f"x^{z-1}"
            z -= 1
        elif i == t - 1:
            out = out + " + C" + sub(i)
    return out


def Area(y):
    global x
    ul = float(pe(input("Upper limit: ")))
    ll = float(pe(input("Lower limit: ")))
    y = pe(intgrt(y))
    yul = y.subs({x: ul})
    yll = y.subs({x: ll})
    result = positive(yul - yll)
    return f"Area: {result}"


def minmaxima(y):
    global x
    y = symper(y)
    df = sp.diff(y, x)
    critical_points = str(sp.solve(df, x))
    return critical_points


def positive(num):
    return num if num > 0 else -num


def validate(y):
    if "x" not in y:
        try:
            float(y)
        except ValueError:
            exit("Error: Variable 'x' not found.")

    t = re.findall(r"[^x0-9\/\.\+\*\^\(\)\s\-]", y)
    if t != [] and (
        ("l" not in str(t) and "o" not in str(t) and "g" not in str(t))
        and ("l" not in str(t) and "n" not in str(t))
    ):
        print(t)
        exit("Error: You didn't follow the rules for input")
    symper(y)


def smplfy(y):
    return super(str(sp.expand(sp.simplify(symper(y)))))


def root(y):
    global x
    y = symper(y)
    y = sp.solve(y, x)
    return y


if __name__ == "__main__":
    main()
