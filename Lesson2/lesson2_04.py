"""
list（リスト型）
●リストのコピー
listはクラスなのでメソッドをもっています。helpで詳細を確認できます。
リストのコピーには参照渡しと値渡しの2つの方法があります。
"""
print("●参照渡し（「=」で代入）")
lis = [1,2,3,4,5,6,7,8,9]
tmp = lis
print(f"lis:{lis}\ttmp:{tmp}")
print(f"lis:{lis}\tアドレス番地:{id(lis)}")
print(f"tmp:{tmp}\tアドレス番地:{id(tmp)}")   #参照渡しなので同じアドレス番地になる
tmp[0] = 100        #tmpを変更
print(f"lis:{lis}\ttmp:{tmp}")      #参照渡しなので両方値が変更される

print("\n●値渡し（「「copy関数」使用）")
lis = [1,2,3,4,5,6,7,8,9]
tmp = lis.copy()
print(f"lis:{lis}\tアドレス番地:{id(lis)}")
print(f"tmp:{tmp}\tアドレス番地:{id(tmp)}")   #値渡しなのでアドレス番地が異なる
tmp[0] = 100        #tmpを変更
print(f"lis:{lis}\ttmp:{tmp}")      #値渡しなので元のリストの値は変更されない
