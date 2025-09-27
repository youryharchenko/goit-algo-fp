
class LList():

    
    def __init__(self, value=None):
        match value:
            case None | []:
                self.pair = None
                self.len = 0
            case tuple((_, _)):
                self.pair = value
                self.len = 1
            case list([*items]):
                self.pair = self.make_llist(items)
                self.len = len(items)
            case _:
                raise ValueError("value must be list or None" )
            
    def make_llist(self, items):
        l = len(items) 
        if l > 0:
            current = None
            for i in range(l, 0, -1):
                next = (items[i-1], current)
                current = next
            return current
        else:
            return None
        
    def cons(self, item):
        self.pair = (item, self.pair)
        self.len += 1
        return self
        
    def first(self):
        if self.pair is not None:
            return self.pair[0]
        else:
            return None
        
    def pop(self):
        if self.pair is not None:
            value = self.pair[0] 
            self.pair = self.pair[1]
            self.len -= 1
            return value 
        else:
            return None
        
    def tail(self):
        if self.pair:
            return LList(self.pair[1])
        else:
            return LList()
        
    def to_plist(self):
        plist = []
        current = self.pair
        while current is not None:
            plist.append(current[0])
            current = current[1]
        return plist
    
    # Цей метод створює новий список із зворотнім порядком елементів
    def reverse_new(self):
        result = LList()
        current = self.pair
        while current is not None:
            result.cons(current[0])
            current = current[1]
        return result
    
    # Цей метод робить зворотній порядок елементів по місцю, змінюючи посилання між вузлами
    def reverse_inplace(self):
        current = self.pair
        prior = None
        while current is not None:
            prior = (current[0], prior)
            current = current[1]
        self.pair = prior

    
    # Цей метод повертає новий відсортований список
    def insertion_sort(self):
        sorted, unsorted = LList(), LList(self.to_plist())
        
        while unsorted.len > 0:
            rev = LList()
            
            key = unsorted.pop()
            current = sorted.pair
            while current is not None:
                if key is not None and key < current[0]:
                    break
                else:
                    rev.cons(current[0])
                current = current[1]
            
            next = (key, current)
            rev_current = rev.pair
            while rev_current is not None:
                next = (rev_current[0], next)
                rev_current = rev_current[1]
            
            sorted.pair = next
            sorted.len += 1
            
        return sorted
    
    # Цей метод зливає два відсоротованих списки в новий відсортований список
    def merge(self, llist):
        left = LList(self.to_plist)
        right = LList(llist.to_plist)
        merged = LList()
        

        while left.len > 0 and right.len > 0 :
            left_first = left.first()
            right_first =  right.first()
            if left_first is not None and right_first is not None:
                if left_first <= right_first:
                    merged.cons(left.pop())
                else:
                    merged.cons(right.pop())

        while left.len > 0:
            merged.cons(left.pop())

        while right.len > 0:
            merged.cons(right.pop())

        merged.reverse_inplace
        return merged
    
   
    def __repr__(self):
        return f"{self.pair}"

def main():
    print(LList())
    print(LList([])) 
    print(LList([1])) 
    print(LList([1, 2])) 
    print(" "*8)

    print(LList().to_plist())
    print(LList([]).to_plist())
    print(LList([1]).to_plist()) 
    print(LList([1, 2]).to_plist()) 
    print(" "*8)

    print(LList().first())
    print(LList([]).first())
    print(LList([1]).first()) 
    print(LList([1, 2]).first()) 
    print(" "*8)

    print(LList().tail().to_plist())
    print(LList([]).tail().to_plist())
    print(LList([1]).tail().to_plist()) 
    print(LList([1, 2]).tail().to_plist())
    print(LList([1, 2, 3, 4]).tail().to_plist())
    print(" "*8)

    print(LList([1, 2, 3, 4]).cons(0).to_plist())
    print(" "*8)

    ll = LList().cons(0).cons(1)
    print(ll.to_plist())

    ll2 = LList([1, 2, 3, 4])
    print(ll2.to_plist())
    print(ll2.reverse_new().to_plist())

    ll3 = LList([1, 2, 3, 4])
    print(ll3.to_plist())
    ll3.reverse_inplace()
    print(ll3.to_plist())

    print(" "*8)

    ll4 = LList([5, 2, 1, 3, 4])
    print(ll4.to_plist())
    ll4_sorted = ll4.insertion_sort()
    print(ll4_sorted.to_plist())
    print(ll4.len)
    print(ll4.to_plist())


    

