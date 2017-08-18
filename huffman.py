# Justin Mo
import linked_list 
import linked_list 
from sys import * 
from huffman_bits_io import *

# file -> List
# Takes in a text file and returns a list of occurences.
def occurences(filename):
    txt_file = open(filename, "r")
    array_or_linked_list = linked_list.empty_list()
    lines = txt_file.readlines()
    #i = 0
    list_of_occurences = linked_list.empty_list()
    if len(lines) == 0:
        for i in range(0, 256):
            list_of_occurences = linked_list.add(list_of_occurences, i, 0)
        txt_file.close()
        return list_of_occurences
    #for each_char in each_line:
        #array_or_linked_list = add(array_or_linked_list, i, each_char) 
        #i += 1
    for i in range(0, 256):
        list_of_occurences = linked_list.add(list_of_occurences, i, 0)
    for each_line in lines:
        for each_char in each_line:
            list_of_occurences = linked_list.set(list_of_occurences, ord(each_char), linked_list.get(list_of_occurences, ord(each_char)) + 1) 
    txt_file.close()
    return list_of_occurences

# class Leaf is a Node that has no children
class Leaf:
    def __init__(self, ascii_val, frequency):
        self.ascii_val = ascii_val # an int
        self.frequency = frequency # an int

    def __repr__(self):
        return "Leaf(Ascii Value: {!r}, Frequency: {!r})".format(self.ascii_val, self.frequency)

    def __eq__(self, other):
        return type(other) == Leaf and self.ascii_val == other.ascii_val and self.frequency == other.frequency

# a Huffman tree is one of 
# ~ Leaf or 
# ~ Node(left, right)
class Node:
    def __init__(self, ascii_val, frequency, left, right):
        self.ascii_val = ascii_val # an int
        self.frequency = frequency # an int
        self.left = left # a node
        self.right = right # a node
        
    def __repr__(self):
        return "Node(Ascii Value: {!r}, Frequency: {!r}, Left Node: {!r}, Right Node: {!r})".format(self.ascii_val, self.frequency, self.left, self.right)

    def __eq__(self, other):
        return type(other) == Node and self.ascii_val == other.ascii_val and self.frequency == other.frequency and self.left == other.left and self.right == other.right

# Huffman tree -> string
# Takes in a Huffman tree and returns a string by traversing the tree in a pre-order traversal and appending the characters of the visited leaf nodes.
def the_creator(node, string=""):
    if node == None:
        return ""
    if type(node) == Node:
        string = the_creator(node.left, string)
        string += the_creator(node.right, string)
        return string
    # if type(node) == Leaf:
    else:
        return str(chr(node.ascii_val))

# tree tree -> bool
# Takes in two trees and returns a bool based on whether tree a is smaller than tree b.
def comes_before(a, b):
    if a.frequency == b.frequency:
        return (a.ascii_val < b.ascii_val)
    return (a.frequency < b.frequency)

# LinkedList -> tree
# Takes in a list of occurences and returns a sorted list of leaves.
def construct_helper(lst, counter=0, linked_counter=0, list_of_leaves=None):
    if lst != None:    
        if lst.first != 0:
            leaf = Leaf(counter, lst.first)
            counter += 1
            list_of_leaves = linked_list.insert_sorted(list_of_leaves, leaf, comes_before)
            linked_counter += 1
            return construct_helper(lst.rest, counter, linked_counter, list_of_leaves)
        else:
            counter += 1
            return construct_helper(lst.rest, counter, linked_counter, list_of_leaves)
    return list_of_leaves 

# LinkedList -> tree
# Takes in a list of sorted leaves and returns the root node of the Huffman tree
def construct(lst):
    if lst == None:
        return None
    if lst.rest != None:
        parent_frequency = lst.first.frequency + lst.rest.first.frequency
        if lst.first.ascii_val < lst.rest.first.ascii_val:
            parent_ascii_val = lst.first.ascii_val
        else:
            parent_ascii_val = lst.rest.first.ascii_val
        lst = linked_list.insert_sorted(lst.rest.rest, Node(parent_ascii_val, parent_frequency, lst.first, lst.rest.first), comes_before)
        return construct(lst)
    return lst.first

# tree -> node
# Takes in a tree and returns a generator that iterates through tuples where the first value represents the node's ascii value and the second value represents the character code.
def code_builder(node, char_code=""):
    if type(node) == Leaf:
        yield (node.ascii_val, char_code)
    else:
        yield from code_builder(node.left, char_code + "0")
        yield from code_builder(node.right, char_code + "1")

# tree -> list
# Takes in a tree and returns a list of tuples where the first value is the ascii value and the second value is the binary character code.
def list_builder(node):
    if node == None:
        return None
    lst = linked_list.empty_list()
    try:
        generator = code_builder(node)
        booli = True
        counter = 0
        while booli:
            lst = linked_list.add(lst, counter, next(generator))
            counter += 1
    except StopIteration:
        return lst

