🕊 Bu döküman [**@KekikAkademi**](https://t.me/KekikAkademi "Telegram: @KekikAkademi") için oluşturulmuştur. ✌🏼
________________________________
# Mechanize Modülü
![Mechanize Kurulum](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/2-Mechanize-Mod%C3%BCl%C3%BC/images/mechanize-kurulum.png)

### **Mechanize Modülü Nedir?**
John J. Lee tarafından geliştirilen, web siteleri üzerinde browser gibi davranarak işlemler yapmamızı sağlayan python modülüdür. Aynı zamanda perl ve ruby dilleri için de yazılmıştır. Python kurulumuyla beraber gelen urllib standart modülü ile de aynı işlemleri yapabilirsiniz fakat mechanize kadar pratik değildir. Mechanize sayesinde web siteleri üzerinde proxy, cookie, header, user-agent gibi bilgileri bir kaç satır kodla yazarak zamandan kazanabilirsiniz.

### **Neler Yapabilirim?**
	-   İstediğiniz bir web sitesi hakkında günün belli saatlerinde bilgi alabilir veya bilgi gönderebilirsiniz.
    -   Haftalık hava durumu takibi
    -   Yorum yazma
    -   Mesaj gönderme
    -   Bildirimleri okuma
    -   Makaleleri kaydetme vs.
	-   Brute force aracı yazabilirsiniz.(uzman kullanıcılar)
    -   Cookie engellerini aşma
    -   [robots.txt](https://web.archive.org/web/20190720033020/https://support.google.com/webmasters/answer/6062608?hl=tr)  dosya engelini atlatma
    -   Çok sayıda  [User-Agent](https://web.archive.org/web/20190720033020/https://wmaraci.com/nedir/user-agent)  tanımlayarak farklı tarayıcılar gibi davranma
    -   Wordlist yükleyerek olasılığı arttırma
    -   Proxy listesi ekleyerek anonimliği arttırma
    -   Yapacağınız işlemleri random modülü kullanarak ip engelinden korunma

### **Windows Kurulumu**
-   [https://pypi.python.org/pypi/mechanize/](https://web.archive.org/web/20190720033020/https://pypi.python.org/pypi/mechanize/)  adresinden zip uzantılı dosyayı indirip masaüstüne çıkartın.
-   Komut satırını yönetici olarak açarak masaüstü dizinine çıkarttığınız mechanize-0.2.5 dizinine cd komutunu kullanarak gelin.

		python setup.py install
        
-   Komutuyla yükleme işlemini başlatın. Python konsolda import mechanize ile yüklendiğini test edebilirsiniz.
-   Python path’e ekliyse windows cmd de, linux kurulumunda verdiğim pip ve easy_install paket yöneticileriyle yükleyebilirsiniz.

### **Linux Kurulumu**
Python paket yöneticilerini kullanarak:

   	pip install mechanize
    
veya

    easy_install mechanize

### **Mechanize Metodlarını Listeleyelim**
Aşağıdaki kodları py uzantısıyla kaydedip çalıştıralım ve kullanabileceğimiz metodları görelim.

    import mechanize
    for i in dir(mechanize):
        print i

### **Facebook Login Örneği**
    import mechanize
    br=mechanize.Browser()
    br.set_handle_robots(False)
    #br.set_cookie("cookie data")
    #br.addheaders = [("Referer", "http://website.com")]
    #br.set_proxy("ipadress:port","http")
    br.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
    op=br.open("https://facebook.com")
    dos=open("Facebook.txt","rb+")
    username=input("enter your facebook username: ")
    password=input("enter your facebook password: ")
    br.select_form(nr=0)
    br.form["email"]=username
    br.form["pass"]=password
    br.method="POST"
    br.submit()
    dos.write(br.open("https://facebook.com").read())
    dos.seek(0)
    text=dos.read().decode("UTF-8")
    if(text.find("home_icon",0,len(text))!=-1):
     print("success login.")
    else:
     print("error login.")
    dos.close()

**Satırları açıklayacak olursak:**
- **1-**  Mechanize modülünü dahil ediyoruz.
- **2-**  Browser nesnesi oluşturuyoruz.
- **3-**  Browser nesnesinin set_handle_robots metodunu kullanarak robots.txt engeli için False değerini veriyoruz.
- **4-** Cookie değeri ekleyebiliriz.
- **5-** Referer bilgisi ve daha bir çok header için gerekli olan tanımlamaları yapabiliriz.
- **6-** Proxy tanımlayabiliriz. Dosya işlemleriyle proxy list yükleyerek her üç login denemesinden sonra değişecek şekilde ayarlayabiliriz. set_proxy fonksiyonunun ilk parametresine dosyadan okuduğumuz tek satırlık string proxy değerini verebiliriz, yapacaklarınız hayal gücünüze bağlı.
- **7-**  Browser kimliğini (user-agent) tanımlıyoruz. Kendi tarayıcınızın user-agent bilgisini öğrenmek için live http header gibi eklentiler kullanabilirsiniz veya bu siteden user-agent listesine ulaşabilirsiniz > [useragentstring.com](https://web.archive.org/web/20190720033020/http://www.useragentstring.com/)
- **8-**  Browser nesnesinin open fonksiyonunu kullanarak sayfayı açıyoruz.
- **9-**  Masaüstünde html kodlarının kaydedileceği dosyayı oluşturuyoruz. [user değerini kendi kullanıcı adınızla değiştirmeyi unutmayın.](https://stackoverflow.com/a/23566951) Bu kod windows dizin değerine göre oluşturuldu. Linux için değerleri ayarlamalısınız.
- **10-**  Kullanıcıdan user pass alıyoruz.
- **12-**  Post yapacağımız form kısmının html kodunda kaçıncı sırada olduğunu belirtiyoruz. Sayfa içerisinde birden fazla form kısmı olabilir. Html kaynak kodunu inceleyerek öğreniyoruz. İlk sıradaysa sıfır yazıyoruz.
- **13-** Sayfada bulunan username ve password kısmının name değerlerine raw_inputla aldığımız değerleri atıyoruz.
- **15-**  Form verilerinin hangi metotla işleneceğini belirliyoruz.
- **16-**  Girilen verileri gönderiyoruz.
- **17-**  Login denemesinden sonra anasayfanın html kodunda işlem yapacağımız için browser nesnesinin read fonksiyonuyla masaüstü dizinine kaydediyoruz.
- **18-**  Dosya işaretçisini başa alıyoruz.
- **19-**  Açmış olduğumuz dosyayı text değişkeniyle işlem yapmak için eşitliyoruz.
- **20-**  Login olup olamadığımızı kontrol etmek için ana sayfadaki html kodundan login sayfasında bulunmayan bir kod seçiyoruz.Farklı bir değerde seçebilirdik. Facebook’ta güncellemeler yapıldığında kullandığım  bu html değeri değişebilir ve kod düzgün çalışmaz. Bu değeri siz güncelleyebilirsiniz.

### **Denemek isteyenler için programın derlenmiş hali:**
 -   Derlemek için pyInstaller kullanıldı.
 -   Diğer bilgisayarlarda çalışabilmesi için winpaths modülü kullanıldı.
 -   Komut satırının hemen kapanmaması için time kütüphanesiyle 3 saniye bekleme süresi konuldu.
     - **Kod:**  [Facebook.py](https://github.com/KekikAkademi/KekikPython/blob/master/2-Mechanize-Mod%C3%BCl%C3%BC/facebook.py "Python3 Facebook.py")
     - **exe:** [indir](https://github.com/KekikAkademi/KekikPython/blob/master/2-Mechanize-Mod%C3%BCl%C3%BC/facebook.exe?raw=true "Facebook.exe")

> Gördüğünüz gibi browser gibi davranan bu modülle çok güzel işler yapılabilir.
> 
> Fahri Güreşçi

[Kaynak](http://python4hackers.com/genel/python-mechanize-modulu.html "Saygı ve Özlemle...")
________________________________

📃 **Yandex.Disk Bünyemizde 900GB veri olmuştur.**

_Paylaşılan Kursların Tümünü_ [**@KekikKahve**](https://t.me/KekikKahve) _Grubu notlarından Çağırabilirsiniz.._

🕊️ Bize **oy verip** _paylaşarak_ destek olmaya ne dersin? ✌🏼
#
> Bu readme sayfası oluşturulurken [prose.io](http://prose.io/ "prose.io") ve [stackedit.io](https://stackedit.io/app "stackedit.io") araçlarından yardım alınmıştır..
> Emojiler için [webfx](https://www.webfx.com/tools/emoji-cheat-sheet/ "Emoji Cheat Sheet") sayfası kullanılmıştır.