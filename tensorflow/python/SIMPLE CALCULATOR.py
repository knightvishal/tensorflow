print("""\t\tSIMPLE CALCULATOR\n""")
print("""\t\tPress 1 for ADD\n\t\tPress 2 for SUB\n\t\tPress 3 for MUL\n\t\tPress 4 for DIV""")
num1=float(input("Enter the number 1 :"))
num2=float(input("Enter the number 2 :"))

choice=int(input("SELECT OPERATION :"))
if choice==1:
    result=num1+num2
elif choice==2:
    result=num1-num2
elif choice==3:
    result=num1*num2
elif choice==4:
    result=num1/num2
else:
    result=("INVALID ATTEMPT")
print (result)
