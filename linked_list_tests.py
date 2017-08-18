# Justin Mo
import unittest
from linked_list import *

class TestList(unittest.TestCase):
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)
    def test_repr_song(self):
        self.assertEqual(repr(Song(3, 'hi', 'im', 'jmo')), str('3--hi--im--jmo'))
    def test_sort(self):
        linkedlist = Pair(Song('1', 'B', 'C', 'A'), Pair(Song('0', 'A', 'B', 'C'), Pair(Song('2', 'C', 'A', 'B'), None)))
        linked_list = Pair(Song('0', 'A', 'B', 'C'), Pair(Song('1', 'B', 'C', 'A'), Pair(Song('2', 'C', 'A', 'B'), None)))
        linkedlist = sort(linkedlist, less_than_number_first)
        self.assertEqual(linkedlist, linked_list)
        linkedlist1 = Pair(Song('1', 'B', 'C', 'A'), Pair(Song('0', 'A', 'B', 'C'), Pair(Song('2', 'C', 'A', 'B'), None)))
        linkedlist2 = Pair(Song('0', 'A', 'B', 'C'), Pair(Song('1', 'B', 'C', 'A'), Pair(Song('2', 'C', 'A', 'B'), None)))
        linkedlist1 = sort(linkedlist1, less_than_title_first)
        self.assertEqual(linkedlist1, linkedlist2) 
        linkedlist4 = Pair(Song('0', 'lol', 'A', 'fwe'), Pair(Song('1', 'wef', 'B', 'rew'), Pair(Song('2', 'gah', 'C', 'hue'), None)))
        linkedlist3 = Pair(Song('1', 'wef', 'B', 'rew'), Pair(Song('0', 'lol', 'A', 'fwe'), Pair(Song('2', 'gah', 'C', 'hue'), None)))
        linkedlist3 = sort(linkedlist3, less_than_artist_first)
        self.assertEqual(linkedlist3, linkedlist4)
        linkedlist7 = Pair(Song('0', 'hey', 'sup', 'b'), Pair(Song('1', 'ay', 'lmao', 'c'), Pair(Song('2', 'ia', 'heh', 'a'), None)))
        linkedlist8 = Pair(Song('2', 'ia', 'heh', 'a'), Pair(Song('0', 'hey', 'sup', 'b'), Pair(Song('1', 'ay', 'lmao', 'c'), None)))
        linkedlist7 = sort(linkedlist7, less_than_album_first)
        self.assertEqual(linkedlist7, linkedlist8)
        linkedlist9 = Pair(Song('0', 'hi', 'im', 'jmo'), Pair(Song('1', 'hi', 'im', 'jmo'), Pair(Song('2', 'hi', 'im', 'jmo'), None)))
        linkedlist9 = sort(linkedlist9, less_than_title_first)
        self.assertEqual(linkedlist9, linkedlist9)
        linkedlist9 = sort(linkedlist9, less_than_artist_first)
        self.assertEqual(linkedlist9, linkedlist9)
        linkedlist9 = sort(linkedlist9, less_than_album_first)
        self.assertEqual(linkedlist9, linkedlist9)
        linkedlist10 = Pair(Song('0', 'hi', 'a', 'jmo'), Pair(Song('1', 'hi', 'b', 'jmo'), Pair(Song('2', 'hi', 'c', 'jmo'), None)))
        linkedlist10 = sort(linkedlist10, less_than_title_first)
        self.assertEqual(linkedlist10, linkedlist10)
        linkedlist11 = Pair(Song('0', 'hi', 'im', 'a'), Pair(Song('1', 'hi', 'im', 'b'), Pair(Song('2', 'hi', 'im', 'c'), None)))
        linkedlist11 = sort(linkedlist11, less_than_title_first)
        self.assertEqual(linkedlist11, linkedlist11)
        linkedlist12 = Pair(Song('0', 'hi', 'im', 'a'), Pair(Song('1', 'hi', 'im', 'b'), Pair(Song('2', 'hi', 'im', 'c'), None)))
        sort(linkedlist12, less_than_artist_first)
        linkedlist13 = Pair(Song('0', 'a', 'im', 'jmo'), Pair(Song('1', 'b', 'im', 'jmo'), Pair(Song('2', 'c', 'im', 'jmo'), None)))
        sort(linkedlist13, less_than_artist_first)
        linkedlist14 = Pair(Song('0', 'hi', 'a', 'jmo'), Pair(Song('1', 'hi', 'b', 'jmo'), Pair(Song('2', 'hi', 'c', 'jmo'), None)))
        sort(linkedlist14, less_than_album_first)
        linkedlist15 = Pair(Song('0', 'a', 'im', 'jmo'), Pair(Song('1', 'b', 'im', 'jmo'), Pair(Song('2', 'c', 'im', 'jmo'), None)))
        sort(linkedlist15, less_than_album_first)
    def test_foreach(self):
        linked_list = Pair(1, None)
        def f(val):
            val += 1
            return val
        foreach(linked_list, f)
    def test_repr(self):
        self.assertEqual(repr(Pair(3, None)), str(Pair(3, None)))
    def test_empty(self):
        self.assertEqual(empty_list(), None)
    def test_length(self):
        self.assertEqual(length(Pair(4, Pair(3, None))), 2)
        self.assertEqual(length(None), 0)
    def test_add(self):
        self.assertEqual(add(Pair(1, Pair(3, None)), 1, 2), Pair(1, Pair(2, Pair(3, None))))
        self.assertEqual(add(Pair(3, None), 0, 9), Pair(9, Pair(3, None)))
        with self.assertRaises(IndexError):
            add(Pair(3, None), 5, 9)
        self.assertEqual(add(Pair(3, None), 1, 9), Pair(3, Pair(9, None)))
        self.assertEqual(add(None, 0, 5), Pair(5, None))
        list1 = Pair(2, Pair(3, Pair(4, None)))
        self.assertEqual(get(add(list1, 3, 5), 3), 5)
    def test_get(self):
        self.assertEqual(get(Pair(3, None), 0), 3)
        self.assertEqual(get(Pair(3, Pair(4, None)), 1), 4)
        with self.assertRaises(IndexError):
            get(Pair(3, None), 5)
    def test_set(self):
        with self.assertRaises(IndexError):
            set(None, 4, 5), Pair(5, None)
        self.assertEqual(set(Pair(2, None), 0, 5), Pair(5, None))
        self.assertEqual(set(Pair(2, Pair(3, Pair(5, None))), 1, 5), Pair(2, Pair(5, Pair(5, None))))
        self.assertEqual(set(Pair(2, Pair(3, None)), 1, 5), Pair(2, Pair(5, None)))
    def test_remove(self):
        with self.assertRaises(IndexError):
            remove(Pair(1, None), 5)
        self.assertEqual(remove(Pair(1, Pair(2, None)), 0), (1, Pair(2, None)))
        self.assertEqual(remove(Pair(1, Pair(2, Pair(3, None))), 1), (2, Pair(1, Pair(3, None))))
        self.assertEqual(remove(Pair(1, Pair(2, Pair(3, None))), 0), (1, Pair(2, Pair(3, None))))
        self.assertEqual(remove(Pair(1, None), 0), (1, None))
        with self.assertRaises(IndexError):
            remove(None, 1)
    def test_remove_helper(self):
        self.assertEqual(remove_helper(Pair(1, Pair(2, None)), 0), 1)
        with self.assertRaises(IndexError):
            remove_helper(None, 2)
        with self.assertRaises(IndexError):
            remove_helper(Pair(1, Pair(2, None)), 3)
    def test_remove_helper2(self):
        with self.assertRaises(IndexError):
            remove_helper2(None, 2)
        with self.assertRaises(IndexError):
            remove_helper2(Pair(1, Pair(2, None)), 3)
if __name__ == '__main__':
    unittest.main()
