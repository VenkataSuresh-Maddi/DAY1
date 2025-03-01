import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9',]
symbols = ['!','#','$','%','&','*','+','@']
print("Welcome to password Generator!")
while True:
    user_choice = input("Select password level? Type Easy or Hard\n").lower()
    if user_choice in ("easy", "hard"):
        break
    else:
        print("Invalid option. Please type 'easy' or 'hard'.")
password_letters = int(input("How many letters would you like in your password?\n"))
password_symbols = int(input(f"How many symbols would you like?\n"))
password_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level
if user_choice == "easy":
    password = ""
    for char in range (0, password_letters):
        password += random.choice(letters)
    for char in range (0, password_letters):
        password += random.choice(symbols)
    for char in range (0, password_letters):
        password += random.choice(numbers)
    print(f"Your password is: {password}")

# Hard Level
elif user_choice == "hard":
    password_list = []
    for char in range (0, password_letters):
        password_list.append(random.choice(letters))
    for char in range (0, password_letters):
        password_list.append(random.choice(symbols))
    for char in range (0, password_letters):
        password_list.append(random.choice(numbers))
    print(password_list)
    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")
