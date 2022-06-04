
num_list = [1,2,3,4,5,6,7]
def triple(num_list):
     lst1 = []
     for i in num_list:
         i = i * 3
         lst1.append(i)
     return lst1

data = triple(num_list)
print(data)