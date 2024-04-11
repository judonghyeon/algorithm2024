# 1. 문제 정의
# 키를 받아 리스트 안의 내용을 순차 탐색하여 어느 인덱스에 키와 같은 값이 존재하는지 판별하는 문제
# 2. 알고리즘 설명
# 키와 리스트를 입력받아 리스트를 길이까지 키와 같은지 판별하고 리스트 내에 있다면 그 인덱스를 반환, 아니면 -1을 반환
# 3 손으로 푼 예제
# ![image](https://github.com/judonghyeon/algorithm2024/assets/94613341/e49b3720-9b55-4667-9ea0-694fc25b3cd2)
# 4. 알고리즘 개요
# A = 정렬되지 않은 리스트이다, Key = 리스트 안에 있는 숫자와 비교하는 키, i = 키와 같은 값의 리스트 인덱스 값, -1 = 리스트에 없는 경우의 반환 값
# 5. 알고리즘 코드 
# ![image](https://github.com/judonghyeon/algorithm2024/assets/94613341/1af6e56d-74c0-40ee-9d26-41b1d3d3ff3f)
# 6. 테스트 코드
# ![image](https://github.com/judonghyeon/algorithm2024/assets/94613341/3849d17e-a6b8-4c33-8cdb-b2136c0df0f7)
# 7. 수행 결과
# ![image](https://github.com/judonghyeon/algorithm2024/assets/94613341/b2392667-d7a7-4698-9557-cdb2f67e1060)
# 8. 복잡도 분석
# 리스트의 길이 n만큼 시행하는 함수 이기 때문에 복잡도는 O(n) 이다. 
# 9. 조별 협력 내용
# (주동현) 문제 3.2 해결, (김민상) 문제 3.4 해결, (홍민기) 문제 3.1 해결, (서강찬) 문제 3.3 해결 (주동현, 김민상) 문제 3.6 해결