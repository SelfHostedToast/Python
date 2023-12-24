name1 = input("What is the first name? ") # What is your name?
name2 = input("What is the second name? ") # What is their name?

names_combined = name1 + name2
names_combined = names_combined.lower()

T = names_combined.count('t')
R = names_combined.count('r')
U = names_combined.count('u')
E = names_combined.count('e')

true = T + R + U + E

L = names_combined.count('l')
O = names_combined.count('o')
V = names_combined.count('v')
E = names_combined.count('e')

love = L + O + V + E

true_love_score = str(true) + str(love)
true_love_score = int(true_love_score)

if true_love_score < 10 or true_love_score > 90:
  print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif true_love_score > 40 and true_love_score < 50:
  print(f"Your score is {true_love_score}, you are alright together.")

else:
  print(f"Your score is {true_love_score}.")

