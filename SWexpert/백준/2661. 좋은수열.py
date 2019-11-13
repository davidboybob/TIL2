N = 7

# N = int(input())

# data = [1, 2, 3]

nums = [0] * N

def makesequence(k):
    if k == N:
        print(*nums)
        return True


    # if S[-1] != '1' or len(S) == 0:
    #     makesequence(k + 1, S + '1')
    # if S[-1] != '2':
    #     makesequence(k + 1, S + '2')
    # if S[-1] != '3':
    #     makesequence(k + 1, S + '3')

    for i in range(1, 4):
        nums[k] = i

        makesequence(k+1)

    return False

makesequence(0)



