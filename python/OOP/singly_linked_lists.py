class SList:
  def __init__(self):
    self.head = None
  def add_to_front(self, val):	# added this line, takes a value
     new_node = Node(val)	# create a new instance of our Node class using the given value
     current_head = self.head	# save the current head in a variable
     new_node.next = current_head	# SET the new node's next TO the list's current head
     self.head = new_node	# SET the list's head TO the node we created in the last step
     return self	                # return self to allow for chaining
  def print_values(self):
  	runner = self.head	# a pointer to the list's first node
  	while (runner != None):	# iterating while runner is a node and not None
  		print(runner.value)	# print the current node's value
  		runner = runner.next 	# set the runner to its neighbor
  	return self	                # once the loop is done, return self to allow for chaining
  def add_to_back(self, val):	# accepts a value
    if self.head == None:	# if the list is empty
    	self.add_to_front(val)	# run the add_to_front method
    	return self	# let's make sure the rest of this function doesn't happen if we add to the front

    new_node = Node(val)	# create a new instance of our Node class with the given value
    runner = self.head	    # set an iterator to start at the front of the list
    while (runner.next != None):	# iterator until the iterator doesn't have a neighbor
    	runner = runner.next # increment the runner to the next node in the list
    runner.next = new_node	# increment the runner to the next node in the list
    return self
  def remove_from_front(self):
  	runner = self.head
  	self.head = runner.next
  	runner = runner.next
  	while(runner.next != None):
  		runner.next = runner.next
  		runner = runner.next
  	return self
  def remove_from_back(self):
  	runner = self.head
  	count = 0
  	while(runner.next != None):
  		count += 1
  		runner = runner.next
  	runner = self.head
  	while(count - 1 > 0):
  		runner = runner.next
  		count -= 1
  	runner.next = None
  	return self
  def remove_val(self, val):
  	runner = self.head
  	match = False
  	while(runner.next != None):
  		if(runner.value == val):
  			match = True
  			break
  		else:
  			runner = runner.next
  	if(match):
  		runner = None
  	return self
  def insert_at(self, val, n):
  	runner = self.head
  	count = 0

  	while(count != n):
  		runner = runner.next
  		count += 1

  	insert_node = Node(val)
  	insert_node.next = runner
  	
  	count = 0
  	runner = self.head
  	
  	while(count != n-1):
  		runner = runner.next
  		count += 1 

  	runner.next = insert_node	

  	return self	

class Node:
	def __init__(self, val):
	  self.value = val
	  self.next = None

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_front("Python is a powerful language.").add_to_back("fun!").print_values()    # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!

my_list.insert_at("Inserting here.", 2).print_values()