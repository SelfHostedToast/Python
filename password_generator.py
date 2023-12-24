import random
numbers_list = ["0","1","2","3","4","5","6","7","8","9"]
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols_list = ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]","|",":",";","<",">","?"]
print("Welcome to the PyPassword Generator!")
letter_amount = int(input('How many letters would you like in your password?\n'))
if letter_amount > 0:
  letter_selection = ""
  symbol_selection = ""
  number_selection = ""

  for letters in range(0, letter_amount):
    letter_selection += str(random.choice(letters_list))
  symbol_amount = int(input('How many symbols would you like in your password?\n'))
  for symbols in range(0, symbol_amount):
    symbol_selection += str(random.choice(symbols_list))
  number_amount = int(input('How many numbers would you like in your password?\n'))
  for numbers in range(0, number_amount):
          number_selection += str(random.choice(numbers_list))

print(f"Your letters generated: {letter_selection}")
print(f"Your symbols generated: {symbol_selection}")
print(f"Your numbers generated: {number_selection}")

password = letter_selection + symbol_selection + number_selection
password_list = list(password)
password_shuffle = random.shuffle(password_list)
final_password = ''.join(random.sample(password_list,len(password_list)))

print(f"Your strong password is : {final_password}")