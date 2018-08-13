# class Node(object):
#     """结点类"""
#
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
#
# class SingleLinkList(object):
#     """单链表"""
#
#     def __init__(self, node=None):
#         self.__head = node
#
#     def is_empty(self):
#         """链表是否为空
#         :return 如果链表为空 返回真
#         """
#         return self.__head is None
#
#     def length(self):
#         """链表长度"""
#         cur = self.__head
#         count = 0
#         while cur is not None:
#             count += 1
#             cur = cur.next
#         return count
#
#     def travel(self):
#         """遍历整个链表"""
#         cur = self.__head
#         while cur is not None:
#             print(cur.item, end=" ")
#             cur = cur.next
#         print("")
#
#     def add(self, item):
#         """链表头部添加元素
#         :param item: 要保存的具体数据
#         """
#         node = Node(item)
#         node.next = self.__head
#         self.__head = node
#
#     def append(self, item):
#         """链表尾部添加元素"""
#         node = Node(item)
#         # 如果链表为空，需要特殊处理
#         if self.is_empty():
#             self.__head = node
#         else:
#             cur = self.__head
#             while cur.next is not None:
#                 cur = cur.next
#             # 退出循环的时候，cur指向的尾结点
#             cur.next = node
#
#     def insert(self, pos, item):
#         """指定位置添加元素"""
#         # 在头部添加元素
#         if pos <= 0:
#             self.add(item)
#         # 在尾部添加元素
#         elif pos >= self.length():
#             self.append(item)
#         else:
#             cur = self.__head
#             count = 0
#             while count < (pos - 1):
#                 count += 1
#                 cur = cur.next
#             # 退出循环的时候，cur指向pos的前一个位置
#             node = Node(item)
#             node.next = cur.next
#             cur.next = node
#
#     def remove(self,item):
#         """删除元素"""
#         cur = self.__head
#         pre = None
#         while cur != None:
#             if cur.item == item:
#                 if not pre:
#                     self.__head = cur.next
#                 else:
#                     pre.next = cur.next
#
#                 break
#             else:
#                 pre = cur
#                 cur = cur.next
#
#
#
#
# if __name__ == '__main__':
#     # s = SingleLinkList()
#     # s.append(1)
#     # s.append(2)
#     # s.append(4)
#     # s.append(2)
#     # s.travel()
#
#     list_a = [("a",100,20),("x",20)]
#     print({key[0]:[i for i in key[1:]] for key in list_a})
#



#
#
#
# class Stack(object):
#     """栈"""
#     def __init__(self):
#         # self.__items = SingleLinkList()
#         self.__items = []
#
#     def push(self, item):
#         """添加一个新元素item到栈顶"""
#         self.__items.append(item)
#         # self.__items.insert(0,item)
#
#     def pop(self):
#         """弹出栈顶栈顶元素"""
#         self.__items.pop()
#         # self.__items.pop(0)
#
#     def peek(self):
#         """返回栈顶元素"""
#         return self.__items[-1]
#
#     def is_empty(self):
#         """判断栈是否为空"""
#         return self.__items == []
#
#     def size(self):
#         """返回栈的元素个数"""
#         return len(self.__items)
#
#
#

#
# class Stack(object):
#     """队列"""
#     def __init__(self):
#         # self.__items = SingleLinkList()
#         self.__items = []
#
#     def push(self, item):
#         """添加一个新元素item到栈顶"""
#         self.__items.append(item)
#         # self.__items.insert(0,item)
#
#     def pop(self):
#         """弹出栈顶栈尾元素"""
#         # self.__items.pop()
#         self.__items.pop(0)
#
#     def peek(self):
#         """返回栈尾元素"""
#         return self.__items[0]
#
#     def is_empty(self):
#         """判断栈是否为空"""
#         return self.__items == []
#
#
#     def size(self):
#         """返回栈的元素个数"""
#         return len(self.__items)
#
#
#
#

# def bubble_sort(alist):
#     """冒泡排序"""
#     n = len(alist)
#     for j in range(n-1):
#         count = 0
#         for i in range(n-1-j):
#             if alist[i].lower() > alist[i+1].lower():
#                 alist[i],alist[i+1] = alist[i+1],alist[i]
#                 count += 1
#         if 0 == count:
#             break


# if __name__ == '__main__':
#     li = ["xyz","XYZ","abd","ABc","xya"]
#     bubble_sort(li)
#     print(li)


