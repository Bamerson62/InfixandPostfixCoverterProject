from postfix_evaluator import evaluate_postfix
from infix_converter import infix_to_postfix

postfix_tests = [
    "5 3 +",
    "8 2 - 3 +",
    "5 3 8 * +",
    "6 2 / 3 +",
    "5 8 + 3 -",
    "5 3 + 8 *",
    "8 2 3 * + 6 -",
    "5 3 8 * + 2 /",
    "8 2 + 3 6 * -",
    "5 3 + 8 2 / -"
]

infix_tests = [
    "A + B",
    "A + B * C",
    "( A + B ) * C",
    "A * B + C / D",
    "( A + B ) * ( C - D )",
    "A + B * C - D / E",
    "A * ( B + C ) / D",
    "( A + B * C ) / ( D - E )",
    "A + ( B - C ) * D",
    "( A + B * ( C - D ) ) / E"
]

def main():
    print("----- Postfix Evaluator -----")
    for expr in postfix_tests:
        result = evaluate_postfix(expr)
        print(f"[{expr}] = {result}")

    print("\n----- Infix to Postfix Converter -----")
    for expr in infix_tests:
        converted = infix_to_postfix(expr)
        print(f"[{expr}] -> [{converted}]")

if __name__ == "__main__":
    main()

