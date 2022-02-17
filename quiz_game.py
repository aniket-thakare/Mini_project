print('\033[38;5;206m','\033[21m',"###### Welcome to Quiz Game! ######",'\033[0m','\033[3m')

playin = input("Do you want to play Game? -->>  ")

if playin.lower() != "yes":
    quit()

print("Shuffling Question's For You 😎")
Score = 0

ans = input("Who invented the Light Bulb? --> ")
if ans.lower() == "thomas alva edison":
    print('Correct !')
    Score += 1
else:
    print('Wrong Answer !')

ans = input("Which is the hottest planet in our solar system? --> ") 
if ans.lower() == "venus":
    print('Correct !')
    Score += 1
else:
    print('Wrong Answer !')

ans = input("What is the National Flower of India? --> ")  
if ans.lower() == "lotus":
    print('Correct !')
    Score += 1
else:
    print('Wrong Answer !')

ans = input("Which planet is nearest to Earth? --> ")  
if ans.lower() == "venus":
    print('Correct !')
    Score += 1
else:
    print('Wrong Answer !')

ans = input("Which is the largest continent? --> ")  
if ans.lower() == "asia":
    print('Correct !')
    Score += 1
else:
    print('Wrong Answer !')

ans = input("Who founded Facebook? --> ")  
if ans.lower() == "mark zuckerberg":
    print('Correct !')
    Score += 1
else:
    print('Wrong Answer !')

ans = input("1024 Kilobytes is equal to? --> ")  
if ans.lower() == "1mb":
    print('Correct !')
    Score += 1
else:
    print('Wrong Answer !')

ans = input("Brain of computer is? --> ")  
if ans.lower() == "cpu":
    print('Correct !')
    Score += 1
else:
    print('Wrong Answer !')

ans = input("Which is the longest river on the earth? --> ")  
if ans.lower() == "nile":
    print('Correct !')
    Score += 1
else:
    print('Wrong Answer !')

ans = input("Smallest state of India is? --> ")  
if ans.lower()== "goa":
    print('Correct !')
    Score += 1
else:
    print('Wrong Answer !')

if Score<= 3 :
    print(f'You Get {Score} Answer Correct , Do Better Next Time 😤')
elif Score <= 7 :
    print(f'You Get {Score} Answer Correct , Nice But You Can Get Correct Next Time .. OK 😎')    
else :
    print(f'You Get {Score} Answer Correct , You Are Awesom.. Hureeeeee 🥳')
    