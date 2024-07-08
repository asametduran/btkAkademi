
#1 1-Girilen 2 sayıdan hangisi büyüktür ?
# number1 = int(input("Enter a number"))
# number2 = int(input("Enter a number"))
# if number1>number2:
#     input("number1 is bigger than the other one")
# else:
#     input("number2 is bigger than the other one")    

#2-Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#3-Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# midTerm = float(input("\nEnter your mid-term point: "))
# final = float(input("\nEnter your final point: "))

# result = midTerm*0.6 + final*0.4

# if result>= 50:
#     print(f"Succes! Your point: {result}")
# else:
#     print(f"Failure! Your point: {result}")

#4-Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# number = int(input("Enter a number: "))

# if(number%2==0):
#     print(f"{number} is even")
# else:
#    print(f"{number} is odd")
#5-Girilen bir sayının negatif pozitif durumunu yazdırın.
# number = int(input("Enter a number: "))

# if(number>0):
#     print(f"{number} is positive")
# else:
#    print(f"{number} is negative")
#6-Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#(email: email@sadikturan.com parola:abc1231)

email = str(input("Enter your e-mail:"))
password = str(input("Enter your password"))

if(email== "email@sadikturan.com" and password == "abc1231"):
    print("Succesful!")
else:
    print("Email or password is wrong")    