#Function is used cause it is a reusable block of code
def get_number(number):#Paramater used so that you can pass a value to the function and tat function can use that value
    while True:
        operand = input("Number " + str(number) + ": ")
        try: # try is used so that instead of throwing an error it will allow us to handle it
            return float(operand)
        except:
            print("Invalid number, try again.")

operand = get_number(1)
operand2 = get_number(2)
sign = input("Sign: ")

result = 0
    
if sign ==  "+":
    result = operand + operand2
elif sign ==  "-":
    result = operand - operand2
elif sign ==  "/":
    if operand2 != 0:
        result = operand / operand2
    else:
            print("Division by zero.")
elif sign ==  "*":
    result = operand * operand2
else:
    print("Invalid sign")
   
print(result)