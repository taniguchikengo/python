"""
変数の宣言
pythonは変数宣言の際に型を指定しなくてもよい
インタプリタが自動で型を決めてくれる。型推論という
"""
n = 10            #整数型
st = "Hello World!" #文字列型
flag = True         #boolean型
print(n,st)       #コンソールに変数の内容を表示する


"""
python3.6以降は、明示的に型宣言できるようになりました
"""
num:int = 100
name:str = "tanaka"


"""
変数の型の確認
type関数を使用し、型の確認ができる
"""
print(n,":" ,type(n))
print(st,":" ,type(st))
print(flag,":",type(flag))
print(num,":",type(num))
print(name,":",type(name))
