# Practice8: API 데이터 수집
# 1. 개요 및 대상 API 정보
# API 이름: 행정안전부_착한가격업소 현황
# API URL: https://www.data.go.kr/data/3045247/fileData.do 

# 목표: httpx를 통해 공공데이터 API를 호출하고, pandas를 활용해 업소명, 주소, 가격 데이터를 구조화한 뒤 통계 분석을 수행합니다.
# 2. 상세 요구사항
# 2-1 (API 호출 및 파라미터 설정):
# 지정된 API URL에 인증키(serviceKey)를 포함하여 요청합니다.
# 임의의 100건의 데이터를 수집

# 2-2 (데이터프레임 적재):
# 응답받은 JSON 데이터 중 실제 행 목록인 data 배열을 추출하여 pandas.DataFrame으로 변환합니다.

# 2-3 (데이터 전처리 및 분석):
# 가격1 컬럼의 데이터를 숫자형(pd.to_numeric)으로 변환합니다.
# 수집된 100건 데이터 기준 가격1의 평균값을 산출하여 출력합니다.

# 2-4 (업종별 평균 가격 집계 및 시각화):
# groupby('업종')을 사용하여 업종별 가격1의 평균 가격을 계산합니다.
# seaborn의 barplot 활용하여 업종별 평균 가격 비교 막대그래프를 시각화합니다.

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV를 읽고 첫 100건 선택
data_dir = Path(__file__).resolve().parent
csv_path = data_dir / '행정안전부_착한가격업소 현황_20260930.csv'
df = pd.read_csv(csv_path, encoding='utf-8-sig').head(100).copy()

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 가격1의 쉼표 제거 후 숫자로 변환
df['가격1'] = pd.to_numeric(
    df['가격1'].astype('string').str.replace(',', '', regex=False),
    errors='coerce'
)

# 선택한 100건의 평균 가격 출력
print(f"가격1 평균: {df['가격1'].mean():,.2f}원")

# 업종별 평균 가격 계산
industry_mean = df.groupby('업종', as_index=False)['가격1'].mean()
print(industry_mean)

# 업종별 평균 가격 막대그래프
plt.figure(figsize=(12, 6))
sns.barplot(data=industry_mean, x='업종', y='가격1')

plt.title('업종별 평균 가격')
plt.xlabel('업종')
plt.ylabel('평균 가격(원)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
