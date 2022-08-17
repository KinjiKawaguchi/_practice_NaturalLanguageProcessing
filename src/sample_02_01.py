#文字コードを変換しながらWebページを取得する
import urllib.request

if __name__ == '__main__':
    url = 'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC'
    with urllib.request.urlopen(url) as res:
        byte = res.read()
        #文字コード変換
        html = byte.decode('utf-8')#Unicodeからstr型に変換
        print(html)