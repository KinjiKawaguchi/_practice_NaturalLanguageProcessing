#テキストデータのクレンジング

#クレンジングとは、データ分析をする前に、分析処理をしやすくするために整形することである。
#CaboChaを使う上で適切なテキストデータを変換しておくことでトラブルを減らします。
import re
import unicodedata

text = '    ＣＬＥＡＮＳ ing  によりﾃｷｽﾄﾃﾞｰﾀを変換すると　トラブルがすくなくなります。'
print('Before',text)

translation_table = str.maketrans(dict(zip('()!','（）！')))#CaboChaは全角記号を前提としているので()!を全角に変換（）！
text = unicodedata.normalize('NFKC',text).translate(translation_table)#unicodedataライブラリのnormalize関数で各文字の表記を「Normalization Form Compatibility Composition」統一
text = re.sub(r'\s+','',text)#２つ以上連続する空白記号が日本語の文字列に混ざると問題になるので、連続する空白記号は1つの半角空白記号へ置換。
print('After:',text)