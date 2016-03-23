class node:
	n=None
	next_node = None
def insert(root, key):
	current = root
	while(current.next_node!=None):
		current = current.next_node
	current.next_node = node()
	current.next_node.n = key
head = node()
def reverse(current):
	if(current.next_node==None):
		global head
		head=current
		return current
	c = reverse(current.next_node)
	c.next_node = current
	return current
print "Please enter number of nodes you want to insert"
number_of_nodes = input()
for i in range(0,number_of_nodes):
	m = input()
	if(i==0):
		head.n=m;
	else:
		insert(head,m)
c= reverse(head)
c.next_node = None
current=head
while(1):
	print current.n,
	if(current.next_node==None):
		exit()
	current=current.next_node
