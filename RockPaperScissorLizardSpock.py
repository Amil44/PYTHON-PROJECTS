import random

print('[y] -- new game\n\
[e] -- exit\n\
[a] -- about the game\n')

while True:
    menu = input('Select([y] or [e] or [a]): ')
    match menu:
        case 'y':
            print('[t] -- two players mode\n\
[c] -- play with computer\n')
            
            game_mode = input()
            match game_mode:
                case 't':
                    who_wins_p1_p2 = 0
                    for round in range(3, 0, -1):
                        print(f'\nYou have {round} rounds!')

                        Player1 = input("Player 1 is choosing...\n\
        [r] -- rock\n\
        [s] -- scissors\n\
        [k] -- spoke\n\
        [l] -- lizard\n\
        [p] -- paper\n")
                        
                        if Player1 =='r' or Player1 =='s' or Player1 =='k' or Player1 =='l' or Player1 =='p':
                            Player2 = input("Player 2 is choosing...\n\
        [r] -- rock\n\
        [s] -- scissors\n\
        [k] -- spoke\n\
        [l] -- lizard\n\
        [p] -- paper\n")
                            if Player2 =='r' or Player2 =='s' or Player2 =='k' or Player2 =='l' or Player2 =='p':
                        
                                if (Player1 == 'r' and Player2 == 'r') or (Player1 == 's' and Player2 == 's') or (Player1 == 'k' and Player2 == 'k') or (Player1 == 'l' and Player2 == 'l') or (Player1 == 'p' and Player2 == 'p'):
                                    print('EQUAL')

                                elif Player1 == 'r' and (Player2 == 's' or Player2 == 'l'):
                                    print('This Tour Player 1 win!')
                                    who_wins_p1_p2 += 1
                                elif Player1 == 'r' and (Player2 == 'k' or Player2 == 'p'):
                                    print('This Tour Player 2 win!')
                                    who_wins_p1_p2 -= 1

                                elif Player1 == 's' and (Player2 == 'p' or Player2 == 'l'):
                                    print('This Tour Player 1 win!')
                                    who_wins_p1_p2 += 1
                                elif Player1 == 's' and (Player2 == 'r' or Player2 == 'k'):
                                    print('This Tour Player 2 win!')
                                    who_wins_p1_p2 -= 1

                                elif Player1 == 'k' and (Player2 == 's' or Player2 == 'r'):
                                    print('This Tour Player 1 win!')
                                    who_wins_p1_p2 += 1
                                elif Player1 == 'k' and (Player2 == 'l' or Player2 == 'p'):
                                    print('This Tour Player 2 win!')
                                    who_wins_p1_p2 -= 1

                                elif Player1 == 'l' and (Player2 == 'k' or Player2 == 'p'):
                                    print('This Tour Player 1 win!')
                                    who_wins_p1_p2 += 1
                                elif Player1 == 'l' and (Player2 == 's' or Player2 == 'r'):
                                    print('This Tour Player 2 win!')
                                    who_wins_p1_p2 -= 1

                                elif Player1 == 'p' and (Player2 == 'r' or Player2 == 'k'):
                                    print('This Tour Player 1 win!')
                                    who_wins_p1_p2 += 1
                                elif Player1 == 'p' and (Player2 == 's' or Player2 == 'l'):
                                    print('This Tour Player 2 win!')
                                    who_wins_p1_p2 -= 1

                            else:
                                print('\t\t\t\t\t\t-------------!Enter Correct Operation!-------------'.upper())

                        else:
                            print('\t\t\t\t\t\t-------------!Enter Correct Operation!-------------'.upper())

                    if who_wins_p1_p2 > 0:
                        print('*****OVERALL PLAYER 1 IS WINNER*****')

                    elif who_wins_p1_p2 < 0:
                        print('*****OVERALL PLAYER 2 IS WINNER*****')

                    else:
                        print('*****NO WINNER*****')

                case 'c':
                    who_wins_p_c = 0
                    for round in range(3, 0, -1):

                        print(f'\nYou have {round} rounds!')
                        comp = ['rock', 'scissors', 'spoke', 'lizard', 'paper']
                        you = input("Player is choosing...\n\
            [r] -- rock\n\
            [s] -- scissors\n\
            [k] -- spoke\n\
            [l] -- lizard\n\
            [p] -- paper\n")
                        
                        comp_select = random.choice(comp)
                        if you =='r' or you =='s' or you =='k' or you =='l' or you =='p':

                            if (comp_select == 'rock' and you == 'r') or (comp_select == 'scissors' and you == 's') or (comp_select == 'spoke' and you == 'k') or (comp_select == 'lizard' and you == 'l') or (comp_select == 'paper' and you == 'p'):
                                print('EQUAL')

                            elif comp_select == 'rock' and (you == 's' or you == 'l'):
                                print(f'This Tour Computer win!\nComputer chose the rock')
                                who_wins_p_c += 1
                            elif comp_select == 'rock' and (you == 'k' or you == 'p'):
                                print('This Tour You win!\nComputer chose the rock')
                                who_wins_p_c -= 1

                            elif comp_select == 'scissors' and (you == 'p' or you == 'l'):
                                print(f'This Tour Computer win!\nComputer chose the scissors')
                                who_wins_p_c += 1
                            elif comp_select == 'scissors' and (you == 'r' or you == 'k'):
                                print('This Tour You win!\nComputer chose the scissors')
                                who_wins_p_c -= 1

                            elif comp_select == 'spoke' and (you == 's' or you == 'r'):
                                print(f'This Tour Computer win!\nComputer chose the spoke')
                                who_wins_p_c += 1
                            elif comp_select == 'spoke' and (you == 'l' or you == 'p'):
                                print('This Tour You win!\nComputer chose the spoke')
                                who_wins_p_c -= 1

                            elif comp_select == 'lizard' and (you == 'k' or you == 'p'):
                                print(f'This Tour Computer win!\nComputer chose the lizard')
                                who_wins_p_c += 1
                            elif comp_select == 'lizard' and (you == 's' or you == 'r'):
                                print('This Tour You win!\nComputer chose the lizard')
                                who_wins_p_c -= 1

                            elif comp_select == 'paper' and (you == 'r' or you == 'k'):
                                print(f'This Tour Computer win!\nComputer chose the paper')
                                who_wins_p_c += 1
                            elif comp_select == 'paper' and (you == 's' or you == 'l'):
                                print('This Tour You win!\nComputer chose the paper')
                                who_wins_p_c -= 1

                        else:
                                print('\t\t\t\t\t\t-------------!Enter Correct Operation!-------------'.upper())

                    if who_wins_p_c > 0:
                        print('*****OVERALL COMPUTER IS WINNER*****')

                    elif who_wins_p_c < 0:
                        print('*****OVERALL YOU ARE WINNER*****')
                    else:
                        print('*****NO WINNER*****')

        case 'e':
            print('Game Exited')
            break

        case 'a':
            print('''🪨 Rock (Daş)
Breaks Scissors
Crushes Lizard
Loses to Paper
Loses to Spock

📄 Paper (Kağız)
Covers Rock
Disproves Spock
Loses to Scissors
Loses to Lizard

✂️ Scissors (Qayçı)
Cuts Paper
Decapitates Lizard
Loses to Rock
Loses to Spock

🦎 Lizard (Kərtənkələ)
Poisons Spock
Eats Paper
Loses to Rock
Loses to Scissors

🖖 Spock
Crushes Scissors
Vaporizes Rock
Loses to Paper
Loses to Lizard''')

        case _:
            print('Select Correct Operation!')










