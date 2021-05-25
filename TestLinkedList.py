#  File: TestLinkedList.py

#  Description: Tests the functionality of a linked list.

class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        current = self.first

        # 0 nodes in linked list
        if current.data is None:
            return 0

        # 1 node in linked list
        elif current.next is None:
            return 1

        # start count at 1 for first node and increase with each node
        count = 1
        while current.next is not None:
            current = current.next
            count += 1
        return count

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)

        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)

        # find the last link
        current = self.first
        if (current == None):
            self.first = new_link
            return
        while (current.next != None):
            current = current.next
        current.next = new_link

    # add an item in an ordered list in ascending order
    def insert_in_order(self, data):
        new_link = Link(data)

        current = self.first
        previous = self.first

        # if first node is empty or larger than data, insert data
        if (current == None) or (data <= current.data):
            new_link.next = self.first
            self.first = new_link
            return

        # if data input is larger than node, increase node
        # else, insert data into list
        while (current.next != None):
            if current.data <= data:
                previous = current
                current = current.next
            else:
                new_link.next = previous.next
                previous.next = new_link
                return

        # check the final value of the linked list
        if current.data <= data:
            current.next = new_link
        else:
            new_link.next = previous.next
            previous.next = new_link
        return

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first

        # check for empty list
        if (current.data is None):
            return None
        while current.data != data:
            # end of the linked list
            if current.next is None:
                return None
            current = current.next
        return current.data

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first

        # check for empty list
        if (current.data is None):
            return None

        # return number if found and None if the current node
        # is larger than the data
        while current.next is not None:
            if current.data == data:
                return current.data
            elif current.data > data:
                return None
            current = current.next

        # check last node
        if current.data == data:
            return current.data
        return None

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first

        # check for empty node
        if (current == None):
            return None

        # return none of node not found, remove it found
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next
        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next
        return current

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
            current = self.first
            linked_list = ""
            i = 0 # counter for each line
            while (current != None):
                linked_list += str(current.data) + "  "
                current = current.next
                i += 1
                if (i != 0) and (i % 10 == 0):
                    linked_list +='\n' # for correct output
            return linked_list

    # Copy the contents of a list and return new list
    def copy_list(self):
        new_linked_list = LinkedList() # create empty linked list
        current = self.first

        # insert each node of linked list into empty linked list
        # by appending each integer and return new linked list
        while current != None:
            new_linked_list.insert_last(current.data)
            current = current.next
        return new_linked_list

    # Reverse the contents of a list and return new list
    def reverse_list(self):
        new_linked_list = LinkedList()
        current = self.first

        # insert each node of linked list into empty linked list
        # by prepending each integer and return new linked list
        while current != None:
            new_linked_list.insert_first(current.data)
            current = current.next
        return new_linked_list

    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        new_linked_list = LinkedList()
        current = self.first

        # insert each node of linked list into empty linked list
        # in order and return new sorted linked list
        while current is not None:
            new_linked_list.insert_in_order(current.data)
            current = current.next
        return new_linked_list


    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        previous = self.first
        current = previous.next

        # Check that each node starting from 2 to n is larger than
        # its proceeding node.
        while current is not None:
            if previous.data <= current.data:
                current = current.next
                previous = previous.next
            else:
                return False
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        current = self.first
        if current is None:
            return True
        return False

    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        current1 = self.first
        current2 = other.first
        new_linked_list = LinkedList()

        # add elements into empty linked list in sorted order until
        # one of the sorted lists reaches the end
        while (current1 is not None) and (current2 is not None):
            if current1.data > current2.data:
                new_linked_list.insert_last(current2.data)
                current2 = current2.next
            elif current1.data <= current2.data:
                new_linked_list.insert_last(current1.data)
                current1 = current1.next

        # if list 2 reached the end but list 1 ddidnt, add
        # the remaining nodes of list 1 into the new linked list
        while current1 is not None:
            new_linked_list.insert_last(current1.data)
            current1 = current1.next

        # if list 1 reached the end but list 2 didn't, add
        # the remaining nodes of list 2 into the new linked list
        while current2 is not None:
            new_linked_list.insert_last(current2.data)
            current2 = current2.next
        return new_linked_list

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        current1 = self.first
        current2 = other.first
        if (current1 is None) and (current2 is None): # empty lists are equal
            return True
        elif (current1 is None) or (current2 is None): # one empty list means not equal
            return False

        # return false when elements are equal
        while (current1 is not None) and (current2 is not None):
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next

        # check that the linked lists are of the same length
        if (current1 is None) and (current2 is None):
            return True
        return False

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        current = self.first
        new_linked_list = LinkedList()
        occur = []
        while current is not None:
            if current.data in occur: # if node is in occur, do nothing and move to next node
                current = current.next
            else:
                occur.append(current.data) # add elements that are added to linked list to occur
                new_linked_list.insert_last(current.data)
                current = current.next
        return new_linked_list

    def rotate (self, k):
        current = self.first
        size = 1
        while current != None:
            size += 1
            current = current.next
        no_rotate = size - k
        newList = LinkedList()
        for i in range (no_rotate):
            newList.insert_last(current)
        while k > 0:
            current = self.first
            while current.next != None:
                current = current.next
            newList.insert_first(current)
            self.delete_link(current)
            k -= 1
        return newList



def main():


