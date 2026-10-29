import numpy as np # 넘파이 호출
# 1] 병합 : vstack ([배열1],[배열2]), hstack()
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
z = np.vstack([x,y])
print(z)
z = np.hstack([x,y])
print(z)

# 2] 병합2 , concatenate((배열1, 배열2), )
z= np.concatenate((x,y), axis=0) # axios =0 세로방향 =1 가로방향
print(z)
z = np.concatenate((x,y), axis=1)
print(z)

# 3] 정렬 , .sort(배열) : 오름차순 , [::-1] : 내림차순
x= np.array([3,1,4,2,5])
print(np.sort(x))
print(np.sort(x)[::-1])
print(x) # 원본변경안됨
x.sort() # 배열.sort()
print(x) # 원본 자체 변경됨
z= np.argsort(x)
print(z)

# 4] 값 자체를 정렬하지 않고 배열을 정렬 위치순번 반환
scores = np.array([75,95,60,88])
z= np.argsort(scores) #[2 0 3 1] 정렬했을때 위치순번 반환
print(z)

# 5] 필터링/조건식
x = np.array([10,20,30,40,50]) #[False False True True]
print(x>30) # 인덱싱 안에서 조건식 사용하면 True값 추출 [40,50]
y = np.array([[1,2,3],[4,5,6],[7,8,9]])
print( y % 2 == 0 )
# [[False True False][ True False True] [False True False]]
print( y[ y % 2 == 0 ]) # [2 4 6 8]

# 6] 삼항연산자 , np.where(조건,참,거짓)
print( np.where(x>30, 0, 0))
print( np.where(y%2==0, 0, 1))

# 7] 다수 조건, & | ~
# 조건 2개 이상이면 () 또는 변수
a= y%2==0
print(y[a & (y%4==0)]) # 짝수이면서 4배수
print(y[a | (y%4==0)]) # 짝수이거나 4배수
print(y[~a]) # 짝수가 아닌
# 주의할점 : C/JAVA에서 &비트(0/1) 연산자, numpy에서는 &논리연산자
# 넘파이는 파이썬에서 실행되는 구조(중복에 따른 오버라이딩 제한)

