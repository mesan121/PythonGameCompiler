import random

#First game function Rock Paper Scissors
def rock_paper_scissors():
  #confirms user wants to play
  global confirm
  confirm = input("Hey and welcome to the rock, paper, and scissors game! print y to continue and q to exit: ")

  if confirm == "y":
    print("Great let's start")
  else:
    quit()
  
  #Users options/computers options
  global options
  options = ["rock", "paper", "scissors"]
  
  global user_score
  user_score = 0

  global computer_score
  computer_score = 0
  #scans who wins the game overall
  global scanner
  def scanner():
    if user_score > computer_score:
      print("You won! Congrats! You scored", str(user_score), "while the computer score", computer_score,".")
    elif user_score < computer_score:
      print("You lost! You scored", str(user_score), "while the computer scored", computer_score,".")
    elif user_score == computer_score:
      print("No one won! It's a tie! You both scored", str(computer_score),".")

  while True:
    global user_pick
    user_pick = input("type either rock paper or scissors and q to exit: ").lower()

    if user_pick == "q":
      scanner()
      quit()

    global random1
    random1 = random.randint(0, 2)

    global computer_pick
    computer_pick = options[random1]

    #checks who wins in 1 round
    if user_pick == "rock" and computer_pick == "scissors":
      print("You won! The computer chose", computer_pick + ".")
      user_score += 1
    elif user_pick == "paper" and computer_pick == "rock":
      print("You won! The computer chose", computer_pick + ".")
      user_score += 1
    elif user_pick == "scissors" and computer_pick == "paper":
      print("You won! The computer chose", computer_pick + ".")
      user_score += 1
    elif user_pick == computer_pick:
      print("No one won! The computer also chose", computer_pick + ".")
    else:
      print("You lost! the computer chose", computer_pick + ".")
      computer_score += 1


def Guess_Number():
  global number
  number = random.randint(1, 25)
  
  global Tries
  Tries = 0

  print("Hello and welcome to my game!")

  global confirm
  confirm = input("Do you want to continue? If you do type yes: ")

  if confirm.lower() == "yes":
   print("Okayyy let's begin!")
  else:
   print("Aww maybe next time then:(")
   quit()
  
  global Guess
  Guess = input("Pick a random number from 1-25 and hopefully you get it right:")
  
  #checks if user input is a number
  if Guess.isdigit:
   Guess = int(Guess)
  
  #scans if the computer generated number is either lower or higher from yours
  global scan
  def scan():
    if Guess < int(number):
     print("It was higher")
    else:
     if Guess > number:
      print("It was lower")
  
  #shows amount of tries it took user to guess
  if Guess == number:
   print("You got it!")
   print("It only took you 1 try!")
  else:
   Tries += 1
   scan()
   print("")
   print("Try again")
   print("")
  
  #while loop to repeat the program if user is wrong
  while Guess != number:
   Guess = input("Pick a random number and hopefully you get it right:")
   if Guess.isdigit:
    Guess = int(Guess)

   if Guess == number:
    print("You got it!")
    print("Let's play again next time!")
    print("It took you " + str(Tries) + " tries to get it correct.")
    print("")
    quit()
   else:
    Tries += 1
    scan()
    print("Try again")
    print("")
    print("")

