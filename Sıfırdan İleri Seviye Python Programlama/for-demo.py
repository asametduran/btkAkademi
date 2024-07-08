sayilar = [1,3,5,7,9,12,21]

#1 Sayılar listesindeki hangi sayilar 3'un katidir?

for sayi in sayilar:
    if sayi%3==0:
        print(sayi)

#2 Sayilar listesinde sayilarin toplami kactir?
total = 0
for sayi in sayilar:
    total += sayi

print(total)

#3 Sayilar listesindeki tek sayıların karesini aliniz

for sayi in sayilar:
    if sayi%2!=0:
        print(sayi**2)

sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

#4 sehirlerden hangileri en fazla 5 karakterlidir?

for sehir in sehirler:
    if(len(sehir)<=5):
        print(sehir)

urunler= [{'name':'samsung S6','price':'3000'},
          {'name':'samsung S7','price':'4000'},
          {'name':'samsung S8','price':'5000'},
          {'name':'samsung S9','price':'6000'},
          {'name':'samsung S10','price':'7000'}]    
#urunlerin fiyatlari toplami nedir?
total =0
for urun in urunler:
    total+= int(urun['price'])

print(total)

#6 urunlerin fiyatı en fazla 5000 olan urunleri gosteriniz.
for urun in urunler:
    if int(urun['price'])<=5000:
        print(urun) 