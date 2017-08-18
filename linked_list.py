# Justin Mo

# a Song is one of
# ~ number, title, artist, or album
class Song:
    def __init__(self, number, title, artist, album):
        self.number = number # an int
        self.title = title # a str
        self.artist = artist # a str
        self.album = album # a str

    def __repr__(self):
        return "{:n}--{:s}--{:s}--{:s}".format(int(self.number), self.title, self.artist, self.album)

    def __eq__(self, other):
        return type(other) == Song and self.number == other.number and self.title == other.title and self.artist == other.artist and self.album == other.album

# An AnyList is one of
# -- "None" or
# -- Pair(first, rest)
class Pair:
    def __init__(self, first, rest):
        self.first = first # any value
        self.rest = rest # anylist

    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.first, self.rest)

    def __eq__(self, other):
        return type(other) == Pair and self.first == other.first and self.rest == other.rest

# LinkedList function -> LinkedList
# takes in a list and a "less than" function and returns a sorted list in ascending order
def sort(linkedlist, func):
    if linkedlist == None:
        return None
    else:
        return insert(sort(linkedlist.rest, func), linkedlist.first, func)

# LinkedList value function -> LinkedList
# Takes in a sorted linked list, value, and function and returns the new linked list.
def insert_sorted(sortedlist, value, func):
    if sortedlist == None:
        return Pair(value, None)
    bool = func(value, sortedlist.first)
    if sortedlist.rest == None and bool:
        return Pair(value, Pair(sortedlist.first, None))
    elif sortedlist.rest == None and not bool:
        return Pair(sortedlist.first, Pair(value, None))
    elif bool:
        return Pair(value, sortedlist)
    else:
        return Pair(sortedlist.first, insert(sortedlist.rest, value, func))

# LinkedList value function -> LinkedList
# Takes in a sorted linked list, value, and function and returns the new linked list.
def insert(sortedlist, value, func):
    if sortedlist == None:
        return Pair(value, None)
    bool = func(value, sortedlist.first)	
    if sortedlist.rest == None and bool:
        return Pair(value, Pair(sortedlist.first, None))
    elif sortedlist.rest == None and not bool:
	    return Pair(sortedlist.first, Pair(value, None))
    elif bool:
        return Pair(value, sortedlist)
    else:
        return Pair(sortedlist.first, insert(sortedlist.rest, value, func))

#sortedlist.rest.value > value
#linkedlist == [2]
#acc == [1, 3]
# LinkedList function -> None
# takes in a List and a function and applies the provided function to the value at each position in the list
def foreach(linked_list, f):
    if linked_list is not  None:
        f(linked_list.first)
        foreach(linked_list.rest, f)

# None -> None
# takes in no arguments and returns an empty list
def empty_list():
    return None

# NumList -> int
# Takes in a anylist and returns the length of the list
def length(anylist):
    if anylist == None:
        return 0
    return 1 + length(anylist.rest)

# AnyList int value -> AnyList
# takes in anylist, an index, and a value and return a new anylist with the value inserted at the given index
def add(anylist, index, value, counter=0): 
    if index == 0:
        return Pair(value, anylist)
    if index == counter and anylist == None:
        return Pair(value, None)
    if index == counter:
        return Pair(value, anylist)
    if index < 0 or anylist == None:
        raise IndexError
    return Pair(anylist.first, add(anylist.rest, index, value, counter + 1))

# AnyList int -> int
# takes in anylist and an index and returns the value at the given index
def get(anylist, index, counter=0):
    if index < 0 or anylist == None:
        raise IndexError
    if index == counter:
        return anylist.first
    return get(anylist.rest, index, counter + 1)

# AnyList int value -> AnyList
# takes in anylist, an index, and a value and returns a new list where the value at the given index is replaced by the new given value
def set(anylist, index, value, counter=0):
    if index < 0 or anylist == None:
        raise IndexError
    if index == counter:
        return Pair(value, anylist.rest)
    return Pair(anylist.first, set(anylist.rest, index, value, counter + 1))

# AnyList int -> int
# takes in anylist and an index and returns the value of that index
def remove_helper(anylist, index):
    if anylist == None:
        raise IndexError
    if index > 0 and anylist.rest == None:
        raise IndexError
    if index == 0:
        return anylist.first
    return remove_helper(anylist.rest, index - 1)

# AnyList int -> Anylist
# takes in anylist and an index and returns a new anylist with the value at the given index removed
def remove_helper2(anylist, index):
    if anylist == None:
        raise IndexError
    if index > 0 and anylist.rest == None:
        raise IndexError
    if index == 0:
        return anylist.rest
    return Pair(anylist.first, remove_helper2(anylist.rest, index - 1))

# AnyList int -> tuple
# takes in anylist and an index and returns a tuple containing the value removed and the resulting list
def remove(anylist, index):
    if anylist == None:
        raise IndexError
    if anylist.rest == None and index > 0:
        raise IndexError
    else:
        return (remove_helper(anylist, index), remove_helper2(anylist, index))

# Song Song -> Boolean
# takes in two songs and returns a boolean based on whether the first song is less than the second song by number first
def less_than_number_first(s1, s2):
    return (int(s1.number) < int(s2.number))

# Song Song -> Boolean
# takes in two songs and returns a boolean based on whether the first song is less than the second song by title first
def less_than_title_first(s1, s2):
    if s1.title == s2.title:
        if s1.artist == s2.artist:
            if s1.album == s2.album:
                return (s1.number < s2.number)
            return (s1.album < s2.album)
        return (s1.artist < s2.artist)
    return (s1.title < s2.title)

# Song Song -> Boolean
# takes in two songs and returns a boolean based on whether the first song is less than the second song by artist first
def less_than_artist_first(s1, s2):
    if s1.artist == s2.artist:
        if s1.album == s2.album:
            if s1.title == s2.title:
                return (s1.number < s2.number)
            return (s1.title < s2.title)
        return (s1.album < s2.album)
    return (s1.artist < s2.artist)

# Song Song -> Boolean
# takes in two songs and returns a boolean based on whether the first song is less than the second song by album first
def less_than_album_first(s1, s2):
    if s1.album == s2.album:
        if s1.artist == s2.artist:
            if s1.title == s2.title:
                return (s1.number < s2.number)
            return (s1.title < s2.title)
        return (s1.artist < s2.artist)
    return (s1.album < s2.album)
