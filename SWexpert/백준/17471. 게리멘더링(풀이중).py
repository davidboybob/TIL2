# import sys
# sys.stdin = open('input_17471.txt', 'r')
#
# TC = int(input())
# for tc in range(1):
#     N = int(input())
#     P = [0] + list(map(int, input().split()))
#
#     G = [[] for _ in range(N+1)]
#     print(P)
#     for i in range(1, N+1):
#         data = list(map(int, input().split()))
#         for j in range(1, len(data)):
#             G[i].append(data[j])

    # 로 두 부분으로 나누기
A, B = [], []

def subset(idx, select):

subset(1, 0)
