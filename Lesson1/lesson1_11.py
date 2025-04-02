"""
str（文字列型）
●文字列型のメソッド　
strはクラスなのでメソッドをもっています。helpで詳細を確認できます。
参考URL：https://docs.python.org/ja/3.13/library/stdtypes.html#text-sequence-type-str
"""
#print(help(str))

s = "春はあけぼの。やうやう白くなりゆく山ぎは、"
print("●find関数")
print(f"「あけぼの」検索:{s.find('あけぼの')}")     #「あけぼの」を検索インデックス番号2で発見
print(f"6文字目以降で「あけぼの」検索：{s.find('あけぼの',5)}")     #発見できない場合は「-1」
print(f"6文字目から11文字目までで「白く」検索：{s.find('白く',5,11)}\n") 

print("●count関数")
print(f"「やう」の数：{s.count('やう')}")
print(f"8文字目以降の「やう」の数：{s.count('やう',8)}")
print(f"先頭から7文字目までの「やう」の数：{s.count('やう',0,7)}\n")

print("●replace関数")
print(f"「や」と「よ」を置換：{s.replace('や','よ')}")          #「や」を「よ」に置き換え
print(f"「や」と「よ」を1回置換：{s.replace('や','よ',1)}")     #「や」を「よ」に1回だけ置き換え
print(f"元の文字列：{s}\n")                                     #元の文字は変更されていない

f_name = "class_NAME.text"

print(f"capitalize（先頭だけ大文字）:{f_name.capitalize()}")        #capitalize:先頭だけ大文字
print(f"元の文字列：{f_name}\n")                                    #f_nameは変更されていない

print(f"title(単語の頭文字だけ大文字):{f_name.title()}")            #title:単語の頭文字だけ大文字
print(f"元の文字列：{f_name}\n")                                    #f_nameは変更されていない

print(f"upper(すべて大文字):{f_name.upper()}")                      #upper:すべて大文字
print(f"元の文字列：{f_name}\n")                                    #f_nameは変更されていない

print(f"lower(すべて小文字):{f_name.lower()}")                      #lower:すべて小文字
print(f"元の文字列：{f_name}\n")                                    #f_nameは変更されていない
