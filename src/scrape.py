import re
import unicodedata
from bs4 import BeautifulSoup

translation_table = str.maketrans(dict(zip('()!', '（）！')))#CaboChaは全角記号を前提としているので()!を全角に変換（）！

def cleanse(text):
    text = unicodedata.normalize('NFKC', text).translate(translation_table)#unicodedataライブラリのnormalize関数で各文字の表記を「Normalization Form Compatibility Composition」統一
    text = re.sub(r'\s+', ' ', text)#２つ以上連続する空白記号が日本語の文字列に混ざると問題になるので、連続する空白記号は1つの半角空白記号へ置換。
    return text

def scrape(html):#htmlから本文とタイトルを抽出
    soup = BeautifulSoup(html, 'html.parser')
    #__EOS__の挿入
    for block in soup.find_all(['br', 'p', 'h1', 'h2', 'h3', 'h4']):
        if len(block.text.strip()) > 0 and \
            block.text.strip()[-1] not in ['。', '！']:
                block.append('<__EOS__>')
    #本文の抽出
    text = '\n'.join([cleanse(block.text.strip())
                      for block in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4'])
                      if len(block.text.strip()) > 0])
    #タイトルの抽出
    title = cleanse(soup.title.text.replace(' - Wikipedia', ''))
    return text, title

