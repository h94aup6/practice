class Game:
    #剪刀石頭布
    def pss(self,number_of_player):
        self.number_of_player = number_of_player
        pss_list = ["剪刀","石頭","布"]

        #與電腦猜拳
        def single_player():
            import random

            #電腦選擇
            a_choice = random.choice(pss_list)
            print("電腦選擇完畢")

            #玩家選擇
            b_choice = input("玩家出拳：")
            while b_choice not in pss_list:
                print(f"請出{pss_list}中的一種!!!")
                b_choice = input("玩家出拳：")

            #輸贏階段        
            print("\n電腦出" + a_choice)
            if b_choice == "剪刀" and a_choice == "布"\
            or b_choice == "石頭" and a_choice == "剪刀"\
            or b_choice == "布" and a_choice == "石頭":
                print("玩家勝利")
            elif a_choice == b_choice:
                print("平手")
            elif b_choice == "剪刀" and a_choice == "石頭"\
            or b_choice == "石頭" and a_choice == "布"\
            or b_choice == "布" and a_choice == "剪刀":
                print("電腦勝利")


        #多人猜拳
        def multiple_players():
            import os
            import keyboard
            
            #出拳階段
            p = 1
            players_choices = []
            keyboard.block_key("up") #禁止作弊
            keyboard.block_key("right") #禁止作弊
            while p <= number_of_player:
                choice = input(f"玩家{p}出拳：")
                while choice not in pss_list:
                    print(f"請出{pss_list}中的一種!!!")
                    choice = input(f"玩家{p}出拳：")
                players_choices.append(choice)
                p+=1
                os.system("cls")
            print("所有玩家出拳完畢，請按Enter判斷勝負：")
            keyboard.wait("enter")
            
            #輸贏階段
            p = 0
            for i in players_choices:
                print(f"玩家{p+1}出{players_choices[p]}")
                p+=1
            
            print("\n結果：")
            p = 0
            players_choices_set = set(players_choices)
            if len(players_choices_set) == 3 or len(players_choices_set) == 1:
                print("平手")
            elif "剪刀" not in players_choices_set:
                for i in players_choices:
                    if i == "布":
                        print(f"玩家{p+1}勝利")
                    p+=1
            elif "石頭" not in players_choices_set:
                for i in players_choices:
                    if i == "剪刀":
                        print(f"玩家{p+1}勝利")
                    p+=1
            elif "布" not in players_choices_set:
                for i in players_choices:
                    if i == "石頭":
                        print(f"玩家{p+1}勝利")
                    p+=1

        if number_of_player == 1:
            single_player()
        elif number_of_player >= 2:
            multiple_players()

    

    #幾A幾B
    def guess_number_AABB(self,number_of_player):
        self.number_of_player = number_of_player

        #判斷數字是否重複
        def repeat_or_not(a):
            b = a
            check = []
            for i in b:
                check.append(i)
            for j in check:
                if check.count(j) > 1:
                    raise

        #單人模式
        def single_player():
            import random
            while True:    
                try:
                    global answer
                    answer = str(random.randint(1000,9999))
                    repeat_or_not(answer)
                except:
                    pass
                else:
                    print(answer)
                    print("電腦出題完畢")
                    break

        #雙人模式
        def two_players():
            while True:
                try:
                    global answer
                    answer = int(input("請出題："))
                    if answer < 1000 or answer > 9999: #確認數字範圍
                        raise
                    answer = str(answer)
                    repeat_or_not(answer) #確認無重複數字
                except:
                    print("範圍是1000～9999的整數，數字不可重複")
                else:
                    import os
                    os.system("cls")
                    break

        #猜的過程
        def guess():
            count = 1
            import keyboard
            while True:
                keyboard.block_key("up")
                keyboard.block_key("right")
                your_guess = input("請猜：")
                try:
                    int(your_guess) #確保是數字
                    if len(your_guess) != 4: #確保是四位數
                        raise ValueError
                    if your_guess == answer:
                        print(f"猜對了。總共花了{count}次")
                        break
                    else:
                        A = 0
                        B = 0
                        position = 0
                        repeat_number = [] #避免對重複數字進行判斷
                        try:
                            for yg in your_guess:
                                if yg in answer:
                                    if your_guess[position] == answer[position]:
                                        if yg not in repeat_number:
                                            A+=1
                                            repeat_number.append(yg)
                                        elif yg in repeat_number:
                                            A+=1
                                            B-=1

                                    elif your_guess[position] != answer[position]:
                                        if yg not in repeat_number:
                                            B+=1
                                            repeat_number.append(yg)

                                position+=1
                            print(f"{A}A{B}B,目前花了{count}次")
                            count+=1
                        except:
                            pass
                except ValueError:
                    print("請輸入四個數字!!!")
        
        if number_of_player == 1:
            single_player()
            guess()
        elif number_of_player == 2:
            two_players()
            guess()
        

a = Game().pss(2)
# a = Game().guess_number_AABB(2)
