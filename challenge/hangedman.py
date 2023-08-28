
import random

answers = ["いと", "くつした", "きつね", "こーひー",
           "たこやき", "とうきょう", "かみさま",
           "がれき", "なべ", "くるま", "おじさん",
           "しごと", "かんこうきゃく", "ひらがな",
           "うどん", "しょうがつ", "りんじん",
           "やさいいため", "ぱそこん"
           ]

w = random.randint(0, 18)


def hangedman(word):
    wrong = 0
    stages = ["",
              "________       ",
              "|              ",
              "|       |      ",
              "|       O      ",
              "|      /|      ",
              "|       |      ",
              "|      /       "
              "|              "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングドマンへようこそ！")
    print("\n")
    print("ゲームルール")
    print("吊るし人が完成する前に、お題になっている単語（ひらがな数文字）を一文字づつ当てよう")

    while wrong < len(stages) -1:
        print("\n")
        msg = "一文字を予想して入力して下さい"
        
        char = input(msg)
        if char in rletters:
            print("\n")
            print("あたり！！")
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            print("\n")
            print("外れ...")
            wrong += 1

        print("ヒント↓")
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！！")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け....正解は {}".format(word))

hangedman(answers[w])
