# katok = ["다현", "정연", "쯔위", "사나", "지효"]

# def add_data(friend):
#     katok.append(None)
#     len1=len(katok)
#     katok[len1-1] = friend

# def insert_data(index, friend):
#     katok.append(None)
#     len1=len(katok)

#     for i in range(len1-1,index,-1):
#         katok[i] = katok[i-1]
#         katok[i-1] = None
#     katok[index] = friend

# def delete_data(index):

#     len1=len(katok)
#     katok[index] = None

#     for i in range(index, len1-1):
#         katok[i]=katok[i+1]
#         katok[i+1] = None
#     del(katok[len1-1])
    
# insert_data(2,"문별")
# insert_data(6,"솔라")
# delete_data(6)
# delete_data(2)

# print(katok)

# 최고차항 반복 프로그램

# px=[7,-4,0,5]

# def printploy(px):
#     len1= len(px)-1
#     polystr = "P(x) = "

#     for i in range(len1+1):
#         coef = px[i]
#         if (coef>0):
#             polystr +="+"
#         if (coef==0):
#             continue
#         polystr += str(coef) +"x^"+ str(len1-i)
   
#     return polystr
# print(printploy(px))


# # 카톡 친구 자동 삽입하기
# def find_and_insert_data_31(friend, k_count):
#     findPos_31 =-1
#     for i_31  in range(len(katok_31)):
#         pair_31 = katok_31[i_31]
#         if k_count>=pair_31[1]:
#             findPos_31=i_31 
#             break
#     if findPos_31 == -1:
#         findPos_31 = len(katok_31)

#     insert_data_31(findPos_31,(friend,k_count))

# def insert_data_31(position,friend):
#     if position <0 or position> len(katok_31):
#         print("데이터를 삽입할 범위를 벗어났습니다.")
#         return

#     katok_31.append(None)
#     klen_31 = len(katok_31)

#     for i  in range(klen_31-1,position,-1):
#         katok_31[i] = katok_31[i-1]
#         katok_31[i-1] =None

#     katok_31[position] = friend

# katok_31 = [('다현',200),('정연',150),('쯔위',90),('사나',30),('지효',15)]

# if __name__=="__main__":

#     while True:
#         data_31 = input("추가할 친구--> ")
#         count_31 = int(input("카톡 횟수--> "))
#         find_and_insert_data_31 (data_31,count_31)
#         print(katok_31)


# 단순 연결 리스트 생성
# class Node():
#     def __init__(self):
#         self.data = None
#         self.link = None

# def PrintNodes(start):
#     current = start
#     if current == None:
#         return
#     print(current.data, end=" ")
#     while current.link != None:
#         current = current.link
#         print(current.data, end=" ")
#     print()

# ##전연변수 선언 부분
# memory = []
# head, current, pre = None, None, None
# dataArray= ["다현", "정연", "쯔위", "사나", "지효"]


# if __name__== "__main__":


#     node = Node()
#     node.data = dataArray[0]
#     head = node
#     memory.append(node)

#     for data in dataArray[1:]:
#         pre = node
#         node = Node()
#         node.data = data
#         pre.link =  node
#         memory.append(node)
#     PrintNodes(head)

# 스택
# stack = [None,None, None,None, None]
# top =-1

# top+=1
# stack[top] = "커피"
# top += 1
# stack[top] = "녹차"
# top += 1
# stack[top] = "꿀물"

# print("------ 스택상태------")
# for i in range(len(stack)-1,-1,-1):
#     print(stack[i])

# 스택의 일반구현
# SIZE = 5
# stack = [None for i in range(SIZE)]
# top =-1

# def IsStackFull():
#     global SIZE, stack,top
#     if top >= (SIZE-1):
#         return True
#     else:
#         return False

# def push(data):
#     global SIZE,top,stack
#     if (IsStackFull()):
#         print("스택이 가득 찼습니다")
#         return
#     top+=1
#     stack[top] = data
# def IsStackEmpty():
#     global stack,top, SIZE
#     if top ==-1:
#         return True
#     else:
#         return False

