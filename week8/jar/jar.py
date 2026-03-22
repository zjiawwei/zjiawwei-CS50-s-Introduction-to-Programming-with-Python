class Jar:
    def __init__(self,capacity=12):
        if capacity < 0:
            raise ValueError("capacity is not a non-negative")
        self._capacity = capacity
        self._size = 0
    
    def __str__(self):
        return "🍪" * self._size

    def deposit(self,n):
        if n < 0:
            raise ValueError("cannot deposit negative cookies")
        if self._size + n > self._capacity:
            raise ValueError("exceed the cookie jar's capacity")
        self._size += n

    def withdraw(self,n):
        if n < 0:
            raise ValueError("cannot withdraw negative cookies")
        if self._size - n < 0:
            raise ValueError("there aren't that many cookies in the cookie jar")
        self._size -= n
    
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,value):
        if value < 0:
            raise ValueError("capacity cannot be negative")
        self._capacity = value
    
    @property
    def size(self):
        return self._size