"""
計算
●ランダム
random関数使用（外部ライブラリ）
外部ライブラリは、ライブラリをimportして使用します。
参考URL：https://docs.python.org/ja/3.13/library/random.html
"""

import random

"""
●random.random()
ランダムな浮動小数点数（範囲は 0.0 <= X < 1.0）を返します。
"""
print("0.0から1.0までの間のランダムな少数")
print(random.random())
print()


"""
●random.uniform(a, b)
 a <= N <= b  のランダムな浮動小数点数 N を返します。
"""
print("3.0から5.0までの間のランダムな浮動小数点数")
print(random.uniform(3.0,5.0))
print()


"""
●random.randint(a, b)
a <= N <= b であるようなランダムな整数 N を返します。
"""
print("7から10までの間のランダムな整数")
print(random.randint(7,10))
print()


"""
●random.seed(a=None, version=2)
乱数生成器を初期化します。
a が省略されるか None の場合、現在のシステム時刻が使用されます。
a が int の場合、それが直接使われます。
"""
random.seed(100)
print("毎回同じ値")
print(random.random())
