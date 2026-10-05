def calculate(data: dict):
    num1 = float(data["num1"])
    opt = data["opt"]
    num2 = float(data["num2"])
    print("Number 1: ", num1)
    print("Number 2: ", num2)
    print("Operation: ", opt)
    try:
        if opt == "+":
            data["result"] = num1 + num2
        elif opt == "-":
            data["result"] = num1 - num2
        elif opt == "*":
            data["result"] = num1 * num2
        elif opt == "/":
            data["result"] = num1 / num2
        else:
            return {"message:" "Invalid operation"}
    except ArithmeticError:
        print("Arithmetic error thrown.")
        return 0
    except TypeError:
        print("Type error thrown. Do not mix strings and numeric types.")
        return 0
    return {"message": "Success", "data": data}
