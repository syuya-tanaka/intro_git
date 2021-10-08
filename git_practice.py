print("hello")
print("say hello")
print("git add")
print("眠たいですね")
print("いろいろありますね")


def saiki(x):
    while True:
        if x < 0:
            return 0
        return saiki(x - 1) + x


print(saiki(10))

# git pull コマンドを学んでいます


CHOICE_CATEGORY = (
    # Modelにだけ、ホームの選択肢を追加
    # Formにはユーザーがフォームで選択できないように追加していない。
    ("", "選択してください。"),
    ("ホーム", "ホーム"),
    # 上のホームはデータベースをやり直した場合のみコメントアウトを解除する。
    # データベースをやり直した時の手順
    # まずadminにいって、CategoryModelを全て作成する。
    # 次にThreadModelを'ホーム'で作成する。
    # そして最後にこのホームをコメントアウトする。
    # 理由は、ユーザーがスレッドを作成するフォームでホームが選択可能になっているからだ。対処は雑になっているがこうする。
    # 原因はCategoryModelには無かった。
    # ホームをコメントアウトにしてもカテゴリのChoicefieldには'ホーム'があった。
    # foreignkeyでつないでいるため、
    # 作成されたオブジェクトを取得しているだけだと思う。
    ("日常", "日常"),
    ("数学", "数学"),
    ("IT", "IT"),
    ("読書", "読書"),
    ("映画", "映画"),
    ("音楽", "音楽"),
    ("エンタメ", "エンタメ"),
    ("スポーツ", "スポーツ"),
    ("服飾", "服飾"),
    ("議論", "議論"),
)


def ddtest():
    for i in range(1, 12):
        category = CHOICE_CATEGORY[i][0]
        count = int()
        count += 1
        print(category)


ddtest()
