website = "http://www.sadikturan.com"
course = "Python Kursu : Baştan Sona Python Programlama Rehberiniz (40 saat)"
#' Hello World 'karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
s = " Hello World "
sYeni = s.split()
print(sYeni[0]+ " " +sYeni[1])
# ' www.sadikturan.com ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin
link = ' www.sadikturan.com '
linkYeni = link.strip()
print(linkYeni) 
# course karakter dizisinin tüm karakterlerini küçük harf yapın.
print(course.lower())
# website içinde kaç tane a karakteri vardır ? (count('a'))
print(website.count('a'))
# website www” ile başlayıp com ile bitiyor mu?
print(website.startswith('www') + website.endswith('com'))
# 'website' içinde ' . com' ifadesi var mı?
print(website[website.find('.com')])
# course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
print(course.isalpha())
# 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
value = 'Contents'
print(value.center(50))
print(value.rjust(50,'*'))
print(value.ljust(50,'*'))
# course' karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin.
print(course.replace(' ','-'))
# 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
print('Hello World'.replace('World','There'))
# course' karakter dizisini boşluk karakterlerinden ayırın.
print(course.split())