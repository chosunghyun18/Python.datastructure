class deque:
    def __init__(self, string):
        self.items = []
        for i in range(len(string)):
            self.items.append(string[i])  # 문자들 다 넣기

    def append(self, c):
        self.itmes.append(c)  # 오른쪽으로 in

    def appendleft(self, c):
        self.items.insert(0, c)  # 왼쪽으로 in

    def pop(self):
        return self.items.pop()  # 오른쪽으로 out

    def popleft(self):
        tmp = self.items[0]  # 다른 방법도 있음 -> front index로 칸을 지우지않고 포인터만 이동
        del self.items[0]  # 맨앞에 제거
        return tmp

    def __len__(self):
        return len(self.items)


    def right(self):
        return self.items[-1]
    
    def left(self):
        return self.items[0]


def check_palindrome(s):
        dq = deque(s)  # 생성과 동시, 문자열 보냄
        palindrome = True  # 초기값 True
        while len(dq) > 1:  # 짝수 0개 남음/ 홀수 1개 남음
            if dq.popleft() != dq.pop():  # 양쪽으로 꺼내서 비교
                palindrome = False  # 다르면 False
                return palindrome
        return palindrome  # 모두 같아서 True 반환


s = input()
print(check_palindrome(s))
