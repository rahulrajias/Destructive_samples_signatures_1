# %matplotlib notebook
import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.get_backend()
import matplotlib.pyplot as plt
import os
import re

folder_folders = os.walk("/home/alone/Documents/Destructive/data_19_22_feb_2018")
folder_list = []
folder_names = []
for root, dirs, files in os.walk("/home/alone/Documents/Destructive/data_19_22_feb_2018", topdown=False):
    for name in dirs:
        if not os.path.isfile(os.path.join(root, name)):
            folder_list.append(os.path.join(root, name))
            folder_names.append(name)
            print (os.path.join(root, name))
# print(folder_list)
print(folder_names)

all_data_dict = {}
for k in range(len(folder_list)):
    all_data = pd.DataFrame(columns=["Lambda"])
    file_list = os.listdir(folder_list[k])
    for j in range(len(file_list)):
        raw_data = open(os.path.join(folder_list[k],file_list[j]), "r")
        f = raw_data.readlines()
        usable_part = f[78:459]
        usable_part = [i.split("  ") for i in usable_part]
        data = pd.DataFrame(usable_part)
        for index,rows in data.iterrows():
            re_pattern = r"(.*)\n"
            data.set_value(index, 2, re.search(re_pattern, rows[2]).group(1))
        data.columns=["Lambda","target","ref"]
        data.ref=pd.to_numeric(data.ref)
        data.target=pd.to_numeric(data.target)
        Reflectance=(data.target)/(data.ref)
        data=data.drop("ref",1)
        data=data.drop("target",1)
        if all_data["Lambda"].empty:
            all_data["Lambda"] = data["Lambda"]
        all_data["R"+str(j+1)]=Reflectance
    all_data_dict [folder_names[k]] = all_data

print("all_data_dict is a dictionary where key is folder name and stored values are dataFrame consists of reflectance values of that folder ")


plt.figure()
D1R1=all_data_dict['D1R1_destructive']
#In this folder R1 to R27 is from D1R1 all 9 subplots (3 reading from one leaf of each subplot. R28 to R36 is from
#very first plot of D1R1 i.e. D1R1I3N3 3 readings from top leaf then 3 from middle then 3 from bottom)
plt.plot(D1R1.Lambda,D1R1.R1, color='r')
plt.plot(D1R1.Lambda,D1R1.R2, color='r')
plt.plot(D1R1.Lambda,D1R1.R3, color='r')
plt.plot(D1R1.Lambda,D1R1.R4, color='r')
plt.plot(D1R1.Lambda,D1R1.R5, color='b')
plt.plot(D1R1.Lambda,D1R1.R6, color='g')
plt.plot(D1R1.Lambda,D1R1.R7, color='r')
ax=plt.gca()
ax.axis([400.35,998.65,0,1])
# plt.show()
a=ax.get_children()
print(a)
