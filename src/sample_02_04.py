#テキストデータのクレンジング
import re
import unicodedata

text = '    ＣＬＥＡＮＳ ing  によりﾃｷｽﾄﾃﾞｰﾀを変換すると　トラブルがすくなくなります。'
print('Before',text)

translation_table = str.maketrans(dict(zip('()!','（）！')))
text = unicodedata.normalize('NFKC',text).translate(translation_table)
text = re.sub(r'\s+','',text)
print('After:',text)