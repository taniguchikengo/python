"""
str（文字列型）
●文字列の連結
文字列は「+」を使用し連結することができます。
"""
a ,b = "hello ","world"
print(a+b)              #文字列どうしの連結は「+」でつなぐだけ

num,name = 20,"斎藤"
print(name + "さんは" + str(num) + "才です")    #numはint型のためstr型に変換しないと文字列nameに連結できない
#print(name + "さんは" + num + "才です")        #エラーになる


"""
str（文字列型）
●文字列の連結 format関数
format関数を使用し、文字列を連結することができる。
文字列.format(val1, val2)
文字列に埋められた{}を引数のval1,val2に置き換える
"""
s1 = "本日"
s2 = "晴れ"
print("{}の天気は、{}です。".format(s1,s2))

s1 = input("誰が：")                #input関数：コンソールから入力を受け取る
s2 = input("何を")
s3 = input("どうした")
print("{}が{}を{}".format(s1,s2,s3)) 


"""
str（文字列型）
●文字列の連結 f-string
f-stringを使用し、文字列を連結することができる。
python3.6からf-stringが使用できるようになりました。
format関数と同じように{}を使用しますが、{}の中に変数を入れるのが特徴です。
また、書式の設定もできます。「"」の前にfを記入します。
f"文字列{変数}"
"""
x,y,z = "今日","天気","晴れ"
print(f"{x}の{y}は{z}だ")

num = 1234
print(f'{num}') 
print(f'{num:,}')   #桁区切り
print(f'{num:8}')   #8桁で表示。指定桁未満の場合はスペース
print(f'{num:08}')  #0埋め。＃や＊なども指定できます
print(f'{num:*>8}') #右寄せ、８桁
print(f'{num:*^8}') #中央寄せ、８桁
print(f'{num:*<8}') #左寄せ、８桁
num = 1234.567
print(f'{num:.2f}') #小数点第3位を四捨五入し、2桁表示
