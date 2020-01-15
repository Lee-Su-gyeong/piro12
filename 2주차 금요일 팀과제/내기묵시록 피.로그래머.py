class User:
    
    def __init__(self, name):
        self.name = name
        self.money = 200000
        self.mental = 100
        self.SeongMoLoan=False

    def Hangman(self):
        import random

        WORDS = ['WATERFALL', 'SNOWFLAKE', 'IMAGINE', 'JAPANESE', 'BEVERAGE']
        word = random.choice(WORDS)
        positive = ['대환: 오 좀 하는데?', '대환: 내가.. 지는건가?', '대환: 운이 좋은걸?']
        negative = ['대환: 틀렸어~', '대환: 실력이 이거밖에 안돼?', '대환: 이러다 택시비 내겠어~']
        so_far = '*' * len(word)
        used = []
        life = 7

        while life > 0 and so_far != word:
            print('대환: 지금까지 맞춘 단어야: ', so_far)
            print('대환: 지금까지 사용한 알파벳이야: ', used)
            print('대환: 남은 목숨 개수야: ', life)
            time.sleep(1)
            print()
            guess = input('대환: 알파벳 하나를 말해봐: ').upper()

            while guess in used:
                print('대환: 이미 사용한 알파벳 이자나.')
                time.sleep(1)
                guess = input('대환: 다른 알파벳 하나를 말해봐: ').upper()

            while guess not in 'ABCDEFGHIJKLNMOPQRSTUVWXYZ' or len(guess) != 1:
                print('대환: 잘못 말했어.')
                time.sleep(1)
                guess = input('대환: 다시 알파벳 하나를 말해봐: ').upper()

            used.append(guess)

            if guess in word:
                print(random.choice(positive))
                time.sleep(1)
                print()

                update = ''
                for i in range(len(word)):
                    if guess == word[i]:
                        update += guess
                    else:
                        update += so_far[i]
                so_far = update

            else:
                print(random.choice(negative))
                time.sleep(1)
                print()
                life -= 1
        if life == 0:
            print('대환: 하하하 역시 신동한테는 안되는구만!! 택시비는 너가 내라고~')
            time.sleep(1)
            print('%s: 억장이 무너진다. 겨우 이동하는데 6만5천원이나 써야된다니…' % u.name)
            time.sleep(1)
            print('[돈이 65,000원 감소합니다. 멘탈이 소폭 감소합니다.]')
            time.sleep(1)
            u.money -= 65000
            u.mental -= 20

        else:
            print('대환: 이 신동을 꺾다니… 졌으니 택시비는 내줄게…')
            time.sleep(1)
            print('%s: 야호! 저 중독자 상대로 이겼다! 돈 굳었다…')
            time.sleep(1)

        print()
        print()

    def Reverse_Typing(self):
        import time
        Q=["파이선 다음은 장고","커피 몇잔째더라","오늘 팀플은 몇시까지 할까","돈이 0이 되면","재미있는 이벤트가 생긴다"]
        right=0
        wrong=0
        print("-"*8, "문장 반대로 적기!", "-"*8,'\n')
        while True:
            start= input("게임을 시작할 준비가 되었으면 Y를 눌러 주세요!: ").upper()
            if(start=='Y'):
                for i in range(1,6):
                    T= time.time()
                    time.sleep(1)
                    print("-" * 10)
                    print("민정: 자 %d번째 문장이야!"%i)
                    print(Q[i-1])
                    A= input()
                    print()
                    if(Q[i-1]!=A[::-1] or time.time()-T > 10):
                        wrong+=1
                        print("민정: 내가 이겼다! 지금 %s는(은) %d번 이겼어 \n"%(u.name, right))
                    else:
                        right+=1
                        print("민정: 오 좀 잘하는데...?? 지금 %d번 이겼어!\n" %right)
                    if(wrong>=3 or right>=3):
                        break
                print("\n", '-' * 20)
                print("\n\n<<과제 내기 - 문장 반대로 적기 결과>>")
                if(right>=3):
                    print("\t승리자: %s\n" %u.name)
                else:
                    print("\t승리자: 민정\n")
                print("\n", '-' * 20)

                time.sleep(2)
                if(right<3):
                    u.mental -=60
                    print("망했다.....")
                    time.sleep(1)
                    print("과제가 두배....")
                    print("아무리 봐도 이건 밤샘 각이다.\n")
                    print("스트레스가 엄청나게 쌓이는게 느껴진다.")
                    time.sleep(2)
                    print("[멘탈 지수가 대폭 하락합니다.]")
                    time.sleep(1)

                else:
                    u.mental+=10
                    print("이겼다!!")
                    time.sleep(1)
                    print("오늘 밤은 집에 가자마자 자야지!")
                    print("옆에서 민정이가 괴로워하는게 보인다.\n")
                    time.sleep(2)
                    print("[멘탈 지수가 소폭 회복됩니다.]")
                    time.sleep(1)
                break

            else:
                print("민정: 진짜 안할거야..? 'Y'를 눌러야 된다구!\n")





    def BlackJack(self):
        exit=""
        while exit != "exit":
            import time
            from random import randint
            import random
            print(   "────────────────────────────────────",   sep="")
            print(  "    블랙잭 게임을 시작하겠습니다")
            print(  "────────────────────────────────────\n\n",   sep="")
            time.sleep(2)
            #deck이 랜덤하게 설정되었습니다.
            card_value = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
            card_type = ['♥','♠','♣','◆']
            deck=[]
            for i in card_type:
                    for j in card_value:
                        deck.append(j + ' of ' + i)


            #유저에게 deck을 랜덤하게 배분
            cards_1 = [deck[random.randint(1,len(deck)-1)],deck[random.randint(1,len(deck)-1)]]
            cards_2 = [deck[random.randint(1,len(deck)-1)],deck[random.randint(1,len(deck)-1)]]
            print('         카드를 받았습니다')
            print(  "────────────────────────────────────",   sep="")
            print("     ",cards_1[0],"    /    ",cards_1[1])
            print(  "────────────────────────────────────\n\n", sep="")
            time.sleep(2)
            #이것은 카드의 벨류값 설정 (else값 확인하기)
            x =  [cards_1[0][:2].strip(' c'),cards_1[1][:2].strip(' c')]
            y =  [cards_2[0][:2].strip(' c'),cards_2[1][:2].strip(' c')]


            # x 첫번째
            if x[0] in ['2','3','4','5','6','7','8','9','10']:
                x[0] = int(x[0])
            if x[0] in ['J', 'Q', 'K']:
                x[0] = int(10)
            if x[0] in ["A"]:
                A_answer = input("A를 11과 1중에 어떤수로 하시겠습니까?(1 또는 11 입력)\n")
                if A_answer == "1" :
                    x[0] = int(1)
                if A_answer == "11":
                    x[0] = int(11)

            # x 두번쨰
            if x[1] in ['2','3','4','5','6','7','8','9','10']:
                x[1] = int(x[1])
            if x[1] in ['J', 'Q', 'K']:
                x[1] = int(10)
            if x[1] in ["A"]:
                A_answer = input("A를 11과 1중에 어떤수로 하시겠습니까?(1 또는 11 입력)\n")
                if A_answer == "1" :
                    x[1] = int(1)
                if A_answer == "11":
                    x[1] = int(11)

            # 상대방 카드 y 첫번째 값 변경
            if y[0] in ['2','3','4','5','6','7','8','9','10']:
                y[0] = int(y[0])
            if y[0] in ['J', 'Q', 'K']:
                y[0] = int(10)
            if y[0] in ["A"]:
                y[0] = int(1)

            # 상대방 카드 y 두번쨰 값 변경
            if y[1] in ['2','3','4','5','6','7','8','9','10']:
                y[1] = int(y[1])
            if y[1] in ['J', 'Q', 'K']:
                y[1] = int(10)
            if y[1] in ["A"]:
                y[1] = int(1)

            #게임시작
            #나의 카드가 21인 경우
            if x[0] + x[1] == 21 :
                print(  "────────────────────────────────────\n",   sep="")
                print("블랙잭! 당신이 이겼습니다.")
                print(  "\n────────────────────────────────────", "┘\n", sep="")
                exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
            #상대방이 21보다 작으면 한장 더받기
            if y[0] + y[1] == 21:
                print(  "────────────────────────────────────",   sep="")
                print("\n상대방이 블랙잭이므로 당신은 졌습니다.\n")
                print(  "────────────────────────────────────", "┘\n", sep="")
                u.money -= 80000
                print("내돈  80000ㅠㅠㅠㅠㅠㅠ")
                exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")

            #나의 카드가 21보다 작은 경우
            if x[0] + x[1] <= 20 and y[0] + y[1] >=11 and y[0] + y[1] < 21:
                B_answer = int(input("카드를 더 받으시겠습니까? 안받으시겠습니까?\n(받으려면 숫자 1을, 안받으려면 숫자 0을 넣어주세요)\n\n"))
                
                if B_answer == 1 : 
                    x.append(deck[random.randint(1,len(deck)-1)])
                    x[2] = x[2][:2].strip(' c')
                    if x[2] in ['2','3','4','5','6','7','8','9','10']:
                        x[2] = int(x[2])
                    if x[2] in ['J', 'Q', 'K']:
                        x[2] = int(10)
                    if x[2] in ["A"]:
                        A_answer = input("A를 11과 1중에 어떤수로 하시겠습니까?(1 또는 11 입력)\n\n")
                        if A_answer == "1" :
                            x[2] = int(1)
                        elif A_answer == "11":
                            x[2] = int(11)   

                    if x[0]+x[1]+x[2] > 21:
                        print(  "────────────────────────────────────",   sep="")
                        print("     \n패의 합이 21이 넘어서 패배 했습니다.\n")
                        print(  "────────────────────────────────────",   sep="")
                        u.money -= 80000
                        print("내돈  80000ㅠㅠㅠㅠㅠㅠ")
                        exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                    if x[0]+x[1]+x[2] == 21 :
                        print(  "────────────────────────────────────",   sep="")
                        print("         \n블랙잭! 당신이 이겼습니다.\n")
                        print(  "────────────────────────────────────", "┘\n", sep="")
                        exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")


                    
                    if x[0]+x[1]+x[2] < 21:
                        
                        print(  "────────────────────────────────────",   sep="")
                        print("\n당신 카드 숫자의 합은", x[0]+x[1]+x[2], "\n" )    
                        print('상대방 카드 숫자의 합은', y[0]+y[1])
                        print(   "────────────────────────────────────",   sep="")
                        if abs(21 - (x[0] + x[1] + x[2])) < abs(21 -(y[0]+y[1])):
                            print(  "────────────────────────────────────",   sep="")
                            print("\n당신이 이겼습니다!", abs(21 - (x[0] + x[1] +x[2])), "<" ,abs(21 -(y[0]+y[1])))
                            print(   "\n────────────────────────────────────",   sep="")
                            exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                        if abs(21 - (x[0] + x[1] + x[2])) == abs(21 -(y[0]+y[1])):
                            print(  "────────────────────────────────────\n",   sep="")
                            print("비겼습니다!", abs(21 - (x[0] + x[1] + x[2])), "=" ,abs(21 -(y[0]+y[1])))
                            exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                            print(   "\n────────────────────────────────────",   sep="")
                        if abs(21 - (x[0] + x[1] +x[2])) > abs(21 -(y[0]+y[1])):
                            print(  "────────────────────────────────────\n",   sep="")
                            print("당신이 졌습니다!", abs(21 - (x[0] + x[1] +x[2])), ">" , abs(21 -(y[0]+y[1])))  
                            print(   "\n────────────────────────────────────",   sep="")
                            u.money -= 80000
                            print("내돈  80000ㅠㅠㅠㅠㅠㅠ")
                            exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                            
                    
                if B_answer == 0 :      
                    print(   "────────────────────────────────────",   sep="")
                    print("\n당신 카드 숫자의 합은", x[0]+x[1] )
                    print('상대방 카드 숫자의 합은', y[0]+y[1])
                    print(   "\n────────────────────────────────────",   sep="")
                    
                    if abs(21 - (x[0] + x[1])) < abs(21 -(y[0]+y[1])):
                        print(  "────────────────────────────────────\n",   sep="")
                        print("당신이 이겼습니다!", abs(21 - (x[0] + x[1])), "<" ,abs(21 -(y[0]+y[1])))
                        print(   "\n────────────────────────────────────",   sep="")
                        exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                    if abs(21 - (x[0] + x[1])) == abs(21 -(y[0] + y[1])) :
                        print(  "────────────────────────────────────\n",   sep="")
                        print("비겼습니다!", abs(21 - (x[0] + x[1])), "=" ,abs(21 -(y[0]+y[1])))
                        print(   "\n────────────────────────────────────\n",   sep="")
                        exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                    if abs(21 - (x[0] + x[1])) > abs(21 -(y[0]+y[1])):
                        print(  "\n────────────────────────────────────\n",   sep="")
                        print("당신이 졌습니다!", abs(21 - (x[0] + x[1])), ">" , abs(21 -(y[0]+y[1])))    
                        print(   "\n────────────────────────────────────",   sep="")
                        u.money -= 80000
                        print("내돈  80000ㅠㅠㅠㅠㅠㅠ")
                        exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
            #상대방이 카드 추가하는경우
            if x[0] + x[1] <= 20 and y[0] + y[1] <= 10:
                y.append(deck[random.randint(1,len(deck)-1)])
                y[2] = y[2][:2].strip(' c')

                if y[2] in ['2','3','4','5','6','7','8','9','10']:
                    y[2] = int(y[2])
                if y[2] in ['J', 'Q', 'K']:
                    y[2] = int(10)
                if y[2] in ["A"]:
                    y[2] = int(1)

                if y[0]+y[1]+y[2] > 21:
                    print(  "────────────────────────────────────\n",   sep="")
                    print("상대방 패의 합이 21이 넘어서 이겼습니다.")
                    print(   "\n────────────────────────────────────",   sep="")
                    exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                if y[0]+y[1]+y[2]  == 21:
                    print(  "────────────────────────────────────",   sep="")
                    print("\n상대방이 블랙잭이므로 당신은 졌습니다.\n")
                    print(  "────────────────────────────────────", sep="")
                    u.money -= 80000
                    print("내돈  80000ㅠㅠㅠㅠㅠㅠ")
                    exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                if y[0]+y[1]+y[2] < 21:

                    C_answer = int(input("카드를 더 받으시겠습니까? 안받으시겠습니까?\n(받으려면 숫자 1을, 안받으려면 숫자 0을 넣어주세요)\n\n"))
                    if C_answer == 1 : 
                        x.append(deck[random.randint(1,len(deck)-1)])
                        x[2] = x[2][:2].strip(' c')
                        if x[2] in ['2','3','4','5','6','7','8','9','10']:
                            x[2] = int(x[2])
                        if x[2] in ['J', 'Q', 'K']:
                            x[2] = int(10)
                        if x[2] in ["A"]:
                            A_answer = input("A를 11과 1중에 어떤수로 하시겠습니까?(1 또는 11 입력)\n\n")
                            if A_answer == "1" :
                                x[2] = int(1)
                            if A_answer == "11":
                                x[2] = int(11)   
                        if x[0]+x[1]+x[2] > 21:
                            print(  "────────────────────────────────────",   sep="")
                            print("     \n패의 합이 21이 넘어서 패배 했습니다.\n")
                            print(  "────────────────────────────────────",   sep="")
                            u.money -= 80000
                            print("내돈  80000ㅠㅠㅠㅠㅠㅠ")
                            exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                        print(  "────────────────────────────────────\n",   sep="")
                        print("\n당신 카드 숫자의 합은", x[0]+x[1]+x[2] )
                        print('상대방 카드 숫자의 합은', y[0]+y[1]+y[2])
                        print(   "\n────────────────────────────────────",   sep="")
                        if abs(21 - (x[0] + x[1] + x[2])) < abs(21 -(y[0]+y[1]+y[2])):
                            print(  "────────────────────────────────────\n",   sep="")
                            print("당신이 이겼습니다!", abs(21 - (x[0] + x[1] +x[2])), "<" ,abs(21 -(y[0]+y[1]+y[2])))
                            print(   "\n────────────────────────────────────",   sep="")
                            exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                        if abs(21 - (x[0] + x[1] + x[2])) == abs(21 -(y[0]+y[1]+y[2])):
                            print(  "────────────────────────────────────\n",   sep="")
                            print("비겼습니다!", abs(21 - (x[0] + x[1] + x[2])), "=" ,abs(21 -(y[0]+y[1])))
                            print(   "\n────────────────────────────────────",   sep="")
                            exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                        if abs(21 - (x[0] + x[1] +x[2])) > abs(21 -(y[0]+y[1]+y[2])):
                            print(  "────────────────────────────────────\n",   sep="")
                            print("당신이 졌습니다!", abs(21 - (x[0] + x[1] +x[2])), ">" , abs(21 -(y[0]+y[1]+y[2])))    
                            print(   "\n────────────────────────────────────",   sep="")
                            u.money -= 80000
                            print("내돈  80000ㅠㅠㅠㅠㅠㅠ")
                            exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                        
                        




                    if C_answer == 0 :      
                        print(   "────────────────────────────────────",   sep="")
                        print("\n당신 카드 숫자의 합은", x[0]+x[1] )
                        print('상대방 카드 숫자의 합은', y[0]+y[1]+y[2])
                        print(   "\n────────────────────────────────────",   sep="")
                        if abs(21 - (x[0] + x[1])) < abs(21 -(y[0]+y[1]+y[2])):
                            print(  "────────────────────────────────────\n",   sep="")
                            print("당신이 이겼습니다!", abs(21 - (x[0] + x[1])), "<" ,abs(21 -(y[0]+y[1]+y[2])))
                            print(   "\n────────────────────────────────────",   sep="")
                            exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                        if abs(21 - (x[0] + x[1])) == abs(21 -(y[0]+y[1]+y[2])):
                            print(  "────────────────────────────────────\n",   sep="")
                            print("비겼습니다!", abs(21 - (x[0] + x[1])), "=" ,abs(21 -(y[0]+y[1]+y[2])))
                            print(   "\n────────────────────────────────────",   sep="")
                            exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
                        if abs(21 - (x[0] + x[1])) > abs(21 -(y[0]+y[1]+y[2])):
                            print(  "────────────────────────────────────\n",   sep="")
                            print("당신이 졌습니다!", abs(21 - (x[0] + x[1])), ">" , abs(21 -(y[0]+y[1]+y[2])))    
                            u.money -= 80000
                            print("내돈  80000ㅠㅠㅠㅠㅠㅠ")
                            print(   "\n────────────────────────────────────",   sep="")
                            exit = input("""\n\n밥 먹으러 갈라믄 'exit'를 입력해주세요""")
        return
        

    def Ladder(self):
        import turtle
        import random

        t1 = turtle.Turtle()
        t1.shape("turtle")
        t1.color('purple')

        t2 = turtle.Turtle()
        t2.shape("turtle")
        t2.color('red')

        t3 = turtle.Turtle()
        t3.shape("turtle")
        t3.color('blue')
        t4 = turtle.Turtle()
        t4.shape("turtle")
        t4.color('green')

        t1.speed(2)
        t2.speed(2)
        t3.speed(2)
        t4.speed(2)

        t1.penup()
        t2.penup()
        t3.penup()
        t4.penup()

        t1.setpos(-200, 100)
        t2.setpos(-200, 0)
        t3.setpos(-200, -100)
        t4.setpos(-200, -200)

        t1.pendown()
        t2.pendown()
        t3.pendown()
        t4.pendown()

        t1.speed(1)
        t2.speed(1)
        t3.speed(1)
        t4.speed(1)

        a1=-200
        b1=100
        t1.setpos(a1,b1)
        t1.setpos(a1+100,b1)
        for i in range(100,400,100):
            bb=random.choice([-100,0,100])
            t1.setpos(a1+i,b1+bb)
            t1.setpos(a1+(i+100),b1+bb)
        (x1,y1)=t1.position()    
        
        a2=-200
        b2=0
        t2.setpos(a2,b2)
        t2.setpos(a2+100,b2)
        for i in range(100,400,100):
            bb=random.choice([-100,0,100])
            t2.setpos(a2+i,b2+bb)
            t2.setpos(a2+(i+100),b2+bb)
        (x2,y2)=t2.position()
    

        a3=-200
        b3=-100
        t3.setpos(a3,b3)
        t3.setpos(a3+100,b3)
        for i in range(100,400,100):
            bb=random.choice([-100,0,100])
            t3.setpos(a3+i,b3+bb)
            t3.setpos(a3+(i+100),b3+bb)
        (x3,y3)=t3.position()
        

        a4=-200
        b4=-200
        t4.setpos(a4,b4)
        t4.setpos(a4+100,b4)
        for i in range(100,400,100):
            bb=random.choice([-100,0,-100])
            t4.setpos(a4+i,b4+bb)
            t4.setpos(a4+(i+100),b4+bb)
        (x4,y4)=t4.position()
        

        max=0
        min=0

        if y1>y2:
            max=y1
            min=y2
        else:
            max=y2
            min=y1

        if max<y3:
            max=y3
        if max<y4:
            max=c
        
        if min>y3:
            min=y3
        if min>y4:
            min=y4
        

        if min==y1:
            print("보라 거북이 당첨")
        elif min==y2:
            print("파란 거북이 당첨")
        elif min==y3:
            print("빨강 거북이 당첨")
        else:
            print("초록 거북이 당첨")





    def Baskin_Robbins_31(self):
        import random
        print("\n\n")
        time.sleep(2)
        print("게임 플레이어는 성익, 소현, 종인, 영주, %s\n" % u.name)
        time.sleep(2)
        print('＼(´ ∇`)ノ ＼(´∇｀)ノ' * 2 + "베스킨~라빈스~써리~원! 베스킨~라빈스~써리~원!" + '＼(´ ∇`)ノ ＼(´∇｀)ノ' * 2 + '\n')
        time.sleep(2)

        playerList = ['성익', '소현', '종인', '영주']
        brCount = 1
        fool = None
        while brCount <= 31:

            for i in range(len(playerList)):
                ri = random.randint(1, 3)
                if brCount >= 27:
                    ri = 1
                turn = [i for i in range(brCount, brCount + ri)]
                if turn[-1] >= 31:
                    time.sleep(1)
                    print("%s 당첨!" % playerList[i])
                    fool = playerList[i]
                    return fool
                brCount += ri
                sturn = str(turn)
                print("%s : " % playerList[i], end='')
                print(sturn.strip('[]') + "!\n")
                if brCount == 31:
                    if playerList[i] == '영주':
                        time.sleep(1)
                        print("%s 당첨!" % u.name)
                        fool = u.name
                        return fool
                    else:
                        time.sleep(1)
                        print("%s 당첨!" % playerList[i + 1])
                        fool = playerList[i + 1]
                        return fool
                time.sleep(1)

            print("몇개를 더 내지? 1,2,3중 하나를 고르자!")
            ui = int(input())
            while ui < 1 or ui > 3:
                print("베스킨 라빈스는 최대 세 개밖에 못내지.. 요새 술게임을 너무 안했나? 다시 골라보자.")
                print("몇개를 더 내지? 1,2,3중 하나를 고르자!")
                ui = int(input())

            if brCount + ui > 31:
                time.sleep(1)
                print("%s 당첨!" % u.name)
                fool = u.name
                return fool
            turn = [i for i in range(brCount, brCount + ui)]
            brCount += ui
            sturn = str(turn)
            print("%s : " % u.name, end='')
            print(sturn.strip('[]') + "!\n")
            time.sleep(1)

        return


    def SeongMo_check(self):
        import time
        if(u.money<=0):
            print("\n\n큰일났다....\n")
            time.sleep(2)
            print("돈이 정말 한푼도 안남았다.")
            print("앞으로 내기를 어떻게 할지 고민중인 그 때")
            print("회장이 앞에 나타났다.\n")
            time.sleep(3)
            print("성모: %s님... 혹시 돈 다 떨어지셨나요?\n"%u.name)
            print("어떻게 알았지??")
            print("%s: 네....\n"%u.name)
            time.sleep(3)
            print("성모: %s님 제가 5만원을 빌려드릴 테니까"%u.name)
            print("     오늘 일정 끝나고 나서 이자까지 갚으시는 거에요!")
            print("     혹시 못갚으시면.... ㅎ.. 코딩 더 하시는걸로?\n")
            time.sleep(3)
            print("%s: 지금보다 더 한다고요? 미쳤다..."%u.name)
            print("      까짓것 한번 해보죠!\n\n")
            time.sleep(2)
            print("[회장에게 5만원을 빌렸다!]")
            time.sleep(2)
            print("빌린 돈의 10프로 이자까지 갚지 않으면, 엄청난 일을 당할 것 같은 느낌이 든다...")
            time.sleep(3)
            u.money+= 50000
            u.SeongMoLoan=True

    def mental_check(self):
        if(u.mental<=0):
            return True
        else:
            return False


