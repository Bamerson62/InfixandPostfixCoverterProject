from stack import Stack

def evaluate_postfix(expr):
    stack = Stack()
    tokens = expr.split()

    for token in tokens:
        
        if token.replace('.', '', 1).isdigit():
            
            if '.' in token:
                value = float(token)
            else:
                value = int(token)
            stack.push(value)
        else:
            
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                stack.push(left + right)
            elif token == '-':
                stack.push(left - right)
            elif token == '*':
                stack.push(left * right)
            elif token == '/':
                stack.push(left / right)
            else:
                raise ValueError(f"Unknown operator: {token}")

    return stack.pop()
