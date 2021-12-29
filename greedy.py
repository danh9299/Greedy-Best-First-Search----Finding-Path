from collections import defaultdict
from queue import PriorityQueue
#Luu lai du lieu cua do thi
data = defaultdict(list)
data['A'] = ['B','C','D',6]
data['B'] = ['E','F',3]
data['C'] = ['G','H',4]
data['D'] = ['I','J',5]
data['E'] = [5]
data['F'] = ['K','L','M',1]
data['G'] = [6]
data['H'] = ['N','O',2]
data['I'] = [5]
data['J'] = [4]
data['K'] = [2]
data['L'] = [0]
data['M'] = [4]
data['N'] = [0]
data['O'] = [4]
#Tạo ra 1 class Node lưu giá trị các nút
class Node:
    #Hàm tạo
    def __init__(self,name,par=None,h=0):
        self.name = name
        self.par = par
        self.h = h
    #In ra Node
    def display(self):
        print(self.name,self.h)
    #So sánh hàm đánh giá giữa 2 Node
    def __lt__(self,other):
        if other == None:
            return False
        return self.h < other.h
    #Xem 2 Node có giống nhau không
    def __eq__(self,other):
        if other == None:
            return False
        return self.name == other.name
#------------------------------------
#Kiểm tra xem 2 Node có cùng tên không
def equal(O,G):
    if O.name == G.name:
        return True
    return False
#Kiểm tra xem Node có trong hàng đợi không
def checkInPriority(tmp,c):
    if tmp == None:
        return False
    return (tmp in c.queue)
#In ra đường đi và quãng đường
def getPath(O, distance):
    print(O.name)
    distance += O.h
    if O.par != None:
        getPath(O.par, distance)
    else:
        print('Quãng đường: ',distance)
        return
#Thuật toán tìm kiếm Greedy Best First Search
def greedyBestFirstSearch(S,G):
    Open = PriorityQueue()
    Closed = PriorityQueue()
    S.h = data[S.name][-1]
    Open.put(S)
    while True:
        if Open.empty() == True:
            print('Tìm kiếm thất bại')
            return
        O = Open.get()
        Closed.put(O)
        print('Duyệt nút: ',O.name,"(",O.h,")")
        if equal(O,G) == True:
            print('Tìm kiếm đã thành công!')
            print('Đường đi: ')
            distance = 0
            getPath(O,distance)
            return
        #Kiem tra con cua O
        i=0
        while i<len(data[O.name]) - 1:
            name = data[O.name][i]
            h = data[name][-1]

            tmp = Node(name = name, h=h)
            tmp.par = O

            ok1 = checkInPriority(tmp, Open)
            ok2 = checkInPriority(tmp,Closed)

            if not ok1 and not ok2:
                Open.put(tmp)
            i += 1
#Nhập điểm bắt đầu và kết thúc
S=input("Nhập điểm bắt đầu: ")
S=S.upper()
while S not in data:
    print("Vui lòng nhập điểm có trong đồ thị!")
    S=input("Nhập lại điểm bắt đầu: ")
    S=S.upper()

G=input("Nhập điểm kết thúc: ")
G=G.upper()
while G not in data:
    print("Vui lòng nhập điểm có trong đồ thị!")
    G=input("Nhập lại điểm kết thúc: ")
    G=G.upper()
    
#Gọi hàm
greedyBestFirstSearch(Node(S),Node(G))
