# The volume of a sphere with radius r is (4/3)* pie * r**2. 
# What is the volume of the sphere with radius 5. 
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places
radius = float(input("Enter the radius: ")) 
pie = (22/7)
volume_of_sphere = (4/3) * pie * radius**2
print(f"The volume of the sphere is {volume_of_sphere:.2f}")

# Create a program to calculate the area of a triangle (1/2 * base * height). 
# Base and height should be entered using the keyboard. 
base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
area = (1/2) * base * height
print(f"The area of the triangle is {area} square cm")

# WITI has tasked you to automate a simple grading system. 
# As a python student, write a program using  to display the grades that 
# the students will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89%   Grade is  B
# 70% - 79%   Grade is C                                                        
# 60% - 69%   Grade is D                  
# 50% - 59%   Grade is E  
# < 50% Fail 
mark = int(input("Enter the marks: "))
if 90 <= mark <= 100:
    print("The grade is A")
elif 80 <= mark <= 89:
    print("The grade is B")
elif 70 <= mark <= 79:
    print("The grade is C")
elif 60 <= mark <= 69:
    print("The grade is D")
elif 50<= mark <= 59:
    print("The grade is E")
else:
    print("fail")

#  WITI Academy is proposing a Sacco to help students save their money. 
#  Design a platform that will do the following.
#  Welcome to, WITIAcademy Sacco.
#  1. Deposit Money
#  2. Withdraw Money
#  3. Check Balance
#  Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#  If the student selects 3, the account balance should be displayed.
balance = 0  

print("Welcome to WITI Academy Sacco")
print("\nPlease choose an option:")
print("1. Deposit Money")
print("2. Withdraw Money")
print("3. Check Balance")

choice = input("Enter your choice (1/2/3): ")
if choice == '1':  
    amount = float(input("Enter amount to deposit: "))
    if amount >= 1000:
        balance += amount
        print(f"Successfully deposited {amount}. New balance is {balance}.")
    else:
        print("Minimum deposit amount is 1000.")
elif choice == '2': 
    amount = float(input("Enter amount to withdraw: "))
    if amount >= 500:
        if balance >= amount:
            balance -= amount
            print(f"Successfully withdrew {amount}. New balance is {balance}.")
        else:
            print("Insufficient balance.")
    else:
        print("Minimum withdrawal amount is 500.")
elif choice == '3':  # Check Balance
    print(f"Your current balance is {balance}.")
else:
    print("Invalid choice.")

