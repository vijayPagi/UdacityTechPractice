from numpy.core.tests.test_mem_overlap import xrange
def compare(a, b):
    # check if set1 and set2 are equal
    for i in a:
        if i in b:
            if a[i] == b[i]:
                b.pop(i)
            else:
                return False
        else:
            return False
    if len(b) == 0:
        return True
    else:
        return False
    
def question1(s, t):
    # lets make sure s is a sting
    if type(s) != str:
        return "Please update the value of s and try again, s doesn't seem to be a string"

    # lets make sure t is also a string
    if type(t) != str:
        return "Please update the value of t and try again, t doesn't seem to be a string"

    if len(s) == 0 or len(s) < len(t):
        return False

    if len(t) == 0:
        return True

    # Storing character counts of t
    char_counts_t = {}
    for i in t:
        if i in char_counts_t:
            char_counts_t[i] += 1
        else:
            char_counts_t[i] = 1

    # Storing character counts length of t characters of s
    char_counts_s = {}
    for i in xrange(len(t)):
        
        if s[i] in char_counts_s:
            char_counts_s[s[i]] += 1
        else:
            char_counts_s[s[i]] = 1
    
    # Lets use compare to compare if they are anagrams
    if compare(char_counts_t, char_counts_s.copy()):
        return True

    # compare the rest of sets
    for i in xrange(len(t), len(s)):

        # add new character in the set
        if s[i] in char_counts_s:
            char_counts_s[s[i]] += 1
        else:
            char_counts_s[s[i]] = 1

        # remove old character in the set
        j = i - len(t)
        char_counts_s[s[j]] -= 1
        if char_counts_s[s[j]] == 0:
            char_counts_s.pop(s[j])
        
        # compare if they are anagrams
        if compare(char_counts_t, char_counts_s.copy()):
            return True

    # There is no matching anagram of t in consecutive substring of s
    return False

def test1():
    print("Test: 1")
    print("Test Case 1: For (numpy, nm):", " Its passed" if True == question1("numpy", "nm") else "Oops, Fail")
    print("Test Case 2: Edge case (non string value):", "Its passed" if "Please update the value of s and try again, s doesn't seem to be a string" == question1(898, 98.8) else "Oops, Fail")
    print("Test Case 3: Lets check one more Edge scenaro, t longer than s", "Its passed" if False == question1("pd", "pandas") else "Oops, Fail")
    print("Test Case 4: s equal to t:", "Its passed" if True == question1("abcd", "abcd") else "Fail")
    print("Test Case 5: (very long string):", "Its passed" if True == question1("abhuihuh auohoihoihohoidlhfhiuelfduisfgiuwfuilfgfisdgfdaadsshagldhghdldfahgafd",
                                                                  "adgdaliu") else "Oops, Fail")
    print("Test Case 6 (repeating substrings):", "Its passed" if True == question1("hgrgheghgrgheghgrgheghgrgheghgrgheg", "hggeha") else "Oops, Fail")

test1()

### QUESTION 2 ###

# Returns substrings of a String passed as a parameter
def findSubstrings(x):
    length = len(x)
    sub_strings = []
    # looping through a string for its length iterations
    for i in range(length):
        subString = ''
      
        for j in range(i + 1, length + 1):
            sub_string = x[i:j]
            # appends each substring to substrings array
            sub_strings.append(subString)
    # returns all substrings of a string
    return sub_strings

# checks if a string is a palindrome
def isPalindrome(y):
    # checks if a string is the same as Reverse of that string
    if y == y[::-1]:
        # returns True if string equals reverse string
        return True
    # else returns False
    return False

# returns longest palindrome in the passed string
def question2(a):
    longest_palindrome = ''
    # if the string is shorter than 2 characters, returns string
    if len(a) < 2:
        return a
    else:
        # iterates through all substrings of the given string
        for i in findSubstrings(a):
            # checks if a substring is a palindrome
            if isPalindrome(i) and len(i) > len(longest_palindrome):
                longest_palindrome = i
    # returns longest palindrome
    return longest_palindrome

