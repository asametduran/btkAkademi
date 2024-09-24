import requests
import json

api_key = "093d6b6a16dacc0d8e6d0964"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan Döviz Türü: ") #USD veya TRY
alinan_doviz = input("Alınan Döviz Türü: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz? "))

sonuc = requests.get(api_url + bozulan_doviz)

# print(sonuc.text) #Burada bize bir <Responese [200]> geliyor. Bunu .json  formatına dönüştürmemiz gerekiyor.
sonuc_json = json.loads(sonuc.text)

#print(sonuc_json("conversion_rates")[alinan_doviz]) #

print("1 {0} = {1} {2}".format(bozulan_doviz, sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))
print("{0}{1}{2}{3}".format(miktar,bozulan_doviz,"=",miktar*sonuc_json["conversion_rates"][alinan_doviz]))