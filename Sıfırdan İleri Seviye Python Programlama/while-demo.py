sayilar = [1,3,5,7,9,12,19,21]

#1 sayilar listesini wgile ile ekrana yazdirin
i = 0
while (i<len(sayilar)):
    print(sayilar[i])
    i+=1

#baslangic ve bitis degerlerini kullanicidan alip aradaki tum tek sayilari ekrana yazdir

startNum = int(input('Baslangic: '))
endNum = int(input('Bitis: '))

while startNum<=endNum:
    if(startNum%2!=0):
        print (startNum)
    startNum+=1

# 1-100 arasındaki sayilari azalan sekilde yazdirin

num = 100

while num>=1:
    print(num)
    num-=1

#Kullanicidan alacaginiz 5 sayiyi ekranda sirali bir sekilde yazdirin

numbers = [0,0,0,0,0]
i=0
while i<5:
    numbers[i]= int(input('Sayi degerini giriniz'))
    i+=1
#numbers.append() ile de ekleyebilirdin
numbers.sort()
print(numbers)