# def pop():
#     global SIZE,top,stack
#     if IsStackEmpty():
#         print(" 더 이상 스택이 없습니다")
#         return
#     data = stack[top]
#     stack[top] = None
#     top -=1

# def peek():
#     global SIZE, top,stack
#     if IsStackEmpty():
#         print("스택이 비었습니다")
#         return
#     return stack[top]

# if __name__ = "__main__":
#     select = input("삽입(I)/ 추출(E)/확인(V)/종료(X) 중 하나를 선택")
#     while (select != "X" or select != "x"):
#         if#######



# 스택의 응용
# import webbrowser
# import time

# SIZE = 100
# stack = [None for i in range(SIZE)]
# top = -1

# def IsStackFull():
#     global SIZE, stack,top
#     if top >= (SIZE-1):
#         return True
#     else:
#         return False

# def push(data):
#     global SIZE,top,stack
#     if (IsStackFull()):
#         print("스택이 가득 찼습니다")
#         return
#     top+=1
#     stack[top] = data
# def IsStackEmpty():
#     global stack,top, SIZE
#     if top ==-1:
#         return True
#     else:
#         return False

# def pop():
#     global SIZE,top,stack
#     if IsStackEmpty():
#         print(" 더 이상 스택이 없습니다")
#         return 
#     data = stack[top]
#     stack[top] = None
#     top -=1

# def peek():
#     global SIZE, top,stack
#     if IsStackEmpty():
#         print("스택이 비었습니다")
#         return
#     return stack[top]

# if __name__ == "__main__":
#     urls = ["naver.com","google.com","nate.com"]
    
#     for url in urls:
#         push(url)
#         webbrowser.open("http://"+url)
#         print(url,end="-->")
#         time.sleep(1)

#     print("방문종료") 
#     time.sleep(3)

#     while True:
#         url = pop()
#         if url ==None:
#             break
#         webbrowser.open("http://"+url)
#         print(url,end="-->")
#         time.sleep(1)
#     print("방문종료")

# katok = []
# def add_data(friend):
#     katok.append(None)
#     klen=len(katok)
#     katok[ken-1]=friend

# def insert_data(position,friend):
#     katok.append(None)
#     klen = len(katok)

#     for i  in range(klen-1,position,-1):
#         katok[i]=katok[i-1]
#         katok[i-1]=None
#     katok[position] = friend

# def delete_data(positon):
#     katok[positon] = None
#     klen = len(katok)
#     for i  in range(positon,klen-1):
#         katok[i]=katok[i+1]
#         katok[i] = None
#     del(katok[klen-1])

    
# # 단순연결리스트
# class Node():
#     def __init__(self):
#         self.data = None
#         self.link = None

# dataArray=['a','b','c','d','e']

# # 첫 노드
# node = Node()
# node.data = dataArray[0]
# head = node

# # 두번째 노드 
# pre = node
# node = Node()
# node.data = dataArray[1:]
# pre.link = node 

# # 첫 노드 삽입
# node = Node()
# node.data = "0"
# node.link = head
# head = Node

# # 중간 노드 삽입
# current = head
# while current !=None:
#     pre = current
#     current=current.link
#     if current.data =="2":
#         node=Node()
#         node.data= "루트2"
#         node.link = current
#         pre.link = Node

# 순차큐

# size = int(input("큐의 크기를 적어주세요"))
# queue = [None for i in range(size)]
# front = rear = -1

# def IsQueueFull():
#     global size, queue,front,rear
#     if  rear != size -1:
#         return False
#     elif  rear == size -1 and front == -1:
#         return True
#     else:
#         for i  in range(front+1,size):
#             queue[i-1] = queue[i]
#             queue[i] =None
#         front -=1
#         rear-= 1
#         return False    
# def enQueue(data):
#     global size, queue, front,rear
#     if IsQueueFull():
#         print("큐가 가득찼습니다.")
#         return
#     rear +=1
#     queue[rear] = data

# def IsQueueEmpty():
#     global szie, queue, front,rear
#     if front == rear:
#         return True
#     else:
#         return False

