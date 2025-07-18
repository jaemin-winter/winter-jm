# 세그먼트 트리 만들고 조회까지

arr = [0, 1000, 3000, 1000, 500, 1000, 2000, 800, 1000]

# 배열의 크기를 4N으로 만들면 안전하게 만들 수 있다. (암기해야 편함)
# 최악의 경우를 생각해보기 -> 8개말고, 더 늘어날 수 있음
segTree = [0] * (4 * len(arr))

# 파라미터 : 현재 인덱스와 바라보고 있는 범위의 시작 / 끝
def makeSeg(n, s, e):

    # 기저 조건 : 리프 노드일 때 (리프 노드를 판단해야함)
    if s == e:
        segTree[n] = arr[s]
        return segTree[n]

    # 좌우로 내려가는 코드
    mid = (s + e) // 2

    # 왼쪽
    left = makeSeg(n * 2, s, mid)

    # 오른쪽
    right = makeSeg(n * 2 + 1, mid + 1, e)

    segTree[n] = min(left, right)

    return segTree[n]

# 파라미터: 현재 바라보고 있는 범위, 타겟의 범위
def querySeg(n, s, e, ts, te):
    # 2. 기저 조건
    # 2.1 현재 바라보고 있는 범위가 타겟에 완벽하게 포함되는 경우
    # - 바라보고 있는 범위 내의 최소값
    # - return segTree[현재 인덱스]
    if ts <= s and e <= te:
        return segTree[n]

    # 2.2 완벽하게 나간다면
    # - 계산에 영향이 없는 값을 return 해줘야함
    # 최소: 최대값
    # 최대: 최소값
    # 합: 0
    if e < ts or te < s:
        return float('INF')


    # 3. 재귀 호출 (범위가 일부만 포함된다면)
    # 왼쪽, 오른쪽으로 나눠서 재귀호출
    mid = (s + e) // 2
    left = querySeg(n * 2, s, mid, ts, te)
    right = querySeg(n * 2 + 1,  mid + 1, e, ts, te)
    return min(left, right)

makeSeg(1, 1, len(arr) - 1)

print(segTree)

result = querySeg(1, 1, len(arr) - 1, 2, 7)

print(result)