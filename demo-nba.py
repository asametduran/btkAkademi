import pandas as pd
import numpy as np

data = pd.read_csv("nba.csv")
dataFrame = pd.DataFrame(data)
# print(dataFrame)


# 1- İlk 10 kaydı getiriniz.

# print(dataFrame.head(10))

# # 2- Toplam kaç kayıt vardır ?

# print(len(dataFrame))

# # 3- Tüm oyuncuların toplam maaş ortalaması nedir ?

# print(dataFrame["Salary"].mean())

# # 4- En yüksek maaşı ne kadardır ?

# print(dataFrame["Salary"].max())

# 5- En yüksek maaşı alan oyuncu kimdir ?

# highestSalaryPlayer = dataFrame["Salary"].idxmax()

# print(dataFrame["Name"][highestSalaryPlayer])

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.

# df = dataFrame[(dataFrame["Age"] >= 20) & (dataFrame["Age"] <= 25)].sort_values("Age", ascending=False)
# df = dataFrame.drop("Height",axis=1,inplace=True)
# df = dataFrame.drop("Weight",axis=1,inplace=True)
# df = dataFrame.drop("College",axis=1,inplace=True)
# df = dataFrame.drop("Salary",axis=1,inplace=True)
# df = dataFrame.drop("Number",axis=1,inplace=True)
# df = dataFrame.drop("Position",axis=1,inplace=True)
# print(dataFrame)


# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?

# johnHolland = dataFrame["Name"] == "John Holland"
# print(dataFrame[johnHolland]["Team"])

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?

result = dataFrame.groupby("Team").mean()["Salary"]


# 9- Kaç farklı takım mevcut ?

result = len(dataFrame.groupby("Team"))
result = dataFrame["Team"].nunique()

# 10- Her takımda kaç oyuncu oynamaktadır ?

result = dataFrame["Team"].value_counts()

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
dataFrame = dataFrame.dropna(inplace=True)
result = dataFrame[dataFrame["Name"].str.contains("and")]

def str_find(name):
    if "and" in name.lower():
        return True
    else:
        return False

result = dataFrame[dataFrame["Name"].apply(str_find)]

print(result)