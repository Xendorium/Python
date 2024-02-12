# calculator

def add(n1, n2):
    """Add numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Subtract numbers"""
    return n1 - n2


def multiply(n1, n2):
    """multiply numbers"""
    return n1 * n2


def divide(n1, n2):
    """divide numbers"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculation():
    num1 = float(input("Write first number: "))
    while True:
        for symbol in operations:
            print(symbol)
        operation = input("Pick operation from above: ")
        num2 = float(input("Write second number: "))
        function = operations[operation]
        answer = function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        pick = input(f"Type 'y' to continue calculating with {answer} or type 'n' to calculate with the new one: ")
        if pick == "y":
            num1 = answer
        elif pick == "n":
            calculation()

calculation()