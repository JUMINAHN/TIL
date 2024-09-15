# import sys
#
# sys.stdin = open('input2816.txt')
# #테스트 케이스 개수
# T = int(input())
# for tc in range(1, T+1):
N= int(input()) #채널 개수
#내리는것 1, 올리는 것 4
channel = []
for _ in range(N):
    channel.append(input())
#print(channel)

#channel 위치 찾기
result = '' #값을 담을 곳
kbs1_idx=0
kbs2_idx=0
for i in range(N):
    if channel[i] == 'KBS1':
        kbs1_idx = i
    if channel[i] == 'KBS2':
        kbs2_idx = i
result+='1'*kbs1_idx
result+='4'*kbs1_idx
if kbs1_idx > kbs2_idx: #얘가 더 먼저 나온 경우 -> 한칸 밀림
    kbs2_idx += 1
result+='1'*kbs2_idx
result+='4'*(kbs2_idx-1)#한칸 적게 올려야 함
print(result)
