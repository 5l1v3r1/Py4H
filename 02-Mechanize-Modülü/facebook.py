import mechanize
from time import sleep

br=mechanize.Browser()
br.set_handle_robots(False)
br.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
op=br.open("https://facebook.com")
dos=open("facebook.txt","rb+")
print("python4hackers.com\n")
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
sleep(3)