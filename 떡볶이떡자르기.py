N,M = map(int, input().split())

array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0

while start <= end:
    mid = (start + end) // 2
    ttuk = 0
    for x in array:
        if x > mid:
            ttuk += x - mid

    if ttuk == M:
        result = mid
        break
    elif ttuk < M:
        end = mid -1
    else:
        result = mid
        start = mid+1

print(result)
