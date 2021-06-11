class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0  # 높이 정보도 유지함에 유의!!

    def __str__(self):
        return str(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):  # . mlR
        if v:
            print(v.key, end=" ")
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")

    def find_loc(self, key):
        if self.size == 0: return None
        p = None  # insert OF THERE IS NO KEY PRINT OUT PARENTS NODE
        v = self.root
        while v:
            if v.key == key:
                return v

            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None

    def insert(self, key): # return Node
        v = Node(key)
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)
            if p and p.key != key:  # p is parent of v
                if p.key < key:
                    p.right = v
                else:
                    p.left = v
                v.parent = p
        self.updateheight(key)
        self.size += 1
        return v

    def deleteByMerging(self, x):
        if x == None: return None
        m= None
        L,R,pt = x.left,x.right,x.parent

        if L == None:
            c = R
        else:
            c = m = L
            while m.right:
                m = m.right
            m.right = R
            if R: R.parent = m
        # 루트
        if self.root == x:
            if c: c.parent = None
            self.root = c
        # 그외
        else:
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c: c.parent = pt

        #하이트 조절
        if m:self.updateheight(m.key)
        if not m and R:self.updateheight(R.key)
        if self.root ==c:
            self.size -=1
            return None
        else:self.updateheight(pt.key)

        self.size -= 1

    def deleteByCopying(self, x):
        if x == None: return None
        pt, L, R = x.parent, x.left, x.right
        if L:  # L이 있음
            y = x.left
            while y.right:
                y = y.right
            x.key = y.key
            if y.left:
                y.left.parent = y.parent
            if y.parent.left is y:
                y.parent.left = y.left
            else:
                y.parent.right = y.left
            self.updateheight(y.parent.key)
            del y

        elif not L and R:  # R만 있음
            y = R
            while y.left:
                y = y.left
            x.key = y.key
            if y.right:
                y.right.parent = y.parent
            if y.parent.left is y:
                y.parent.left = y.right
            else:
                y.parent.right = y.right
            self.updateheight(y.parent.key)
            del y

        else:  # L도 R도 없음
            if not pt:  # x가 루트노드인 경우
                self.root = None
            else:
                if pt.left is x:
                    pt.left = None
                else:
                    pt.right = None

                self.updateheight(pt.key)
            del x
        self.size -= 1

    def height(self, x):  # 노드 x의 height 값을 리턴
        if x == None:
            return -1
        else:
            return x.height

    # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
    # 입력 T.search(int) >> 노드를 받음
    def succ(self, x):
        if not x :    # x 가 트리에 없을때
            return None
        # R 과 부모 모두 없을때
        if not x.right and not x.parent :
            return None
        R, pt = x.right,x.parent
        # R 확인
        if R :
            if not R.left :
                return R
            else : # 가장 좌측에 있는것
                while R.left.left:
                    R.left=R.left.left
                return R.left
        # R이 없고 부모만 있을때
        if not R and pt:
            while x : # 루트 노드 까지
                pt = x.parent
                if pt and pt.left:
                    if pt.left == x:
                        return pt
                x = pt

        return None

    def pred(self, x):  # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴               #succ 의 좌우 방향 반대
        if not x :    # x 가 트리에 없을때
            return None
        # L 과 부모 모두 없을때
        if not x.left and not x.parent :
            return None
        pt,L = x.parent ,x.left
        # L 확인
        if L :
            if not L.right :
                return L
            else : # 가장 좌측에 있는것
                while L.right.right:
                    L.right=L.right.right
                return L.right
        # L이 없고 부모만 있을때
        if not L and pt:
            while x!= None : # 루트 노드 까지
                pt=x.parent
                if pt and pt.right:
                    if pt.right == x:
                        return pt
                x = pt
            return x


    def rotateLeft(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)# testcase 9
        y = x.right  # assume that z != None
        if y == None: return  # if y == None: nothing changed
        b = y.left  # b == None 인 경우도 가능
        y.parent = x.parent
        if x.parent:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        if y: y.left = x
        x.parent = y
        x.right = b
        if b:b.parent = x
        self.updateheight(x.key)
        # x == self.root라면 y가 새로운 루트가 되어야 함!
        if x == self.root and x != None:
            self.root = y

    def rotateRight(self, z):  # rotateLeft도 유사하게 정의
        y = z.left  # assume that z != None
        if y == None: return  # if y == None: nothing changed
        b = y.right  # b == None 인 경우도 가능
        y.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = y
            else:
                z.parent.right = y
        y.right = z
        z.parent = y
        z.left = b
        if b:b.parent = z
        self.updateheight(z.key)
        # z == self.root라면 y가 새로운 루트가 되어야 함!
        if z == self.root and z != None:
            self.root = y

    # [주의] height가 있다면 x와 z의 height 값을 수정하는 코드 추가 필요

    def updateheight(self, x):  # get key = x
        x = self.find_loc(x)
        if self.size == 0:  # only have a one node  ,  root node
            return None
        while x:
            L, R, pt = x.left, x.right, x.parent
            # leaf node
            if not L and not R:
                x.height = 0
                x = pt
            # only have a left side node
            elif L and not R :
                if L.height + 1  != x.height:
                   x.height = L.height + 1
                x = pt
            elif R and not  L :
                if R.height + 1 != x.height:
                    x.height = R.height + 1
                x = pt
            # both childnode
            else :
                # find max
                max = 0
                if max <= L.height: max = L.height
                if max <= R.height: max = R.height

                if x.height != max +1 :
                    x.height = max + 1
                x = pt


T = BST()


while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'Rleft':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(v)
            print("@ Rotated left at node {0}".format(cmd[1]))
    elif cmd[0] == 'Rright':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(v)
            print("@ Rotated right at node {0}".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