# def deQueue():
#     global size, queue, front,rear
#     if IsQueueEmpty():
#         print(" 큐가 비었습니다.")
#         return None
#     front += 1
#     data = queue[front]
#     queue[front] = None
#     return data

# def peek():
#     global size, queue, front, rear
#     if IsQueueEmpty():
#         print("큐가 비었습니다")
#         return None
#     return queue[front+1]

# 원형 큐
# size = int(input("큐의 크기를 적어주세요"))
# queue = [None for i in range(size)]
# front = rear = 0

# def IsQueueFull():
#     global size, queue,front,rear
#     if  front == (rear+1) %szie:
#         return True
#     else:
#         return False
     
# def enQueue(data):
#     global size, queue, front,rear
#     if IsQueueFull():
#         print("큐가 가득찼습니다.")
#         return
#     rear = (rear+1) %size
#     queue[rear] = data

# def IsQueueEmpty():
#     global szie, queue, front,rear
#     if front == rear:
#         return True
#     else:
#         return False

# def deQueue():
#     global size, queue, front,rear
#     if IsQueueEmpty():
#         print(" 큐가 비었습니다.")
#         return None
#     front = (front+1) %size
#     data = queue[front]
#     queue[front] = None
#     return data

# def peek():
#     global size, queue, front, rear
#     if IsQueueEmpty():
#         print("큐가 비었습니다")
#         return None
#     return queue[(front+1)%size]

# 트리 구조
# class TreeNode():
#     def __init__(self):
#         self.data = None
#         self.left = None
#         self.right = None

# def preorder(node):
#     if node ==None:
#         return
#     print(node.data,end= "->")
#     preorder(node.left)
#     preorder(node.right)

# def inorder(node):
#     if node == None:
#         return
#     inorder(node.left)
#     print(node.data, end="->")
#     inorder(node.right)

# def postorder(node):
#     if node == None:
#         return
#     postorder(node.left)
#     postorder(node.right)
#     print(node.data, end="->")

# node1 = TreeNode()
# node1.data = '화사'

# node2 = TreeNode()
# node2.data = '솔라'
# node1.left = node2

# node3 = TreeNode()
# node3.data = '문별'
# node1.right = node3

# node4 = TreeNode()
# node4.data = '휘인'
# node2.left = node4

# node5 = TreeNode()
# node5.data = '쯔위'
# node2.right = node5

# node6 = TreeNode()
# node6.data = '선미'
# node3.left = node6

# print(preorder(node1))
# print(inorder(node1))
# print(postorder(node1))


# 이진 탐색 트리의 일반 구현
# class TreeNode():
#     def __init__(self):
#         self.data = None
#         self.left = None
#         self.right = None

# node = TreeNode()


# current = root
# # 이진 탐색 트리의 삽입 작동
# while True:
#     if name< currnet.data:
#         if current.left==None:
#             current.left  = node
#             break
#         current = current.left
#     else:
#         if currnt.right ==None:
#             current.right =node
#             break
#         currnet = current.right
# # 이진 탐색 트리의 검색 작동
# while True:
#     if findname == currnt.data:
#         print(findname , "을 찾음")
#         break
#     elif findname<current.data:
#         if currnt.left == None:
#             print(findname, "이(가) 트리에 없음")
#             break
#         current = current.left
#     else:
#         if currnt.left == None:
#             print(findname, "이(가) 트리에 없음") 
#             break
#         current = current.right
# # 이진 탐색 트리의 삭제 작동
# current = node
# parent =None
# while True:
#     if deletename == currnet.data:

#         if current.left ==None and current.right==None:
#             if parent.left ==current:
#                 parent.left = None
#             else:
#                 parent.right = None
#             del(currnet)
        
#         elif current.left != None and current.right ==None:
#             if parent.left == current:
#                 parent.left = current.left
#             else:
#                 parent.right = parent.left
#             del(current)

