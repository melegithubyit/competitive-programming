def evalRPN(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            else:  # token == '/'
                result = int(operand1 / operand2)

            stack.append(result)

    return stack[0]
