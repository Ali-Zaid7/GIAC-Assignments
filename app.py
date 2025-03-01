import random

print("""Welcome to the game this is a number guessing name \n
  You get a five attempts to guess the number  """)
number_to_guess = random.randrange( 50 ,100)
chances = 5
guess_counter = 0

while guess_counter < chances :
 guess_counter +=1
 my_guess = int(input("Please Enter your guess: "))

 if my_guess == number_to_guess: 
   print(f"The number is {number_to_guess} and you find it right! in the {guess_counter} attempt")
   break

 elif guess_counter >= chances and my_guess != number_to_guess:
   print(f"Oooo..ps the number is {number_to_guess} good luck! /n try next time")

 elif my_guess > number_to_guess:
   print("Your guess is very high try again")

 elif my_guess < number_to_guess:
  print("Your guess is very low try again")