#Lotto A.I. Game
def lotto():
  print("Hello and welcome to this Lotto simulation")
  print("")
  print("Just type in a number from 1-45 and let's see if you get lucky")
  print("")
  print("Do you want a hint?")
  
  #the isx picks of the computer
  global computer_pick
  computer_pick = [random.randint(1,45), random.randint(1,45), random.randint(1,45), random.randint(1,45), random.randint(1,45), random.randint(1,45)]
  
  global hint
  hint = input("Type y if you want a hint and no if not: ")
  
  #function that will randomly give player a hint and which place from the 6
  global hint_confirmed
  def hint_confirmed():
    global generated_hint
    generated_hint = random.randint(0, 5)

    global random_hint
    random_hint = computer_pick[generated_hint]
    
    #Says which place the hint is
    if random_hint == computer_pick[0]:
      print("The hint is the first number which is", random_hint)
    elif random_hint == computer_pick[1]:
      print("The hint is the second number which is", random_hint)
    elif random_hint == computer_pick[2]:
      print("The hint is the third number which is", random_hint)
    elif random_hint == computer_pick[3]:
      print("The hint is the fourth number which is", random_hint)
    elif random_hint == computer_pick[4]:
      print("The hint is the fifth number which is", random_hint)
    elif random_hint == computer_pick[5]:
      print("The hint is the sixth number which is", random_hint)

  
  if hint == "y":
    hint_confirmed()
  
  #checks if user is giving the right input
  global userpick1
  userpick1 = input("Number from 1-45: ")
  if userpick1.isdigit:
    userpick1 = int(userpick1)

  if userpick1 > 45:
    print("ERROR number given is higher than 45")
    print("Try Again")
    quit
  elif userpick1 < 1:
    print("ERROR number given is lower than 1")
    print("Try Again")
    quit
  
  global userpick2
  userpick2 = input("Number from 1-45: ")
  if userpick2.isdigit:
    userpick2 = int(userpick2)

  if userpick2 > 45:
    print("ERROR number given is higher than 45")
    print("Try Again")
    quit
  elif userpick2 < 1:
    print("ERROR number given is lower than 1")
    print("Try Again")
    quit

  global userpick3
  userpick3 = input("Number from 1-45: ")
  if userpick3.isdigit:
    userpick3 = int(userpick3)

  if userpick3 > 45:
    print("ERROR number given is higher than 45")
    print("Try Again")
    quit
  elif userpick3 < 1:
    print("ERROR number given is lower than 1")
    print("Try Again")
    quit

  global userpick4
  userpick4 = input("Number from 1-45: ")
  if userpick4.isdigit:
    userpick4 = int(userpick4)

  if userpick4 > 45:
    print("ERROR number given is higher than 45")
    print("Try Again")
    quit
  elif userpick4 < 1:
    print("ERROR number given is lower than 1")
    print("Try Again")
    quit

  global userpick5
  userpick5 = input("Number from 1-45: ")
  if userpick5.isdigit:
    userpick5 = int(userpick5)

  if userpick5 > 45:
    print("ERROR number given is higher than 45")
    print("Try Again")
    quit
  elif userpick5 < 1:
    print("ERROR number given is lower than 1")
    print("Try Again")
    quit

  global userpick6
  userpick6 = input("Number from 1-45: ")
  if userpick6.isdigit:
    userpick6 = int(userpick6)

  if userpick6 > 45:
    print("ERROR number given is higher than 45")
    print("Try Again")
    quit
  elif userpick6 < 1:
    print("ERROR number given is lower than 1")
    print("Try Again")
    quit
  
  #all the picks of said user
  userpicks = [userpick1, userpick2, userpick3, userpick4, userpick5, userpick6]
  
  #checks if userpicks matches computer picks
  if userpicks == computer_pick:
    print("WOOOOOOOOOWW CONGRAAAAATSS")
    print("These are the computer picks", computer_pick)
    print("These are your picks", userpicks)
  elif userpicks != computer_pick:
    print("Better luck next time!")
    print("These are the computer picks", computer_pick)
    print("These are your picks", userpicks)
  
#Starting message
user_choice = input("Hey and welcome to my game inventory!! Pick a game from 3 options. Type RPS for rock paper scissors, NGG for the number guessing game, and LOTTO for the LOTTO AI game! if you wanna stope just type q to quit. Have Fun!!: ")

#Pick a game 
if user_choice == "RPS":
  rock_paper_scissors()
elif user_choice == "NGG":
  Guess_Number()
elif user_choice == "LOTTO":
  lotto()
elif user_choice == "q":
  quit
else:
  quit
  

  


  #Check if you can add a list of games