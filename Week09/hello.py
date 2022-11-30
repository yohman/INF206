import random

print("じゃんけん・・・・・・・")

hands = ["グー✊","チョキ✌️","パー✋"]


while True:
  
  player_hand = int(input("0:グー✊ 1:チョキ✌️ 2:パー✋"))

  print("あなたは{}を出しました".format(hands[player_hand]))

  computer_hand = random.randrange(3)

  print("コンピューターは{}を出しました".format(hands[computer_hand]))

  if player_hand == 0 and computer_hand == 1:
    print("あなたの勝ち！🥳")
    break
  elif player_hand == 0 and computer_hand == 2:
    print("コンピューターの勝ち…😡")
    break
  elif player_hand == 1 and computer_hand == 0:
    print("コンピューターの勝ち…😡")
    break
  elif player_hand == 1 and computer_hand == 2:
    print("あなたの勝ち！🥳")
    break
  elif player_hand == 2 and computer_hand == 0:
    print("あなたの勝ち！🥳")
    break
  elif player_hand == 2 and computer_hand == 1:
    print("コンピューターの勝ち…😡")
    break
  else:
    print("あいこで…")