# # 이진트리탐색 응용
# import random
# ## 함수 선언 부분 ##
# class TreeNode() :
# 	def __init__ (self) :
# 		self.left = None
# 		self.data = None
# 		self.right = None

# ## 전역 변수 선언 부분 ##
# memory = []
# rootBook, rootAuth = None, None
# bookAry = [ ['어린왕자', '쌩떽쥐베리'],['이방인', '까뮈'], ['부활', '톨스토이'],
# 		   ['신곡', '단테'], ['돈키호테', '세브반테스'], ['동물농장', '조지오웰'],
# 		   ['데미안','헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅'] ]
# random.shuffle(bookAry)

# # 책이름
# node = TreeNode()
# node.data = bookAry[0][0]
# rootBook = node

# for book in bookAry[1:]:
#     name = book[0]
#     node = TreeNode()
#     node.data = name
    
#     current = rootBook
#     while True:
#         if name < current.data:
#             if current.left == None:
#                 current.left = node
#             break
#         current = current.left

#         if name >current.data:
#             if current.right == None:
#                 current.right = node
#             break
#         current = current.right

# # 작가이름
# node = TreeNode()
# node.data = bookAry[0][1]
# rootAuth = node

# for book in bookAry[1:]:
#     name = book[0]
#     node = TreeNode()
#     node.data = name
    
#     current = rootBook
#     while True:
#         if name < current.data:
#             if current.left == None:
#                 current.left = node
#             break
#         current = current.left

#         if name >current.data:
#             if current.right == None:
#                 current.right = node
#             break
#         current = current.right

# # 책이름 및 작가 이름 검색
# book_or_author = input("책검색(1), 작가검색(2) -->")
# findname = input("검색할 책 또는 작가")

# if book_or_author == 1:
#     root = rootBook
# else:
#     root = rootAuth

# current = root
# while True:
#     if findname == current.data:
#         print(findname, "을 찾음")
#         findYN= True
#         break
#     elif findname < current.data:
#         if current.left ==None:
#             print(findname, "가 없음")
#             break
#         current = current.left
#     elif findname > current.data:
#         if current.right ==None:
#             print(findname, "가 없음")
#             break
#         current = current.right
       
# 그래프
# 무방향 그래프
# class Graph():
#     def __init__(self,size):
#         self.SIZE = size
#         self.graph = [[0 for i in range(size)] for i in range(size)]
# len = int(input("사이즈를 입력하세요"))
# G1 = Graph(len)
# G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
# G1.graph[1][0] = 1; G1.graph[1][2] = 1
# G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
# G1.graph[3][0] = 1; G1.graph[3][2] = 1

# print("무방향 그래프")
# for row in range(len):
#     for col  in range(len):
#         print(G1.graph[row][col], end= " ")
#     print()

# G3 = Graph(4)
# G3.graph[0][1] = 1; G3.graph[0][2] = 1
# G3.graph[3][0] = 1; G3.graph[3][2] = 1

# print("방향 그래프")
# for row in range(4):
#     for col in range(4):
#         print(G3.graph[row][col], end= " ",)
#     print()


# class Graph():
#     def __init__(self,size):
#         self.SIZE = size
#         self.graph = [[0 for i in range(size)] for i in range(size)]

# nameAry=["문별","솔라","휘인","쯔위","선미","화사"]

# g1 = Graph(len(nameAry))

# def PrintGraph(g):
#     print(' ', end = "   ")
#     for a_row  in range(g.SIZE):
#         print(nameAry[a_row], end = " ")
#     print()
#     for row in  range(g.SIZE):
#         print(nameAry[row], end= " ")
#         for col in  range(g.SIZE):
#             print(g.graph[row][col], end ="    ")
#         print()
#     print()
    
# PrintGraph(g1)

# 깊이 우선 탐색기 스택 이용!
# class Graph():
#     def __init__(self,size):
#         self.SIZE = size
#         self.graph = [[0 for i in range(size)] for i in range(size)] 


# G1 = None
# stack =[]
# visitedAry =[]

