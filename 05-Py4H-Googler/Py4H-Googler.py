#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
import mechanize,sys,re,html.parser,urllib.request,urllib.parse,urllib.error # kullanacağımız modüller(kütüphaneler)
from bs4 import BeautifulSoup # kullanacağımız modüller(kütüphaneler)

h = html.parser.HTMLParser() # HtmlParser metodu için referans gösterdik
br = mechanize.Browser() # mechanize Browser metodu için referans gösterdik
br.set_handle_robots(False) # robots.txt engellerine yakalanmamak için false dedik
br.addheaders = [('User-agent', 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)')] # tarayıcımıza header bilgisi ekledik.


def giris(): # giris fonksiyonumuz
	try:
		if sys.argv[1] == "-d" and sys.argv[3] == "-s" and sys.argv[5] == "-f": #Eğer '-d,-s,-f' argümanları var ise
			dork = sys.argv[2] # dorkumuzu aldık
			sayfa_sayisi = sys.argv[4] # sayfa sayısını aldık
			dosya_ismi = sys.argv[6] # sonuçların kayıt edileceği dosyamızı aldık
			arama(dork,sayfa_sayisi,dosya_ismi) # arama fonksiyonuna gönderdik
		else: #argümanlar yok ise
			print("    >> python googler.py -d /admin.php -s 10 -f cikti.txt \n\n    -d = dork \n    -s = Sayfa sayısı\n    -f = kaydedilcek dosya ismi")
	except:
		print("    >> python googler.py -d /admin.php -s 10 -f cikti.txt \n\n    -d = dork \n    -s = Sayfa sayısı\n    -f = kaydedilcek dosya ismi")


def arama(dork,sayfa_sayisi,dosya_ismi): # arama fonksiyonumuz ve fonksiyona gelen değerler
	dosya = open(dosya_ismi,"a") # dosyamızı açtık
	dorks=urllib.parse.quote(dork) #dorkumuzu encode ettik bazı karakterlerden ötürü hata vermemesi için
	for i in range(0,int(sayfa_sayisi)): # sayfa sayisi kadar dönen döngümüz
		ss = i+1 # ss 1 arttırdık
		url = "https://www.google.com.tr/search?q=%s&noj=1&start=%s0" %(dorks,i) # url de değerleri yerine koyduk
		print("[+] %s. Sayfa yazildi.." %ss) # uyarı mesajımız
		a = br.open(url) # linkimizi açtık
		kodlar = a.read() # kaynak kodlarımızı aldık çıkan sayfadan
		kazan = BeautifulSoup(kodlar) # Ben buna kodları kazana atmak diyorum.
		ayiklama = kazan.find_all('h3') # kaynak kodlardan h3 taglarını aldık ve liste olarak kayıt ettik dikkat 'ayiklama' listedir.
		for i in ayiklama: # listemizde ki elemanları tek tek dökerken
			ayiklama1 = i.find_all('a') # aynı şekilde dökülen her elemandan a taglarını aldık <a href=''></a> şeklinde olur..
			#print ayiklama1
			for a in ayiklama1: # a taglarını döküyoruz
				hedef = a.get('href') # a taglarının içinde ki href değerlerini aldık
				l = hedef.lstrip('/url?q=') # değerlerin solundan birşeyleri kestik attık.
				f = re.findall('(.*?)&sa',l) # hala istemediğimiz değerler vardı bu şekilde son defa re.findall ile basit bir kural belirleyerek istediğimizi aldık.
				for hedef in f: # son aldığımız değerleri döküyoruz
					asd = h.unescape(urllib.parse.unquote(hedef)) # değerler html encode halinde ve bazı bozuklukları var tamir ettik
					dosya.write(asd+"\n") # dosyamıza yazdırdık
					#print hedef

	dosya.close() # dosyamızı kapattık
	print("\n[-] İşlem bitmiştir.. ") #uyarı mesajı

giris() #giris fonksiyonunu çalıştır.