# leaf leaf -> bool
# Takes in two leaves and returns true depending on whether leaf a has a lower ascii value.
def comes_before_2(a, b):
    return a.ascii_val < b.ascii_val

# list -> list
# Takes in a list sorted by frequency and returns a list sorted by ascii value.
def encode_helper(sorted_leaves, sorted_ascii=None):
    while sorted_leaves != None:
        sorted_ascii = linked_list.insert_sorted(sorted_ascii, sorted_leaves.first, comes_before_2) 
        sorted_leaves = sorted_leaves.rest
    return sorted_ascii

# tuple tuple -> bool
# Takes in two tuples that compares the first value of the tuple (ascii value) to the second tuples's first value and returns a bool depending on whether it's smaller.
def comes_before_3(a, b):
    return a[0] < b[0]

# list -> list
# Takes in a list of tuples and returns a list of tuples sorted by ascii value.
def encode_helper_3(list_of_tuples, sorted_tuples=None):
    while list_of_tuples != None:
        sorted_tuples = linked_list.insert_sorted(sorted_tuples, list_of_tuples.first, comes_before_3)
        list_of_tuples = list_of_tuples.rest
    return sorted_tuples

# file file -> string
# Takes in an input file and output file and writes the encoded input file to the output file and returns a string representation of the huffman tree in preorder traversal. "aaabbc" -> "acb"
def huffman_encode(input_file, output_file):
    bin_file = open(output_file, "w")
    bin_file.close()
    bin_file = open(output_file, "w")
    txt_file = open(input_file, "r")
    lines = txt_file.readlines()
    hb_writer = HuffmanBitsWriter(output_file)
    if len(lines) == 0:
        hb_writer.write_byte(0)
        hb_writer.close()
        bin_file.close()
        txt_file.close()
        return ""
    list_of_occurences = occurences(input_file) 
    sorted_leaves = construct_helper(list_of_occurences)
    tree = construct(sorted_leaves)
    list_of_tuples = list_builder(tree)
    #while list_of_tuples is not None:
    #    txt_file.write(str(list_of_tuples.first[1]))
    #    list_of_tuples = list_of_tuples.rest
    string = the_creator(tree)
    number_of_codes = len(string)
    hb_writer.write_byte(number_of_codes)
    sorted_ascii = encode_helper(sorted_leaves)
    sorted_tuples = encode_helper_3(list_of_tuples)
    while sorted_ascii is not None: 
        hb_writer.write_byte(sorted_ascii.first.ascii_val) 
        hb_writer.write_int(sorted_ascii.first.frequency)
        sorted_ascii = sorted_ascii.rest
    for each_letter in lines[0]:
        while sorted_tuples is not None:  
            if ord(each_letter) == sorted_tuples.first[0]:
                hb_writer.write_code(sorted_tuples.first[1])
            sorted_tuples = sorted_tuples.rest
        sorted_tuples = encode_helper_3(list_of_tuples)
    hb_writer.close()
    bin_file.close()
    txt_file.close()
    return string

# tree int file file -> None
# Takes in a tree and the sum of occurences and writes the original input to the output text file
#def decode_helper(tree, binput_file, output_file, hb_reader):
    #txt_file = open(output_file, "w")
    #while sum_of_occurences != 0:
    #print(str(chr(tree.ascii_val)))
    #if type(tree) == Leaf:
    #    print(str(chr(tree.ascii_val)))
    #    txt_file.write(str(chr(tree.ascii_val)))
    #    txt_file.close()
    #else:
    #    if hb_reader.read_bit() == True:
    #        return decode_helper(tree.left, binput_file, output_file, hb_reader)
    #    else:
    #        return decode_helper(tree.right, binput_file, output_file, hb_reader)

# file file -> None
# Takes in a compressed bin file and writes the contents of the compressed file into a output text file.
def huffman_decode(binput_file, output_file):
    hb_reader = HuffmanBitsReader(binput_file)
    txt_file = open(output_file, "w")
    txt_file.close()
    txt_file = open(output_file, "w")
    number_of_diff_chars = hb_reader.read_byte()
    if number_of_diff_chars == 0:
        txt_file.write("")
        txt_file.close()
        hb_reader.close()
        return
    list_of_tuples = linked_list.empty_list()
    for i in range(0, number_of_diff_chars):
        list_of_tuples = linked_list.add(list_of_tuples, i, (hb_reader.read_byte(), hb_reader.read_int()))
    list_of_occurences = linked_list.empty_list()
    sum_of_occurences = 0
    for i in range(0, 256):
        list_of_occurences = linked_list.add(list_of_occurences, i, 0)
    for i in range(0, number_of_diff_chars):
        sum_of_occurences += list_of_tuples.first[1]
        list_of_occurences = linked_list.set(list_of_occurences, list_of_tuples.first[0], list_of_tuples.first[1])
        list_of_tuples = list_of_tuples.rest
    sorted_leaves = construct_helper(list_of_occurences)
    tree = construct(sorted_leaves)
    #while sum_of_occurences != 0:     
    #    if hb_reader.read_bit() == True:
    #        binary_code += "1"
    #    else:
    #        binary_code += "0"
    #print(binary_code)
    for i in range(0, sum_of_occurences):
        while type(tree) != Leaf:
            lol = hb_reader.read_bit()
            if lol == True:
                tree = tree.right
            else:
                tree = tree.left
        txt_file.write(str(chr(tree.ascii_val)))
        tree = construct(sorted_leaves)
        #txt_file.write(str(decode_helper(tree)))
    txt_file.close()
    hb_reader.close()

