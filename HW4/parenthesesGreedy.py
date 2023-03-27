def max_expression_value(expression):
    number_stack = []
    index = 0
    length = len(expression)
    while index < length:
        if expression[index] == '+':
            num1 = number_stack.pop()
            number_stack.append(num1 + int(expression[index + 1]))
            index += 2

        elif expression[index] == '*':
            index += 1
            continue
        else:
            number_stack.append(int(expression[index]))
            index += 1

    result = 1
    for index in range(len(number_stack)):
        result *= number_stack[index]

    return result


def main():
    expr = input()
    expr = expr.split()
    print(max_expression_value(expr))


if __name__ == '__main__':
    main()
