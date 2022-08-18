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


n=int(input("choose a number"))
#Write your code below this line 👇
a=random.randint(0,2)
if n==0 and a==0:
  print(scissors)
  print(scissors)
  
  print("draw")
if n==1 and a==0:
  print(rock)
  print(scissors)
  print("win")
if n==2 and a==0:
  print(paper)
  print(scissors)
  print("loss")
if n==0 and a==1:
  print(scissors)
  print(rock)
  print("loss")
if n==1 and a==1:
  print(rock)
  print(rock)
  print("draw")
if n==2 and a==1:
  print(paper)
  print(rock)
  print("win")
if n==0 and a==2:
  print(scissors)
  print(paper)
  print("loss")
if n==1 and a==2:
  print(rock)
  print(paper)
  print("win")
if n==2 and a==2:
  print(paper)
  print(paper)
  print("draw")




  

  

