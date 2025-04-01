"""
計算
●数学関数
math関数使用（外部ライブラリ）
外部ライブラリは、ライブラリをimportして使用します。
参考URL：https://docs.python.org/ja/3.13/library/math.html
Math関数は対数や三角関数・浮動小数点数・平方根・絶対値などの
数学に使用するような複雑な計算を行うための関数です。
"""

import math

print("平方根：",math.sqrt(10))         #math.sqrt(x) : xの平方根を返す

print("切り捨て：",math.trunc(3.1415))  #math.trunc(x)：xの小数点以下を切り捨てて返す

print("最大整数",math.floor(-3.14))     #math.floor(x)：x以下の最大値の整数を返す（truncとceilとの違いに注意）

print("最小整数",math.ceil(-3.14))      #math.ceil(x)：x以下の最小値の整数を返す（truncとfloorとの違いに注意）

print("絶対値",math.fabs(-12.5))        #math.fabs(x)：xの絶対値を返

print("べき乗",math.pow(2,10))          #math.pow(x,y)：xのy乗を返す

print("対数",math.log2(3))              #math.log2(x)：2を底とするxの対数を返す

print(help(math))                       #Math関数のヘルプを表示
