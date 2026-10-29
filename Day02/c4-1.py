# p.192
# 리스트란? 대괄호[]에 자료를 쉼표로 구분하여 여러 자료들을 저장 
# [ 요소, 요소, 요소 ] , 요소=element
# 인덱스란? 리스트내 요소들이 저장된 순서번호, 0번시작~

# 리스트 
list_a = [ 273, 32, 103, "문자열", True , False ] # 리스트 선언
print( list_a[ 2 ] )    # 인덱싱 # 103
print( list_a[ 1:3 ] )  # 1~2 # [32,103] # 슬라이싱
list_a[2] = 7 # 요소 값 수정/변경
print( list_a[2] ) # 7
print( list_a[-2] ) # True # 파이썬에서는 인덱싱 음수로 가능 
print( list_a[3][1] ) # 자 # 문자열도 리스트/배열 # 문자=리터럴
# print( list_a[1][1] ) # 오류 # 리터럴/1차원값
list_1 = [ 1, 2, 3 ] # 1차원
list_2 = [ [ 1, 2 ] , [ 3 , 4 ] , [ 5 , 6 ] ] # 2차원
print( list_2[1][0] ) # 3 , #[행][열] => 판다스/데이터

# p.196 , +연결 , *반복 , len( )길이
list_a = [ 1,2,3 ]
list_b = [ 4,5,6 ]
print( list_a + list_b ) # 리스트+리스트 => 연결 
print( list_a * 3 ) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print( len(list_a ) ) # 3
list_aa = [ [1], [2] , [3] ]
print( list_a + list_aa ) # [1, 2, 3, [1], [2], [3]]
list_a.append( 4 ) # 요소 추가 
print( list_a ) # [1, 2, 3, 4]
list_a.insert( 0 , 5 ) # 특정 인덱스 요소 삽입 # .insert( 위치 , 값 )
print( list_a ) # [5, 1, 2, 3, 4]
# 주의할점 : 
list_c = [ 1 , 2 ]
list_c + [3]        # 방법1] [ 1,2,3 ] 새로운리스트 생성 , list_c 변화 없다.
list_c.append(3)    # 방법2] [ 1,2,3 ] 기존 리스트 포함 , list_c 변화 있다.