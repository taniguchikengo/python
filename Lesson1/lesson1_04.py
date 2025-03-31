"""
計算
●四則演算
C言語やJavaとほぼ同じ
"""
a,b = 17,3      #一行で複数代入できる（アンパック代入）
print("a+b =",a+b)      #足し算
print("a-b =",a-b)      #引き算
print("a*b =",a*b)      #掛け算
print("a**b =",a**b)    #べき乗
print("a/b =",a/b)      #割り算（表示可能領域まで小数点以下を表示）
print("a//b =",a//b)    #割り算（整数）
print("a%b =",a%b)      #余り


"""
●四捨五入
round関数使用（標準関数）
round(number, ndigits=None)
number を小数点以下 ndigits 桁の精度で四捨五入した値を返す。
ndigits が省略されたり、None だった場合、入力値に最も近い整数を返す。
"""
print("a/b =",round(a/b))       #小数点第1位で四捨五入して、整数を表示
print("a/b =",round(a/b,3))     #小数点第4位で四捨五入して、小数点第3位までを表示
