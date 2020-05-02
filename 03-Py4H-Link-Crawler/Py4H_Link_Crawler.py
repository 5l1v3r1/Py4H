#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
import mechanize,sys,re


br = mechanize.Browser() # br adında tarayıcı(Browser) nesnesi oluşturduk.
br.set_handle_robots(False) # tarayıcımızın robot engeline takılmaması için ufak bir ayar
br.addheaders = [('user-agent',
				  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]
#Tarayıcımıza üstteki kodda başlık ekledik.

def bilgi(): # kullanıcıya bilgi veren fonksiyonumuz.
	print("[-] Example Usage:")
	print("[+] python crawler.py www.google.com")

try: # olası hatalar için try yapımız
	dosya = open("sonuc.txt","w") # dosyamızı açtık
	link = sys.argv[1] # bağlantımızı argüman ile aldık
	denetle = link.split(".") # denetlemek için . (nokta) ile bağlantımızı ayrıştırdık.

	if re.findall(":",denetle[0]): # eğer bağlantıda : var ise
		bilgi() # bilgi metodumuz başlıyacak
		sys.exit() # program sonlancak

	d_link = "http://"+link # bağlantımızı istediğimiz hale çevirdik
	print("Start scanning...  >>  "+link) #bağlantı taranıyor

	br.open(d_link) # bağlantımızı açtık
	for links in br.links(): # tüm bağlantıları topladık ve for döngüsü ile boşaltıcaz içini
		if re.findall(denetle[1],links.url): # www.site.com site kelimesi topladığımız bağlantıda var mı ?
			dosya.write(links.url+"\n") # varsa dosyaya yaz
		else: # yoksa
			dosya.write(d_link+links.url+"\n") # dosyaya bu şekilde yaz. /wiev.php gibi kaynak koddaki bağlantılar için.
	print("[+] Done. Read file >> sonuc.txt") # BİTTİ

except: # Hata varsa
	bilgi() #bilgi metodunu çağır