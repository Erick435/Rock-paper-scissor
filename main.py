import random

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

#Write your code below this line 👇

choices = [rock, paper, scissors]

user_input = input('''
Please enter a number (1 - 3) for your choice
                   
1) Rock
2) Paper
3) Scissors
''')

ai_choice = random.randint(0, 2)

# print(f"\nYou chose {choices[int(user_input)]}\n\n Your opponent chose {choices[int(ai_choice)]}")

if int(user_input) == 1:
    print(f"\n\nYou chose Rock {choices[int(user_input) - 1]}\n\nVERSUS\n\n")
    if ai_choice == 0:
        print(f"Rock{choices[0]}\n\nDRAW")
    if ai_choice == 1:
        print(f"Paper{choices[1]}\n\nPaper Beats Rock - You Lose")
    if ai_choice == 2:
        print(f"Scissors{choices[2]}\n\nRock Beats Scissors - You Win!")
elif int(user_input) == 2:
    print(f"\n\nYou chose Paper {choices[int(user_input) - 1]}\n\nVERSUS\n\n")
    if ai_choice == 0:
        print(f"Rock{choices[0]}\n\nPaper Beats Rock - You Win!")
    if ai_choice == 1:
        print(f"Paper{choices[1]}\n\nDRAW")
    if ai_choice == 2:
        print(f"Scissors{choices[2]}\n\nScissors Beats Paper - You Lose")
elif int(user_input) == 3:
    print(f"\n\nYou chose Scissors {choices[int(user_input) - 1]}\n\nVERSUS\n\n")
    if ai_choice == 0:
        print(f"Rock{choices[0]}\n\n Rock beats Scissors - You Lose")
    if ai_choice == 1:
        print(f"Paper{choices[1]}\n\nScissors Beats paper - You Win!")
    if ai_choice == 2:
        print(f"Scissors{choices[2]}\n\nDRAW")
