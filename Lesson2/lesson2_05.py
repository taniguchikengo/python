"""
list（リスト型）
●リストを空にする
リストの内容を空にする方法は「lis.clear()」と「lis=[]」の2種類あるが、少し違います
"""
original_lis = [1,3,5,7]
lis1 = original_lis
lis2 = original_lis
print(f"original_lisアドレス:{str(id(original_lis))}")
print(f"lis1アドレス:{str(id(lis1))}")
print(f"lis2アドレス:{str(id(lis2))}")
print("参照渡しなのですべて同じアドレス")

lis1 = []       #lis1を空にする
print("\n●lis1 = []")
print(f"lis1アドレス:{str(id(lis1))}\t宣言しなおしているのでアドレスが変わる")      
print(f"original_lis：{original_lis},lis1：{lis1}")     #当然オリジナルは変更されていない

lis2.clear()
print("\n●lis2.clear")
print(f"lis2アドレス:{str(id(lis2))}\tアドレスは変わらない")      #アドレスは変わっていない
print(f"original_lis：{original_lis},lis2：{lis2}")
