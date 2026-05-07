from stack import Stack

_PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

def infix_to_postfix(expr):
    stack = Stack()
    output = []
    tokens = expr.split()

    for token in tokens:
        
        if token.isalnum():
            output.append(token)

        elif token == '(':
            stack.push(token)

        elif token == ')':
            # pop until '('
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            if not stack.is_empty():
                stack.pop()  # discard '('
        else:
            # operator
            while (not stack.is_empty() and
                   stack.peek() != '(' and
                   _PRECEDENCE.get(stack.peek(), 0) >= _PRECEDENCE[token]):
                output.append(stack.pop())
            stack.push(token)

    # empty the stack
    while not stack.is_empty():
        output.append(stack.pop())

    return " ".join(output)
