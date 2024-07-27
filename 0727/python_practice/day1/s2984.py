password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."

first_char = password[28:36] #28번쨰부터 35번째까지 작성된 글자
second_world = password[113:118] #113부터 117까지 --> 총 5글자니까
third_world = password[68:65:-1] # 66부터 68까지 문자를 뒤집어서 출력 --> 역순 슬라이싱**
fourth_world = password[326:321:-1] #322부터 326까지 뒤집어 출력
fifth_world = password[365:371] #365부터 6글자

#문자열을 자를 때

#해당 부분 모두 출력
print(f'{first_char}{second_world} {third_world}{fourth_world} "{fifth_world}".')