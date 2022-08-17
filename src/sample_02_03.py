#HTMLデータからテキストを抜き出す
import urllib.request
import cchardet#文字コードを推定するためのライブラリ
from bs4 import BeautifulSoup#タイトルと本文を抜き出す

if __name__ == '__main__':
    url = 'https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC'
    with urllib.request.urlopen(url) as res:
        byte = res.read()
        #文字コード変換
        html = byte.decode(cchardet.detect(byte)['encoding'])#Unicodeからstr型に変換
        soup = BeautifulSoup(html,'html.parser')

        title = soup.head.title#<head>-><title>のようにHTMLタグをたどり、そこのテキストをｔる魏の行でprintする。
        print('[title]:',title.text,'\n')

        for block in soup.find_all(['p','h1','h2','h3','h4']):#'p','h1','h2','h3','h4'のタグの内容を取得。
            print('[block]:',block.text)