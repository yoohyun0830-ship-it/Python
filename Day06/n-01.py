# 터미널 키고 pip install numpy 입력 후 설치 (12MB)

# 설치 후 day06 n-01.py 파일에
#  1. 넘파이 설치 , 터미널 : pip install numpy
#  2. 넘파이 불러오기
# import 라이브러리이름
# import 라이브러리이름 as 별칭
import numpy as np
print( np.__version__)
#  3. 넘파이 학습하는 이유 : 1) 데이터분석(수치계산) 2) ML/DL 라이브러리들이 사용

# 1] 배열 생성
x = np.array([1, 2, 3, 4, 5]) # 1차원 배열
print(x) # [1 2 3 4]
x = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
) # 2차원 배열
print(x)
# [[1, 2, 3],
# [4, 5, 6]]
# 동적(자동으로 타입 정해주는) 타입 느리다. 넘파이는 정적타입 빠름
# int a = 10 : 정적타입 , a = 10 동적타입
x = np.array([1, True, "안녕"])
print(x) # ['1' 'True' '안녕']

# 2] 0으로 채워진 배열로 초기화 , .zeros(( 행개수 , 열개수 ))
x = np.zeros((2,3)) #
print(x)
# [[0,0,0]
# [0,0,0]]

# 3] 1로 채워진 배열로 초기화
x = np.ones((2,3))
print(x)
# [[1,1,1]
# [1,1,1]]

# 4] range(시작인덱스, 끝인덱스, 단계)
x = np.arange(0, 10, 2)
print(x) # [0 2 4 6 8]

# 5] linespace( 시작값, 끝값, 사이범위 )
x = np.linspace(0, 1, 5)
print(x)

# * 넘파이는 리스트 또는 튜플 타입의 자료들을 넘파이 타입으롭 ㅕㄴ환
x = np.array((2,3))
print(x)

# 6] 배열 길이 확인
x = np.array([[1,2,3],[4,5,6]]) # 2차원
print(x.shape) # (2,3) 2행 3열

# 7] 배열 타입 확인
x = np.array([1.0, 2.0, 3.0])
print(x.dtype) # flpat64

# 8] 배열 차원 수 확인
x = np.array( [ [[1],[2]],[[3],[4]],[[5],[6]]] )
print(x.size) # 요소/자료 개수
print(x.ndim) # 차원 개수

# 9] 배열의 데이터 타입 , np.array(리스트/튜플 , dtype=np.타입명)
# np.타입명(비트수) , 32bit ---> 4byte
# np.bool_ : 언더바 주의( 파이썬 bool / 넘파일 bool_)
# np.bytes : 영문 또는 일부 특수문자(아스키코드) 1바이트, 한글(UTF-8) 3바이트
x = np.array([1,2,3] , dtype = np.int32)
print( x.dtype )
x = np.array([1.0, 2.0, 3.0] , dtype= np.float32)
print(x.dtype)
x = np.array([True, False, True] , dtype = np.bool_)
print(x.dtype)
x = np.array(['apple','banana','cherry'], dtype = np.bytes_)

# 10] 타입변환 , astype(np.새로운타입)
x=np.array([1.5, 2.5, 3.5] , dtype = np.float32)
y=x.astype(np.int32)
print(y)

# * 타입 지정한 이유 
# 1. 메모리의 효율성/속도/정밀연산
# 2. 텐서플로우/파이토치 라이브러리
