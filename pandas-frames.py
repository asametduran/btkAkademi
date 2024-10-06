import pandas as pd

list = [["Ahmet",50],["Ali",60],["Yağmur",70],["Cinar",80]]
dict = {"Name": ["Ahmet","Ali","Yağmur","Çınar"],"Grades": [50,60,70,80]}
dict_list = [{"Name": "Ahmet","Grades": 50},{"Name": "Ali","Grades": 60},{"Name": "Yağmur","Grades": 70},{"Name": "Çınar","Grades": 80}]
# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# df = pd.DataFrame(data, columns =['Name','Grades'],index=[1,2,3,4] )

df = pd.DataFrame(dict_list)

print(df)

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, oranges = s2)

# df = pd.DataFrame(data)

# # print(df)