# def select_sort(aList):
#     """选择排序"""
#
#     n = len(aList)
#     for j in range(n-1):
#         min_index = j
#         for i in range(j+1,n):
#             if aList[i] < aList[min_index]:
#                 min_index = i
#         if j != min_index:
#             aList[j], aList[min_index] = aList[min_index],aList[j]
#
#
# if __name__ == '__main__':
#     li = [42,54,23,56,75,123,34,1,13]
#     select_sort(li)
#     print(li)

#
# def insert_sort(aList):
#     """插入排序"""
#     n = len(aList)
#     for j in range(1,n):
#         for i in range(j,0,-1):
#             if aList[i] < aList[i-1]:
#                 aList[i], aList[i-1] = aList[i-1], aList[i]
#             else:
#                 break
#
# if __name__ == '__main__':
#     li = [42,54,23,56,75,123,34,1,13]
#     insert_sort(li)
#     print(li)
#
#

#
# def shell_sort(aList):
#     n = len(aList)
#     gap = n//2
#     print(gap)
#     while gap>0:
#         for i in range(gap,n):
#             j = i
#             while j>=gap and aList[j-gap] > aList[j]:
#                 aList[j-gap],aList[j] = aList[j],aList[j-gap]
#                 j -= gap
#
#         gap = gap // 2
#
#
#
# if __name__ == '__main__':
#     li = [42,54,23,56,75,123,34,1,22,42]
#     shell_sort(li)
#     print(li)


# def quick_sort(aList,start,end):
#     if start >= end:
#         return
#
#     # 起始元素为基准元素
#     mid = aList[start]
#
#     low = start
#     high = end
#
#     while low < high:
#         while low < high and aList[high] >= mid:
#             high -= 1
#         while low < high and aList[low] < mid:
#             low += 1
#         aList[high],aList[low] = aList[low],aList[high]
#
#     aList[low] = mid
#
#     quick_sort(aList,start,low-1)
#     quick_sort(aList,low+1,end)
#
#
# if __name__ == '__main__':
#     li = [42,54,23,56,75,123,34,1,22,42]
#     quick_sort(li,0,9)
#     print(li)


# def merge_sort(aList):
#     """归并排序"""
#     n = len(aList)
#     if 1 == n:
#         return aList
#
#     mid = n//2
#     left_sorted_li = merge_sort(aList[:mid])
#
#     right_sorted_li = merge_sort(aList[mid:])
#
#     left,right = 0,0
#     merge_sorted_li = []
#
#     left_n = len(left_sorted_li)
#     right_n = len(right_sorted_li)
#
#     while left < left_n and right < right_n:
#         if left_sorted_li[left] <= right_sorted_li[right]:
#             merge_sorted_li.append(left_sorted_li[left])
#             left += 1
#         else:
#             merge_sorted_li.append(right_sorted_li[right])
#             right += 1
#
#     merge_sorted_li += left_sorted_li[left:]
#     merge_sorted_li += right_sorted_li[right:]
#
#     return merge_sorted_li
#
#
#
# if __name__ == '__main__':
#     li = [42,54,23,56,75,123,34,1,22,42]
#     new_li = merge_sort(li)
#     print(li)
#     print(new_li)
#
#
#

# def binary_search(aList,item):
#     n = len(aList)
#     if n == 0:
#         return False
#
#     midpoint = len(aList) // 2
#     if aList[midpoint] == item:
#         return True
#     elif aList[midpoint] < item:
#         return binary_search(aList[:midpoint],item)
#     else:
#         return binary_search(aList[midpoint+1:],item)
#
#
#
# if __name__ == '__main__':
#     li = [42,54,23,56,75,123,34,1,22,42]
#     print(binary_search(li, 123))
#     print(50*0.9225)
#
#
#
# class Node(object):
#     """结点类"""
#     def __init__(self,item):
#         self.item = item
#         self.lchild = None
#         self.rchild = None
#
#
# class BinaryTree(object):
#     """二叉树"""
#     def __init__(self, node=None):
#         self.root = node
#
#     def add(self, item):
#         """
#         广度优先遍历方式添加结点
#         :param item:
#         :return:
#         """
#
#         if self.root is None:
#             self.root = Node(item)
#         else:
#             queue = []
#             queue.append(self.root)
#
#             while len(queue) > 0:
#                 node = queue.pop(0)
#                 if not node.lchild:
#                     node.lchild = Node(item)
#                     return
#                 else:
#                     queue.append(node.lchild)
#                 if not node.rchild:
#                     node.rchild = Node(item)
#                     return
#                 else:
#                     queue.append(node.rchild)
#
#
#     def breadh_travel(self):
#         """广度优先遍历"""
#         if self.root is None:
#             return
#
#         queue = []
#         queue.append(self.root)
#
#         while len(queue) > 0:
#             node = queue.pop(0)
#             print(node.item, end=" ")
#             if node.lchild:
#                 queue.append(node.lchild)
#
#             if node.rchild:
#                 queue.append(node.rchild)
#
#     def preorder_travel(self, root):
#         """先序"""
#         if root:
#             print(root.item, end=" ")
#             self.preorder_travel(root.lchild)
#             self.preorder_travel(root.rchild)
#
#     def inorder_travel(self, root):
#         """中序"""
#         if root:
#             self.inorder_travel(root.lchild)
#             print(root.item, end=" ")
#             self.inorder_travel(root.rchild)
#
#     def order_travel(self, root):
#         """后序"""
#         if root:
#             self.inorder_travel(root.lchild)
#             print(root.item, end=" ")
#             self.inorder_travel(root.rchild)


