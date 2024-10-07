K, N = map(int, input().split())

def pop_n_times(res):

    if len(res) == N:
        print(*res)
        return
    
    for i in range(1, K + 1):
        pop_n_times(res + [i])

pop_n_times([])