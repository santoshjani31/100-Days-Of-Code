rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
optionstxt = ["Rock", "Paper", "Scissors"]
import random

# Player Choice
choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors?\n"))

# Computer Choice
comp_sel = random.randint(0, 2)
print(comp_sel)

if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(options[choice])
    print("Computer selects:")
    print(optionstxt[comp_sel])
    print(options[comp_sel])

    if choice == 0 and comp_sel == 2:
        print("You Win!")
    elif comp_sel == 0 and choice == 2:
        print("You Lose!")
    elif comp_sel > choice:
        print("You Lose!")
    elif choice > comp_sel:
        print("You Win!")
    elif choice == comp_sel:
        print("It's A Draw")

# This code is a long way of doing it but still works
# if (choice == 0):
#  if (comp_sel == 0):
#    print(options[choice] + "\n" + "Computer choose:\n" + optionstxt[comp_sel] + "\n" + options[comp_sel] + "\n" + \
#    "It's A Draw")
#  elif (comp_sel == 1):
#    print(options[choice] + "\n" + "Computer choose:\n" + optionstxt[comp_sel] + "\n" + options[comp_sel] + "\n" + \
#    "Computer Wins!")
#  elif (comp_sel == 2):
#    print(options[choice] + "\n" + "Computer choose:\n" + optionstxt[comp_sel] + "\n" + options[comp_sel] + "\n" + \
#    "You Win!")
# elif (choice == 1):
#  if (comp_sel == 0):
#    print(options[choice] + "\n" + "Computer choose:\n" + optionstxt[comp_sel] + "\n" + options[comp_sel] + "\n" + \
#    "You Win!")
#  elif (comp_sel == 1):
#    print(options[choice] + "\n" + "Computer choose:\n" + optionstxt[comp_sel] + "\n" + options[comp_sel] + "\n" + \
#    "It's A Draw")
#  elif (comp_sel == 2):
#    print(options[choice] + "\n" + "Computer choose:\n" + optionstxt[comp_sel] + "\n" + options[comp_sel] + "\n" + \
#    "Computer Wins!")
# elif (choice == 2):
#  if (comp_sel == 0):
#    print(options[choice] + "\n" + "Computer choose:\n" + optionstxt[comp_sel] + "\n" + options[comp_sel] + "\n" + \
#    "Computer Wins!")
#  elif (comp_sel == 1):
#    print(options[choice] + "\n" + "Computer choose:\n" + optionstxt[comp_sel] + "\n" + options[comp_sel] + "\n" + \
#    "You Win!")
#  elif (comp_sel == 2):
#    print(options[choice] + "\n" + "Computer choose:\n" + optionstxt[comp_sel] + "\n" + options[comp_sel] + "\n" + \
#    "It's A Draw")
# else:
#  print (f"{choice} is an invalid option. Please try again!")