# class Node(object):
#
#     def __init__(self, item):
#         self.root = item
#         self.lchild = None
#         self.rchild = None
#
# class BinaryTree(object):
#     def __init__(self,root=None):
#         self.root = root
#
#
#     def add(self, item):
#         if self.root is not None:
#             self.root = Node(item)
#         else:
#             queue = []
#             queue.append(self.root)
#
#             while len(queue) > 0:
#                 node =  queue.pop(0)
#                 if not
#


# if __name__ == '__main__':
#     tree = BinaryTree()
#     tree.add(0)
#     tree.add(1)
#     tree.add(2)
#     tree.add(3)
#     tree.add(4)
#     tree.add(5)
#     tree.add(6)
#     tree.add(7)
#     tree.add(8)
#     tree.add(9)
#     tree.breadh_travel()
#     print("")
#     tree.preorder_travel(tree.root)
#



#
# def bubble_sort(alist):
#     """冒泡排序"""
#     n = len(alist)
#     for j in range(n-1):
#         count = 0
#         for i in range(n-1-j):
#             if alist[i] > alist[i+1]:
#                 alist[i],alist[i+1] = alist[i+1],alist[i]
#                 count += 1
#         if 0 == count:
#             break
# if __name__ == '__main__':
#     yusuan = int(input("预算:"))
#     li = input("单价:")
#     li = li.split(" ")
#     li = [int(i) for i in li]
#     bubble_sort(li)
#     price = 0
#     for i in range(len(li)):
#         if price+li[i] <= yusuan:
#             price += li[i]
#
#     print(price)


# def test1():
#     data = input("请输入")
#     data_list = data.split(" ")
#     data_list2 = []
#     for i in data_list:
#         try:
#             datas = int(i)
#             data_list2.append(datas)
#         except:
#             data_list2.append(i)
#
#     n = len(data_list2)
#     for i in range(n-1):
#         for j in range(0,n-1):
#             x = 1
#             while True:
#                 try:
#                     if type(data_list2[i]) == type(data_list2[i+x]):
#                         if data_list2[i] > data_list2[i+x]:
#                             data_list2[i],data_list2[i+x] = data_list2[i+x],data_list2[i]
#                             break
#                 except:
#                     break
#                 x += 1
#
#     for i in data_list2:
#         print(i,end=" "
#
# test1()

# import requests
#
# url = "http://lscs.service.zhangyoubao.com/service/rest?api=news.getposts&game=lscs&userId=0&platformVersion=206020"
# headers = {"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1; vivo V3M A Build/LMY47I) anzogame supportAnzogameSdk 2016 lscs 206020",
#            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#             "Host": "lscs.service.zhangyoubao.com",
#             "Connection": "Keep-Alive",
#             "Accept-Encoding": "gzip",
#             "Content-Length": "383"}
#
# data = {"check_timestamp":1534094114}
#
# response = requests.get(url=url,headers=headers)
# html = response.content.decode()
# print(html)

# def select_sort(aList):
#     """选择排序"""
#
#     n = len(aList)
#     for j in range(n-1):
#         min_index = j
#         for i in range(j+1,n):
#             if aList[i] < aList[min_index]:
#                 min_index = i
#         if j != min_index:
#             aList[j], aList[min_index] = aList[min_index],aList[j]



def sort(aList):
    n = len(aList)
    for j in range(n-1):
        min_index = j
        for i in range(j+1,n):
            if aList[i] > aList[min_index]:
                aList[i],aList[min_index] = aList[min_index],aList[i]
                print(min_index)

if __name__ == '__main__':
    a = [(0, 0.35), (2, 0.45), (5, 0.67),(2, 0.23),(3,0.35),(6,0.78)]
    li = [i[1] for i in a]
    sort(li)
    print(li)



