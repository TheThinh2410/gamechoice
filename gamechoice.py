print('''TheThinh Tran
gamelogger.py
October 9th, 2025
CISW 24'''
)
import sys
import os 
import datetime

timestamp = datetime.datetime.now()
timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

def myLogger(s):
    logEntry = timestamp + " " + s + "\n"
    logFile = open('log.txt', 'a+')
    logFile.write(logEntry)
    logFile.close()


playerName= input("Player: What is your name? ")
player_entry = "New Player Entry: " + playerName; 
myLogger(player_entry)

game_played=0
wins = 0
losses = 0

lets_play = input('Would you like to play a game? (y/n/q): ')
if lets_play == 'n':
    player_stats = "Totals: wins - {} losses - {}".format(wins,losses)
    myLogger(player_stats)
    player_quit= "Player " + playerName + "stop playing"
    myLogger (player_quit)
    print('Thank you for playing. Good bye.')
    sys.exit()
elif lets_play == 'q':
    player_stats = "Totals: wins - {} losses - {}".format(wins,losses)
    myLogger(player_stats)
    player_quit= "Player " + playerName + "stop playing"
    myLogger (player_quit)
    print('Thank you for playing. Good bye.')
    sys.exit()



while True:
    game_choice=input('''
    Choose a game or quit:
        1) Tic, Tac, Toe
        2) Rock, Paper, Scissors
        3) The Game 21
        q) to quit
    Enter your choice: ''')

    
    if game_choice == '1':
            player_game_choice = playerName + " chose Tic, Tac, Toe."
            myLogger(player_game_choice)
            print('You chose Tic, Tac, Toe! Have a nice game.')
            result = input("Did you win or lose? (w/l): ").lower()
            if result == "w":
                wins +=1 
            elif result == "l":
                losses+=1 
            else:
                print("Invalid input. Please enter 'w' or 'l'.")

    elif game_choice == '2':
            player_game_choice = playerName + " chose RPS."
            myLogger(player_game_choice)
            print('You chose Rock, Paper, Scissors! Have a nice game.')
            result = input("Did you win or lose? (w/l): ").lower()
            if result == "w":
                wins +=1 
            elif result == "l":
                losses+=1 
            else:
                print("Invalid input. Please enter 'w' or 'l'.")
    
    elif game_choice == '3':
            player_game_choice = playerName + " chose The Game 21."
            myLogger(player_game_choice)
            print('You chose The Game 21! Have a nice game.')
            result = input("Did you win or lose? (w/l): ").lower()
            if result == "w":
                wins +=1 
            elif result == "l":
                losses+=1 
            else:
                print("Invalid input. Please enter 'w' or 'l'.")
    else:
            print('Invalid choice, please try again.')

    play_again = input("Would you like to play another game? (y/n/q): ")
    
    if play_again.lower() == 'y':
        continue  

    elif play_again.lower() == 'n'or'q':
        
        player_stats = "Totals: wins - {} losses - {}".format(wins,losses)
        myLogger(player_stats)

        print("Thanks for playing! Goodbye.")
        player_quit= "Player " + playerName + " stop playing"
        myLogger (player_quit)
        sys.exit()
    else:
        print("Invalid choice. Exiting.")
        sys.exit()

    
