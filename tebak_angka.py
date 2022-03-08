import random

topOfRange = input("Ketik angka: ")

if topOfRange.isdigit():
    topOfRange = int(topOfRange)

    if topOfRange <= 0:
        print("Tolong ketik nomor lebih besar dari 0!")
else:
    print("Tolong ketik nomor")

randomNumber = random.randint(0, topOfRange)
guesses = 0 
while True:
    guesses += 1
    userGuess = input("Tebak angka: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("Tolong ketik nomor.")
        continue

    if userGuess == randomNumber:
        print("You got it!")
        break
    else:
        if userGuess > randomNumber:
            print("You were above the number!")
        else:
            print("You were below the number! ")

print("Kamu dapat menebak dalam " + str(guesses) + " tebakan")