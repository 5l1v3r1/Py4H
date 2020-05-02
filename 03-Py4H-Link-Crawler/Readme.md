🕊 Bu döküman [**@KekikAkademi**](https://t.me/KekikAkademi "Telegram: @KekikAkademi") için oluşturulmuştur. ✌🏼
________________________________
# Py4H Link Crawler
![Py4H Link Spider-Crawler](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/3-Py4H-Link-Crawler/images/py4h-link-spider-crawler.png)

Hedef web uygulamadaki/sitedeki bağlantı adreslerini (linklerini) toplayan bir araç kodlayacağız.

### **Saldırı Senaryosu:**
Hedef siteye ait kaynak koddaki tüm bağlantı adreslerini listeleyip o linklerde (inject points) Sql Injection, XSS gibi ataklar denenecektir.

### **Algoritma:**
-   Başla
   -   Hedef siteye git
   -   Kaynak koddaki bağlantıları topla
   -   Bağlantıları düzelt
   -   Ekrana yaz
   -   Bitti

### **Kod Paylaşımı:**
Aşağıdaki kodlarda bilgi fonksiyonu ile kullanıcının aracı nasıl kullanacağı hakkında bilgilendirdik. Gerekli kütüphaneleri aktardık ve tarayıcımızın ayarını yaptık.

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
Aşağıdaki kodlar asıl işi yapan kodlarımızdır. Argümanımızı alıp bağlantımızı açıp sitedeki tüm bağlantıları toplayıp ekrana yazabilirdik fakat bazen bağlantılar **/index.php** formatında olabiliyor. Bu yüzden bu formatta ise başına gittiğimiz adresi getir dedik.

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

[Kodların Tamamına Burdan Ulaşabilirsiniz!](https://github.com/KekikAkademi/KekikPython/blob/master/3-Py4H-Link-Crawler/Py4H_Link_Crawler.py)

### **Notlar:**
   -   Python 3x sürümü ile yazdığımız bu araçta third party modül olarak sadece mechanize kullanılmıştır. Eğer bu modül sisteminizde kurulu değilse kurmanız gerekmektedir. Diğer modüller standart modüller olup sizde kurulu gelmektedir.

   -   Yazdığımız aracın kullanımı python `crawler.py www.hedefsite.com` şeklindedir.

> Bir sonraki yazımızda görüşmek üzere.

[Kaynak](http://python4hackers.com/python-information-gathering-tools/py4h-link-crawler.html "Saygı ve Özlemle...")
________________________________

📃 **Yandex.Disk Bünyemizde 900GB veri olmuştur.**

_Paylaşılan Kursların Tümünü_ [**@KekikKahve**](https://t.me/KekikKahve) _Grubu notlarından Çağırabilirsiniz.._

🕊️ Bize **oy verip** _paylaşarak_ destek olmaya ne dersin? ✌🏼
#
> Bu readme sayfası oluşturulurken [prose.io](http://prose.io/ "prose.io") ve [stackedit.io](https://stackedit.io/app "stackedit.io") araçlarından yardım alınmıştır..
> Emojiler için [webfx](https://www.webfx.com/tools/emoji-cheat-sheet/ "Emoji Cheat Sheet") sayfası kullanılmıştır.