# https://leetcode.com/problems/middle-of-the-linked-list/description/

def middlenode(head):
    size = 0
    if (head):
        current_node = head
        while (current_node):
            size = size + 1
            current_node = current_node.next
        middl = int(size / 2)
        while middl:
            head = head.next
            middl -= 1
        return head