# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup
import requests
from janome.tokenizer import Tokenizer
import sys


def rhyme (text):
    try:
		t = Tokenizer()
		tokens = t.tokenize(unicode(text,'utf-8'))
		rhyme_text = ""
		for token in tokens:
			if (token.part_of_speech.split(',')[0] == u"名詞") or (token.part_of_speech.split(',')[0] ==u"副詞"):
				url = "https://kujirahand.com/web-tools/Words.php?m=boin-search&opt=comp&len=%3F&key="+token.reading.encode('utf-8')
				html = urllib2.urlopen(url)
				soup = BeautifulSoup(html, "html.parser")
				rym = soup.find('rb').string
				rhyme_text += rym.encode('utf-8')
			else:
				rhyme_text += token.surface.encode('utf-8')
	
		return rhyme_text

    except:
		import traceback
		traceback.print_exc()
		return "見つかりませんでした"



def main():
	args = sys.argv
	message = args[1]		
	print message
	print rhyme(message)


if __name__ == "__main__":
	main()
