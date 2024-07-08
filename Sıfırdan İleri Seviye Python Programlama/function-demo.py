#Gonderilen bir kelmiyeyi belirtilen kez ekranda gösteren fonksiyon
def display(n,message):
    i=0
    while i<n:
        print(message)
        i+=1

display(4,'Selam')

#Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye ceviren fonksiyon yaziniz

def function(*params):
    liste=[]
    for param in params:
        liste.append(param)

function(1,2,3,4,5,6,7,8,9)   

#Gonderilen 2 sayı arasındaki tüm asal sayıları bulun

sayi1 = int(input('sayi 1 : '))
sayi2 = int(input('sayi 2 : '))

def asalSayilarBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi >1:
            for i in range(2,sayi):
                if sayi%i==0:
                    break
            else:
                print(sayi)

asalSayilarBul(sayi1,sayi2)

#4 Kendisine göndeirlen sayılarin bir tam bolenin gosteren fonksiyon

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if(sayi%i==0):
            tamBolenler.append(i)

    return tamBolenler

tamBolenleriBul(20)