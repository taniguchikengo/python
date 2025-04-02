"""
list（リスト型）
●リストのメソッド　
listはクラスなのでメソッドをもっています。helpで詳細を確認できます。
参考URL：https://docs.python.org/ja/3.13/library/stdtypes.html#typesseq-mutable
"""
#print(help(list))

print("●リストのメソッド")
lis1 ,lis2 = [1,2,3,4,5,1,2,3],[6,7,8,9,10]

lis1.append(10)
print(f"append：{lis1}")    #末尾に10追加

lis1.insert(0,200)          #最初の要素を200に変更
print(f"insert：{lis1}")

x = lis1.pop() 
print(f"popした値x:{x}\npop後のリスト：{lis1}" )

del lis1[0]                 #指定した要素番号の要素を削除
print(f"del：{lis1}")

lis1.remove(2)              #指定した値を削除（複数ある場合は最初の値だけ削除）
print(f"remove：{lis1}")

lis1.extend(lis2)           #リストの結合
print(f"extend：{lis1}")

ans = lis1.index(3)         #リストから「3」を検索して、対処のインデックス番号を返す
print(f"index：{ans}")

ans = lis1.count(3)         #対象の値がリストに何個あるか個数を返す
print(f"count：{ans}")

lis1.sort()                 #昇順で並び替え
print(f"sort(昇順)：{lis1}")

lis1.sort(reverse=True)     #降順で並び替え
print(f"sort(降順)：{lis1}") 
print(f"remove：{lis1}")
