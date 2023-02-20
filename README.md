# python-codingtest-2023
파이썬 코딩테스트 리포지토리

# 1일차
1. 코딩테스트 소개
2. 코딩테스트 학습
    - 자료구조 - 배열/리스트
    - 구간합

# 2일차
! 파이썬 파일명에는 _만 사용할 것!!

1. 코딩테스트 학습
    - 구간합 2
    - 자료구조 다시
        - 연결리스트
        - 스택
        - pythonds 스택 확인!

# 3일차
1. 코딩테스트 학습
    - 자료구조
        - 큐
        - pythonds 큐 확인
        - 이진 트리
            - 삭제는 연결리스트 삭제와 유사
        - 그래프

# 4일차
1. 코딩테스트 학습
    - 자료구조
        - 그래프 - DFS
        - 재귀호출
        - 정렬 소개 

# 5일차
1. 코딩테스트 학습
    - 자료구조 / 알고리즘 (정렬, 다이나믹프로그램 -> 알고리즘 (자료구조x)
        - 정렬
        - 검색
        - 다이나믹 프로그래밍 / 피보나치 실행시간 비교

# 6일차
1. 코딩테스트 학습
    - 자료구조
        - deque (덱)
    - 코딩테스트 알고리즘
        - 백준
        - 프로그래머스

```python
# 백준 11003 - 최솟값찾기 1
from collections import deque
# == from pythonds.basic.deque import Deque

mydeque = deque()
N, L = map(int, input().split()) # 12 3
now = list(map(int, input().split())) # 1 5 2 3 6 2 3 7 3 5 2 6

# 새값이 들어올때마다 정렬 대신 현재수보다 큰 값을 덱에서 제거
# 시간복잡도를 줄이는 것

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]: # 인덱스가 현재값보다 크면
        mydeque.pop() # 빼버린다
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L: # 범위를 벗어난 값도 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0], end=' ') # 이 값은 무조건 최소값(min() 과동일)
```