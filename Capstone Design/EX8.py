class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other.data:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other.data:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)

    def issubset(self, other):
        for x in self.data:
            if x not in other.data :
                return False
        return True
    
    def issuperset(self, other):
        return other.issubset(self)

    def intersection_update(self, other):
        res = [x for x in other.data if x in self.data]
        return Set(res)
    
    def difference_update(self, other):
        res = [x for x in self.data if x not in other.data]
        return Set(res)

    def symmetric_difference_update(self, other):
        sub = self & other
        res = [x for x in self.data if not x in sub]
        res += [y for y in other.data if not y in sub]
        return Set(res)

    def add(self, elem):
        self.concat([elem])

    def remove(self, elem):
        try:
            del self.data[self.data.index(elem)]
        except ValueError as e:
            print(e)
            pass

    
    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __le__(self, other):    return self.issubset(other)                                     # self  <= other
    def __lt__(self, other):    return self.issubset(other) and not len(self) == len(other)     # self  <  other
    def __ge__(self, other):    return self.issuperset(other)                                   # self  >= other
    def __gt__(self, other):    return self.issuperset(other) and not len(self) == len(other)   # self  >  other
    def __ior__(self, other):   
        self = self.union(other)                # self |= other
        return self
    def __isub__(self, other):  
        self = self.difference_update(other)    # self -= other
        return self
    def __iand__(self, other):  
        self = self.intersection_update(other)  # self &= other
        return self
    def __ixor__(self, other):  
        self = self.symmetric_difference_update(other)  # self ^= other
        return self
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:
    
if __name__ == '__main__':
    x = Set([1,3,5,7, 1, 3])
    y = Set([2,1,4,5,6])
    print(x, y, len(x))
    print(x.intersection(y), y.union(x))
    print(x & y, x | y)
    print(x[2], y[:2])
    for element in x:
        print(element, end=' ')
    print()
    print(3 not in y)  # membership test
    print(list(x))   # convert to list because x is iterable

    #------------subset test------------#
    print('='*30)
    print('subset test')
    print('='*30)
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,6])
    print('x = ',x);print('y = ',y)
    
    print('\ny is subset of x?: ',y.issubset(x))
    print('y<=x?',y<=x)
    print('y<x?',y<x)

    print('\nx is subset of y?: ',x.issubset(y))
    print('x<=y',x<=y)
    print('x<y',x<y)
   
    print('\ny is superset of x?: ',y.issuperset(x))
    print('y>=x?', y>=x)
    print('y>x?', y>x)
   
    print('\nx is superset of y?', x.issuperset(y))
    print('x>=y?', x>=y)
    print('x>y', x>y)
    print()
    x = Set([1, 4, 6, 6, 3, 1])
    y = Set([1,3,6,5,7])
    print('x = ',x);print('y = ',y)
    print('\ny is subset of x?: ',y.issubset(x))
    print('y<=x?',y<=x)
    print('y<x?',y<x)

    print('\nx is subset of y?: ',x.issubset(y))
    print('x<=y',x<=y)
    print('x<y',x<y)

    print('\ny is superset of x?: ',y.issuperset(x))
    print('y>=x?', y>=x)
    print('y>x?', y>x)

    print('\nx is superset of y?', x.issuperset(y))
    print('x>=y?', x>=y)
    print('x>y', x>y)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,6,5])
    print('x = ',x);print('y = ',y)
    print('\ny is subset of x?: ',y.issubset(x))
    print('y<=x?',y<=x)
    print('y<x?',y<x)

    print('\nx is subset of y?: ',x.issubset(y))
    print('x<=y',x<=y)
    print('x<y',x<y)

    print('\ny is superset of x?: ',y.issuperset(x))
    print('y>=x?', y>=x)
    print('y>x?', y>x)

    print('\nx is superset of y?', x.issuperset(y))
    print('x>=y?', x>=y)
    print('x>y', x>y)

    #---------- set |= other test ----------#
    print('='*30)
    print('set |= other test')
    print('='*30)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,6])
    print('x = ',x);print('y = ',y)
    x|=y
    print('\nafter x|=y, x is',x)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,6,5,7])
    print('x = ',x);print('y = ',y)
    x|=y
    print('\nafter x|=y x is',x)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,6,5])
    print('x = ',x);print('y = ',y)
    x|=y
    print('\nafter x|=y x is',x)

    #----------- set &= other test ----------#
    print('='*30)
    print('set &= other test')
    print('='*30)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,6])
    print('x = ',x);print('y = ',y)
    x&=y
    print('\nafter x&=y, x is',x)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,4,8,7])
    print('x = ',x);print('y = ',y)
    x&=y
    print('\nafter x&=y x is',x)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,6,5])
    print('x = ',x);print('y = ',y)
    x&=y
    print('\nafter x&=y x is',x)

    #----------- set -= other test ----------#
    print('='*30)
    print('set -= other test')
    print('='*30)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,6])
    print('x = ',x);print('y = ',y)
    x-=y
    print('\nafter x-=y, x is',x)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,4,8,7])
    print('x = ',x);print('y = ',y)
    x-=y
    print('\nafter x-=y x is',x)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,6,5])
    print('x = ',x);print('y = ',y)
    x-=y
    print('\nafter x-=y x is',x)

    #----------- set ^= other test ----------#
    print('='*30)
    print('set ^= other test')
    print('='*30)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,6])
    print('x = ',x);print('y = ',y)
    x^=y
    print('\nafter x^=y, x is',x)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,4,8,7])
    print('x = ',x);print('y = ',y)
    x^=y
    print('\nafter x^=y x is',x)
    print()
    x = Set([1, 5, 6, 6, 3, 1])
    y = Set([1,3,6,5])
    print('x = ',x);print('y = ',y)
    x^=y
    print('\nafter x^=y x is',x)

    #---------- add and remove operation ----------#
    print('='*30)
    print('add and remove test')
    print('='*30)
    x = Set([1, 5, 6, 6, 3, 1])
    print()
    print('The First x = ',x)
    print('\nbefore add', x)
    print('add element 7')
    x.add(7)
    print('after add',x)
    print('\nbefore add', x)
    print('add element 5')
    x.add(5)
    print('after add',x)

    print('\nbefore remove', x)
    print('remove 9')
    x.remove(9)
    print('after remove', x)
    print('\nbefore remove', x)
    print('remove 5')
    x.remove(5)
    print('after remove', x)