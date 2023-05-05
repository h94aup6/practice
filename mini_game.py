class Game:
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
        def one_player():
            import random
            while True:    
                try:
                    global answer
                    answer = str(random.randint(1000,9999))
                    repeat_or_not(answer)
                except:
                    print(answer)
                    pass
                else:
                    print(answer)
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
                    break

        #猜數字
        def guess():
            count = 1
            while True:    
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
                                            position+=1
                                        elif yg in repeat_number:
                                            A+=1
                                            B-=1
                                            position+=1

                                    elif your_guess[position] != answer[position]:
                                        if yg not in repeat_number:
                                            B+=1
                                            repeat_number.append(yg)
                                            position+=1
                                        elif yg in repeat_number:
                                            position+=1
                                
                                elif yg not in answer:
                                    position+=1
                            print(f"{A}A{B}B,目前花了{count}次")
                            count+=1
                        except IndexError: #當position >= 4後中斷迴圈
                            break
                except ValueError:
                    print("請輸入四個數字!!!")
        
                
        if self.number_of_player == 1:
            one_player()
            guess()
        elif self.number_of_player == 2:
            two_players()
            guess()
        
Game().guess_number_AABB(1)
