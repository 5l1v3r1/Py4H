🕊 Bu döküman [**@KekikAkademi**](https://t.me/KekikAkademi "Telegram: @KekikAkademi") için oluşturulmuştur. ✌🏼
________________________________
# Py4H Googler
![Python Google Searcher](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/5-Py4H-Googler/images/python-google-searcher.jpg)

Merhaba arkadaşlar. Bugün **Hackerlar için Python Programlama Dili** yani **Python4Hackers** diyerek ilk projemizi beraber yapıyor olacağız.
Başlıktan da anlaşılacağı gibi Google arama motorunu kullanan bir searcher projesi yapıyoruz.
Googler, aramak istediğimiz d0rkları Google üzerinden arayarak çıkan sonuçları bize veren bir programdır.

### **Saldırı Senaryosu:**
Örneğin Joomla’nın X bir eklentisinde SQL Injection zafiyeti tespit edilmiş ve biz de bu zafiyeti exploit edebilmek için X eklentisini kullanan Joomla siteleri Google arama motorunu kullanarak tespit edeceğiz.

### **Algoritma:**
-   Başla
   -   Eğer argümanlarda “-d,-s,-f” varsa 3. adıma git, yoksa programdan çık
   -   Argümanları -d,-s,-f al
   -   Argümanları arama() fonksiyonuna gönder
   -   -f argüman değeriyle dosyayı oluştur ve aç
   -   i = 0
   -   ss = i+1 ve -d değeri için Google’a Get isteği gönder
   -   Sayfanın kaynak kodunu al
   -   Kaynak kodu parçala ve çıkan linkleri al
   -   Çıkan linkleri dosyaya kaydet
   -   i++
   -   Eğer i < -s ise 7. adıma git
   -   Dosyayı kapat
   -   print ("\n[-] İşlem bitmiştir.. ")
   -   Bitti

### **Kod Paylaşımı:**
İlk olarak genel ayarları yaptık, kullanacağımız modülleri (mechanize, sys, re, HTMLParser, urllib, BeautifulSoup) projemize import ettik ve değişken atamalarımızı yaptık:

	import mechanize,sys,re,html.parser,urllib.request,urllib.parse,urllib.error # kullanacağımız modüller(kütüphaneler)
	from bs4 import BeautifulSoup # kullanacağımız modüller(kütüphaneler)

	h = html.parser.HTMLParser() # HtmlParser metodu için referans gösterdik
	br = mechanize.Browser() # mechanize Browser metodu için referans gösterdik
	br.set_handle_robots(False) # robots.txt engellerine yakalanmamak için false dedik
	br.addheaders = [('User-agent', 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)')] # tarayıcımıza header bilgisi ekledik.

**giris** fonksiyonumuzu oluşturduk. **try** ve **except** metodu ile olası hatalar kullanıcının gözünden gizlenmek istenmiştir. Her seferinde kullanıcının programı nasıl kullanacağını göstermek için de uyarı mesajlarımızı eksik etmedik:

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

Aşağıdaki kodlarımız **arama fonksiyonu**muza aittir. Burada kaynak kodları parçalarken merdiven gibi taglar arasında iniş yaptım fakat sizler istediğiniz değerleri almak için harika bir **regex** kuralı yazarak tek seferde alabilirsiniz. Her sayfada işimiz bittikten sonra sıradaki sayfalar içinde aynı şeyi yaparak değerlerimizi çektik arkadaşlar.

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

[Kodların Tamamına Burdan Ulaşabilirsiniz!](https://github.com/KekikAkademi/KekikPython/blob/master/5-Py4H-Googler/Py4H-Googler.py)

### **Notlar:**
   -   Projede kullandığımız mechanize, BeautifulSoup, HtmlParser modülleri Python’ın sabit modülleri olmayıp sizin haricen yüklemeniz gerekmektedir.

> Bir sonraki yazımızda görüşmek üzere.

[Kaynak](http://python4hackers.com/python-search-engine-tools/py4h-googler.html "Saygı ve Özlemle...")
________________________________

📃 **Yandex.Disk Bünyemizde 900GB veri olmuştur.**

_Paylaşılan Kursların Tümünü_ [**@KekikKahve**](https://t.me/KekikKahve) _Grubu notlarından Çağırabilirsiniz.._

🕊️ Bize **oy verip** _paylaşarak_ destek olmaya ne dersin? ✌🏼
#
> Bu readme sayfası oluşturulurken [prose.io](http://prose.io/ "prose.io") ve [stackedit.io](https://stackedit.io/app "stackedit.io") araçlarından yardım alınmıştır..
> Emojiler için [webfx](https://www.webfx.com/tools/emoji-cheat-sheet/ "Emoji Cheat Sheet") sayfası kullanılmıştır.
