# p.293 재귀함수 , 재귀 : 자기 자신을 호출하는 것
# 1] 팩토리얼 반복문
def factorial1(n) :
    output = 1
    for i in range( 1, n+1 ):
        output *= i
    return output
factorial1(2)   # 2! -> 1~2 -> 1*2
factorial1(3)   # 3! -> 1~3 -> 1*2*3

# 2] 팩토리얼 재귀
def factorial2(n):
    # 무한 재귀 방지
    if n == 0:
        return 1
    else: # 재귀함수
        return n * factorial2(n-1)
factorial1(2)   
factorial1(3)

# 구구단 반복문
for 단 in range( 2, 10, 1 ): # 단
    for 곱 in range(1, 10, 1): # 곱
        print(단*곱)
# 2단~3단 까지 / 1~4 곱까지 의 반복문 순서도 작성

# 구구단 재귀
def 구구단( 단=2, 곱=1 ):
    if 단 > 9 : # 재귀 끝
        return
    if 곱 > 9 : # 단마다 곱하기 9까지 했으면 단 올리기
        구구단(단+1, 1)
        return
    print(단*곱)
    구구단(단, 곱+1) # 곱 올리기
# 2단~3단 까지 / 1~4 곱까지 의 반복문 순서도 작성

# 297p. 피보나치수열1  -------------------
counter = 0 
def fibonacci( n ) : 
    print( "fibonacci({})를 구합니다".format(n) )
    global counter
    counter += 1 
    if n == 1 :
        return 1 
    if n == 2 : 
        return 1 
    else : 
        return fibonacci( n-1 ) + fibonacci( n - 2 )
print( fibonacci( 5 ) ) 

# 301p. 피보나치수열2 메모화 -------------
dictionary = { 1 : 1 , 2 : 1 }
def fibonacci2( n ) : 
    if n in dictionary :
        return dictionary[n]
    else : 
        output = fibonacci2( n - 1 ) + fibonacci2( n - 2 )
        dictionary[n] = output
        return output
print( fibonacci2( 5 ) ) 
