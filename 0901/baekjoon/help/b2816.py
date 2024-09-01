# import sys
#
# sys.stdin = open('input2816.txt')
#테스트 케이스 개수
# T = int(input())
# for tc in range(1, T+1):
N = int(input()) #채널의 개수
channel = []
k1_idx = k2_idx = 0 #kbs 채널들의 index번호
for i in range(N):
    data = input()
    if data == 'KBS1':
        k1_idx = i
    elif data == 'KBS2':
        k2_idx = i
    channel.append(data)
#채널 자체의 list가 완성되었고, kbs들의 idx도 확보함
#먼저 kbs1의 위치를 찾아갈 것
result = '' #결과값을 담을 빈 문자열
#화살표를 아래로 내린다.
result += '1'* k1_idx #idx개수만큼
#그리고 해당 위치에 있는것을 4번버튼을 이용해서 맨위로 올린다.
result += '4'* k1_idx #0번쨰 idx기 떄문에 idx만큼 다시 올리면된다.
#그리고 다음 KBS2를 동일하게 반복한다.
#단 유의할 점은 kbs2가 kbs1의 첫 idx보다 위에있을 경우 idx가 1씩 밀린다(전반적으로 1씩밀린다)
if k1_idx > k2_idx:
    k2_idx += 1 #따라서 idx번호를 1 증가시켜주고
result += '1' * k2_idx
result += '4' * (k2_idx-1) #0번쨰 idx로 위치시키는게 아니기 떄문에 -> 1번쨰 idx로 이동시켜야 함
print(result)