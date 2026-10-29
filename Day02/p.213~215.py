# 1
list_a = [0,1,2,3,4,5,6,7]

list_a.extend(list_a)
print("extend:", list_a)

list_a.append(10)
print("append:", list_a)

list_a.insert(3,0)
print("insert:", list_a)

list_a.remove(3)
print("remove:", list_a)

list_a.pop(3)
print("pop:", list_a)

list_a.clear()
print("clear:", list_a)

# 2
numbers = [273 ,103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number >= 100:
        print("-100이상의 수" , number)

# 3-1
numbers = [273 ,103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number %2 == 1:
        print(number,"는 짝수입니다")
    else:
        print(number,"는 홀수입니다")

# 3-2
numbers = [273 ,103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    print(number, len(str(number)), "자릿수입니다")

# 4
numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]
for number in numbers:
    output[(number-1)%3].append(number)
    print(output)

# 5
numbers = [1,2,3,4,5,6,7,8,9]
for i in range(0, len(numbers)//2):
    j = (i*2)+1
    print(f"i={i} , j={j}")
    numbers[j] = numbers[j] **2
print(numbers)