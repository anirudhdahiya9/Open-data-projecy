import random

class Node:
	"""Node CLass"""

	def __init__(self,data):
		"""Constructor"""
		self.nextNode=None;
		self.data=data;

class LinkList(Node):
	"""LinkList Class"""

	def __init__(self,data):
		"""Constructor"""
		Node.__init__(self,data);#calls the constructor of Node Class
	
	def insert(self,data):
		if not self.nextNode:
			self.nextNode=LinkList(data);
			return;
		self.nextNode.insert(data);
		return;
	
#Printing normally
	def printList(self):
		current=self;
		while current.nextNode:
			print current.data,;
			current=current.nextNode;
		print current.data;
	
#Printing recurrsively
	def printListRecurrsive(self):
		current=self;
		if current.nextNode:
			print current.data,;
			current.nextNode.printListRecurrsive();
		else:
			print current.data;
			
#Reversing normally
	def reverseList(self):
		current=self;
		previous=None;
		while current.nextNode:
			temp=current.nextNode;
			current.nextNode=previous;
			previous=current;
			current=temp;
		current.nextNode=previous;
		return current;

#Reversing recurrsively
	def reverseListRecurrsive(self,previous):
		current=self;
		if current.nextNode:
			temp=current.nextNode;
			current.nextNode=previous;
			previous=current;
			return temp.reverseListRecurrsive(current);
		else:
			current.nextNode=previous;
			return current;

if __name__ == "__main__":
	linkList=LinkList(2);
	listLen=random.randint(3,40);
	for i in range(1,listLen):
		i=random.randrange(i);
		linkList.insert(i);
	print "Inital Link List";
	linkList.printList();
#Reversing and printing normally
	print "Link List after reversing";
	linkList=linkList.reverseList();
	linkList.printList();

#Reversing and printing recurrsively
	print "Link List after reversing again";
	linkList=linkList.reverseListRecurrsive(None);
	linkList.printListRecurrsive();
