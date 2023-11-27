"""
 Game [rock/paper/scissors]
USING if-elif-and conditional statement
 """
import random
option = ["rock","paper","scissor"]
computer_choice = random.choice(option)
user_choice = input("Enter Your Choice [rock/paper/scissor] = ")

# IF-ELIF-AND CONDITION STATEMENT USE .

if user_choice=="rock" and computer_choice=="scissor":
    print("You Won")
elif user_choice=="paper" and computer_choice=="rock":
    print("You Won")
elif user_choice=="scissor" and computer_choice=="paper":
    print("You Won")
elif user_choice==computer_choice:
    print("Tied")
else:
    print(f"You Lost , computer choose {computer_choice}.")