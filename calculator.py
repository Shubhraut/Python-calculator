#Calculator using functions

#Creating functions for various operations
#This function will add both values
def add(a,b) :
	return a+b
	
#This function will subtract both values
def sub(a,b):
	return a-b
	
#This function will divide both values
def div(a,b):
	return a/b
	
#This function will multiply both values
def mul(a,b):
	return a*b
	
#Operator options available
print(" Welcome to calculator")
print()
print(" Your choices are...")
print()
print(" 1. Addition")
print(" 2. Subtraction")
print(" 3. Division")
print(" 4. Multiplication")
print()

#Taking choice from input

choices= input(" Enter your choice 1/2/3/4 :- ")
print()
#now assigning user input values

if choices in ('1','2','3','4'):
	
	num1= float(input(" Enter 1st number:- "))
	num2=float(input(" Enter 2nd number:- "))
	print()
	
#Here it will check the conditions and pass the command

	if choices=='1':
		print(num1, "+", num2, "=", add(num1, num2))
	
	elif choices=='2':
		print(num1, "-", num2, "=", sub(num1, num2))
	
	elif choices=='3':
		print(num1, "/", num2, "=", div(num1, num2))
	
	elif choices=='4':
		print(num1, "x", num2, "=", mul(num1, num2))

#If all the above commands get rejected then it will solve this part

else:
	print("Invalid operation")
