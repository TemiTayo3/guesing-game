print('Hello there this is a guessing game, just guess the correct number to win an amazing prize.')
name = input("Please enter your name " )
userGuess = input('Enter your guess ')
numbers = ["3", "12", "30", "17" "55" "32" "38" "73"] 

if userGuess in numbers:
    print('Congratulations ' + name + ' you just won a brand new laptop!!!')
else:
    print('Sorry ' + name + ' you lost, better luck next time.')