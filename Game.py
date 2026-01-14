import random
''' for 1 is snake 
    for 2 is water
    for 3 is gun
    '''

# Dictionary mapping
choices = {
    1: "Snake",
    2: "Water",
    3: "Gun"
}

print("Welcome to Snake–Water–Gun Game ")
print("1. Snake")
print("2. Water")
print("3. Gun")

user = int(input("Enter your choice (1/2/3): "))

computer = random.randint(1, 3)

print("\nYou choose:", choices[user])
print("Computer choose:", choices[computer])

# Game Logic
if user == computer:
    print("Result: It's a DRAW ")

elif user == 1 and computer == 2:
    print("Result: You WIN  (Snake drinks Water)")

elif user == 2 and computer == 3:
    print("Result: You WIN  (Water damages Gun)")

elif user == 3 and computer == 1:
    print("Result: You WIN  (Gun kills Snake)")

else:
    print("Result: You LOSE ")