# G1 = Graph(4)
# G1.graph[0][2] = 1; G1.graph[0][3] = 1
# G1.graph[1][2] = 1
# G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
# G1.graph[3][0] = 1; G1.graph[3][2] = 1

# print('## G1 무방향 그래프 ##')
# for row in range(4) :
#     for col in range(4) :
#         print(G1.graph[row][col], end = ' ')
#     print()

# current = 0
# stack.append(current)
# visitedAry.append(current)

# while(len(stack) != 0):
#     next = None
#     for vertex in range(4):
#         if G1.graph[current][vertex] ==1:
#             if vertex in visitedAry:
#                 pass    
#             else:
#                 next = vertex
#             break

# if next != None:
#     current = next
#     stack.append(current)
#     visitedAry.append(current)
# else:
#     current = stack.pop()


# print('방문순서 -->', end =" ")
# for i in visitedAry:
#     print(chr(ord('A')+i), end =" ")


# import os

# class TreeNode_31():
#     def __init__(self):
#         self.left_31 = None
#         self.data_31 = None
#         self.right_31 = None

# memory_31 = []
# root_31 = None
# fnameAry_31 =[]

# folderName_31 = input("폴더 경로를 입력해 주세요")
# for dirName_31, subDirList_31,fnames_31 in os.walk(folderName_31):
#     for fname_31 in fnames_31:
#         fnameAry_31.append(fname_31)

# node_31 =TreeNode_31()
# node_31.data = fnameAry_31[0]
# root_31 = node_31
# memory_31.append(node_31)

# dupNameAry_31 = []

# for name_31 in fnameAry_31[1:]:
#     node_31 = TreeNode_31()
#     node_31.data = name_31

#     current_31 = root_31
#     while True:
#         if name_31 == current_31.data:
#             dupNameAry_31.append(name_31)
#             break
#         if  name_31 < current_31.data:
#             if current_31.left_31 == None:
#                 current_31.left_31 = node_31
#                 memory_31.append(node_31)
#                 break
#             current_31 = current_31.left_31
#         else:
#             if current_31.right_31 == None:
#                 current_31.right_31 = node_31
#                 memory_31.append(node_31)
#                 break
#             current_31=current_31.right_31

# dupNameAry_31 = list(set(dupNameAry_31))

# print(folderName_31,"및 그 하위 디렉터리의 중복된 파일 목록 ->")
# print(dupNameAry_31)

# import random
# import math

# # 클래스와 함수 선언
# class Node_31():
#     def __init__(self):
#         self.data_31 =None
#         self.link_31 =None

# def printStores_31(start_31):
#     current_31 = start_31
#     if current_31 ==None:
#         return
    
#     while current_31.link_31 != head_31:
#         current_31 =current_31.link_31
#         x,y = current_31.data_31[1:]
#         print(storeName_31, "편의점, 거리: ", math.sqrt(x*x+y*y) )

# def makeStorelist_31(store_31):
#     global memory_31,head_31, current_31,pre_31
#     node_31 = Node_31()
#     node_31.data_31 = store_31
#     memory_31.append(node_31)

#     if head_31 ==None:
#         head_31 =node_31
#         node_31.link_31 = head_31
#         return

#     nodeX_31,nodeY_31 =node_31.data_31[1:]
#     nodeDist_31 = math.sqrt((nodeX_31*nodeX_31)+(nodeY_31*nodeY_31))
#     headX_31,headY_31 = head_31.data_31[1:]
#     headDist_31 = math.sqrt((headX_31*headX_31)+(headY_31*headY_31))
    
#     if headDist_31> nodeDist_31:
        
#         node_31.link_31 = head_31
#         last_31 = head_31
#         while last_31.link_31 != head_31:
#             last_31=last_31.link_31
#         last_31.link_31 = node_31
#         head_31 = node_31
#         return

#     current_31 = head_31
#     while current_31.link_31 != head_31:
#         pre_31 = current_31
#         current_31 = current_31.link_31
#         currX_31, currY_31 = current_31.data_31[1:]
#         currDist_31 = math.sqrt((currX_31*currX_31)+(currY_31*currY_31))
#         if currDist_31> nodeDist_31:
#             pre_31.link_31 = node_31
#             node_31.link_31 = current_31
#             return
    
