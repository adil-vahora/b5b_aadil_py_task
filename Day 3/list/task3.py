list_1=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50 ,15, 20, 25, 30, 35]
list_2=[]
for n in list_1:
    if n not in list_2:
        list_2.append(n)
print('new list:',list_2)