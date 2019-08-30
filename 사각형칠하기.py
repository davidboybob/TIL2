from pprint import pprint
import sys
sys.stdin = open('sample_input.txt', 'r')

def main():
    T = int(input())
    for test_case in range(1, T + 1):

        N, M, K = map(int, input().split())
        DRAW = [[int(num) for num in input().split()] for _ in range(K)]


        arr = [[0] * M for _ in range(N)]
        greys = [0] * 11
        greys[0] = N*M
        for j in range(K):
            Drawing = 1
            y1, x1, y2, x2, grey = DRAW[j]
            if grey == 0:
                continue
            else:
                for y in range(y1, y2+1):
                    for x in range(x1, x2+1):
                        if arr[y][x] > grey:
                            Drawing = 0
                            break
                    if Drawing == 0:
                        break
                if Drawing:
                    for y in range(y1, y2+1):
                        for x in range(x1, x2+1):
                            for p in range(grey):
                                if arr[y][x] == p:
                                    greys[p] -= 1
                            if arr[y][x] != grey:
                                greys[grey] += 1
                            arr[y][x] = grey
        AnswerN = max(greys)
        print("#%d %d" % (test_case, AnswerN))
        print(greys)
        pprint(arr)


if __name__ == "__main__":
    main()
