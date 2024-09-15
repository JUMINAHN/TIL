import sys

sys.stdin = open('input2805.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #농작물 사이즈
    value = [list(map(int, input())) for _ in range(N)] #농작물 가치가 들어있는 배열 idx
    #간단하게 가운데로 나누어 접근
    #핵심은 기준점
    stand_idx = N//2
    #먼저 stand_idx를 구할 윗동네 파트 계산
    farm_value = 0 #내가 계산할 농장의 가치
    #i는 row, j는 col
    for i in range(0, stand_idx + 1): #테케 기준 3번까지구하기 위해서
        for j in range(N): #col은 다 계산할 것
            if value[j] in value[stand_idx - i:stand_idx + i + 1]: #기준점과 같다면, slicing이니까 1군데 더 가야함 'int' object is not subscriptable
                farm_value += value[i][j] #더해준다.
    #print(farm_value) #여기까지는 맞게 들어간 것으로 확인이 된다.
    #아랫동네 파트 계산
    #재 검증을 위해 새로운 변수 farm_value 2를 선언
    #farm_value2 = 0
    for i in range(0, stand_idx):  # 테케 기준 3번까지구하기 위해서
        for j in range(N):  # col은 다 계산할 것
            if value[j] in value[stand_idx - i:stand_idx + i + 1]: # 기준점과 같다면, slicing이니까 1군데 더 가야함 'int' object is not subscriptable
                farm_value += value[N-1-i][j] #더해준다.
                #farm_value2라는 변수 설정을 잘못해서 맞게했는데 오류가 ㅇ떳다..
    print(f'#{tc} {farm_value}')
    #print(farm_value)