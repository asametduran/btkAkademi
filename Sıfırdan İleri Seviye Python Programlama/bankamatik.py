#Bankamatik Uygulaması


SadikHesap = {
    'ad' : 'Sadık Turan',
    'hesapNo' : '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}
AliHesap = {
    'ad' : 'Ali Turan',
    'hesapNo' : '132456789',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap,miktar):
    print(f'Merhaba {hesap['ad']}')
    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print('paranizi alabilrsiniz.')
    else:
        toplam = hesap['bakiye']+hesap['ekHesap']
        if toplam >= miktar:
            ekHesapKullanimi = input('ek hesap kullanilsin mi ? (e/h)')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranizi alabilirsiniz')
            else:
                print(f'{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir.')
        else:
            print('uzgunuz bakiyeniz yetersiz')

def bakiyeSorgula(hesap):
    print(f'{hesap['hesapNo']} nolu hesabınzda {hesap['bakiye']} TL Bulunmaktadir. Ek hesapta ise {hesap['ekHesap']} TL bulunmaktadir')
paraCek(SadikHesap,3000)
bakiyeSorgula(SadikHesap)
paraCek(SadikHesap,2000)
