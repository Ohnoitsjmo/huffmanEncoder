# Justin Mo
import unittest
from array_list import *

class TestList(unittest.TestCase):
    def test_repr(self):
        list1 = List()
        list1.array = [1, 2, 3, 4, 5]
        list1.length = 5
        list1.capacity = 10
        self.assertEqual(repr(list1), "1, 2, 3, 4, 5")

    def test_eq(self):
        list1 = List()
        list2 = List()
        list1.array = [1, 2, 3, 5, 7]
        list1.length = 5
        list1.capacity = 10
        list2.array = [1, 2, 3, 4, 8]
        list2.length = 5
        list1.capacity = 10
        self.assertFalse(list1 == list2)

    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)
    
    def test_repr_song(self):
        list1 = List()
        list1.array = [Song(0, 'hi', 'im', 'jmo'), Song(1, 'hi', 'im', 'jmo'), Song(2, 'hi', 'im', 'jmo')]
        list1.length = 3
        list1.capacity = 10
        self.assertEqual(repr(list1), "0--hi--im--jmo, 1--hi--im--jmo, 2--hi--im--jmo")

    def test_sort(self):
        list0 = empty_list()
        list0.length = 3
        list0.capacity = 10
        list0.array = [Song('5', 'a', 'b', 'c'), Song('3', 'd', 'e', 'f'), Song('4', 'g', 'b', 'c')]
        sort(list0, less_than_title_first)
        list69 = empty_list()
        list69.length = 3
        list69.capacity = 10
        list69.array = [Song('5', 'a', 'b', 'c'), Song('3', 'a', 'e', 'c'), Song('4', 'a', 'f', 'c')]
        sort(list69, less_than_title_first)
        list70 = empty_list()
        list70.length = 3
        list70.capacity = 10
        list70.array = [Song('5', 'a', 'b', 'd'), Song('3', 'a', 'b', 'f'), Song('4', 'a', 'b', 'g')]
        list71 = empty_list()
        list71.length = 3
        list71.capacity = 10
        list71.array = [Song('5', 'a', 'b', 'c'), Song('3', 'a', 'b', 'c'), Song('4', 'a', 'b', 'c')]
        sort(list71, less_than_title_first)
        sort(list70, less_than_title_first)
        sort(None, less_than_number_first)
        sort(list0, less_than_artist_first)
        sort(list69, less_than_artist_first)
        sort(list70, less_than_artist_first)
        sort(list71, less_than_artist_first)
        sort(list0, less_than_album_first)
        sort(list69, less_than_album_first)
        sort(list70, less_than_album_first)
        sort(list71, less_than_album_first)
        list1 = empty_list()
        list1.length = 3
        list1.capacity = 20
        list1.array = [Song('5', 'a', 'b', 'c'), Song('3', 'a', 'b', 'c'), Song('4', 'a', 'b', 'c')]
        list2 = empty_list()
        list2.length = 3
        list2.capacity = 20
        list2.array = [Song('3', 'a', 'b', 'c'), Song('4', 'a', 'b', 'c'), Song('5', 'a', 'b', 'c')]
        list1 = sort(list1, less_than_number_first)
        self.assertEqual(list1, list2)
    
    def test_foreach(self):
        list1 = empty_list()
        list1.length = 5
        list1.capacity = 15
        list1.array = [1, 2, 3, 4, 5]
        def add_one(val):
            return val + 1
        foreach(list1, add_one)
        list2 = empty_list()
        list2.length = 5
        list2.capacity = 15
        list2.array = [1, 2, 3, 4, 5]
        self.assertEqual(list1, list2)

    def test_empty(self):
        list1 = empty_list() 
        list1.length = 5 
        list1.capacity = 15 
        list2 = empty_list() 
        list3 = empty_list()
        self.assertEqual(list1.length, 5)
        self.assertEqual(list1.capacity, 15) 
        self.assertEqual(list2, list3) 

    def test_length(self):
        list1 = List()
        list1.length = 5
        self.assertEqual(length(list1), 5)
        self.assertEqual(length(None), 0)

    def test_get(self):
        list1 = List()
        list1.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list1.length = 10
        self.assertEqual(get(list1, 1), 2)
        list3 = List()
        list3.array = [1, 2, 3]
        list3.length = 3
        list4 = List()
        list4.array = [9, 2, 5]
        list4.length = 2
        with self.assertRaises(IndexError):
            get(list3, 5) 
        with self.assertRaises(IndexError):
            get(list3, -1)
        with self.assertRaises(IndexError):
            get(empty_list(), 0)
        self.assertRaises(IndexError, get, list4, 2)
        list5 = List()
        list5.length = 5
        list5.capacity = 6
        list5.array = [None, None, None, 5]
        list6 = List()
        list6.length = 4
        list6.capacity = 10
        list6.array = [1, 2, 3, 4]
        self.assertEqual(get(list6, 3), 4)

    def test_add(self):
        list1 = List()
        list1.array = [1, 3, 4, 5, 6, 7, 8, 9, 10]
        list1.length = 9
        list1.capacity = 10
        list2 = List()
        list2.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list2.length = 10
        list2.capacity = 10
        list3 = List()
        list3.array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list3.length = 11
        list3.capacity = 20
        list4 = List()
        list4.array = [1, 2, 3, 4]
        list4.length = 4
        list4.capacity = 10
        list5 = List()
        list5.array = [1, 2, 3, 4, 5]
        list5.length = 5
        list5.capacity = 10
        list6 = List()
        list6.length = 2
        list6.capacity = 10
        list6.array = [None, 1, None, 3]
        list7 = List()
        list7.length = 3
        list7.capacity = 10
        list7.array = [None, 1, 1, 3]
        list8 = List()
        list8.length = 1
        list8.capacity = 10
        list8.array = [None, None, None, 5, None]
        list9 = List()
        list9.length = 2
        list9.capacity = 10
        list9.array = [None, None, None, 5, 6]
        list10 = List()
        list10.length = 2
        list10.capacity = 10
        list10.array = [4, 5]
        list11 = List()
        list11.length = 3
        list11.capacity = 10
        list11.array = [4, 3, 5]
        list12 = List()
        list12.array = [2, 3, 4]
        list12.length = 3
        list12.capacity = 10
        list13 = List()
        list13.array = [2, 3, 4, 5]
        list13.length = 4
        list13.capacity = 10
        list14 = List()
        list14.length = 4
        list14.array = [2, 3, 4, 6]
        list14.capacity = 10
        list15 = List()
        list15.length = 3
        list15.array = [3, 4, 5]
        list15.capacity = 10
        list16 = List()
        list16.length = 4
        list16.capacity = 10
        list16.array = [0, 3, 4, 5]
        list17 = List()
        list17.length = 2
        list17.capacity = 10
        list17.array = [2, 3]
        list18 = List()
        list19 = List()
        list20 = List()
        list20.length = 4
        list20.capacity = 10
        list21 = List()
        list21.length = 5
        list21.capacity = 10
        list21.array = [1, 2, 3, 4, 5, None, None, None, None, None]
        list22 = List()
        list22.length = 5
        list22.array = [1, 2, 3, 4, 5, 6]
        list22.capacity = 10
        list23 = List()
        list23.length = 9
        list23.capacity = 10
        list23.array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        list24 = List()
        list24.length = 3
        list24.capacity = 10
        list24.array = [1, 2, 3]
        list25 = List()
        list25.length = 3
        list25.capcity = 10
        list25.array = [1, 2, 3, None, None, None, None, None, None, None]
        self.assertEqual(get(add(list25, 1, 1), 3), 3)
        self.assertEqual(get(add(list24, 0, 0), 3), 3)
        self.assertEqual(get(add(list23, 9, 10), 9), 10) 
        self.assertEqual(get(add(list22, 3, 9), 3), 9)
        self.assertEqual(get(add(list21, 5, 6), 5), 6)
        self.assertEqual(get(add(add(add(add(add(list19, 0, 1), 1, 3), 2, 3), 3, 5), 4, 6), 3), 5)
        self.assertEqual(get(add(add(add(add(list18, 0, 1), 1, 2), 2, 3), 3, 5), 3), 5)
        self.assertEqual(get(add(add(list17, 2, 4), 3, 5), 3), 5)
        self.assertEqual(get(add(list15, 0, 2), 3), 5)
        self.assertEqual(get(add(list14, 3, 5), 3), 5)
        self.assertEqual(get(add(list12, 3, 5), 3), 5)
        self.assertEqual(add(list10, 1, 3), list11)
        self.assertEqual(add(list1, 1, 2), list2)
        self.assertEqual(add(list2, 0, 0), list3) 
        self.assertEqual(add(list4, 4, 5), list4)
        self.assertEqual(add(list6, 2, 1), list7)
        with self.assertRaises(IndexError):
            add(list1, 100, 1)
        list6 = List()
        list6.array = [12, 4, 5]
        list6.length = 2
        list6.capcity = 10
        self.assertEqual((add(add(empty_list(), 0, 12), 1, 4)), list6)
        self.assertRaises(IndexError, set, list6, 2, 5)
        self.assertRaises(IndexError, set, List(), 1, 12)

    def test_set(self):
        list1 = List()
        list1.array = [1, 1, 3, 4, 5, 6, 7, 8, 9, 10]
        list1.length = 10
        list1.capacity = 10
        list2 = List()
        list2.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list2.length = 10
        list2.capacity = 10
        self.assertEqual(set(list1, 1, 2), list2)
        with self.assertRaises(IndexError):
            set(list1, -2, 1)
        with self.assertRaises(IndexError):
            set(list1, 11, 1)

    def test_remove(self):
        list1 = List()
        list1.array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list1.length = 11
        list1.capacity = 20
        list2 = List()
        list2.array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list2.length = 10
        list2.capacity = 20
        list3 = List()
        list3.array = [1, 3, 4, 5, 6, 7, 8, 9, 10]
        list3.length = 9
        list3.capacity = 20
        self.assertEqual(remove(list1, 0), (0, list2))
        self.assertEqual(remove(list2, 1), (2, list3))
        with self.assertRaises(IndexError):
            remove(list1, 100)

if __name__ == '__main__':
    unittest.main()
