import random

table = {1:10, 2:25, 3:50, 4:100, 5:1000}

table_name = {1:"Easy", 2:"Normal", 3:"Hard", 4:"Extra", 5:"Lunatic"}

table_explan = {1:"1~10", 2:"1~25", 3:"1~50", 4:"1~100", 5:"1~1000"}

#関数処理(難易度選択)
def select_difficulty():
    print("難易度を選択してね")
    print("1: Easy")
    print("2: Normal")
    print("3: Hard")
    print("4: Extra")

    print()

    while True:
        difficulty = int(input("数字を入れてね→"))
        if difficulty in (1, 2, 3, 4, 5):
            break
        else:
            print("無効な数字だよ💦もう一回入力してね")

    max_num = table[difficulty]
    difficulty_name = table_name[difficulty]
    explan = table_explan[difficulty]

    answer = random.randint(1, max_num)
    print(f"{difficulty_name}を選択しました")
    if difficulty in (1, 2, 3, 4):
        print(f"{explan}の数字を当てよう！")
    elif difficulty == 5:
        print(f"{explan}の数字を当てよう！文字通り狂気的だけど頑張ってね")
    return answer

#関数処理(距離ヒント)
def distance_hint(diff):
    if diff <= 1:
        print("ニアピン！！惜しい！")

    elif diff <= 2:
        print("ちょっと近いね、！")
        
    elif diff <= 4:
        print("ボチボチだね🤔")

    else:
        print("ちょっと遠いかな💦")


while True:
    #難易度選択
    answer = select_difficulty()

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
        distance_hint(diff)

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
                exit("遊んでくれてありがとう！")
        elif retry in ("y", "Y"):
                print("もう一度遊ぶんだね！ありがとう😄")
                print("難易度選択に戻るよ！")
                break
        else:
            print("その数字は無効だよ💦")
            print("もう一回選んでね")

    print()