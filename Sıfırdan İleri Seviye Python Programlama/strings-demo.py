website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result = len(course)
print(result)
# 'website' içinden www karakterlerini alın.
print(website[7:10])
# 'website' içinden com karakterlerini alın.
print(website[22:25])
# 'course' içinden ilk 15 ve son 15 karakterlerini alın.
print(course[:15])
print(course[-15:])
# 'course' ifadesindeki karakterleri tersten yazdırın.
print(course[::-1])

name,surname,age,job = 'Bora','Yılmaz',32,'mühendis'

# Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis. '
print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job} ")