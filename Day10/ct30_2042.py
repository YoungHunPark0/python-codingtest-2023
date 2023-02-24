# 백준 2042 - 구간합 구하기3
# 세그먼트 트리 사용
import sys
input = sys.stdin.readline

# 수의 개수, 변경횟수, 구간합을 구하는 횟수
N, M, K = map(int, input().split())
treeHeight = 0
length = N

while length != 0:
    length = length // 2 # // -> 정수로 나누기 2
    treeHeight += 1

treeSize = pow(2, treeHeight+1)
leftNodeStartIndex = treeSize // 2 -1
tree = [0] * (treeSize + 1)

# 데이터를 리프 노드에 저장 / 8 ~ 13-1. 5번
for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + N +1):
    tree[i] = int(input())

# 인덱스 트리 생성 함수
def setTree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1

setTree(treeSize - 1)

# 값 변경 함수
def changVal(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + diff # 차이값을 더함
        index = index // 2
        
# 구간 합 계산 함수
def getSum(s, e):
    partSum = 0
    while s <= e:
        if s % 2 == 1: # 독립노드로 선택
            partSum += tree[s]
            s += 1 # 밑에서 나눌꺼기 때문에
        if e % 2 == 0: # 끝값 독립노드로 서택
            partSum += tree[e]
            e -= 1
        s = s // 2
        e = e // 2

    return partSum

for _ in range(M + K): # m = 변경개수, k = 질문개수
    question, s, e = map(int, input().split())
    if question == 1: # 값을 1로 변경
        changVal(leftNodeStartIndex + s, e)
    elif question == 2:
        s = s + leftNodeStartIndex
        e = e + leftNodeStartIndex
        print(getSum(s, e))