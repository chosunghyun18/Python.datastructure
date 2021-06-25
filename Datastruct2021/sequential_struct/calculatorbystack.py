class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0


def get_token_list(expr):
    token_list = Stack()
    expr1 = expr.split()
    for token in expr1:
        if len(token) > 1:
            a = " ".join(token)
            tmp1 = []
            for i in a:
                if i != " ":
                    if i not in '-+*/()^':
                        tmp1.append(i)
                    else:
                        if len(tmp1) != 0:
                            token_list.push("".join(tmp1))
                            token_list.push(i)
                            tmp1 = []
                        else:
                            token_list.push(i)
            if len(tmp1) != 0:
                token_list.push("".join(tmp1))
        else:
            token_list.push(token)
    return token_list


def infix_to_postfix(token_list):
    opstack = Stack()
    # 계산의 결과를 담는 스택
    outstack = []
    # 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list.items:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while opstack.top() != "(":
                outstack.append(opstack.pop())
            opstack.pop()

        elif token in '+-/*^':
            if opstack.isEmpty() == 1:
                opstack.push(token)
            elif prec[token] > prec[opstack.top()]:
                opstack.push(token)
            else:
                while prec[opstack.top()] >= prec[token]:
                    outstack.append(opstack.pop())
                    if opstack.isEmpty() == True: break
                opstack.push(token)
        else:
            outstack.append(token)

    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    while not opstack.isEmpty():
        outstack.append(opstack.pop())

    return " ".join(outstack)


def compute_postfix(token_list):
    opstack = Stack()
    token_list = token_list.split()
    for token in token_list:
        if token in '+-/*^':
            a1 = float(opstack.pop())
            a2 = float(opstack.pop())
            if token == '+':opstack.push(a2 + a1)
            elif token == '-':opstack.push(a2 - a1)
            elif token == '*':opstack.push(a2 * a1)
            elif token == '/':opstack.push(a2 / a1)
            elif token == '^':opstack.push(a2**a1)
        else:opstack.push(token)
    return opstack.pop()


# 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)