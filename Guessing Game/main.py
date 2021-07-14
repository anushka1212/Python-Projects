import art
import random

print(art.logo)
print("Welcome to the guessing game\n");
print("I'm thinking of a number between 1 to 100\n");
c = input("Choose a difficulty leve. Type 'easy' or 'hard': ").lower();
n = random.randint(1, 100)
flag = 0
if c == 'easy':
    i = 10;
else:
    i = 5;
while i > 0:
    print(f"You have {i} attempts remaining to guess the number");
    g = int(input("Make a guess: "));
    if g > n:
        print("Too high")
    elif g < n:
        print("Too low")
    else:
        print(f"You got it! The answer is {g}.");
        flag = 1;
        break;
    i -= 1;
if flag == 0:
    print("You've run out of guesses, you lose.");
