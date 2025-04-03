"""
list（リスト型）
●リストの作成と表示　
リストは変更可能な（ミュータブル）な配列です。
リストは[]角括弧で囲んで宣言します。
リストの要素は「,」カンマで区切ります。
リストの要素番号は0から始まります。
参考URL:https://docs.python.org/ja/3.13/library/stdtypes.html#lists
"""
lis = ["1月","2月","3月","4月"]
print("●リストの作成と表示")
print(f"要素番号：{'0      1      2      3':>35}")
print(f"リストをそのまま表示：{lis}")
print(f"リストの要素番号2を表示：{lis[2]}")     #要素番号は0から始まる
print(f"リストの要素番号-1を表示：{lis[-1]}") 
print(f"スライスで要素番号1~2を表示：{lis[1:3]}") 
print(f"stepを2にして1つ飛ばしで表示：{lis[::2]}") 
print(f"stepを-1にして逆順で表示：{lis[::-1]}") 

print(f"\nlen関数を使用して要素数を表示：{len(lis)}")   #len(s):オブジェクトSの長さを返す
#参考URL:https://docs.python.org/ja/3.8/library/functions.html?highlight=len#len


"""
list（リスト型）
●二次元リスト
リストを二次元で作成することができます。
"""
print(f"\n●二次元リストの作成") 
lis2_1 = [[]]                       #[[]]で空の二次元配列を宣言できる
print(f"空の二次元リスト：{lis2_1}")
lis2_2 = [[0,1,2],[3,4,5]]          #値を入れて二次元配列を宣言
print(f"二次元リスト：{lis2_2}")
print(f"lis2_2[1]を表示：{lis2_2[1]}")
print(f"lis2_2[1][1]を表示：{lis2_2[1][1]}")
