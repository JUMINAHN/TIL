def cal(operator, n2, n1):
    """연산자를 기반으로 두 숫자를 계산합니다."""
    n2 = int(n2)
    n1 = int(n1)
    if operator == '+':
        return n2 + n1
    elif operator == '-':
        return n2 - n1
    elif operator == '*':
        return n2 * n1
    elif operator == '/':
        return n2 // n1  # 정수 나눗셈
    else:
        raise ValueError("Invalid operator")


def evaluate_postfix(switch_list):
    """후위 표기법을 계산합니다."""
    stack = []

    for s in switch_list:
        if s.isdigit():
            # 숫자는 스택에 추가합니다.
            stack.append(s)

        else:
            # 연산자를 만나면 스택에서 두 숫자를 꺼내 계산합니다.
            if len(stack) < 2:
                raise ValueError("Insufficient values in expression")
            n1 = stack.pop()
            n2 = stack.pop()
            result = cal(s, n2, n1)
            # 계산 결과를 스택에 다시 추가합니다.
            stack.append(result)

    # 계산이 완료된 후 스택에 남아 있는 값이 하나여야 합니다.
    if len(stack) != 1:
        raise ValueError("The expression is invalid")

    return stack.pop()


# Example usage
switch_list = ['6', '5', '2', '8', '-', '*', '2', '/', '+']
result = evaluate_postfix(switch_list)
print(result)  # Expected output: 3