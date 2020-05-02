#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
import sys,re,os,colorama # kullanacağımız modüller(kütüphaneler)

#Renk Kodları
bold = "\033[1m" #Koyulaştıran renk kodu 
underline = "\033[4m" # Kullanmadık ama yazının altını çizen renk kodu
green = "\033[92m" # Yeşil renk kodu
blue = "\033[94m" # Mavi renk kodu
yellow = "\033[93m" # Sarı renk kodu
red = "\033[91m" # Kırmızı renk kodu
endcolor = "\033[0m" # Kodların sonuna gelen renk kodu

taranan_dosyalar = [] # Taranan dosyalar için boş liste
girilen_dizinler = [] # girilen dizinler için boş liste
bulunan_dosyalar = [] # bulunan dosyalar için boş liste

#Scriptteki kodları renklendir
def oku(dosya_ismi): # oku metodumuz ve alınan dosya ismi
	dosya = open(dosya_ismi,"r") # dosyamızı okumak için açıyoruz
	icerik = dosya.readlines() # satır satır olmak üzere okuduk
	satir_sayisi = len(icerik) # kaç satır sayısı olduğunu bulduk
	for i in range(0,satir_sayisi): # for döngümüz satır sayısı kadar döncek
		if re.findall('.*_GET',icerik[i]): # _GET varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*_POST',icerik[i]): # _POST varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*include',icerik[i]): # include varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*require_once',icerik[i]): # require_once varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*readfile',icerik[i]): # readfile varsa 
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*mysql_query',icerik[i]): # mysql_query varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*setcookie',icerik[i]): # setcookie varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*system',icerik[i]): # system varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*fputs',icerik[i]): # fputs varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*eval',icerik[i]): # eval varsa 
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*_REQUEST',icerik[i]): # _REQUEST varsa 
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*shell_exec',icerik[i]): # shell_exec varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*system',icerik[i]): # system varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*exec',icerik[i]): # exec varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*passthru',icerik[i]): # passthru varsa 
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*proc_open',icerik[i]): # proc_open varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*pcntl_exec',icerik[i]): # pcntl_exec
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*assert',icerik[i]): # assert varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*preg_replace',icerik[i]): # preg_replace varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*create_function',icerik[i]): # create_function varsa 
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*phpinfo',icerik[i]): # phpinfo varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*file_include',icerik[i]): # file_include varsa
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		elif re.findall('.*require',icerik[i]): # require varsa 
			print("%s%s%s-)  %s %s" %(bold,green,(i+1),icerik[i],endcolor)) # renklendir(Koyu yeşil)
		else: # hiç biri yoksa
			print("%s%s-)  %s %s" %(blue,(i+1),icerik[i],endcolor)) # açık mavi ile renklendir


#Dizin gezme algoritması
def gezgin(gelen_dizin): # gezgin metodumuz gelen dizini alır
	os.chdir(gelen_dizin) # gelen dizine girilir
	girilen_dizinler.append(gelen_dizin) # girilen dizi girilen_dizinler adlı listeye eklenir
	Arastirmaci() # Arastirmaci metodu çağrılır
	os.chdir(os.pardir) # bir üst dizine çıkılır


def Arastirmaci(): # Arastirmaci metodumuz
	dosyalar =  os.listdir(os.getcwd()) # içinde bulunduğu dizindeki dosyaları kayıt eder
	for i in dosyalar: # kayıt edilen dosyalar for döngüsünde dökülür
		if os.path.isdir(i): # bu dosya bir dizin mi ?
			if girilen_dizinler.count(i) == 0: # peki daha önce bu dizine girdik mi
				gezgin(i) # girmediysek gezgin metodunu çağır
			else: # girilmişse 
				pass # pas geç girme bir daha 
		else: # bu bir dizin değilse
			if taranan_dosyalar.count(i) == 0: #dosyamızı daha önce taradık mı?
				if re.findall('.*php',i): # taramadıysak bu bir php dosyası mı ?
					dosya = open(i,"r") # öyleyse aç bu dosyayı okumak için
					icerik2 = dosya.read() # dosyanın kodlarını oku
					taranan_dosyalar.append(i) # ve taranan dosyalara kaydet 
					if re.findall('.*_GET',icerik2): # okunan kodlarda _GET var mı ?
						bulunan_dosya_ismi = os.getcwd()+"/"+i # varsa dizini ile beaber al
						bulunan_dosyalar.append(bulunan_dosya_ismi) # bulunan_dosyalar listesine ekle
					elif re.findall('.*_POST',icerik2): # okunan kodlarda _POST var mı ?
						bulunan_dosya_ismi = os.getcwd()+"/"+i # varsa dizini ile beraber al
						bulunan_dosyalar.append(bulunan_dosya_ismi) # bulunan_dosyalar listesine kaydet
					else: # okunan kodlarda _GET ve _POST yok mu ?
						pass # boşver
				else: # bu bir php dosyası değilmiş
					pass # boşver
			else: # bu dosyayı daha önce taramışız
				pass # o zaman boşver

def bitti(): # her şeyin bitip ekrana bulduğumuz dosyaları yazan metod
	for i in bulunan_dosyalar: # bulunan_dosyalar for döngüsünde dökülür
		print(bold+blue+i+endcolor) # koyu mavi olarak ekrana yazılır


#Olası hatalar için try-except
try: # try olası hatalar için
	if sys.argv[1] == "-f": # argv 1. eleman -f parametresi almış mı
		oku(sys.argv[2]) # aldıysa 2. elemanı oku
	elif sys.argv[1] == "-p": # eğer 1. eleman -p parametresi aldıysa
		gezgin(sys.argv[2]) # sen gene 2. elemanı oku ve gezgin metodunu çağır bu sefer
		bitti() # bitti metodunu çağır
except IOError: # verdiğin php dosyası yok
	print(bold+red+"Dosya Bulunamadı !"+endcolor) # Hata
except IndexError: # programı yanlış mu kullandın sen ?
	print("""
  ____          _        _   _             _            
 / ___|___   __| | ___  | | | |_   _ _ __ | |_ ___ _ __ 
| |   / _ \ / _` |/ _ \ | |_| | | | | '_ \| __/ _ \ '__|
| |__| (_) | (_| |  __/ |  _  | |_| | | | | ||  __/ |   
 \____\___/ \__,_|\___| |_| |_|\__,_|_| |_|\__\___|_|   V1.0
                                                    
""")
	print(bold+red+"\n Örnek kullanım:\n\n $ python tespit.py -f dosya_ismi >>> php dosyasını renklendirir !"+endcolor)
	print(bold+red+"\n $ python tespit.py -p taranacak_dizin >> Dizini tarar ve size işe yarar php dosyalarını bulur !"+endcolor)