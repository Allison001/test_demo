# lista = [
#     [1,4,7],
#     [2,5,8],
#     [3,6,9]
# ]

# 第一步，将列表换成[1,2,3],[4,5,6],[7,8,9]
# list1 = []
# for i in lista:
#         list1.append(i[0])
# print(list1)


# list1_a = [i[0] for i in lista]
# print(list1_a)

# 第二步，循环打印出[1,2,3],[4,5,6],[7,8,9]
# list2 = []
# for z in range(3):
#     list2.append([i[z] for i in lista])
#
# print(list2)


# # 转换成列表推导式
# list3 = [[i[z] for i in lista] for z in range(3)]
# print(list3)




# list5 = list(zip(*lista))
# print(list5)

# lista = [-1,2,3,12,23,445,43]

# del lista[0]
# print(lista)
# del lista[2:4]
# print(lista)
# del lista[:]
# print(lista)

# print(lista)
# # del lista[0]
# del lista[:]
# print(lista)



# t = 12,34,"hello","2"
# print(t)
# print((t[0]))
#
# a = t,"231",(1,2,3,4)
# print(a)
#
# print(t[0] =3434)




# 集合
# jihe = {12,"da","dd","fe"}
# print(jihe)
# print(type(jihe))
#
# print(12 in jihe)
# print(13 in jihe)


# a = set("abcdefgh")
# b = set("cbd")
# print(a)
# print(b)
# print(a-b)


# 字典
# dic ={"a":12,"b":12,"c":"ab"}
# print(dic)
# print(dic.items())
# for x,y in dic.items():
#     print(x,y)


# for i,v in enumerate(["a","b","c"]):
#     print(i,v)


# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
#
# for i,z in zip(questions,answers):
#     print(f"what's your {i},my name is {z}")


# for i in reversed(range(1,10)):
#     print(i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(basket):
#     print(i)


# for i in sorted(set(basket)):
#     print(i)


# string1,string2,string3 = "","haha","enne"
# a = string1 or string2 or string3
# print(a)

a = (1,2,3) < (1,2,4)
print(a)