import time
end = False

print("-"*80)
print("내기묵시록 - 내기중독 피.로그래머".center(60))
print()
print("made by - 강경욱, 김대환, 김성익, 남민정, 이수경".rjust(68))
print("-"*80)
time.sleep(3)
print("\n\n서울대 SK경영관에서 코딩만 하던 12기 피로그래머들...")
print("그들은 내기 중독에 빠져버리고 마는데..!!\n")
time.sleep(2)
print("당신은 과연 내기에 미친 그들로부터 살아남을 수 있을 것인가?")
print("피.로그래머의 하루를 살아가며 돈과 멘탈을 모두 지켜봅시다!\n")
time.sleep(2)
print("성모: 죄송한데 성함이 어떻게 되시죠?")
userName = input("아 제 이름은...")
u = User(userName)
time.sleep(1)
print("성모: 아 %s님, 네네 출석 확인 되었어요!" %u.name)
time.sleep(2)
print("\n그렇게 피.로그래머의 하루가 시작되었다.")



while u.mental > 0 and end == False:

    #prologue

    time.sleep(1.5)
    print("-"*40)
    print("\n성모: [피.로그래머 공지]")
    time.sleep(2)
    print("      내기에 대하여 미리 안내를 드려야할 것 같아서 공지드립니다.")
    print("      정규일정인 점심, 커피, 뒷풀이 내기와 추가적으로 자유롭게 내기를 하기로 결정했습니다!")
    print("      다양한 내기를 통해서 프로그래밍 실력과 돈, 멘탈을 모두 챙겨봅시다!")
    print("      와아~ 즐겁다~   화이팅! :)")
    time.sleep(4)
    print('\n\n')

    # chapter 1

    print('#'*20,'   Chapter 1   ','#'*20)
    print()

    print('%s: 아 오늘 한파주의보 라더니 너무 춥네. 시간도 모자라는데 10시까지 못가면 보증금 만원 까이는데...' %u.name)
    time.sleep(2)
    print('대환: 추워죽겠는데 카카오리무진 타고 갈래? 공짜로 타고 갈 수 있어.')
    time.sleep(2)
    print('%s: 오 진짜 좋아!! 근데 어떻게 공짜로 타고 가??' %u.name)
    time.sleep(2)
    print('대환: 어떻게냐면... 행맨 신동으로 불리는 나를 행맨으로 이긴다면!!')
    time.sleep(2)
    print('%s: \'신동은 무슨... 그냥 행맨 중독자잖아...\'' %u.name)
    time.sleep(2)
    print('%s: 좋아! 그럼 택시안에서 우리 택시빵 행맨 내기하자!' %u.name)
    time.sleep(2)
    print('대환: 콜!!')
    print()
    time.sleep(1)
    print('(택시안) \n대환: 게임 방법은 알고있겠지만 한번 더 설명해주자면, 내가 영단어를 하나 마음으로 생각하고 있을게. (...)')
    time.sleep(2)
    print('대환: (...) 너가 알파벳 하나를 말해주고 그 알파벳이 단어 안에 있으면 몇번째 철자인지 알려주고 없으면 목숨 하나를 잃는거야. 목숨은 총 7개! 어때 쉽지? 시작해볼까?')
    time.sleep(2.5)
    print()
    print()
    print("-"*20, "   행맨 게임!   ", "-"*20,'\n')
    time.sleep(1)
    A = input("게임을 시작할 준비가 되었으면 Y 또는 y 를 눌러 주세요!: ")
    print()
    time.sleep(1)

    while True:
        if A == 'Y' or A == 'y':
            print('대환: 택시빵 행맨게임을 시작한다!!!')
            print()
            time.sleep(1)
            u.Hangman()
            break
        else:
            print('내기중독 피.로그래머가 내기를 안한다고?? 다시 생각해봐.')
            time.sleep(1)
            A = input("게임을 시작할 준비가 되었으면 Y 또는 y 를 눌러 주세요!: ")
            print()

    print("\n현재 (%s) 멘탈: %d 돈: %d\n" % (u.name, u.mental, u.money))
    time.sleep(5)
    if(u.mental_check()):
        break
    u.SeongMo_check()



    # chapter 2
    print('#'*20,'   Chapter 2   ','#'*20)
    print()
    print("성모: 코딩도장을 다 들었으니 아쉬운만큼 과제를 여러개 드리도록 하겠습니다:) 와아~ Python과 행복한 하루!")
    print()
    time.sleep(1)
    print("어제 팀플로 밤 샜는데....")
    print("회장이 또 과제를 줬다.")
    print("옆에 있는 민정이도 표정이 안좋은게 얘도 어제 밤 샜나보다\n")
    time.sleep(3)
    print("민정: %s, 우리 과제 내기할래??"%(u.name))
    print("%s: 헐 완전 좋아!!! 진 사람이 다 해오는거다!\n"%u.name)
    time.sleep(2)
    print("민정: 내가 문장을 5개 말할테니까 10초안에 반대로 적는거야!")
    print("     3개 이상 맞으면 %s(이)가 이긴걸로 할게\n"%u.name)
    time.sleep(2)
    print("이번엔 과제내기... 꼭 이겨서 오늘은 푹 잔다!\n")
    time.sleep(1)

    u.Reverse_Typing()
    print()
    print("현재 (%s) 멘탈: %d 돈: %d" % (u.name, u.mental, u.money))
    time.sleep(5)
    if (u.mental_check()):
        break
    u.SeongMo_check()

    # chapter 3
    print('#' * 20, '   Chapter 3   ', '#' * 20)
    time.sleep(3)
    print()
    print("\n점심 값 80000원을 걸고 블랙잭을 하게 됐다.\n")
    time.sleep(2)
    print("\n게임에서 이기면 무료밥! 흫히히흐희ㅣ히ㅡ\n")
    time.sleep(2)
    print("\n지면 80000워뉴ㅠㅠㅠㅠ\n")
    time.sleep(2)
    print('\n비기면 엔!빵!\n')
    time.sleep(2)
    u.BlackJack()
    time.sleep(1)
    print("\n\n밥을 다 먹구 후식을 먹으러 가게 됐다\n")
    time.sleep(1)
    print("\n현재 (%s) 멘탈: %d 돈: %d\n" % (u.name, u.mental, u.money))
    time.sleep(1)
    if (u.mental_check()):
        break
    u.SeongMo_check()
    print()
    print()



    # chapter 4
    print('#' * 20, '   Chapter 4   ', '#' * 20)
    print()
    time.sleep(1.5)
    print("대환: 맛있는 점심을 먹고 이제 후식 타임~! 다같이 커피 내기를 시작해볼까요?")
    time.sleep(1.5)
    print("수경: 카페 갈까? 식후엔 마실 거지!! 저기 카페있다!! 비싸보이긴 하는데 갑니다.")
    time.sleep(1.5)
    print("민정: 좋지 좋지 모먹지,, 난 아메리카노^---^")
    time.sleep(1.5)
    print("수경: 난 에이드!!!!")
    time.sleep(1.5)
    print("%s: 나 결정 못하는데..."%u.name)
    print("%s : 뭐야...카페 줄이 길군... 우리 커피 종류를 통일하자."%u.name)
    time.sleep(1.5)
    print()
    answer = input("카페직원: 주문 하시겠어요? 메뉴 보여드릴께요.(ENTER)")
    time.sleep(1.5)

    print()
    print("""ⓒⓞⓕⓕⓔⓔ ⓜⓔⓝⓤ
    ----------------------
    *AMERICANO* 20000원
    *LATTE* 22000원
    *TEA* 22000원
    *JUICE* 16000원 """)
    time.sleep(1.5)
    print()
    print("민정: 미쳤네... 커피 값 봐..2000원이 아니라 20000원이야?")
    time.sleep(1.5)
    print("수경: 맞네 내 눈이 이상한줄 알았어...")
    time.sleep(1.5)
    print("%s: 어차피 내기 잖아 그냥 먹자!!"%u.name)
    time.sleep(1.5)
    print("대환: 나는 절대 안걸리지~!!")
    time.sleep(1.5)
    print("%s: 그래 고고해 난 내기 중독 피로그래머니까,,,"%u.name)
    print()
    time.sleep(1.5)
    print("카페직원: 주문하시겠어요? ")
    time.sleep(1.5)
    print("아메리카노1번, 라떼2번, 차3번, 주스4번")
    time.sleep(1.5)
    menu = input(">>>")
    price=0
    if menu in ["아메리카노", "1번", "1"]:
        print()
        price=20000*4
        print("카페직원: 아메리카노로 준비해드릴께요.")
        time.sleep(1.5)

    elif menu in ["라떼", "2번", "2"]:
        print()
        price = 22000 * 4
        print("카페직원: 라떼로 준비해드릴께요.")
        time.sleep(1.5)

    elif menu in ["차", "3번", "3"]:
        print()
        price = 22000 * 4
        print("카페직원: 차로 준비해드릴께요.")
        time.sleep(1.5)

    elif menu in ["주스", "4번", "4"]:
        print()
        price = 16000 * 4
        print("카페직원: 주스로 준비해드릴께요.")
        time.sleep(1.5)
    print("")
    print("대환: 이제 누가 살지 정해볼까? 사다리 타기게임 어때?")
    time.sleep(1.5)
    print("%s: 좋지 ㄱㄱ!! "%u.name)
    time.sleep(1.5)
    print("거북이 색깔을 골라보세요. (초록, 빨강, 보라, 파랑)")
    time.sleep(1.5)
    turtlecolor = input()
    u.Ladder()
    if turtlecolor in ["초록", "초록 거북이"]:
        print()
        print("당첨 !! 커피 값을 쏘세요!")
        print("%s: 망했다......아오...."%u.name)
        print("[돈이 %d원 감소합니다.]"%price)
        print("[멘탈이 20 감소합니다.]")
        u.money=u.money-price
        u.mental-= 20
        time.sleep(1.5)
    else:
        print()
        print("커피를 얻어 드세요.")
        print("%s: 야호 신난다~~!!!"%u.name)
        time.sleep(1.5)


    print("현재 (%s) 멘탈: %d 돈: %d" % (u.name, u.mental, u.money))
    time.sleep(5)
    if (u.mental_check()):
        break
    u.SeongMo_check()


    # chapter 5
    print('#'*20,'   Chapter 5   ','#'*20)
    print()
    # 피로그래밍 수업이 끝났다.
    print("몇 시간을 봐도 이해되지 않는 classmethod와 staticmethod에 대한 궁금증을 뒤로 한 채로")
    print("길고 긴 오후 수업이 끝나고... ")
    print("오늘은 피로그래밍의 뒤풀이가 있다던데.\n")
    print("성모 : 뒤풀이는 차이나당입니다! %s님도 참여하실거죠?\n" % u.name)
    print("...뒤풀이에 참여하라는 무언의 압박을 받고 뒤풀이 장소로 향하게 되었다.")
    time.sleep(5)
    print("\n이동중...\n")
    time.sleep(3)
    print("종인 : 여기서는 꿔바로우를 시키는게 국룰이야.")
    print("소현 : 무슨 소리! 토마토계란볶음이 비주얼은 좀 그래도 최고라고!")
    print("영주 : 됐고, 일단 고량주부터 시켜.\n")
    time.sleep(3)
    print("모두가 다 흥겨운 것 같다. 나는 어제 팀과제하고 과제하느라 너무 피곤했는데 체력도 좋네.")
    print("그래도 다들 재밌게 노니까 즐겁다. 음식도 맛있네!\n")
    print("[멘탈 지수가 소폭 회복됩니다.]\n")
    u.mental += 10
    print("현재 (%s) 멘탈: %d 돈: %d\n" % (u.name, u.mental, u.money))

    time.sleep(3)
    print("술자리가 무르익고... 이제 집에 갈 시간이 다 되었다.\n")
    print("성익 : 그럼, 우리 오늘 뒤풀이값 몰아주기 내기하자.\n")
    print("성익이 눈치를 보더니... 베스킨 라빈스 31을 시작해버렸다!\n")
    time.sleep(3)
    print("-" * 8, "베스킨 라빈스 31", "-" * 8, '\n')
    A = input("게임을 시작할 준비가 되었으면 Y를 눌러 주세요!: ")

    while 1:
        if A == 'y' or A=='Y':
            fool = u.Baskin_Robbins_31()
            break
        else:
            print("내기묵시록 피.로그래밍에서 내기를 빠지는 일이란 있을 수 없어....")
            print("다시 생각해보자.\n")
            print("-" * 8, "베스킨 라빈스 31", "-" * 8, '\n')
            A = input("게임을 시작할 준비가 되었으면 Y를 눌러 주세요!: ")

    # 베스킨라빈스 31이 끝났다
    print("\n\n")
    time.sleep(2)
    print("모두 : 와~~ %s 고마워! 맛있게 잘 먹었어~\n" % fool)
    if fool == u.name:
        u.money -= 100000
        u.mental -= 40
        print("뒤풀이값이라니… 이건 아니잖아…")
        print("피.로그래밍, 돈과 멘탈 전부 망가졌어…\n")
    else:
        print("이겼다!")
        u.mental += 20
        time.sleep(1)

    print("\n현재 (%s) 멘탈: %d 돈: %d\n" % (u.name, u.mental, u.money))
    time.sleep(5)
    print("아, 오늘 너무 힘들었다. 이제 그만 집에가야지…\n\n")
    if (u.mental_check()):
        break
    u.SeongMo_check()


    end= True