class Tests(unittest.TestCase):
    def test_huffman_decode(self):
        binput_file = "encoded.bin"
        output_file = "decoded.txt"
        huffman_decode(binput_file, output_file)
        binput_file = "blank_encoded.bin"
        output_file = "blank_decoded.txt"
        huffman_decode(binput_file, output_file)
    def test_huffman_encode(self):
        input_file = "input.txt"
        output_file = "encoded.bin"
        self.assertEqual(huffman_encode(input_file, output_file), " bdca")
        input_file = "blank.txt"
        output_file = "blank_encoded.bin"
        self.assertEqual(huffman_encode(input_file, output_file), "")
    def test_code_builder(self):
        tree1 = None
        list_builder(tree1)
        tree = Node(32, 13, Node(32, 6, Leaf(32, 3), Leaf(98, 3)), Node(97, 7, Node(99, 3, Leaf(100, 1), Leaf(99, 2)), Leaf(97, 4)))
        self.assertEqual(list_builder(tree), linked_list.Pair((32, "00"), linked_list.Pair((98, "01"), linked_list.Pair((100, "100"), linked_list.Pair((99, "101"), linked_list.Pair((97, "11"), None))))))
    def test_construct(self):
        lst1 = None
        construct(lst1)
        lst = linked_list.Pair(Leaf(100, 1), linked_list.Pair(Leaf(99, 2), linked_list.Pair(Leaf(32, 3), linked_list.Pair(Leaf(98, 3), linked_list.Pair(Leaf(97, 4), None)))))
        self.assertEqual(construct(lst), Node(32, 13, Node(32, 6, Leaf(32, 3), Leaf(98, 3)), Node(97, 7, Node(99, 3, Leaf(100, 1), Leaf(99, 2)), Leaf(97, 4))))
    def test_construct_helper(self):
        filename = "input.txt"
        lst = occurences(filename)
        lst1 = linked_list.Pair(Leaf(100, 1), linked_list.Pair(Leaf(99, 2), linked_list.Pair(Leaf(32, 3), linked_list.Pair(Leaf(98, 3), linked_list.Pair(Leaf(97, 4), None)))))
        self.assertEqual(construct_helper(lst), lst1) 
    def test_comes_before(self):
        a = Node(97, 4, Leaf(97, 2), Leaf(98, 2))
        b = Node(98, 4, Leaf(98, 2), Leaf(99, 2))
        c = Node(97, 6, Leaf(97, 3), Leaf(98, 3))
        d = Node(98, 5, Leaf(98, 2), Leaf(99, 3))
        self.assertTrue(comes_before(a, b))
        self.assertFalse(comes_before(c, b))
    def test_repr(self):
        self.assertEqual(repr(Leaf(1, 1)), "Leaf(Ascii Value: 1, Frequency: 1)")
        self.assertEqual(repr(Node(1, 1, 1, 1)), "Node(Ascii Value: 1, Frequency: 1, Left Node: 1, Right Node: 1)")
    def test_eq(self):
        self.assertEqual(Leaf(1, 1) == Leaf(1, 1), True)
        self.assertEqual(Node(1, 1, 1, 1) == Node(1, 1, 1, 1), True)
    def test_occurences(self):
        filename = "input.txt"
        occurences(filename)
        filename1 = "blank.txt"
        occurences(filename1)
    def test_the_creator(self):
        node = None
        the_creator(node)
        self.assertEqual(the_creator(Node(32, 13, Node(32, 6, Leaf(32, 3), Leaf(98, 3)), Node(97, 7, Node(99, 3, Leaf(100, 1), Leaf(99, 2)), Leaf(97, 4)))), " bdca")
        self.assertEqual(the_creator(Node(99, 3, Leaf(100, 1), Leaf(99, 2))), "dc")
        self.assertEqual(the_creator(Node(97, 6, Leaf(97, 3), Node(98, 3, Leaf(99, 1), Leaf(98, 2)))), "acb")

if __name__ == '__main__':
    unittest.main()
