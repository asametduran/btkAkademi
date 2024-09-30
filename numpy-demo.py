# 1-) (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
 
import numpy as np

a = np.array([10,15,30,45,60])


# 2-) (5,15) arasındaki sayılarla numpy dizisi oluşturunuz.

a = np.arange(5,15)

# 3-) (50-100) arasında beşer beşer artarak numpy dizisi oluşturunuz.

a = np.arange(50,100,5)

# 4-) 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.

a = np.zeros(10)

# 5-) 10 elemanlı birlerden oluşan bir dizi oluşturunuz.

a = np.ones(10)

# 6-) (0-100) arasında eşit aralıklı 5 sayı üretin.

a = np.linspace(0,100,5)

# 7-) (10-30) arasında rastgele 5 tane tamsayı üretin.

a = np.random.randint(10,30,5)

# 8-) [-1 ile 1] arasında 10 adet sayı üretin.

a = np.random.uniform(-1,1,10)

# 9-) (3x5) boyutlarında (10-50) arasında rastgele bir matris üretiniz.

a = np.random.randint(10,50,(3,5))

# 10-) Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız.

toplam = np.sum(a)
print(toplam)

# 11-) Üretilen matrisin en büyük, en küçük ve ortalaması nedir?

theBiggest = a.max()
theSmallest = a.min()
theAverage = a.mean()

print(theBiggest)
print(theSmallest)
print(theAverage)

# 12-) Üretilen matrisin en büyük değerinin indeksi kaçtır?

maxIndex = a.max()

print (a.argmax())
print(a)

# 13-) (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

b= np.arange(10,20)

print(b[0:3])

# 14-) Üretilen dizinin elemanlarını tersten yazdırın.

print (a[::-1])

# 15-) Üretilen matrisin ilk satırını seçiniz.

print(a[0])

# 16-) Üretilen matrisin 2.satır 3.sütunundaki elemanı hangisidir?

print(a[1,2])

# 17-) Üretilen matrisin tüm satırlardaki ilk elemanını seçiniz.

print(a[:,0])

# 18-) Üretilen matrisin her bir elemanının karesini alınız.

print(a**2)

# 19-) Üretilen matris elemanların hangisi pozitif çift sayıdır?

print(a% 2 == 0) 

# (-50,+50) arasında yapınız.
