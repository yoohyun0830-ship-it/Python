import numpy as np

data = np.genfromtxt(
    "./Day07/Activity/한국도로교통공단_가해운전자 차량용도별 시간대별 교통사고 통계_20251231.csv",
    delimiter=",",
    skip_header=1,
    dtype=str,
    encoding="cp949"
)

# 1. 필요한 데이터 추출
vehicles = data[:, 0]                  # 차량유형
times = data[:, 1]                     # 시간대
accidents = data[:, 2].astype(int)     # 사고건수

# 2. 분석할 차량유형 직접 지정
vehicle_types = [
    "승용차", "화물차", "이륜차", "렌터카",
    "법인택시", "개인택시", "시내버스", "자전거"
]

# 3. 시간대 직접 지정
time_types = [
    "00:00~02:00", "02:00~04:00",
    "04:00~06:00", "06:00~08:00",
    "08:00~10:00", "10:00~12:00",
    "12:00~14:00", "14:00~16:00",
    "16:00~18:00", "18:00~20:00",
    "20:00~22:00", "22:00~24:00"
]

# 4. 차량유형별 평균 사고건수
print("=== 차량유형별 평균 사고건수 ===")

for vehicle in vehicle_types:
    condition = vehicles == vehicle

    total = np.sum(accidents[condition])
    average = total / 12

    print(vehicle, ":", round(average, 2), "건")

# 5. 차량유형 + 시간대별 사고건수
print("\n=== 차량유형 + 시간대별 사고건수 ===")

for vehicle in vehicle_types:
    for time in time_types:
        condition = (vehicles == vehicle) & (times == time)
        count = np.sum(accidents[condition])
        print(vehicle, time, ":", count, "건")


# Step 1. 분석 결과
max_avg = 0
max_vehicle = ""

for vehicle in vehicle_types:
    avg = np.sum(accidents[vehicles == vehicle]) / 12

    if avg > max_avg:
        max_avg = avg
        max_vehicle = vehicle

max_count = 0
max_group = ""

for vehicle in vehicle_types:
    for time in time_types:
        count = np.sum(accidents[(vehicles == vehicle) & (times == time)])

        if count > max_count:
            max_count = count
            max_group = vehicle + " / " + time

print("평균 사고건수가 가장 높은 차량:", max_vehicle, round(max_avg, 2), "건")
print("차량유형+시간대별 최대 사고 그룹:", max_group, max_count, "건")

# Step 2. 특정 위험 그룹 필터링 (Boolean Indexing)

deaths = data[:, 3].astype(int)
serious = data[:, 4].astype(int)

results = []

for vehicle in vehicle_types:
    for time in time_types:
        condition = (vehicles == vehicle) & (times == time)

        total_deaths = np.sum(deaths[condition])
        total_serious = np.sum(serious[condition])

        results.append([vehicle, time, total_deaths, total_serious])

results = np.array(results, dtype=object)

# 사망자 50명 이상 또는 중상자 1,000명 이상
risk = (results[:, 2].astype(int) >= 50) | (results[:, 3].astype(int) >= 1000)
risk_groups = results[risk]

print("위험 그룹 수:", len(risk_groups), "개")
print("위험 그룹:", risk_groups)

# Step 4. 복합 위험군 분석

# 사망자 50명 이상 AND 중상자 1,000명 이상
complex_risk = (results[:, 2].astype(int) >= 50) & (results[:, 3].astype(int) >= 1000)

# Boolean Indexing
complex_groups = results[complex_risk]

# 전체 그룹 대비 비율
ratio = len(complex_groups) / len(results) * 100

print("복합 위험군 수:", len(complex_groups), "개")
print("복합 위험군 비율:", round(ratio, 2), "%")
print("복합 위험군:", complex_groups)