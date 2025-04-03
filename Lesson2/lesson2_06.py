"""
list（リスト型）
●split(文字列を区切ってリストに格納)
split()を使用すると、文字列を区切るくことができます。
str.split(sep=None, maxsplit=-1)
sep をデリミタ文字列(区切文字)として、文字列を区切った単語のリストを返す。
maxsplit が与えられていれば、最大で maxsplit 回分割される。 
maxsplit が与えられないか -1 なら、分割の回数に制限はない (可能なだけ分割される)。
sep が指定されていないか None の場合、スペースをデリミタ文字列とする。
参考URL:https://docs.python.org/ja/3.5/library/stdtypes.html?highlight=split#str.split
"""
csv_str = "リンゴ,バナナ,リンゴ,パイナップル"
lis = csv_str.split(",")
print("●split(文字列を区切ってリストに格納)")
print("・カンマでsplit")
print(f"元データ(csv_str)：{csv_str}")
print(f"「,」（カンマ）でsplitした値：{str(lis)}")

csv_str = "リンゴ バナナ リンゴ パイナップル"
lis = csv_str.split()
print("\n・スペースでsplit")
print(f"元データ(csv_str)：{csv_str}")
print(f"引数を省略してsplitした値：{str(lis)}")


"""
list（リスト型）
●join(リストの中身を結合し文字列にする)
join()を使用すると、リストの中身を結合し文字列にすることができます。
str.join(iterable)
iterable 中の文字列をstrで結合した文字列を返します。
参考URL:https://docs.python.org/ja/3.13/library/stdtypes.html#str.join
"""
lis = ['リンゴ', 'バナナ', 'リンゴ', 'パイナップル']
print("\n●join(リストの中身を結合し文字列にする)")
s1 = ",".join(lis)
s2 = "".join(lis)
print(f"カンマで結合:{s1}")
print(f"結合文字列なし:{s2}")
