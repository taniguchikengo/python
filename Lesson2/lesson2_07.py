"""
tuple（タプル型）
●タプルの作成と表示
タプルは変更不可能な（イミュータブル）な配列です。
タプルは()丸括弧で囲んで宣言します。
タプルの要素は「,」カンマで区切ります。
タプルの要素番号は0から始まります。
タプルの要素が1つの場合は最後に「,」カンマを付けます。
参考URL:https://docs.python.org/ja/3.13/library/stdtypes.html#tuple
"""

tup1 = ('リンゴ', 'バナナ','リンゴ', 'パイナップル')
print("●タプルの作成と表示")
print(f"tup1の型：{type(tup1)}\ttup1の内容：{tup1}")
print(f"tup1の先頭を表示：{tup1[0]}") 
#tup1[0] = "ゴリラ"     #タプルはイミュータブルなのでエラーになる

tup2 = 1,2,3,4,5,6,7
print(f"\n・()丸括弧を省略してもタプルになる")
print(f"tup2の型：{type(tup2)}\ttup2の内容：{tup2}")

print("\n・listメソッドとほぼ同じ操作ができる")
print(f"スライスも使用できる：{tup2[2:5]}")
print(f"indexも使用できる：{tup1.index('バナナ')}")
print(f"countも使用できる：{tup1.count('リンゴ')}")
tup3 = (1,2,3)+(4,5,6)
print(f"結合もできる:{tup3}")


"""
tuple（タプル型）
●アンパック代入
タプルやリストの中身を複数の変数に一行で格納する事ができます。
この操作の事をアンパック代入やアンパッキングと言います。 
"""
tup4 = (10,20,30)
x,y,z = tup4
print(f"\n・アンパック代入")
print("x,y,z：",x,y,z)
#a,b = tup4    #要素数と格納する変数の数が一致していないとエラーになる 
