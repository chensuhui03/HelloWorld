class Node: 
    def __init__(self, d, n):
        self._data = d
        self._next = n
    
    def print(self):
        if (self._next == None):
            print(self._data)
        else:
            print(self._data, self._next)
    
    def set_next(self, next):
        self._next = next

node1 = Node(3, None) 
node2 = Node(2, None)
node1.set_next(node2)
node3 = Node(4, None)
node2.set_next(node3)


node4 = node1

node1.print()
node2.print()
node2_add = id(node2)
print(hex(node2_add))


#print(node1._data, node1._next_node)


def traverse(head):
    node = head
    while (node != None):
        node.print()
        node = node._next

def get_linked_list_len(head):
    node = head
    i = 0
    while (node != None):
        i = i + 1
        node = node._next
    print("Length of linked list is ", i)



# traverse(node1)
get_linked_list_len(node1)

def f_p(n, start):
    if n == 0:
        #print(1)
        if (n == start):
            print(1)
        return 1
        
    if n == 1:
        #print(1)
        if (n == start):
            print(1)
        return 1
    res = f_p(n-1, start) + f_p(n-2, start)
    if (n == start):
        print(res)
    #print(f(n-1) + f(n-2))
    return res
def f(n):
    return f_p(n, n)
f(4)


def sum(n):
    if n == 1:
        return 1

    previous = sum(n-1)

    result = n + previous
    return result
sum(5)