#     current_31.link_31 =node_31
#     node_31.link_31 = head_31    
    


# # 변수 선언
# memory_31 =[]
# head_31,current_31,pre_31 =None,None,None

# # 메인함수
# if __name__ == '__main__':
#     storeAry_31 =[]
#     storeName_31 = 'A'
#     for i in range(10):
#         store_31 = (storeName_31,random.randint(1,100),random.randint(1,100))
#         storeAry_31.append(store_31)
#         storeName_31 = chr(ord(storeName_31)+1)

#     for store_31 in storeAry_31:
#         makeStorelist_31(store_31)

#     printStores_31(head_31)



# # 재귀 함수
# def sumValue(value):
#     if value <= 1:
#         return 1
#     retVal = sumValue(value-1)
#     print("{0} * {1}! = {2} 반환".format(value, value-1, retVal))
#     return value * retVal
    
# print(sumValue(5)) 

# 피보나치 재귀 함수
# def fibo(n):
#     if n ==0:
#         return 0
#     elif n ==1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
    
# print("피보나치 수 -->0 1 ", end = "")
# for i in range(2, 20):
#     print(fibo(i), end=" ")
# print()

# # 반복문 피보나치 수열 
# arr = []
# def fibo_for(n):
#     if n ==0:
#         arr.append(0)
#     elif n ==1:
#         arr.append(1)
#     else:
#         arr.append(arr[n-1]+arr[n-2])
#     return arr[n]
# print("피보나치 수 -->", end = "")
# for i in range(0, 20):
#     print(fibo_for(i), end=" ")


# #회문 판단기
# def palindrome(pstr):
#     if len(pstr)<=1:
#         return True

#     if pstr[0] !=pstr[-1]:
#         return False

#     return palindrome(pstr[1:-1])

# strAry = ["reaver", "kayak", "Borrow or rob", "주유소의 소유주"]

# if __name__=='__main__':
#     for teststr in strAry:
#         print(teststr,end="--> ")
#         teststr = teststr.lower().replace(" ","")
#         if palindrome(teststr):
#             print("O")
#         else:
#             print("x")

# # 원 그리기
# from tkinter import *
# window = Tk()
# window.title("fuck")
# canvas =Canvas(window,height = 1000, width = 1000,bg ='white')
# canvas.pack()

# x = 1000//2
# y = 1000//2
# r = 400
# canvas.create_oval(x-r,y-r,x+r,y+r,width = 2,outline = "black")
# window.mainloop()

# # 프랙탈그리기

# from tkinter import *
# def drawCircle(x,y,r):
#     global count
#     count += 1
#     canvas.create_oval(x-r,y-r,x+r,y+r,width = 2,outline = "black") 
#     canvas.create_text(x,y-r,text = str(count),font=(" ",30))
#     if r >= 100:
#         drawCircle(x-r//2,y,r//2)
#         drawCircle(x+r//2,y,r//2)


# count = 0
# wSize = 1000
# radius = 400

# window = Tk()
# canvas = Canvas(window,height = wSize, width = wSize,bg ='white')
# drawCircle(wSize//2,wSize//2,radius)

# canvas.pack()
# window.mainloop()

# 선택정렬
# def findMin(ary):
#     minindex = 0
#     for i in range(1,len(ary)):
#         if ary[minindex] >ary[i]:
#             minindex = i
#     return minindex

# testAry = [55,88,33,77]
# minPos = findMin(testAry)
# print("최솟값 -->",testAry[minPos] )

# def selectionSort(ary):
#     n = len(ary)
#     for i  in range(0,n-1):
#         minIdx = i
#         for k in range(i+1,n):
#             if ary[minIdx]> ary[k]:
#                 minIdx = k
#         tmp = ary[i]
#         ary[i] = ary[minIdx]
#         ary[minIdx] = tmp
#     return ary

