import random
import string

adjectives = ['poor','rich','good','slow','fast','sleepy','smelly','wet','fat'\
             'proud','brave']
nouns = ['apple','dinosaur','ball','toaster','goat','dragon','hammer','duck','panda','telephone','banana','teacher','flower']
colours = ['red','blue','pink','orange','black','yellow','green','grey','silver','gold','white','purple']

print("Welcome to PASSWORD PICKER 1.0")
while True:
    for num in range(3):
        adj = random.choice(adjectives)
        nou = random.choice(nouns)
        col = random.choice(colours)
        number = random.randrange(0,100)
        special_char = random.choice(string.punctuation)

        password = adj + nou + col + str(number) + special_char
        print ("Your New Password is : {}".format(password))
    response = input("Would you like another password? Type y or n: ")
    if response == 'n':
        break


