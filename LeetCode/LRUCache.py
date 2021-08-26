class LRUCache:
    doubly_Linked_list = None
    node_dictionary = {}

    def __init__(self, capacity: int):
        self.doubly_Linked_list = None
        self.doubly_Linked_list = DoublyLinkedList(capacity)        
        self.node_dictionary = {}

    def get(self, key: int) -> int:
        if key in self.node_dictionary:
            val = self.node_dictionary[key]
            value = val[0]
            node = val[1]
            self.doubly_Linked_list.delete(node)
            node = Node(key)
            self.doubly_Linked_list.insert(node)
            self.node_dictionary[key] = (value, node)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.node_dictionary:
            val = self.node_dictionary[key]
            node = val[1]
            self.doubly_Linked_list.delete(node)
            node = Node(key)
            self.doubly_Linked_list.insert(node)
            self.node_dictionary[key] = (value, node)
        else:   
            node = Node(key)
            self.node_dictionary[key] = (value, node)
            key = self.doubly_Linked_list.insert(node)
            if key != -1:
                del self.node_dictionary[key]

class Node:
    key = None
    next = None
    previous = None

    def __init__(self, key) -> None:
        self.key = key
        self.next = None
        self.previous = None

    def __str__(self) -> str:
        address_of_next = id(self.next)
        address_of_previous = id(self.previous)
        address  = id(self)
        return (f"Data = {self.key} address = {address}  next = {address_of_next} previous = {address_of_previous}")
        
class DoublyLinkedList:
    start = None
    end = None
    capacity = 0
    occupied = 0
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.occupied = 0
        self.start = None
        self.end = None

    def __str__(self) -> str:
        result = ""
        temp = self.start
        while temp != None:
            result += str(temp) + " -> \n"
            temp = temp.next
        return result 

    def insert(self, node) -> int:
        key = -1
        if self.occupied < self.capacity: 
            self.occupied += 1   
            if self.start == None:
                self.start = node
                self.end = node

            elif self.start == self.end:
                self.start.next = node
                self.end = node
                self.end.previous = self.start
            
            else:
                self.end.next = node
                self.end.next.previous = self.end
                self.end = self.end.next
        else:
            key = self.start.key
            if self.start == self.end:
                self.start = node
                self.end = node
            else:
                self.start = self.start.next
                self.start.previous = None

                self.end.next = node
                self.end.next.previous = self.end
                self.end = self.end.next
        return key

    def delete(self, node: Node):
        if self.occupied > 0:
            if self.start == self.end:
                self.start = None
                self.end = None
            elif node == self.start:
                self.start = self.start.next
                self.start.previous = None
            elif node == self.end:
                self.end = self.end.previous
                self.end.next = None
            else:
                previous = node.previous
                next = node.next
                previous.next = next
                next.previous = previous
            self.occupied -= 1    


obj = LRUCache(1)
obj.put(2, 1)
obj.get(2)
obj.put(3, 2)
obj.get(2)
obj.get(3)

print(obj.doubly_Linked_list)
for item in obj.node_dictionary:
    val = obj.node_dictionary[item]
    print(val[0], end = "  ")
    print(val[1], end = "  ")
    print()