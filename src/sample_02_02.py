#utf-8だけでなく、自動で文字コードを判定してstr型に変換
import urllib.request
import cchardet#文字コードを推定するためのライブラリ

if __name__ == '__main__':
    url = 'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC'
    with urllib.request.urlopen(url) as res:
        byte = res.read()
        #文字コード変換
        html = byte.decode(cchardet.detect(byte)['encoding'])#Unicodeからstr型に変換
        print(html)