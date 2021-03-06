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

    def preorder(self, v):
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=' ')
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=' ')

    def find_loc(self, key):
        if self.size == 0: return None
        p = None
        v = self.root
        while v:
            if v.key == key:
                return v
            else:
                if v.key < key:
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

    def insert(self, key):
        # 노드들의 height 정보 update 필요
        v = Node(key)
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)
            if p and p.key != key:
                if p.key < key:
                    p.right = v
                else:
                    p.left = v
                v.parent = p
            self.heightUpdate(v)
        self.size += 1
        return v

    def deleteByMerging(self, x):
        # 노드들의 height 정보 update 필요
        a, b, pt = x.left, x.right, x.parent
        if a == None:
            c = b
        else:
            c = m = a
            while m.right:
                m = m.right
            m.right = b
            if b: b.parent = m

        if self.root == x:
            if c: c.parent = None
            self.root = c
        else:
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c: c.parent = pt
        self.heightUpdate(c)
        self.size -= 1

    def deleteByCopying(self, x):
        # 노드들의 height 정보 update 필요
        pt, L, R = x.parent, x.left, x.right
        if L:  # L이 있음`
            y = x.left
            while y.right:
                y = y.right
            x.key = y.key
            yp = y.parent
            if y.left:
                y.left.parent = y.parent
            if y.parent.left is y:
                y.parent.left = y.left
            else:
                y.parent.right = y.left
            del y
            self.heightUpdate(yp)
            self.size -= 1
            return yp

        elif not L and R:  # R만 있음
            y = R
            while y.left:
                y = y.left
            x.key = y.key
            yp = y.parent
            if y.right:
                y.right.parent = y.parent
            if y.parent.left is y:
                y.parent.left = y.right
            else:
                y.parent.right = y.right
            del y
            self.heightUpdate(yp)
            self.size -= 1
            return yp

        else:  # L도 R도 없음
            if pt == None:  # x가 루트노드인 경우
                self.root = None
            else:
                if pt.left is x:
                    pt.left = None
                else:
                    pt.right = None
            del x
            self.heightUpdate(pt)
            self.size -= 1
            return pt

    def height(self, x):  # 노드 x의 height 값을 리턴
        if x == None:
            return -1
        else:
            return x.height

    def succ(self, x):  # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
        # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
        s = x.right
        if s:
            while s.left:
                s = s.left
            return s
        elif (x.parent != None) and (x.parent.key > x.key):
            return x.parent
        elif (x.parent != None) and (x.parent.key < x.key):
            while (x.parent != None) and (x.parent.key < x.key):
                x = x.parent
            return x.parent
        else:
            return None

    def pred(self, x):  # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
        p = x.left
        if p:
            while p.right:
                p = p.right
            return p
        elif (x.parent != None) and (x.parent.key < x.key):
            return x.parent
        elif (x.parent != None) and (x.parent.key > x.key):
            while (x.parent != None) and (x.parent.key > x.key):
                x = x.parent
            return x.parent
        else:
            return None

    def rotateLeft(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        z = x.right
        if z == None: return
        b = z.left
        z.parent = x.parent
        if x.parent:
            if x.parent.left == x:
                x.parent.left = z
            else:
                x.parent.right = z
        if z: z.left = x
        x.parent = z
        x.right = b
        if b: b.parent = x
        if x == self.root and x != None:
            self.root = z
        # [주의] height가 있다면 x와 z의 height 값을 수정하는 코드 추가 필요
        self.heightUpdate(x)

    def rotateRight(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        z = x.left
        if z == None: return
        b = z.right
        z.parent = x.parent
        if x.parent:
            if x.parent.left == x:
                x.parent.left = z
            else:
                x.parent.right = z
        if z: z.right = x
        x.parent = z
        x.left = b
        if b: b.parent = x
        if x == self.root and x != None:
            self.root = z
        # [주의] height가 있다면 x와 z의 height 값을 수정하는 코드 추가 필요
        self.heightUpdate(x)

    def heightUpdate(self, x):
        while x != None:
            L, R = x.left, x.right
            if L and not R:
                x.height = L.height + 1
            elif not L and R:
                x.height = R.height + 1
            elif L and R:
                if L.height > R.height:
                    x.height = L.height + 1
                else:
                    x.height = R.height + 1
            else:
                x.height = 0
            x = x.parent
