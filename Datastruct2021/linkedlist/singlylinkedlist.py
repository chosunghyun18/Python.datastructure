class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.key)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def printList(self):  # 변경없이 사용할 것!
        v = self.head
        while (v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

    # head 노드의 값 리턴. empty list이면 None 리턴
    def pushFront(self, key, value=None):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pushBack(self, key, value=None):
        new_node = Node(key, value)
        if self.size == 0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node

        self.size += 1

    def popFront(self):
        key = value = None
        if self.size == 0:  # empty list (nothing to pop)
            return None

        if len(self) > 0:
            key = self.head.key
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
        if value == None:
            return key
        return key, value

    def popBack(self):
        if self.size == 0:  # empty list (nothing to pop)
            return None
        else:
            # tail 노드와 그 전 노드인 previous를 찾는다
            previous, current = None, self.head
            while current.next != None:
                previous, current = current, current.next  # 한 노드씩 진행
            # 만약 리스트에 노드가 하나라면 그 노드가 head이면서 동시에 tail임
            # 그런 경우라면 tail을 지우면 빈 리스트가 되어 head = None으로 수정해야함!
            key, value = current.key, current.value
            tail = current
            if self.head == tail:  # 또는 if previous == None:
                self.head = None
            else:
                previous.next = tail.next  # previous가 새로운 tail이 됨!
            self.size -= 1
            if value == None:
                return key
            else:
                return key, value

    def search(self, key):
        search = self.head
        while search:
            if search.key == key:
                return search
            search = search.next
        return None

    # x 는 노드 클라
    def remove(self, x):
        prev = None  # search 노드 전 노드의 key 값을 수정하게 함
        target = self.head  # popback 응용 원하는 노드 찾을때
        if x == None:
            return False

        elif x == self.head:  # 하나의 노드만 있을
            self.popFront()
            return True

        else:
            while target.next != x.next:  # 제거하는 노드가 나올때까지 점진적 증가
                prev = target
                target = target.next

                if target == x:  # 제거하는 노드와 같을때
                    prev.next = x.next
                    prev.value = x.value
                    self.size -= 1
                    return True

    def size(self):
        return self.size

    def reverse(self, x):
        if self.size == 0:
            return None
        x = self.search(x)
        if x == None :
            return None
        # 찾고자 하는 노드가 하나일때
        if x.next == None:
            return None
        prev = None
        current = self.head

        if self.head != x:
            while current != None:
                prev = current
                current = current.next
                bftmp = prev
                if current == x:
                    while current:
                        if current:
                            tmp = current.next  # 다음노드 이동 임시저장
                            current.next = prev  # 노드 방향 변환
                            prev = current  # prev 노드를 전진
                            current = tmp  # 다음 노드로 이동
                        # 완성된 노드의 헤드를 설정
        else:
                prev = current
                current = current.next
                while current:
                        if current:
                            tmp = current.next  # 다음노드 이동 임시저장
                            current.next = prev  # 노드 방향 변환
                            prev = current  # prev 노드를 전진
                            current = tmp  # 다음 노드로 이동
                        # 완성된 노드의 헤드를 설정


        # 완성된 뒤 집은 노드의 해드 설정
        if self.head != x:
            bftmp.next = prev
        else:
            self.head = prev

            # 완성된 뒤즙은 노드 마지막에 none 연결
        while prev != x:
            prev = prev.next
        prev.next = None

    def findMax(self):
        # self가 empty이면 None, 아니면 max key 리턴
        if self.size == 0:
            return None
        tmp = None
        rear = None
        up = self.head
        tmp = up.key
        # 단일 노드
        if up.next == None:
            return tmp

        while up.next != None:

            rear = up
            up = up.next
            if tmp < rear.key:
                tmp = rear.key

        if tmp < up.key:
            tmp = up.key
        return tmp

    # self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
    def deleteMax(self):
        if self.size == 0:
            return None
        max = self.findMax() #int type

        self.remove(self.search(max))

        return max


    # val = new node key
    def insert(self, k, val):
        if self.size <= k:      # k 가 노드의 개수보다 같거나 작으면 뒤에 삽입.
            self.pushBack(val)
        else :
            new_node = Node(val)
            count = 0  # k 번째를 찾게 해줌 k>0 가정 이용
            prev = None
            current = self.head
            self.size += 1
            while current != None:

                if count == k:
                    prev.next = new_node
                    new_node.next = current
                    return 0

                else:
                    prev = current
                    current = current.next
                    count += 1


# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == "pushFront":
        L.pushFront(int(cmd[1]))
        print(int(cmd[1]), "is pushed at front.")
    elif cmd[0] == "pushBack":
        L.pushBack(int(cmd[1]))
        print(int(cmd[1]), "is pushed at back.")
    elif cmd[0] == "popFront":
        x = L.popFront()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from front.")
    elif cmd[0] == "popBack":
        x = L.popBack()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from back.")
    elif cmd[0] == "search":
        x = L.search(int(cmd[1]))
        if x == None:
            print(int(cmd[1]), "is not found!")
        else:
            print(int(cmd[1]), "is found!")
    elif cmd[0] == "remove":
        x = L.search(int(cmd[1]))
        if L.remove(x):
            print(x.key, "is removed.")
        else:
            print("Key is not removed for some reason.")
    elif cmd[0] == "reverse":
        L.reverse(int(cmd[1]))
    elif cmd[0] == "findMax":
        m = L.findMax()
        if m == None:
            print("Empty list!")
        else:
            print("Max key is", m)
    elif cmd[0] == "deleteMax":
        m = L.deleteMax()
        if m == None:
            print("Empty list!")
        else:
            print("Max key", m, "is deleted.")
    elif cmd[0] == "insert":
        L.insert(int(cmd[1]), int(cmd[2]))
        print(cmd[2], "is inserted at", cmd[1] + "-th position.")
    elif cmd[0] == "printList":
        L.printList()
    elif cmd[0] == "size":
        print("list has", len(L), "nodes.")
    elif cmd[0] == "exit":
        print("DONE!")
        break
    else:
        print("Not allowed operation! Enter a legal one!")