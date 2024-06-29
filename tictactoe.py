#Setting the intial value of all boxes i.e. blank or whitespace
e11 = e12 = e13 = e21 = e22 = e23 = e31 = e32 = e33 = '     '

#Function to display introduction of the program and guide ob how to play 
def intro():
    print("""\n\n============= Welcome to the game of Tic Tac Toe =============
This is 2 player game where you wil be playing with your friend
\nHere's a guide for you :-
The blank grid is given to you. to fill the the boxes,you need 
to give coordinates of thate box. The format is <row_no.> <column_no.> 
where row is the horizontal axis and column is the vertical axis. For 
example, if you want to fill the box at thetop left corner, you need 
to give the coordinates as '1 1'.""")

#This function ask user whether to play again or not, if yes, it reset everybox for a new game and if no it shuts off the game 
def game_reset():
    try:
        global e11, e12, e13, e21, e22, e23, e31, e32, e33
        e11 = e12 = e13 = e21 = e22 = e23 = e31 = e32 = e33 = '     '             #Resetting every block to default value
        choice = input("\nDO YOU WANT TO PLAY AGAIN: (Y/N)  ").strip().lower()    #Asking to play again or not
        if choice == 'y'or choice == 'yes':
            print("\nSURE !\n\n")
            main()                                                                
        elif choice == 'n' or choice == 'no':
            print("                               THANK YOU FOR PLAYING\n\n")     
            
        else:
            print("\nINVALID INPUT, TRY AGAIN")
            game_reset()                                                          #If invalid input, trigger same function again

    except KeyboardInterrupt:                                                     #For intentional shut off during the game. Kill the the process in between
        print("\nIntentional shut off, shutting off game!! \n")
    except not KeyboardInterrupt:
        print("\nAn Error occured, restarting the game!! \n")                    #If any error occured, start afresh
        restart()

#Function to check winning or draw
def game_check():
    global p1,p2
    #Checking all possible winning conditions For X
    if (e11==e21==e31=='  X  ') or (e12==e22==e32=='  X  ') or (e13==e23==e33=='  X  ') or (e11==e12==e13=='  X  ') or (e21==e22==e23=='  X  ') or (e31==e32==e33=='  X  ') or (e11==e22==e33=='  X  ') or (e13==e22==e31=='  X  '):
        if p1 == 'X':
            print('                                  PLAYER 1 WINS!')
            return 'completed'
        else:
            print('                                  PLAYER 2 WINS!')
    
    #Checking all possible winning conditions For O
    elif (e11==e21==e31=='  O  ') or (e12==e22==e32=='  O  ') or (e13==e23==e33=='  O  ') or (e11==e12==e13=='  O  ') or (e21==e22==e23=='  O  ') or (e31==e32==e33=='  O  ') or (e11==e22==e33=='  O  ') or (e13==e22==e31=='  O  '):
        if p1 == 'O':
            print('                                  PLAYER 1 WINS!')
            return 'completed'
        else:
            print('                                  PLAYER 2 WINS!')
            
    #Checking for draw
    #Even if 8 out of 9 elements are not matching the winning conditions, declare DRAW.
    else:
        e_list = [e11,e12,e13,e21,e22,e23,e31,e32,e33]
        count = 0
        for i in e_list:
            if i != '     ':
                count += 1
        if count == 8:
            print('                                       DRAW!')
            return 'completed'

#Prints the Tic-tac-toe grid
def print_grid(): 
    print("\n                               ======TIKTACTOE======")
    print(f"""
                                 {e11}|{e12}|{e13}
                                 _____|_____|_____
                                 {e21}|{e22}|{e23}
                                 _____|_____|_____
                                 {e31}|{e32}|{e33}
                                      |     |      
            """)
    print("                               =====================\n")

#declares cross to particular coordinates
def cross(coords):
    global e11, e12, e13, e21, e22, e23, e31, e32, e33
    if coords == '11' and e11 == '     ':
        e11 = '  X  '
    elif coords == '12' and e12 == '     ':
        e12 = '  X  '
    elif coords == '13' and e13 == '     ':
        e13 = '  X  '
    elif coords == '21' and e21 == '     ':
        e21 = '  X  '
    elif coords == '22' and e22 == '     ':
        e22 = '  X  '
    elif coords == '23' and e23 == '     ':
        e23 = '  X  '
    elif coords == '31' and e31 == '     ':
        e31 = '  X  '
    elif coords == '32' and e32 == '     ':
        e32 = '  X  '
    elif coords == '33' and e33 == '     ':
        e33 = '  X  '
    else:
        print('You can\'t place a cross there!\n') 
        return False                              #If coordinate already filled or not available, return False

