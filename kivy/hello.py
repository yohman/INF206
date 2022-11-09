import random
import time

# handsというリストに、じゃんけんの手を覚（おぼ）えておいてもらう
hands=['グー', 'チョキ', 'パー']

# どの数字が、どの手を表（あらわ）しているのかを表示（ひょうじ）する
print('0:グー 1:チョキ 2:パー 3:ゲームを終わる')
# 「じゃんけん」と表示する
print('「じゃんけん……」')

# ゲーム全体（ぜんたい）を繰（く）り返（かえ）す
while True:

    # 正しく入力されたかどうかを判定。入力の部分を繰り返す
    while True:
        # プレイヤーからの入力をinput_strに覚えておいてもらう
        input_str=input('ここに番号を入力してね！>>> ')

        # 入力が'0', '1', '2', '3'のどれかなら、入力の部分の繰り替えしから抜（ぬ）ける
        if input_str in ['0', '1', '2', '3']:
            break
        # 入力が'0', '1', '2', '3'のどれでもなければ、「間違えて入力しているよ」と表示
        else:
            print('間違えて入力しているよ')

    # もし入力された番号が3のときは、ゲームを終わる。このとき、3は数字ではなくて、文字になっているので注意！
    if input_str=='3':
        print('ゲームを終了します')
        break

    # 入力されたものは文字列（もじれつ）になっているので、数値（すうち）に変換（へんかん）したものを、hand_numに覚えておいてもらう
    hand_num=int(input_str)

    # ランダムにコンピュータの手の数字を決めて、computer_hand_numに覚えておいてもらう
    computer_hand_num=random.randrange(3)
    # ランダムで作った数字から、コンピュータがどの手なのかを出して、computer_handに覚えておいてもらう
    computer_hand=hands[computer_hand_num]

    # 入力された数字から、どの手なのかを出して、player_handに覚えておいてもらう
    player_hand=hands[hand_num]

    # 「ぽん」と表示する
    print('「ぽん」')
    # 1秒待つ
    time.sleep(1)

    # player_handに覚えておいてもらった手を表示する
    print('あなたは'+player_hand+'を出しました')
    # computer_handに覚えておいてもらった手を表示する
    print('コンピュータは'+computer_hand+'を出しました')

    # あいこのときは0、プレイヤーが負けたときは-1か2、プレイヤーが勝ったときは-2か1という数字を、変数win_or_loseに覚えておいてもらう
    win_or_loss=computer_hand_num-hand_num

    # 1秒待つ
    time.sleep(1)

    # じゃんけんの勝ち負けを表示する
    if win_or_loss==0:
        print('あいこだね')
    elif win_or_loss==-1 or win_or_loss==2:
        print('あなたの負け')
        # ゲームを終わる
        break
    elif win_or_loss==-2 or win_or_loss==1:
        print('あなたの勝ち')
        # ゲームを終わる
        break
