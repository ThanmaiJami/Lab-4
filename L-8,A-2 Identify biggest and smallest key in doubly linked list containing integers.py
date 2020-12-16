#Identify the biggest and smallest key in a doubly linked list containing integers.
class node:
	def _init_(self,data):
		self.data = data
		self.prev = None
		self.next = None
class LinkedList:
	def _init_(self):
		self.head = None
	def display(self):
		ele = []
		cur = self.head
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print("Doubly LinkedList: ",ele)
	def maxandminNodes(self):
		cur = self.head
		large = self.head.data
		small = self.head.data
		while cur:
			if cur.data > large:
				large = cur.data

			if cur.data < small:
				small = cur.data

			cur = cur.next
		print("Largest element is: ",large)
		print("Smallest node is: ",small)
DLL = LinkedList()
DLL.head = node(10) # head ==> 10
DLL.head.next = node(20) # 10 --> 20
DLL.head.next.next = node(30) # 10 --> 20 --> 30
DLL.display()
DLL.maxandminNodes()
