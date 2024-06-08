class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def sorted_insert(sorted_head, new_node):
    if not sorted_head or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        sorted_head = new_node
    else:
        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    return sorted_head

def insertion_sort(head):
    sorted_head = None
    current = head
    while current:
        next_node = current.next
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    return sorted_head

def merge_sorted_lists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    if head1.data < head2.data:
        merged_head = head1
        merged_head.next = merge_sorted_lists(head1.next, head2)
    else:
        merged_head = head2
        merged_head.next = merge_sorted_lists(head1, head2.next)
    
    return merged_head

# Створюємо та заповнюємо однозв'язний список
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(2)
ll.append(5)
ll.append(4)

print("Original list:")
ll.print_list()

# Реверсуємо список
reversed_head = reverse_list(ll.head)
print("Reversed list:")
ll.head = reversed_head
ll.print_list()

# Сортуємо список
sorted_head = insertion_sort(ll.head)
print("Sorted list:")
ll.head = sorted_head
ll.print_list()

# Об'єднуємо два відсортовані списки
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

merged_head = merge_sorted_lists(ll1.head, ll2.head)
merged_list = LinkedList()
merged_list.head = merged_head

print("Merged sorted lists:")
merged_list.print_list()
