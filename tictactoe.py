import time
e11 = e12 = e13 = e21 = e22 = e23 = e31 = e32 = e33 = '     '

def intro():
    print("""\n\n============= Welcome to the game of Tic Tac Toe =============
This is 2 player game where you wil be playing with your friend
\nHere's a guide for you :-
The blank grid is given to you. to fill the the boxes,you need 
to give coordinates of thate box. The format is <row_no.> <column_no.> 
where row is the horizontal axis and column is the vertical axis. For 
example, if you want to fill the box at thetop left corner, you need 
to give the coordinates as '1 1'.""")

def game_reset():
    try:
        global e11, e12, e13, e21, e22, e23, e31, e32, e33
        e11 = e12 = e13 = e21 = e22 = e23 = e31 = e32 = e33 = '     '
        choice = input("\nDO YOU WANT TO PLAY AGAIN: (Y/N)  ").strip().lower()
        if choice == 'y'or choice == 'yes':
            print("\nSURE !\n\n")
            main()
        elif choice == 'n' or choice == 'no':
            print("                               THANK YOU FOR PLAYING\n\n")
            
        else:
            print("\nINVALID INPUT, TRY AGAIN")
            game_reset()

    except KeyboardInterrupt:
        print("\nIntentional shut off, shutting off game!! \n")
    except not KeyboardInterrupt:
        print("\nAn Error occured, restarting the game!! \n")
        restart()

def game_check():
    global p1,p2
    if (e11==e21==e31=='  X  ') or (e12==e22==e32=='  X  ') or (e13==e23==e33=='  X  ') or (e11==e12==e13=='  X  ') or (e21==e22==e23=='  X  ') or (e31==e32==e33=='  X  ') or (e11==e22==e33=='  X  ') or (e13==e22==e31=='  X  '):
        if p1 == 'X':
            print('                                  PLAYER 1 WINS!')
            return 'completed'
        else:
            print('                                  PLAYER 2 WINS!')
    elif (e11==e21==e31=='  O  ') or (e12==e22==e32=='  O  ') or (e13==e23==e33=='  O  ') or (e11==e12==e13=='  O  ') or (e21==e22==e23=='  O  ') or (e31==e32==e33=='  O  ') or (e11==e22==e33=='  O  ') or (e13==e22==e31=='  O  '):
        if p1 == 'O':
            print('                                  PLAYER 1 WINS!')
            return 'completed'
        else:
            print('                                  PLAYER 2 WINS!')
    elif e11 != e12 != e13 != e11 != e12 != e13 != e11 != e12 != e13 != '     ':
        print('                                          DRAW!')
        return 'completed'

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
        return False

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
        return False

def restart():
    global e11, e12, e13, e21, e22, e23, e31, e32, e33
    e11 = e12 = e13 = e21 = e22 = e23 = e31 = e32 = e33 = '     '
    main()

def player_input():
    try:
        print_grid()
        while True:
            if p1 == 'X':
                player1 = input("PLAYER 1 select your block: ").strip().upper().replace(' ','')
                crs = cross(player1)
                if crs == False:
                    player1 = input("PLAYER 1 select your block: ").strip().upper().replace(' ','')
                    crs = cross(player1)
                print_grid()
                gamecheck = game_check()
                if gamecheck == 'completed':
                    break
                player2 = input("PLAYER 2 select your block: ").strip().upper().replace(' ','')
                crl = circle(player2)
                if crl == False:
                    player2 = input("PLAYER 2 select your block: ").strip().upper().replace(' ','')
                    crl = circle(player2)
                print_grid()
                gamecheck = game_check()
                if gamecheck == 'completed':
                    break

            elif p1 == 'O':
                player1 = input("PLAYER 1 select your block: ").strip().upper().replace(' ','')
                crl = circle(player1)
                if crl == False:
                    player1 = input("PLAYER 1 select your block: ").strip().upper().replace(' ','')
                    crl = circle(player1)
                print_grid()
                gamecheck = game_check()
                if gamecheck == 'completed':
                    break
                player2 = input("PLAYER 2 select your block: ").strip().upper().replace(' ','')
                crs = cross(player2)
                if crs == False:
                    player2 = input("PLAYER 2 select your block: ").strip().upper().replace(' ','')
                    crs = cross(player2)
                print_grid()
                gamecheck = game_check()
                if gamecheck == 'completed':
                    break
        game_reset()

    except KeyboardInterrupt:
        print("\nIntentional shut off, shutting off game!! \n")
    except not KeyboardInterrupt:
        print("\nAn Error occured, restarting the game!! \n")
        restart()

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
            print("Invalid input, please try again")
            print()
            main()
        player_input()

    except KeyboardInterrupt:
        print("\nIntentional shut off, shutting off game!! \n")
    except not KeyboardInterrupt:
        print("\nAn Error occured, restarting the game!! \n")
        restart()

if __name__ == "__main__":
    main()