if(u.mental_check()):
    print("\n\n안녕히 계세요 여러분")
    print("전 이 세상의 모든 굴레와~")
    print("          속박을~ 벗어던지고~")
    print("               제 지갑을 찾아 떠납니다~")
    print()
    print("여러분은 코딩하세요!!!!!")
else:
    time.sleep(1)
    print("엄청난 하루였다...")
    print("오늘 내기만 몇번을 한거야..??")
    time.sleep(2)
    if(u.SeongMoLoan):
        print("회장이 천천히 나한테 다가오는 것이 느껴졌다.\n")
        time.sleep(2)
        print("성모: 성모앤캐시에서 왔습니다 호갱.. 아니 고객님^^")
        print("      5만원에 이자 10프로 더하여서 총 5만 5천원 되겠습니다.\n")
        time.sleep(3)
        if(u.money>0):
            print("%s: 저... 남은 돈이 %d원 밖에 없는데요\n"%(u.name, u.money))
        else:
            print("%s: 죄송해요! 돈이 없어요!\n"%u.name)
        time.sleep(3)
        print("성모: 그럼 시간당 1000원으로 코딩 하시면 돼요 ^^")
        print("%d원이라고 하셨으니까 %d시간 하시면 되겠네요" % (u.money, (55000 - u.money) // 1000))
        time.sleep(3)
        print("으아아아아아아앙아아아아ㅏ앙아ㅏ아아악!!!")

    else:
        print("%s: 맞아 그래도 이 미친 내기 중독자들 사이에서 대출 안한게 어디야!"%u.name)
        if(u.money>0):
            print("남은 돈은... %d원인가?"%u.money)
            print("이정도면 뭐, 내일 내기도 안정적이네!")

    time.sleep(4)

print("-"*80)
print("내기묵시록 - 내기중독 피.로그래머".center(60))
print()
print("플레이 해 주셔서 감사합니다".center(60))
print("-"*80)