def test2():
    print("Test 2")
    print("Test Case 1: question2(abcde):", "Its Passed" if 'a' == question2('abcde') else "Oops, Fail")
    print("Test Case 2: Edge Case question2(''):", "Its Passed" if '' == question2('') else "Oops, Fail")
    print("Test Case 3: Edge Case question2(x):", "Its Passed" if 'x' == question2('x') else "Oops, Fail")
    print("Test Case 4: question2(cinnamon):", "Its Passed" if 'manic' == question2('cinnamon') else "Oops, Fail")
    print("Test Case 5: Edge Case: question2(long string):" , "Its Passed" if 'dueweud' == question2('adsjhdaskjdhasdskhasdlkjhksahsakhdsaksjdhdjkhuadwjkbejhdd') else "Oops, Fail") 


test2()


def question3(G):

    parent = dict()

    # checks if input is a dictionary
    if type(G) == dict:
        # initializes edges as an empty set
        edges = list()

        for v in G:
            parent[v] = v
            for edge in G[v]:
                # will create a tuple (x, y, 2) for 'x': [('y', 2)]
                edges.append((v, edge[0], edge[1]))

        # all the edges in edges are sorted based on the weights
        edges.sort(key = lambda tup: tup[2])
        
        dit = dict()

        used_edges = set()

        for edge in edges:
            # checks if an edge has already been checked
            if edge not in used_edges:
                used_edges.add((edge[0], edge[1]))
                used_edges.add((edge[1], edge[0]))
                # checks for acceptable edges and appends to list
                if unionOf(edge, parent):
                    if edge[0] not in dit:
                        dit[edge[0]] = []
                    dit[edge[0]].append((edge[1], edge[2]))
                    if edge[1] not in dit:
                        dit[edge[1]] = []
                    dit[edge[1]].append((edge[0], edge[2]))

        return dit

    else:
        return None

# returns parent of given node if node is already in tree 
def findParent(node, parent):
    if parent[node] != node:
        parent[node] = findParent(parent[node], parent)
    return parent[node]

# checks if an edge results in a cycle
def unionOf(edge, parent):
    parent_a = findParent(edge[0], parent)
    parent_b = findParent(edge[1], parent)
    # checks for a cycle
    if parent_a == parent_b:
        return False
    
    # makes a and b have the same parent
    parent[parent_a] = parent_b

    return True


def test3():
    graphs = [{},
    {'A': [('B', 2), ('C', 0)],
     'B': [('A', 2), ('C', 1)], 
     'C': [('B', 1), ('A', 0)]},
     {'A': [('B', 2), ('C', 0)],
     'B': [('A', 2), ('C', 1)], 
     'C': [('B', 1), ('A', 0)]},
     {'A': [('B', 10), ('C', 5), ('D', 6)],
     'B': [('A', 10), ('C', 15)], 
     'C': [('B', 15), ('A', 5), ('D', 4)],
     'D': [('C', 4), ('A', 6)]},
     {'A': [('B', 10)],
     'B': [('A', 10)]},
    ]

    outputs = [{},
    {'A': [('C', 0)], 'C': [('A', 0), ('B', 1)], 'B': [('C', 1)]},
    {'A': [('C', 0)], 'C': [('A', 0), ('B', 1)], 'B': [('C', 1)]},
    {'A': [('C', 5), ('B', 10)], 'C': [('D', 4), ('A', 5)], 'B': [('A', 10)], 'D': [('C', 4)]},
    {'A': [('B', 10)], 'B': [('A', 10)]},
    ]

    print("Test 3")
    print("Test Case 1 question3():", "Its Passed" if outputs[3] == question3(graphs[3]) else "Fail")
    print("Test Case 2 question3():", "Its Passed" if outputs[2] == question3(graphs[2]) else "Fail")
    print("Test Case 3 Edge Case question3():", "Its Passed" if outputs[0] == question3(graphs[0]) else "Fail")
    print("Test Case 4 Edge Case question3():", "Its Passed" if outputs[1] == question3(graphs[1]) else "Fail")
    print("Test Case 5 question3():", "Its Passed" if outputs[4] == question3(graphs[4]) else "Fail")

