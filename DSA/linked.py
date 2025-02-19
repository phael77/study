class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_end(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_value

    def remove_from_end(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_value

dll = DoublyLinkedList()

import unittest

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()
    
    def test_add_to_front(self):
        self.dll.add_to_front(10)
        self.assertEqual(self.dll.head.value, 10)
        self.assertEqual(self.dll.tail.value, 10)
        
        self.dll.add_to_front(20)
        self.assertEqual(self.dll.head.value, 20)
        self.assertEqual(self.dll.head.next.value, 10)
        self.assertEqual(self.dll.tail.value, 10)
    
    def test_add_to_end(self):
        self.dll.add_to_end(10)
        self.assertEqual(self.dll.head.value, 10)
        self.assertEqual(self.dll.tail.value, 10)
        
        self.dll.add_to_end(20)
        self.assertEqual(self.dll.tail.value, 20)
        self.assertEqual(self.dll.tail.prev.value, 10)
        self.assertEqual(self.dll.head.value, 10)
    
    def test_remove_from_front(self):
        self.dll.add_to_front(10)
        self.dll.add_to_front(20)
        removed = self.dll.remove_from_front()
        self.assertEqual(removed, 20)
        self.assertEqual(self.dll.head.value, 10)
        
        removed = self.dll.remove_from_front()
        self.assertEqual(removed, 10)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
    
    def test_remove_from_end(self):
        self.dll.add_to_end(10)
        self.dll.add_to_end(20)
        removed = self.dll.remove_from_end()
        self.assertEqual(removed, 20)
        self.assertEqual(self.dll.tail.value, 10)
        
        removed = self.dll.remove_from_end()
        self.assertEqual(removed, 10)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
    
    def test_remove_from_empty_list(self):
        self.assertIsNone(self.dll.remove_from_front())
        self.assertIsNone(self.dll.remove_from_end())

if __name__ == "__main__":
    unittest.main()