# # 삽입정렬
# def findInsertIdx(ary, data):
#     findIdx = -1
#     for i in range(0, len(ary)):
#         if ary[i]>data:
#             findIdx = i
#             break
#     if findIndx == -1:
#         return len(ary)
#     else:
#         return findIdx

# dataAry = [188,162,168,12050,150,177,105]

# def insertionSort(ary):
#     n =len(ary)
#     for end in range(1,n):
#         for cur  in range(end, 0, -1):
#             if ary[cur-1] >ary[cur]:
#                 ary[cur-1],ary[cur] = ary[cur],ary[cur-1]
#     return ary

# dataAry = insertionSort(dataAry)
# print(dataAry)

# def selectionSort(ary):
#     n =len(ary)
#     for i in range(0,n-1):
#         minIdx = i
#         for k in range(1+i,n):
#             if ary[minIdx]>ary[k]:
#                 minIdx=k

#         ary[i],ary[minIdx] = ary[minIdx], ary[i]
#     return ary

# moneyAry = [7,5,11,6,9,80000,10,6,15,12]
# print(selectionSort(moneyAry))
# moneyAry.sort()
# print("중앙값 ->", moneyAry[len(moneyAry)//2])
# moneyAry.sort()
# a= sorted(moneyAry)
# print(a)


# 퀵정렬
# def quickSort(ary):

#     n=len(ary)
#     if n <=1:
#         return ary
#     pivot = ary[n//2]
#     leftAry,mindAry, rightAry = [],[],[]
    
#     for num in ary:
#         if num <pivot:
#             leftAry.append(num)
#         elif num >pivot:
#             rightAry.append(num)
#         else:
#             mindAry.append(num)

#     return quickSort(leftAry) +mindAry + quickSort(rightAry)

# dataAry = [120,120,188,150,168,50,50,162,105,120,177,50]


# dataAry = quickSort(dataAry)
# print(dataAry)


# 퀵 일반구현
# def qsort(arr,start,end):
#     if start >=end:
#         return

#     low= start
#     high = end
#     pivot = arr[(low+high)//2]
#     while low <= high:
#         while arr[low]<pivot:
#             low +=1
#         while arr[high]>pivot:
#             high -=1
#         if low <=high:
#             arr[low],arr[high]=  arr[high],arr[low]
#             low,high = low+1 , high -1

#     mid  = low
#     qsort(arr,start, mid-1)
#     qsort(arr, mid, end)

# def quickSort(ary):
#     qsort(ary, 0 ,len(ary)-1)

# dataAry=[120,120,188,150,168,50,50,162,105,120,177,50]

# quickSort(dataAry)
# print(dataAry)

# 퀵정렬 활용
# from tkinter import *
# from PIL import *
# window = Tk("이미지 출력")
# window.geometry("600x600")

# photo =Image.open( "C:\\Users\\강혁\\Desktop\\김정은.PNG")

# paper = Label(window, Image = photo)
# paper.pack(expand =1, anchor=CENTER)
# window.mainloop()

# 데이터의 순차 검색
# def seqSearch(ary,fData):
#     pos =-1
#     size =  len(ary)
#     print("비교한 데이터 -->",end="")
#     for i in range(size):
#         print(ary[i],end='')
#         if fData ==ary[i]:
#             pos = i
#             break
#     print()
#     return pos

# # 전역 변수 선언 부분
# dataAry = [188,150,168,162,105,120,177,50]
# findData = 0

# # 메인함수
# findData = int(input("찾을 값을 입력하세요 --> "))
# print("배열-->", dataAry)
# position =seqSearch(dataAry, findData)
# if position ==-1:
#     print(findData,"가 없네요")
# else:
#     print(findData,"는",position,"에 있습니다")

# # 이진검색
# def binSearch(ary,fData):
#     pos =-1
#     start = 0
#     end= len(ary) -1

#     while (start <= end):
#         mid = (start + end)//2
#         if fData ==ary[mid]:
#             return mid
#         elif fData> ary[mid]:
#             start = mid+1
#         else:
#             end = mid-1
#     return pos