#declares cross to particular coordinates
def circle(coords):
    global e11, e12, e13, e21, e22, e23, e31, e32, e33    
    if coords == '11' and e11 == '     ':
        e11 = '  O  '
    elif coords == '12' and e12 == '     ':
        e12 = '  O  '
    elif coords == '13' and e13 == '     ':
        e13 = '  O  '
    elif coords == '21' and e21 == '     ':
        e21 = '  O  '
    elif coords == '22' and e22 == '     ':
        e22 = '  O  '
    elif coords == '23' and e23 == '     ':
        e23 = '  O  '
    elif coords == '31' and e31 == '     ':
        e31 = '  O  '
    elif coords == '32' and e32 == '     ':
        e32 = '  O  '
    elif coords == '33' and e33 == '     ':
        e33 = '  O  '
    else:
        print('You can\'t place a circle there!\n')
        return False                                 #If coordinate already filled or not available, return False

#Restart game from here if any error occurs
def restart():
    global e11, e12, e13, e21, e22, e23, e31, e32, e33
    e11 = e12 = e13 = e21 = e22 = e23 = e31 = e32 = e33 = '     '
    main()

#Function that takes input from players and triggers most of the functions of the program.
def player_input():
    try:
        print_grid()
        while True:
            if p1 == 'X':
                player1 = input("PLAYER 1 select your block: ").strip().upper().replace(' ','')
                crs = cross(player1)                                                    #Take coordinates and trigger function to place the element at required posn
                if crs == False:
                    player1 = input("PLAYER 1 select your block: ").strip().upper().replace(' ','')
                    crs = cross(player1)                                               #If function returns False, ask again
                print_grid()
                gamecheck = game_check()                    #Checks game condition
                if gamecheck == 'completed':
                    break                                   #break loop if game completed
                player2 = input("PLAYER 2 select your block: ").strip().upper().replace(' ','')
                crl = circle(player2)                                                 #Take coordinates and trigger function to place the element at required posn
                if crl == False:
                    player2 = input("PLAYER 2 select your block: ").strip().upper().replace(' ','')
                    crl = circle(player2)                                             #If function returns False, ask again
                print_grid()
                gamecheck = game_check()                  #Checks game condition
                if gamecheck == 'completed':
                    break                                 #break loop if game completed

            elif p1 == 'O':
                player1 = input("PLAYER 1 select your block: ").strip().upper().replace(' ','')
                crl = circle(player1)                                                    #Take coordinates and trigger function to place the element at required posn
                if crl == False:
                    player1 = input("PLAYER 1 select your block: ").strip().upper().replace(' ','')
                    crl = circle(player1)                                                #If function returns False, ask again
                print_grid()
                gamecheck = game_check()                  #Checks game condition
                if gamecheck == 'completed':
                    break                                 #break loop if game completed
                player2 = input("PLAYER 2 select your block: ").strip().upper().replace(' ','')
                crs = cross(player2)                                                     #Take coordinates and trigger function to place the element at required posn
                if crs == False:
                    player2 = input("PLAYER 2 select your block: ").strip().upper().replace(' ','')
                    crs = cross(player2)                                                 #If function returns False, ask again
                print_grid()
                gamecheck = game_check()                 #Checks game condition
                if gamecheck == 'completed':
                    break                                #break loop if game completed
        game_reset()

    except KeyboardInterrupt:
        print("\nIntentional shut off, shutting off game!! \n")
    except not KeyboardInterrupt:
        print("\nAn Error occured, restarting the game!! \n")
        restart()

#Main Function
def main():
    intro()
    try:
        global p1,p2
        p1= input("\nPLAYER 1, choose your character: X or O  ->  ").strip().upper()
        if p1 == 'X':
            p1, p2 = 'X','O'
            print(f"PLAYER 1: {p1}")
            print(f"PLAYER 2: {p2}")
        elif p1.upper() == 'O':
            p1, p2 = 'O','X'
            print(f"PLAYER 1: {p1}")
            print(f"PLAYER 2: {p2}")
        else:
            print("Invalid input, please try again\n")
            main()
        player_input()

    except KeyboardInterrupt:
        print("\nIntentional shut off, shutting off game!! \n")
    except not KeyboardInterrupt:
        print("\nAn Error occured, restarting the game!! \n")
        restart()

if __name__ == "__main__":
    main()
