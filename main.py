import random

#辞書(設定)
table = {1:10, 2:25, 3:50, 4:100, 5:1000}
table_name = {1:"Easy", 2:"Normal", 3:"Hard", 4:"Extra", 5:"Lunatic"}
table_explan = {1:"1~10", 2:"1~25", 3:"1~50", 4:"1~100", 5:"1~1000"}
table_count = {1:15, 2:10, 3:8, 4:7, 5:10}

#関数処理(難易度選択)
def select_difficulty():
    print("※難易度を1~4(5)で選択してね")
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

    print()

    max_num = table[difficulty]
    difficulty_name = table_name[difficulty]
    explan = table_explan[difficulty]
    init_count = table_count[difficulty]
    comp_value = table_comp_value[difficulty]

    answer = random.randint(1, max_num) 
    print(f"{difficulty_name}を選択しました")
    if difficulty in (1, 2, 3, 4):
        print(f"{explan}の数字を当てよう！")
    else:
        print(f"{explan}の数字を当てよう！文字通り狂気的だけど頑張ってね")
    
    print()

    while True:
        prep = input("確認できたらyを入力→")
        if prep in ("y", "Y"):
            break
        else:
            print("入力しなおしてね")
        
    return answer, init_count, comp_value, difficulty

#関数処理(ルール説明)
def rule_explan(count, difficulty):
    print("※次にルール説明")
    print(f"挑戦回数は {count} 回まで")
    print("回数を超えたらゲームオーバーになるよ")
    print()
    print("初回入力前にヒントがあって以下の範囲を基準値としているよ")
    if difficulty in (1, 2, 3, 4):
        print("Easy: 5~7基準")
        print("Normal: 10~15基準")
        print("Hard: 20~30基準")
        print("Extra: 40~60基準")
    else:
        print("Lunatic: 400~600基準")
    print()
    
    while True:
        prep = input("確認出来たらyを入力してね→")
        if prep in ("y", "Y"):
            break
        else:
            print("無効な文字だよ、入力しなおしてね")

#関数処理(入力前ヒント)
def befinput_hint(init_count, count, comp_value, answer):
    if init_count == count:
        if comp_value == answer:
            print("基準値と一致！")
        elif comp_value < answer:
            print("基準値より大きいよ！")
        elif comp_value > answer:
            print("基準値より小さいよ！")

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
    #設定
    random_easy = random.randint(5, 7)
    random_normal = random.randint(10, 15)
    random_hard = random.randint(20, 30)
    random_extra = random.randint(40, 60)
    random_lunatic = random.randint(400, 600)

    table_comp_value = {1:random_easy, 2:random_normal, 3:random_hard, 4:random_extra, 5:random_lunatic}

    #難易度選択
    answer, init_count, comp_value, difficulty = select_difficulty()
    print()

    #ルール説明
    count = init_count
    rule_explan(count, difficulty)
    print()

    #入力前ヒント
    befinput_hint(init_count, count, comp_value, answer)

    #ゲーム開始
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
    if diff == 0:
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