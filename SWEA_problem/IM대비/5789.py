T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] * (N+1)
    
    # 작업 수행
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            box[j] = i

    result = box[1:]

    print(f'#{tc}', *result)