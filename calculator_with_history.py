HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("NO HISTORY FOUND")
    else:
        for line in reversed(lines):
            print(line.strip())  
    file.close()        


def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("HISTORY IS CLEARED")


def save_to_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()


def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("INVALID INPUT, e.g: A + B = C")
        return 

    num1 = float(parts[0])
    op1 = parts[1]
    num2 = float(parts[2])

    if op1 == "+":
        result = num1 + num2
    elif op1 == "-":
        result = num1 - num2
    elif op1 == "*":
        result = num1 * num2
    elif op1 == "/":
        if num2 == 0:
            print("UNDEFINED")
            return
        result = num1 / num2
    else:
        print("Invalid Operator") 
        return

    if int(result) == result:
        result = int(result)
    print("Results:", result)
    save_to_history(user_input, result)


def main():
    print("<---SIMPLE CALCULATOR--->")
    while True:
        user_input = input("What do you want to do? --> Calculate / History / Clear / Exit: ")
        if user_input == "exit":
            print("THANK YOU, GOODBYE")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)  

main()              







