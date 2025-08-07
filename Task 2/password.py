import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

try:
	length = int(input("Enter the length of your password: "))
	password = []
	password += random.choices(chars, k=length)
	random.shuffle(password)
	password = ''.join(password)    
	print(f"Your required password is: {password}")
except ValueError:
	print("Please enter a valid number.")