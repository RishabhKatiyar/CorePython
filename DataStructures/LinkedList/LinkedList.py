class Linked_List:

    class Node:
        item = None
        next = None

        def __init__(self, item):
            self.item = item

    def Create_Linked_List(self, args):
        start = self.Node(-1)
        ob = start

        for item in args:
            ob.next = self.Node(item)
            ob.next.next = None
            ob = ob.next

        return start.next

    def Reverse_List(self, node:Node):
        temp = node
        p = None
        p1 = None

        while temp != None:
            p1 = temp.next
            temp.next = p
            p = temp
            temp = p1

        return p

    def Print_List(self, node:Node):
        temp = node
        while temp != None:
            print(f'{temp.item} -> ', end='\t')
            temp = temp.next
        print('None')

if __name__ == '__main__':
    items = [1,2,3,4,5,6,7,8,9,10]
    
    ob = Linked_List()
    
    ll = ob.Create_Linked_List(items)
    ob.Print_List(ll)
    
    ll = ob.Reverse_List(ll)
    ob.Print_List(ll)