# dataAry= [50,60,105,120,150,160,162,168,177,188]
# findData = 50

# print("ary -->", dataAry)
# position = binSearch(dataAry,findData)
# print(findData,"는", position,"에 위치한다")

# # 동적계획법 구현
# def knanpsack():
#     print("##메모리제이션 배열##")
#     array = [[0 for i in range(maxWeight+1)]for r in range(rowCount+1)]
#     for row in range(1, rowCount+1):
#         print(row,"개 -->", end=" ")
#         for col in range(1,maxWeight+1):
#             if weight[row]>col:
#                 array[row][col] = array[row-1][col]
#             else:
#                 value1 = money[row] + array[row-1][col-weight[row]]
#                 value2 = array[row-1][col]
#                 array[row][col] = max(value1, value2)
#             print("{}".format(array[row][col]), end=" ")
#         print()
#     return array[rowCount][maxWeight]


# maxWeight = 7
# rowCount= 4
# weight = [0,6,4,3,5]
# money = [0,13,8,6,12]

# maxValue = knanpsack()
# print()
# print("배낭에 담을 수 있는 보석의 최대 가격-->" , maxValue,"억원")

# # 동적 계획법 응용
# def growRich():
#     memo = [[0 for i in range(COL)]for r in range(ROW)]
#     memo[0][0] = golMaze[0][0]

#     rowSum = memo[0][0]
#     for i in range(1,ROW):
#         rowSum += golMaze[0][i]
#         memo[0][i] = rowSum
#     colSum = memo[0][0]
#     for i in range(1,COL):
#         colSum += golMaze[i][0]
#         memo[i][0] = colSum

#     for row in range(1,ROW):
#         for col in range(1,COL):
#             if memo[row][col-1] >memo[row-1][col]:
#                 memo[row][col]= memo[row][col-1]+golMaze[row][col]
#             else:
#                 memo[row][col]= memo[row-1][col]+golMaze[row][col]
#     return memo[ROW-1][COL-1]

# ROW,COL = 5,5
# golMaze = [
#           [1,4,4,2,2],
#           [1,3,3,0,5],
#           [1,2,4,3,0],
#           [3,3,0,4,2],
#           [1,3,4,5,3]]

# macoGold =growRich()
# # print("황금 미로에서 얻은 최대 황금 갯수 -->", macoGold)


# def qSort(arr, start, end):
#     if end <= start:
#         return
    
#     low = start
#     high = end

#     pivot =  arr[(low + high)//2]
#     while low <= high:
#         while arr[low] < pivot:
#             low += 1
#         while arr[high]> pivot:
#             high-= 1
#         if low <= high:
#             arr[low],arr[high] = arr[high],arr[low]
#             low,high = low +1, high-1
    
#     mid = low

#     qSort(arr, start, mid-1)
#     qSort(arr,mid, end)

# def quickSort(ary):
#     qSort(ary, 0 ,len(ary)-1)

# dataAry = [188, 150, 168, 162, 105, 120, 177, 50]

# print("정렬전 -->", dataAry)
# quickSort(dataAry)
# print("정렬후 -->", dataAry)

# # 피보나치 수열 재귀
# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+ fibo(n-2)
# print("0 1",end=" ")
# for  i in range(2, 10):
#     print(fibo(i), end= " ")

# 피보나치 수열 DP
def recu_fibo(n):
    global count_recu
    count_recu +=1
    if n<2:
        return 1
    else:
        return recu_fibo(n-1) + recu_fibo(n-2)

def dp_fibo(n):
    global count_dp
    memo = [1,1]
    if n<2:
        return memo[n]
    else:
        for i in range(2, n+1):
            memo.append(memo[i-1]+ memo[i-2])
            count_dp +=1
        return memo[n]
count_dp,count_recu = 0,0

print("30 번째 피보나치 수열")
res =recu_fibo(30)
print("재귀방식 --> 답: ",res ,", 반복수 : ", count_recu)
res = dp_fibo(30)
print("재귀방식 --> 답: ",res ,", 반복수 : ", count_dp)


