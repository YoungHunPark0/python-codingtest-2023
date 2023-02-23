# 백준 1197 - 최소 신장 트리
# 시간복잡도 0(e*log(e))  e=엣지
import sys
from queue import PriorityQueue

input = sys.stdin.readline
N, M = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (N + 1)

# 유니온파인드를 위한 대표노드 리스트 초기화
for i in range(N+1):
    parent[i] = i

for i in range(M): # 엣지 개수만큼 입력
    s, e, w = map(int, input().split())
    pq.put((w, s, e)) # 가중치를 기준으로 정렬하므로
    
def find(a): # 대표(부모)노드 찾기
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b): # 두 노드 연결
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0

while useEdge < N -1: # MST는 항상 N-1 에지까지 수행
    w, s, e = pq.get()
    if find(s) != find(e): # 같은 부모가 아닌 경우만 연결
        union(s, e)
        result += w
        useEdge += 1 # 중요!! 유니온 할때만 1 증가

print(result)