# Test methods insert_first() and __str__() by adding more than
# 10 items to a list and printing it.
    test = [1,2,3,4,5]
    a = LinkedList()
    for i in test:
        a.insert_last(i)
    print(a)
    c = a.rotate(2)
    print(c)
    print(a)

    print()




    print("Test Insert First")
    testList_insertf = [63, 28, 96, 41, 12, 29, 88, 56, 73, 22, 91, 94, 12]

    linked_list_insertf = LinkedList()
    for data in testList_insertf:
        linked_list_insertf.insert_first(data) # prints reversed order
    print(linked_list_insertf)
    print()

# Test method insert_last()
    print("Test Insert Last")
    testList_insertl = [63, 28, 96, 41, 15, 29, 88, 56, 73, 22, 91, 94, 12]

    linked_list_insertl = LinkedList()
    for data in testList_insertl:
        linked_list_insertl.insert_last(data) # prints the same order
    print(linked_list_insertl)
    print()

# Test method insert_in_order()
    print("Test Insert In Ascending Order")
    testList_insord = [63, 28, 96, 41, 15, 29, 88, 56, 73, 22, 91, 94, 12]

    linked_list_insord = LinkedList()
    for data in testList_insord:
        linked_list_insord.insert_in_order(data) # prints in ascending order
    print(linked_list_insord)
    print()

# Test method get_num_links()
    print("Test Get Number of Links")
    print(linked_list_insertl.get_num_links())
    print()

# Test method find_unordered()
# Consider two cases - data is there, data is not there
    print("Test Find Unordered")
    testList_finduns = [75, 23, 90, 14, 68, 12, 54, 37, 21, 88, 84, 31]
    linked_list_finduns = LinkedList()

    for data in testList_finduns:
        linked_list_finduns.insert_first(data)
    print(linked_list_finduns.find_unordered(14)) # int in linked list
    print(linked_list_finduns.find_unordered(73)) # int not in linked list
    print()


# Test method find_ordered()
# Consider two cases - data is there, data is not there
    print("Test Find Ordered")
    print(linked_list_insord.find_ordered(41)) # int in linked list
    print(linked_list_insord.find_ordered(8)) # int not in linked list
    print()

# Test method delete_link()
# Consider two cases - data is there, data is not there
    print("Test Delete Link")
    testList_del = [75, 23, 90, 14, 68, 12, 54, 37, 21, 88, 84, 31]
    linked_list_del = LinkedList()
    for data in testList_del:
        linked_list_del.insert_last(data)
    linked_list_del.delete_link(68) # delete int in linked list
    print(linked_list_del) # print list without int
    linked_list_del.delete_link(0) # delete int not in linked list
    print(linked_list_del) # print the same list
    print()

# Test method copy_list()
    print("Test Copy List")
    testList = [75, 23, 90, 14, 68, 12, 54, 37, 21, 88, 84, 31]
    linked_list_copy = LinkedList()
    for data in testList:
        linked_list_copy.insert_last(data)
    print(linked_list_copy.copy_list())
    print()

# Test method reverse_list()
    print("Test Reverse List")
    linked_list_rev = LinkedList()
    testList_rev = [9,8,7,6,5,4,3,2,1]
    for data in testList_rev:
        linked_list_rev.insert_last(data)
    print(linked_list_rev.reverse_list())
    print()

# Test method sort_list()
    print("Test Sort List")
    print(linked_list_copy.sort_list())
    print()

# Test method is_sorted()
# Consider two cases - list is sorted, list is not sorted
    print("Test List is Sorted")
    testList = [75, 23, 90, 14, 68, 12, 54, 37, 21, 88, 84, 31]
    linked_list_sorted = LinkedList()
    for data in testList:
        linked_list_sorted.insert_in_order(data)
    print(linked_list_sorted.is_sorted()) # list is sorted
    print(linked_list_insertl.is_sorted()) # list isn't sorted
    print()

# Test method is_empty()
    print("Test Empty List")
    testList_nonemp = [1,2,3,4,5]
    linked_list_nonempty = LinkedList()
    for data in testList_nonemp:
        linked_list_nonempty.insert_last(data)
    linked_list_empty = LinkedList()
    print(linked_list_nonempty.is_empty()) # empty list
    print(linked_list_empty.is_empty()) # non empty list
    print()

# Test method merge_list()
    print("Test Merging Sorted Lists")
    testList1 = [2,14,17,25,61,63,90]
    linked_list_a = LinkedList()
    for data in testList1:
        linked_list_a.insert_last(data)
    testList2 = [1,5,9,16,21,26,49,62]
    linked_list_b = LinkedList()
    for data in testList2:
        linked_list_b.insert_last(data)
    print(linked_list_a.merge_list(linked_list_b))
    print()

# Test method is_equal()
# Consider two cases - lists are equal, lists are not equal
    print("Test Lists are Equal")
    testLista = [1,2,3,4,5,6]
    testListb = [1,2,3,4,5,6]
    testListc = [1,2,3,4,5,7]
    linked_list_i = LinkedList()
    for data in testLista:
        linked_list_i.insert_last(data)
    linked_list_ii = LinkedList()
    for data in testListb:
        linked_list_ii.insert_last(data)
    linked_list_iii = LinkedList()
    for data in testListc:
        linked_list_iii.insert_last(data)
    print(linked_list_i.is_equal(linked_list_ii)) # equal lists
    print(linked_list_ii.is_equal(linked_list_iii)) # non equal lists
    print()


# Test remove_duplicates()
    print("Test Remove Duplicates")
    testList_dup = [3,4,10,4,11,11,3,15,12,19,11]
    linked_list_dup = LinkedList()
    for data in testList_dup:
        linked_list_dup.insert_last(data)
    print(linked_list_dup.remove_duplicates())

if __name__ == "__main__":
    main()
