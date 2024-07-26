# count 함수 사용
# def count_character(msg, keyword):
#     return msg.count(keyword)

def count_character(msg, keyword):
    total = 0
    for m in msg :
        if m == keyword:
            total += 1
    return total

result = count_character("Hello, World!", "o")
print(result)  # 2










# result = count_character("Hello, World!", "o")
# print(result)  # 2