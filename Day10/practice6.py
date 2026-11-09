# 문제1 [ 타이타닉 생존 데이터 분석]
# 출처: Kaggle - Titanic: Machine Learning from Disaster

# [2. 가설]
# 가설 1: 여성과 아동의 생존율이 남성보다 월등히 높을 것이다. (사회적 보호 )
# 가설 2: 높은 객실 등급(1등석)을 이용한 승객일수록 생존율이 높을 것이다. (경제적 지위와 안전의 상관관계)
# 가설 3: 특정 항구(사우샘프턴 등)에서 탑승한 승객은 객실 등급 분포에 따라 생존율 차이가 발생할 것이다.

# [3. 자료수집 ]
# 3-1 : https://www.kaggle.com/competitions/titanic/overview
# 3-2 : train.csv 파일 판다스로 불러오기 

# [4. 데이터 전처리]
# 수치형 결측치 보정: '나이(Age)' 컬럼의 결측치는 이상치에 강건한(Robust) 분석을 위해 중앙값(Median)으로 대체해야 한다.
# 범주형 결측치 보정: '승선 항구(Embarked)' 컬럼의 결측치는 가장 빈번하게 등장하는 최빈값(Mode)으로 대체해야 한다.

# [5. 데이터 시각화 및 분석]
# 5-1 : (sns.countplot) 생존 분포 분석: 전체 생존자와 사망자의 비중을 파악할 수 있는 막대그래프 를 생성한다.
# 5-2 : (sns.hisplot( kde=True) )연령대별 상세 분석:나이에 따른 생존/사망 분포를 히스토그램으로 시각화한다.데이터의 흐름을 파악할 수 있도록 커널 밀도 추정 곡선(KDE)을 포함한다.
# 5-4 (성별): sns.countplot을 사용하여 성별(Sex)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
# 5-5 (객실 등급): sns.countplot을 사용하여 객실 등급(Pclass)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
# 5-6 (승선 항구): sns.countplot을 사용하여 승선 항구(Embarked)에 따른 생존 여부(Survived)별 인원수를 시각화한다.

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
data_dir = Path(__file__).resolve().parent
df = pd.read_csv(data_dir / 'train.csv')

# [4] 결측치 보정
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode().iloc[0])

# [5-1] 0: 사망, 1: 생존
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='Survived', order=[0, 1])
plt.xticks([0, 1], ['사망', '생존'])
plt.ylabel('인원수')
plt.title('전체 승객의 생존 분포')
plt.tight_layout()
plt.show()

# [5-2] histplot으로 연령별 생존/사망 분포와 KDE 표시
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Age', hue='Survived', bins=20, kde=True,
             multiple='layer', alpha=0.5)
plt.xlabel('나이(세)')
plt.ylabel('인원수')
plt.title('연령별 생존 분포 (0: 사망, 1: 생존)')
plt.tight_layout()
plt.show()

# [5-4 ~ 5-6] 성별, 객실 등급, 승선 항구별 생존 인원 비교
for column, label in [('Sex', '성별'), ('Pclass', '객실 등급'),
                      ('Embarked', '승선 항구')]:
    plt.figure(figsize=(7, 5))
    sns.countplot(data=df, x=column, hue='Survived', hue_order=[0, 1])
    plt.xlabel(label)
    plt.ylabel('인원수')
    plt.title(f'{label}에 따른 생존 분포')
    plt.legend(title='생존 여부', labels=['사망', '생존'])
    plt.tight_layout()
    plt.show()

# 인원수가 다른 그룹의 가설 비교에는 생존율도 함께 확인
# 아동은 이 실습에서 18세 미만으로 정의하며, 결측 나이는 중앙값 보정값 사용
df['연령구분'] = df['Age'].map(lambda age: '아동' if age < 18 else '성인')
for column in ['Sex', '연령구분', 'Pclass', 'Embarked']:
    print(f'\n--- {column}별 생존율(%) ---')
    print(df.groupby(column)['Survived'].mean().mul(100).round(2))
print('\n--- 항구별 객실 등급 비율 ---')
print(pd.crosstab(df['Embarked'], df['Pclass'], normalize='index').round(3))


# # 문제2[ 서울시 공공자전거 대여이력 분석]
# 출처: 서울 열린데이터 광장

# [2. 가설]
# 가설 1: 출퇴근 시간대(08시, 18시 전후)의 자전거 대여량이 다른 시간대에 비해 압도적으로 높을 것이다.
# 가설 2: 특정 지하철역 인근이나 유동인구가 많은 지역의 대여소가 대여량 상위권을 차지할 것이다.
# 가설 3: 이용시간과 이용거리 사이에는 강한 양의 상관관계가 존재할 것이다.

