import sys
#in으로 간단하게 풀기
# if str1 in str2:
#     print(f'#{tc} 1')
# else :
#     print(f'#{tc} 0')

sys.stdin = open('input4864.txt')
#테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    #구간합 접근 방식과 동일하게 생각하면 될 듯
    for i in range(0, len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            print(f'#{tc} 1')
            break
    else :
        print(f'#{tc} 0')