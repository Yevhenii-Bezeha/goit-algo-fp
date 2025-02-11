class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self, head):
        if not head or not head.next:
            return head
        mid = self.get_middle(head)
        left = head
        right = mid.next
        mid.next = None
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return self.merge(left, right)

    def get_middle(self, head):
        if not head:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left.data < right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result

    def sort(self):
        self.head = self.merge_sort(self.head)

    @staticmethod
    def merge_sorted_lists(l1, l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

# Example usage
ll = LinkedList()
ll.append(4)
ll.append(2)
ll.append(7)
ll.append(1)
ll.append(5)

print("Original list:")
ll.print_list()

ll.reverse()
print("Reversed list:")
ll.print_list()

ll.sort()
print("Sorted list:")
ll.print_list()

# Merging two sorted lists
ll1 = LinkedList()
ll2 = LinkedList()
for num in [1, 3, 5]:
    ll1.append(num)
for num in [2, 4, 6]:
    ll2.append(num)

merged_head = LinkedList.merge_sorted_lists(ll1.head, ll2.head)
merged_list = LinkedList()
merged_list.head = merged_head
print("Merged sorted list:")
merged_list.print_list()
