from art import logo

def calculator(op,n1,n2):
    n1 = float(n1)
    n2 = float(n2)
    if op == "+":
        ans = n1 + n2
        return ans
    
    elif op == "-":
        ans = n1 - n2
        return ans
    
    elif op == "*":
        ans = n1 * n2
        return ans
    
    elif op == "/":
        ans = n1 / n2
        return ans
    
    
print(logo)
while True:
    n1 = (input("Enter 1st number: "))
    if not n1.isdigit():
        print("bro answer correctly")
    else:
        break


while True:
    print("+\n-\n*\n/")
    while True:
        op = input("Pick an operation: ")
        if op in ["+", "-", "*", "/"]:
            break
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
    while True:
        n2 = (input("Enter 2nd number: "))
        if not n2.isdigit():
            print("bro answer correctly")
        else:
            break
    result = calculator(op,n1,n2)
    print(f"{n1} {op} {n2} = {result}")
    cont_play = input(f"Do you want to continue calculating with {result}? [y/n]")
    if cont_play == "n":
        break
    else:
        n1 = result
        print (f"1st number: {n1}")