# [3. 자료수집]
# 3-1 : https://data.seoul.go.kr/dataList/OA-15182/F/1/datasetView.do
# https://drive.google.com/file/d/1tXfjwXu5HQUyKupqWeEiNk7ZlN0Xf7xw/view
# 3-2 : 2025년 1월, 2월 대여이력 CSV 파일 로드 (encoding='cp949')

# [4. 데이터 전처리 및 병합]
# 4-1 (병합): pd.concat을 사용하여 분리된 월별 데이터를 하나로 통합하고 인덱스를 재부여한다.
# 4-2 (정제): 결측치의 문자열 표현('\N')을 None으로 치환하고, 성별 데이터를 대문자로 통일 및 결측치를 'U'로 보정한다.
# 4-3 (형변환): 이용시간, 거리 등 주요 수치형 변수는 pd.to_numeric으로 변환하고, 날짜 데이터는 pd.to_datetime으로 객체화한다.
# 4-4 (파생변수): 대여일시에서 시간(Hour) 정보를 추출하여 '대여 시간대' 열을 새롭게 생성한다.

# [5. 데이터 시각화 및 분석]
# 5-1 (성별 분포): sns.countplot을 사용하여 성별에 따른 따릉이 이용 비중을 시각화한다.
# 5-2 (시간대 분석): sns.barplot을 사용하여 24시간 중 어느 시간대에 대여가 집중되는지 분석한다.
# 5-3 (인기 대여소): value_counts().head(10)를 활용하여 가장 활발한 상위 10개 대여소를 가로 막대 그래프로 시각화한다.
# 5-4 (상관관계): sns.heatmap을 통해 이용시간, 이용거리, 시간대 등 수치 데이터 간의 밀접도를 분석한다.

def analyze_bikes(data1, data2):
    # [4-1] 월별 데이터 병합 및 인덱스 재부여
    bike_df = pd.concat([data1, data2], ignore_index=True)
    bike_df.columns = bike_df.columns.str.strip()

    # [4-2] 결측 문자열 및 성별 정제
    bike_df = bike_df.replace('\\N', None)
    bike_df['성별'] = (bike_df['성별'].astype('string').str.strip()
                       .str.upper().replace('', None).fillna('U'))

    # [4-3 ~ 4-4] 숫자/날짜 변환 및 대여 시간대 생성
    for column in ['이용시간(분)', '이용거리(M)']:
        bike_df[column] = pd.to_numeric(bike_df[column], errors='coerce')
    for column in ['대여일시', '반납일시']:
        bike_df[column] = pd.to_datetime(bike_df[column], errors='coerce')
    bike_df['대여 시간대'] = bike_df['대여일시'].dt.hour

    plt.figure(figsize=(7, 5))
    sns.countplot(data=bike_df, x='성별')
    plt.xlabel('성별 (U: 미상)')
    plt.ylabel('대여 건수')
    plt.title('성별 공공자전거 이용 분포')
    plt.tight_layout()
    plt.show()

    # 시간대별 대여 건수를 먼저 집계하여 barplot에 전달
    hourly_counts = (bike_df['대여 시간대'].value_counts()
                     .reindex(range(24), fill_value=0).sort_index())
    plt.figure(figsize=(10, 5))
    sns.barplot(x=hourly_counts.index, y=hourly_counts.values, color='steelblue')
    plt.xlabel('대여 시간대(시)')
    plt.ylabel('대여 건수')
    plt.title('시간대별 공공자전거 대여량')
    plt.tight_layout()
    plt.show()

    top_stations = bike_df['대여 대여소명'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_stations.values, y=top_stations.index, color='steelblue')
    plt.xlabel('대여 건수')
    plt.ylabel('대여소')
    plt.title('대여량 상위 10개 대여소')
    plt.tight_layout()
    plt.show()

    correlation = bike_df[['이용시간(분)', '이용거리(M)', '대여 시간대']].corr()
    plt.figure(figsize=(7, 6))
    sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm',
                vmin=-1, vmax=1, center=0, square=True)
    plt.title('공공자전거 이용 지표 간 상관계수')
    plt.tight_layout()
    plt.show()
    return bike_df


bike_paths = [data_dir / f'서울특별시 공공자전거 대여이력 정보_{month}.csv'
              for month in ['2501', '2502']]
missing_paths = [path for path in bike_paths if not path.is_file()]
if missing_paths:
    print('\n문제 2 실행에 필요한 CSV를 Day10 폴더에 넣어 주세요:')
    for path in missing_paths:
        print(f'- {path.name}')
else:
    data1 = pd.read_csv(bike_paths[0], encoding='cp949')
    data2 = pd.read_csv(bike_paths[1], encoding='cp949')
    bike_df = analyze_bikes(data1, data2)
