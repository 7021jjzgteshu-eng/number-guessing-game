import random

while True:
    #難易度選択
    print("難易度を選択してね")
    print("1: Easy")
    print("2: Normal")
    print("3: Hard")
    print("4: Extra")

    while True:
        difficulty = int(input("数字で選択してね→"))
        if difficulty in (1, 2, 3, 4, 5):
            break
        else:
            print("その数字は無効だよ💦もう一回入力してね")

    print()

    if difficulty == 1:
        answer = random.randint(1, 10)
        print("Easy を選択しました")
        print("1=10までの数を当てよう")
        
    elif difficulty == 2:
        answer = random.randint(1, 25)
        print("Normal を選択しました")
        print("1~25までの数を当てよう")

    elif difficulty == 3:
        answer = random.randint(1, 50)
        print("Hard を選択しました")
        print("1~50までの数を当てよう")

    elif difficulty == 4:
        answer = random.randint(1, 100)
        print("Extra を選択しました")
        print("1~100までの数を当てよう")

    elif difficulty == 5:
        answer = random.randint(1, 1000)
        print("Lunatic を選択しました")
        print("1~1000までの数字だよ。文字通り狂気的だけど頑張ってね")

    #ゲーム開始
    count = 15
    print()
    print("挑戦回数は15回までだよ")
    print("回数を超えたらゲームオーバー😭")

    while True:
        #ループ開始
        print()
        print(f"あと {count} 回だよ！")

        #入力と処理
        guess = int(input("数字を入れてね→"))
        diff = abs(guess - answer)
        count -= 1

        #判定
        if diff == 0:
            print(f"答えは {answer} だね！正解！")
            break

        if count <= 0:
            print("ゲームオーバー😭")
            break

        #ヒント表示(方向)
        if guess < answer:
            print("もっと大きいよ")

        elif guess > answer:
            print("もっと小さいよ")

        #ヒント表示(距離)
        if diff <= 1:
            print("ニアピン！！惜しい！")

        elif diff <= 2:
            print("ちょっと近いね、！")
        
        elif diff <= 4:
            print("ボチボチだね🤔")

        else:
            print("ちょっと遠いかな💦")
        
    #終了後コメント
    print()
    if diff <= 0:
        print("クリアできたね！！おめでとう😃")
        
    elif count <= 0:
        print("クリアできなかったね。。。ざんねん😭")

    #リトライ選択
    while True:
        print()
        retry = input("もう一度遊ぶ？ (y/n)→")

        print()

        if retry in ("n", "N"):
                exit("遊んでくれてありがとう")
        elif retry in ("y", "Y"):
                print("もう一度遊ぶんだね！ありがとう😄")
                print("難易度選択に戻るよ！")
                break
        else:
            print("その数字は無効だよ💦")
            print("もう一回選んでね")

    print()