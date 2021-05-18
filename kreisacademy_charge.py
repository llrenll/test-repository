#自販機のお釣りの計算

#購入金額、投入金額の入力
kounyu = input('購入金額を入力してください')
tounyu = input('お金を投入してください')

#trueを入れておく
j = True

#投入金額が購入金額を上回っているかの判定（足りない場合はここで終了）
if int(tounyu) <= int(kounyu):
    print("お金が足りません")
    j = False

#投入金額が足りた場合
if j == True:
    oturi = int(tounyu) - int(kounyu)
    print('おつりは{}円です'.format(oturi))

    #お釣りの計算
    oturi_5000 = oturi // 5000
    print("5000円札は{}枚です".format(oturi_5000))
    oturi = oturi - oturi_5000 * 5000
    oturi_1000 = oturi // 1000
    print("1000円札は{}枚です".format(oturi_1000))
    oturi = oturi - oturi_1000 * 1000
    oturi_500 = oturi // 500
    print("500円玉は{}枚です".format(oturi_500))
    oturi = oturi - oturi_500 * 500
    oturi_100 = oturi // 100
    print("100円玉は{}枚です".format(oturi_100))
    oturi = oturi - oturi_100 * 100
    oturi_50 = oturi // 50
    print("50円玉は{}枚です".format(oturi_50))
    oturi = oturi - oturi_50 * 50
    oturi_10 = oturi // 10
    print("10円玉は{}枚です".format(oturi_10))
    oturi = oturi - oturi_10 * 10
    oturi_5 = oturi // 5
    print("5円玉は{}枚です".format(oturi_5))
    oturi = oturi - oturi_5 * 5
    oturi_1 = oturi // 1
    print("1円玉は{}枚です".format(oturi_1))
    oturi = oturi - oturi_1 * 1

#終了
print("ご利用ありがとうございました。")