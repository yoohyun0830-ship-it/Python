# 1
dict_a = {}

array = dict_a

dict_a["name"] = "구름"
print(dict_a)

del dict_a["name"]
print(dict_a)

# 2
pets = [
    {"name":"구름" , "age":5},
    {"name":"초코" , "age":3},
    {"name":"아지" , "age":1},
    {"name":"호랑이" , "age":1},
]
print("#우리동네 반려동물")
for pet in pets:
    print(pet["name"],str(pet["age"])+"살")

# 3
numbers = [1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,1,2,3,4,5]
counter = {}
for number in numbers:
    if number in counter:
        counter[number] = counter[number]+1
    else:
        counter[number]=1
    print(counter)

