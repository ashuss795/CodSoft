n1=float(input("Enter the first number: "))
n2=float(input("Enter the second number: "))

print("Select operation:")
print("Addition(+)")
print("Subtraction(-)")
print("Multiplication(*)")
print("Division(/)")

ch=input("Enter your choice: ") 
if ch=='+':
    print(n1,"+",n2,"=",n1+n2)
elif ch=='-':
    print(n1,"-",n2,"=",n1-n2)  
elif ch=='*':
    print(n1,"*",n2,"=",n1*n2)
elif ch=='/':
    if n2 != 0:
        print(n1,"/",n2,"=",n1/n2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")

print("Thanks for using our tool!.")