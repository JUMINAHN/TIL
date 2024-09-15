# 1.카운트 정렬 접근 -> 행자체에
# 2. 1의 개수가 3개이면 total에 +1을 해준다
# 3. 1이면 누적적으로 count하고, 연속을 방해하는 0을 만나게되면 이전 값을 저장하고 count에 0을 대입한다.
# 4. 즉 행열을 다 읽어야 함
# etc. 전체에서 range 3이나 slicing을 해서 모두 1인경우를 카운팅할 수 있을 것 같음
# 나 -> 한줄씩 전체 row와 전체 col을 합산하는 방식을 사용함
import sys

sys.stdin = open('input1979.txt')

#행열 한줄씩 카운트
def count_row(arr, count):
    for row in range(N):
        s = 0 #단순 확인 카운트고
        for col in range(N):
            if 1 == arr[row][col]:
                s += 1
            else :
                if s == K: #바뀌기 전에 s가 3인게 확인이되면
                    count += 1
                s = 0 # 단순하게 0을 하면 사라지기 때문에
        if s == K: #이것도 있어야하는게 마지막 카운트가 3인게 누적이 되어야 하기 때문에
            count += 1
    return count

def count_col(arr,count):
    for col in range(N):
        s = 0 #단순 확인 카운트고
        for row in range(N):
            if 1 == arr[row][col]:
                s += 1
            else :
                if s == K: #바뀌기 전에 s가 3인게 확인이되면
                    count += 1
                s = 0 # 단순하게 0을 하면 사라지기 때문에
        if s == K: #이것도 있어야하는게 마지막 카운트가 3인게 누적이 되어야 하기 때문에
            count += 1
    return count


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] #행을 만든다. --> input 값 모두
    count = 0 #전체 카운트
    count = count_col(arr, count)
    count = count_row(arr, count)

    print(f'#{tc} {count}')