test3()


### Question4 ###

def question4(T, r, n1, n2):
    # checks if n1 and n2 are on different sides of the root
    if (n1 > r and n2 < r) or (n1 < r and n2 > r):
        # returns root if n1 and n2 are on different sides
        # as the root being the only common ancestor
        return r
    # checks if both n1 and n2 are smaller than root
    elif (n1 < r and n2 < r):
        left = T[r].index(1)
        # checks if n1 or n2 equals left child of root
        if n1 == left or n2 == left:
            return r
        # changes root to left child
        else:
            r = left
    # checks if both n1 and n2 are greater than root
    elif (n1 > r and n2 > r):
        right = len(T[r]) - T[r][::-1].index(1) - 1
        # checks if n1 or n2 equals right child of root
        if n1 == right or n2 == right:
            return r
        else:
            # changes root to right child
            r = right
            
    # runs recursively with updated root
    return question4(T, r, n1, n2)

# test cases
# Given nodes are children of same parent
# Given nodes are children of different parents
# Given nodes have a parent child relationship
# Given nodes are on same side of BST
# Given nodes are on different sides of BST

def test4():
    inputs = [[[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
           [[0, 0, 0, 0, 0, 0, 0],
           [1, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 1]],
           [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    ]

    print("Test 4")
    print("Test Case 1 Edge Case question4():", "Its Passed" if 3 == question4(inputs[0], 3, 0, 4) else "Oops, Fail")
    print("Test Case 2 Edge Case question4():", "Its Passed" if 3 == question4(inputs[1], 3, 2, 6) else "Fail")
    print("Test Case 3 question4():", "Its Passed" if 3 == question4(inputs[0], 3, 1, 4) else "Oops, Fail")
    print("Test Case 4 question4():", "Its Passed" if 1 == question4(inputs[1], 3, 0, 2) else "Oops, Fail")
    print("Test Case 5 question4():", "Its Passed" if 3 == question4(inputs[2], 6, 1, 4) else "Oops, Fail")

test4()

### Question 5 ###

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def get_length(ll):
    # get the length of ll
    # also checking whether the linked list is circular
    # returns -1 if the linked list is circular

    # length == 1
    if ll.next == None:
        return 1
    
    length_ll = 0
    current_node = ll
    current_node2 = ll.next
    while current_node != None and current_node != current_node2:
        current_node = current_node.next
        if current_node2 != None:
            current_node2 = current_node2.next
        if current_node2 != None:
            current_node2 = current_node2.next
        length_ll += 1

    if current_node == None:
        return length_ll
    else:
        return -1

def question5(ll, m):
    # ll should be a Node
    if type(ll) != Node:
        return "Failed: ll is not a Node!"

    # m should an integer
    if type(m) != int:
        return "Failed: m is not an integer!"
    
    # length of ll
    length_ll = get_length(ll)

    #ll should not be circular
    if length_ll == -1:
        return "Failed: circular linked list!"
        
    # make sure m is less than or equal to the length of ll
    if length_ll < m:
        return "Failed: m is greater than the length of ll"
    
    # traverse to the last mth element
    current_node = ll
    for i in xrange(length_ll - m):
        current_node = current_node.next
        
    return current_node.data

def test5():
    n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
    n4.next = n5
    n3.next = n4
    n2.next = n3
    n1.next = n2
    
    print("Test 5")
    print("Test Case 3 Edge case (ll is not a Node):", "Its Passed" if "Failed: ll is not a Node!" == question5(123, 111) else "Oops, Fail")
    print("Test Case 4 Edge case (m > length of ll):", "Its Passed" if "Failed: m is greater than the length of ll" == question5(n1, 6) else "Oops, Fail")
    print("Test Case 1 (ll = n1 and m = 3):", "Its Passed" if 3 == question5(n1, 3) else "Oops, Fail") 
    n5.next = n1
    print("Test Case 2 (circular linked list):", "Its Pass" if "Failed: circular linked list!" == question5(n1, 3) else "Oops, Fail") 
test5()