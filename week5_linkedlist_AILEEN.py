# linked list assignment - week 5
# basically a chain of nodes that point to each other

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # points to the next node, none if its the last one


class SinglyLinkedList:

    def __init__(self):
        self.head = None  # empty list to start
        self.count = 0


    # adds to the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node  # if list is empty this becomes the first node
        else:
            current = self.head
            while current.next:  # walk till the last node
                current = current.next
            current.next = new_node  # attach at the end

        self.count += 1


    # adds to the front
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  # new node points to old head
        self.head = new_node
        self.count += 1


    # insert at any position, 0 = front, 1 = second, etc
    def insert_at_position(self, data, pos):

        if pos < 0 or pos > self.count:
            print(f"position {pos} is out of range")
            return

        if pos == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head

        # stop one node before the target position
        for i in range(pos - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.count += 1


    # deletes the first node that matches the value
    def delete_by_value(self, value):

        if self.head is None:
            print("list is empty")
            return

        # if its the head node
        if self.head.data == value:
            self.head = self.head.next
            self.count -= 1
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next  # skip over it
                self.count -= 1
                return
            current = current.next

        print(f"{value} not found")


    # returns index of value or -1 if not found
    def search(self, value):
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1

        return -1


    # prints the whole list
    def display(self):
        if self.head is None:
            print("empty list")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    def is_empty(self):
        return self.head is None


    def size(self):
        return self.count


# ------- tests -------

print("test 1 - append")
ll = SinglyLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()                   # 10 -> 20 -> 30 -> None
print("size:", ll.size())      # 3


print("\ntest 2 - prepend")
ll.prepend(5)
ll.display()                   # 5 -> 10 -> 20 -> 30 -> None


print("\ntest 3 - insert at position")
ll.insert_at_position(15, 2)
ll.display()                   # 5 -> 10 -> 15 -> 20 -> 30 -> None


print("\ntest 4 - search")
print(ll.search(15))           # 2
print(ll.search(99))           # -1


print("\ntest 5 - delete")
ll.delete_by_value(15)
ll.display()                   # 5 -> 10 -> 20 -> 30 -> None
ll.delete_by_value(99)         # not found
