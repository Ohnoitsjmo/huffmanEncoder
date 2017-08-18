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

# ArrayList is a
# -- List
class List:
    def __init__(self):
        self.array = [None]*1000 # an array list
        self.length = 0 # an int
        self.capacity = 10 # an int

    def __repr__(self):
        c = "{:s}".format(str(self.array[0]))
        for i in self.array[1:self.length]:
            c += ", {:s}".format(str(i))
        return c

    def __eq__(self, other):
        if type(other) != List:
            return False
        else: 
            bool = True 
            for i in range(self.length - 1):
                if self.array[i] != other.array[i]:
                    bool = False
            return type(other) == List and bool and self.length == other.length and self.capacity == other.capacity

# ArrayList function -> ArrayList
# takes in a list and a "less than" function and returns a sorted list in ascending order
def sort(arraylist, func):
    if arraylist == None:
        return None
    else:
        for j in range(arraylist.length - 1):
            for i in range(arraylist.length - 1):
                bool = func(arraylist.array[arraylist.length - i - 1], arraylist.array[arraylist.length - i - 2])
                if bool == True:
                    larger_value = arraylist.array[arraylist.length - i - 2]
                    smaller_value = arraylist.array[arraylist.length - i - 1]
                    arraylist.array[arraylist.length - i - 2] = smaller_value
                    arraylist.array[arraylist.length - i - 1] = larger_value
        return arraylist


# ArrayList function -> None
# takes in a List and a function and applies the provided function to the value at each position in the list
def foreach(array_list, f):
    if array_list is not None:
        for each_value in range(array_list.length):
            f(array_list.array[each_value])

# None -> None
# takes in no arguments and returns an empty list
def empty_list():
    return List()

# ArrayList -> int
# takes in an array and returns the length of the list
def length(arraylist):
    if arraylist == None:
        return 0
    return arraylist.length

# ArrrayList int value -> ArrayList
# takes in an array, an index, and a value and returns a new array with the value inserted at the given index
def add(arraylist, index, value):
	arraylist.array += [None] * (arraylist.capacity - arraylist.length)
	if arraylist.length == 0  and index == 0:
		arraylist.array[index] = value
		arraylist.length += 1
		return arraylist
	if arraylist.length == index:
		arraylist.length += 1
		arraylist.array += [None]
		arraylist.array[index] = value
		return arraylist
	if arraylist.length != 0 and index >= 0 and arraylist.length >= index:
		if arraylist.length == arraylist.capacity:
			arraylist.capacity += 10
			new_array = [None] * (arraylist.capacity + 10)
			for i in range(arraylist.length):
				new_array[i] = arraylist.array[i]
			arraylist.array = new_array
		for i in range(arraylist.length):
			arraylist.array[arraylist.length - i] = arraylist.array[arraylist.length - i - 1]
		arraylist.array[index] = value
		arraylist.length += 1
		return arraylist
	else:
		raise IndexError

# ArrayList int -> int
# takes in array and an index and returns the value at that index
def get(arraylist, index):
    if arraylist.length <= index or index < 0:
        raise IndexError
    return arraylist.array[index]

# ArrayList int value -> ArrayList
# takes in arraylist, an index, and a value and returns a new list where the value at the given index is replaced by the new given value
def set(arraylist, index, value):
    if arraylist.length <= index or arraylist == List() or index < 0:
        raise IndexError
    arraylist.array[index] = value
    return arraylist

# ArrayList int -> tuple
# takes in arraylist and an index and returns a tuple containing the value removed and the resulting list
def remove(arraylist, index):
    if arraylist == List() or index < 0 or arraylist.length <= index:
        raise IndexError
    else:
        value = arraylist.array[index]
        arraylist.length -= 1
        for i in range(index, arraylist.length):
            arraylist.array[i] = arraylist.array[i + 1]
        return (value, arraylist)

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
