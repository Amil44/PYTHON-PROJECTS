x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = ' '

ISTIFADECI_X_YOXSA_O = input('istifadeci_1 uchun X yoxsa O: ')
if ISTIFADECI_X_YOXSA_O =='X' or ISTIFADECI_X_YOXSA_O == 'O':
    while True:
        match ISTIFADECI_X_YOXSA_O:
            case "X":
                if ((x1 == 'X' and x2 == 'X' and x3 == 'X') or (x1 == 'O' and x2 == 'O' and x3 == 'O')) or ((x1 == 'X' and x4 == 'X' and x7 == 'X') or (x1 == 'O' and x4 == 'O' and x7 == 'O')) or ((x1 == 'X' and x5 == 'X' and x9 == 'X') or (x1 == 'O' and x5 == 'O' and x9 == 'O')) or ((x2 == 'X' and x5 == 'X' and x8 == 'X') or (x2 == 'O' and x5 == 'O' and x8 == 'O')) or ((x3 == 'X' and x6 == 'X' and x9 == 'X') or (x3 == 'O' and x6 == 'O' and x9 == 'O')) or ((x3 == 'X' and x5 == 'X' and x7 == 'X') or (x3 == 'O' and x5 == 'O' and x7 == 'O')) or ((x4 == 'X' and x5 == 'X' and x6 == 'X') or (x4 == 'O' and x5 == 'O' and x6 == 'O')) or ((x7 == 'X' and x8 == 'X' and x9 == 'X') or (x7 == 'O' and x8 == 'O' and x9 == 'O')):
                    print('Istifadeci2 QAZANDI')
                    break

                else:
                    istifadeci_1 = input('Secim istifadeci_1: ')

                    if istifadeci_1 == 'x1' or istifadeci_1 == 'x2' or istifadeci_1 == 'x3' or istifadeci_1 == 'x4' or istifadeci_1 == 'x5' or istifadeci_1 == 'x6' or istifadeci_1 == 'x7' or istifadeci_1 == 'x8' or istifadeci_1 == 'x9':
                        if istifadeci_1 == 'x1' and x1 == ' ':
                            x1 = 'X'
                        elif istifadeci_1 == 'x2' and x2 == ' ':
                            x2 = 'X'
                        elif istifadeci_1 == 'x3' and x3 == ' ':
                            x3 = 'X'
                        elif istifadeci_1 == 'x4' and x4 == ' ':
                            x4 = 'X'
                        elif istifadeci_1 == 'x5' and x5 == ' ':
                            x5 = 'X'
                        elif istifadeci_1 == 'x6' and x6 == ' ':
                            x6 = 'X'
                        elif istifadeci_1 == 'x7' and x7 == ' ':
                            x7 = 'X'
                        elif istifadeci_1 == 'x8' and x8 == ' ':
                            x8 = 'X'
                        elif istifadeci_1 == 'x9' and x9 == ' ':
                            x9 = 'X'
                        else:
                            continue

                        print(
                        f"""
                        {x1} | {x2} | {x3}
                        --------- 
                        {x4} | {x5} | {x6}
                        --------- 
                        {x7} | {x8} | {x9}
                    """)
                    
                    else:
                        print('Deyeri Yeniden Gir!')
                        continue
                
                if ((x1 == 'X' and x2 == 'X' and x3 == 'X') or (x1 == 'O' and x2 == 'O' and x3 == 'O')) or ((x1 == 'X' and x4 == 'X' and x7 == 'X') or (x1 == 'O' and x4 == 'O' and x7 == 'O')) or ((x1 == 'X' and x5 == 'X' and x9 == 'X') or (x1 == 'O' and x5 == 'O' and x9 == 'O')) or ((x2 == 'X' and x5 == 'X' and x8 == 'X') or (x2 == 'O' and x5 == 'O' and x8 == 'O')) or ((x3 == 'X' and x6 == 'X' and x9 == 'X') or (x3 == 'O' and x6 == 'O' and x9 == 'O')) or ((x3 == 'X' and x5 == 'X' and x7 == 'X') or (x3 == 'O' and x5 == 'O' and x7 == 'O')) or ((x4 == 'X' and x5 == 'X' and x6 == 'X') or (x4 == 'O' and x5 == 'O' and x6 == 'O')) or ((x7 == 'X' and x8 == 'X' and x9 == 'X') or (x7 == 'O' and x8 == 'O' and x9 == 'O')):
                    print('Istifadeci1 QAZANDI')
                    break

                else:
                    tf = True

                    while tf:
                        istifadeci_2 = input('Secim istifadeci_2: ')

                        if istifadeci_2 == 'x1' or istifadeci_2 == 'x2' or istifadeci_2 == 'x3' or istifadeci_2 == 'x4' or istifadeci_2 == 'x5' or istifadeci_2 == 'x6' or istifadeci_2 == 'x7' or istifadeci_2 == 'x8' or istifadeci_2 == 'x9':
                            if istifadeci_2 == 'x1' and x1 == ' ':
                                x1 = 'O'
                                tf = False
                            elif istifadeci_2 == 'x2' and x2 == ' ':
                                x2 = 'O'
                                tf = False
                            elif istifadeci_2 == 'x3' and x3 == ' ':
                                x3 = 'O'
                                tf = False
                            elif istifadeci_2 == 'x4' and x4 == ' ':
                                x4 = 'O'
                                tf = False
                            elif istifadeci_2 == 'x5' and x5 == ' ':
                                x5 = 'O'
                                tf = False
                            elif istifadeci_2 == 'x6' and x6 == ' ':
                                x6 = 'O'
                                tf = False
                            elif istifadeci_2 == 'x7' and x7 == ' ':
                                x7 = 'O'
                                tf = False
                            elif istifadeci_2 == 'x8' and x8 == ' ':
                                x8 = 'O'
                                tf = False
                            elif istifadeci_2 == 'x9' and x9 == ' ':
                                x9 = 'O'
                                tf = False
                            else:
                                continue

                            print(
                            f"""
                            {x1} | {x2} | {x3}
                            --------- 
                            {x4} | {x5} | {x6}
                            --------- 
                            {x7} | {x8} | {x9}
                        """)
                            
                        else:
                            print('Deyeri Yeniden Gir!')
                            continue
                                    
            case "O":
                if ((x1 == 'X' and x2 == 'X' and x3 == 'X') or (x1 == 'O' and x2 == 'O' and x3 == 'O')) or ((x1 == 'X' and x4 == 'X' and x7 == 'X') or (x1 == 'O' and x4 == 'O' and x7 == 'O')) or ((x1 == 'X' and x5 == 'X' and x9 == 'X') or (x1 == 'O' and x5 == 'O' and x9 == 'O')) or ((x2 == 'X' and x5 == 'X' and x8 == 'X') or (x2 == 'O' and x5 == 'O' and x8 == 'O')) or ((x3 == 'X' and x6 == 'X' and x9 == 'X') or (x3 == 'O' and x6 == 'O' and x9 == 'O')) or ((x3 == 'X' and x5 == 'X' and x7 == 'X') or (x3 == 'O' and x5 == 'O' and x7 == 'O')) or ((x4 == 'X' and x5 == 'X' and x6 == 'X') or (x4 == 'O' and x5 == 'O' and x6 == 'O')) or ((x7 == 'X' and x8 == 'X' and x9 == 'X') or (x7 == 'O' and x8 == 'O' and x9 == 'O')):
                    print('Istifadeci2 QAZANDI')
                    break

                else:
                    istifadeci_1 = input('Secim istifadeci_1: ')

                    if istifadeci_1 == 'x1' or istifadeci_1 == 'x2' or istifadeci_1 == 'x3' or istifadeci_1 == 'x4' or istifadeci_1 == 'x5' or istifadeci_1 == 'x6' or istifadeci_1 == 'x7' or istifadeci_1 == 'x8' or istifadeci_1 == 'x9':
                        if istifadeci_1 == 'x1' and x1 == ' ':
                            x1 = 'O'
                        elif istifadeci_1 == 'x2' and x2 == ' ':
                            x2 = 'O'
                        elif istifadeci_1 == 'x3' and x3 == ' ':
                            x3 = 'O'
                        elif istifadeci_1 == 'x4' and x4 == ' ':
                            x4 = 'O'
                        elif istifadeci_1 == 'x5' and x5 == ' ':
                            x5 = 'O'
                        elif istifadeci_1 == 'x6' and x6 == ' ':
                            x6 = 'O'
                        elif istifadeci_1 == 'x7' and x7 == ' ':
                            x7 = 'O'
                        elif istifadeci_1 == 'x8' and x8 == ' ':
                            x8 = 'O'
                        elif istifadeci_1 == 'x9' and x9 == ' ':
                            x9 = 'O'
                        else:
                            continue

                        print(
                        f"""
                        {x1} | {x2} | {x3}
                        --------- 
                        {x4} | {x5} | {x6}
                        --------- 
                        {x7} | {x8} | {x9}
                    """)
                        
                    else:
                        print('Deyeri Yeniden Gir!')
                        continue
                    
                if ((x1 == 'X' and x2 == 'X' and x3 == 'X') or (x1 == 'O' and x2 == 'O' and x3 == 'O')) or ((x1 == 'X' and x4 == 'X' and x7 == 'X') or (x1 == 'O' and x4 == 'O' and x7 == 'O')) or ((x1 == 'X' and x5 == 'X' and x9 == 'X') or (x1 == 'O' and x5 == 'O' and x9 == 'O')) or ((x2 == 'X' and x5 == 'X' and x8 == 'X') or (x2 == 'O' and x5 == 'O' and x8 == 'O')) or ((x3 == 'X' and x6 == 'X' and x9 == 'X') or (x3 == 'O' and x6 == 'O' and x9 == 'O')) or ((x3 == 'X' and x5 == 'X' and x7 == 'X') or (x3 == 'O' and x5 == 'O' and x7 == 'O')) or ((x4 == 'X' and x5 == 'X' and x6 == 'X') or (x4 == 'O' and x5 == 'O' and x6 == 'O')) or ((x7 == 'X' and x8 == 'X' and x9 == 'X') or (x7 == 'O' and x8 == 'O' and x9 == 'O')):
                    print('Istifadeci1 QAZANDI')
                    break

                else:
                    tf = True

                    while tf:
                        istifadeci_2 = input('Secim istifadeci_2: ')
                        if istifadeci_2 == 'x1' or istifadeci_2 == 'x2' or istifadeci_2 == 'x3' or istifadeci_2 == 'x4' or istifadeci_2 == 'x5' or istifadeci_2 == 'x6' or istifadeci_2 == 'x7' or istifadeci_2 == 'x8' or istifadeci_2 == 'x9':
                            if istifadeci_2 == 'x1' and x1 == ' ':
                                x1 = 'X'
                                tf = False
                            elif istifadeci_2 == 'x2' and x2 == ' ':
                                x2 = 'X'
                                tf = False
                            elif istifadeci_2 == 'x3' and x3 == ' ':
                                x3 = 'X'
                                tf = False
                            elif istifadeci_2 == 'x4' and x4 == ' ':
                                x4 = 'X'
                                tf = False
                            elif istifadeci_2 == 'x5' and x5 == ' ':
                                x5 = 'X'
                                tf = False
                            elif istifadeci_2 == 'x6' and x6 == ' ':
                                x6 = 'X'
                                tf = False
                            elif istifadeci_2 == 'x7' and x7 == ' ':
                                x7 = 'X'
                                tf = False
                            elif istifadeci_2 == 'x8' and x8 == ' ':
                                x8 = 'X'
                                tf = False
                            elif istifadeci_2 == 'x9' and x9 == ' ':
                                x9 = 'X'
                                tf = False
                            else:
                                continue

                            print(
                            f"""
                            {x1} | {x2} | {x3}
                            --------- 
                            {x4} | {x5} | {x6}
                            --------- 
                            {x7} | {x8} | {x9}
                        """)
                            
                        else:
                            print('Deyeri Yeniden Gir!')
                            continue

else:
    print('Duzgun Deyer Girin!')

