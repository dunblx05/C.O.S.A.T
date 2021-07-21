# 이진트리를 생성해서 풀어보자

# import sys
# num  = int(sys.stdin.readline())
# numList =[]
# result = 0
# res = ""
# class TreeNode():
#     def __init__(self):
#         self.left =res+"4"
#         self.data = None
#         self.right = res+"7"
# node = TreeNode()

# def make(n):
#     node = TreeNode()
#     node.data = res
#     root = node
#     numList.append(node)
#     for i in range(num+1):
#         node =TreeNode()
#         node.data =res
#         current = root
#         while n<num:
#             if current.left ==res+"4":
#                 current.left =node
#                 break
#             current = current.left
#             n+=1
#         else:
#             if current.right ==res+"7":
#                 current.right =node
#                 break
#             current = current.right
#             n+=1
#     return res
# print(make(num))
    
# def dfs(i):
#     global numList, res

#     if i ==num: 
#         return numList[num-1].sort()

#     else:
#         if :
#             res += "4"
#             numList.append(res) 
#             make(i+1)
#         if numList[i-2]> numList[i]-1:
#             res += "7"
#             numList.append(res) 
#             make(i+1)

# print(result)

# 이진법 풀이
import sys
num = int(sys.stdin.readline())
bir = format(bin(num+1)[3:])
for i in bir:
    if i=="0":
        print(4,end = "")
    elif  i=="1":
        print(7,end ="")    


