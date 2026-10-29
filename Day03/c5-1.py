# 함수 : 코드의 집합
    # 값저장 = 변수 , 실행코드 저장 = 함수
    # 값 여러개 저장 = 리스트/딕셔너리/튜플
# 매개변수 : 함수를 호출할 때는 괄호 내부에 여러가지를 넣는 변수
# 리턴값 : 함수를 호출해서 최종적으로 나오는 결과

# def 함수명 ( 매개변수명 ) :
#   실행문

# 값 재사용 = 변수 , 코드 재사용 = 반복문(반복패턴 식 존재) / 함수( 입력/출력 )
# 1. 기본적인 함수 
def print_3_time() :        # 함수 정의/만들기
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
print_3_time()   # 함수 사용/호출

# vs
for i in range( 0 , 3 , 1 ):
    print("안녕하세요")

# 매개변수 : 매개(중매-서로 다른 곳에서 연결) , 인수/인자값 -> 매개변수
# 파이썬은 { }가 아닌 탭(들여쓰기) 이용하여 구역 구분
def print_n_times(value, n):
    for i in range(n):
        print(value)
print_n_times( "안녕하세요" , 5 )   # 인수/인자값 : 함수 호출시 매개변수에 전달하는 값
print_n_times( "안녕하세요" , 3 )
# print_n_times( "안녕하세요" )     # 매개변수는 약속 -> 어길시 실행 X

# p.278 가변 매개변수
# 조건1 : 가변매개변수가 가장 뒤로 정의한다.
# 조건2 : 1번만 사용
# def 함수명( 매개변수 , 매개변수 , *가변매개변수 ) :
def print_n_times2( n , *values ) :
    for i in range(n) :       # 3번반복                      # 2번반복
        for value in values : # [안녕하세요,즐거운,파이썬]  #[안녕하세요,즐거운]
            print( value )
        print()
print_n_times2( 3 , "안녕하세요" , "즐거운" , "파이썬" ) # 인수4개 , 안녕하세요/즐거운/파이썬 * 3
print_n_times2( 2 , "안녕하세요" , "즐거운" )           # 인수3개 , 안녕하세요/즐거운 * 2

# p.279 기본 매개변수 , 매개변수에 기본값 대입 형태 , 인수/인자 값 생략시 적용
def print_n_times3(value , n =2 ):
    for i in range(n) :
        print(value)
print_n_times3( "안녕하세요" )          # "안녕하세요""안녕하세요"
print_n_times3( "안녕하세요" , 3 )      # "안녕하세요""안녕하세요""안녕하세요"

# P.280
# 기본 매개변수가 가변 매개변수보다 앞에 올때 , 오류
# 가변 매개변수가 기본 매개변수보다 앞에 올때 , 기본 매개변수 인자값 없다.
# 해결방안 : 키원드 매개변수
print("안녕하세요") # 안녕하세요 출력 코드
print("안녕하세요" , end="\n") # end 매개변수 : 출력 후 무엇을 할지 # \n 기본값 = 기본매개변수
print("안녕하세요" , end="")   # 키워드 매개변수 : 인수 대입시 매개변수명 지정

def print_n_times4(*values , n=2):
    # *매개변수 --> 가변매개변수  # 매개변수명=기본값 --> 기본매개변수 
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times4("안녕하세요","즐거운","파이썬" , n=3) # 키워드 매개변수  # 인수 전달시 매개변수명 지정 *3반복
print_n_times4("안녕하세요","즐거운","파이썬" , 3)  # *2반복

# p.285 , 리턴 : 함수가 종료되면서 반환 되는값
x = 3
y = 2
z = x + y # x + y --> def 내가만든공식() : x + y
# vs
def myFunc( x, y ):
    return x + y
z = myFunc( x, y )

# p.285 자료 없는 리턴하기 , java void
def return_test() :
    print("A 위치입니다")
    return # 리턴/함수종료/함수 끝
    print("B 위치입니다")
return_test() # B위치는 출력 x

# 자료와 함께 리턴하기
def return_test2() :
    return 100
value = return_test2()
print(value)

# 예제 1)
def sum_all(start, end):
    output = 0
    for i in range(start, end+1):
        output += i
    return output
print("0 to 100:", sum_all(0,100))
print("0 to 1000:", sum_all(0,1000))
print("50 to 100:", sum_all(50,100))
print("500 to 1000:", sum_all(500,1000))

# 예제 2)
def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end+1, step):
        output += i
    return output
print("A" , sum_all(0, 100, 10))
print("B" , sum_all(end=100))
print("C" , sum_all(end=100, step=2))


