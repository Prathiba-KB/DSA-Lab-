class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head

        if self.head is None:
            print("List is Empty")
            return

        while temp:
            print(temp.data, "--->", end=" ")
            temp = temp.next

        print()

    def insert_begining(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_end(self, data):
        ne = Node(data)
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = ne

    def insert_position(self, pos, data):
        np = Node(data)
        temp = self.head

        for i in range(pos - 1):
            temp = temp.next

        np.next = temp.next
        temp.next = np

    def delete_beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_end(self):
        prev = self.head
        temp = self.head.next

        while temp.next is not None:
            temp = temp.next
            prev = prev.next

        prev.next = None

    def delete_position(self, pos):
        prev = self.head
        temp = self.head.next

        for i in range(pos - 1):
            temp = temp.next
            prev = prev.next

        prev.next = temp.next


obj = LL()

n1 = Node(10)
obj.head = n1

n2 = Node(20)
n1.next = n2

n3 = Node(30)
n2.next = n3

print("DISPLAY THE CREATED LIST .....")
obj.display()
