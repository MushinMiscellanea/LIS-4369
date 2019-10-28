def requirements():
    print('''1. Sets are mutable, unordered and heterogeneous. They can not hold duplicate values
2. Sets have insert, update, and delete methods
3. Sets cannot contain other mutable items like lists or dicts
4. Sets do not use indexing because they are unordered.
5. Create this program with sets''')

def print_type():
    # declare set using brackets
    my_set = {1, 'domino', 'domingo', 44.0, ('la', 'le', 'lo') }
    # declare set using built-in set method with brackets
    my_set1 = set([1, 2, 3, 'four', 'five'])
    # declare set using built in set() method using parenthasis
    my_set2 = set(('this', 'is', 'fun'))
    # printing sets to screen
    print(my_set)
    print(my_set1)
    print(my_set2)
    # printing set types to make sure they are sets
    print(type(my_set))
    print(type(my_set1))
    print(type(my_set2))
    #print length of set 1
    print(len(my_set))
    # deleting items in set using discard() and remove(). Discard does not raise a typeError if item is not found
    my_set.discard('domino')
    print(my_set)
    my_set.remove('domingo')
    print(my_set)
    print(len(my_set))
    # adding an element  to a set
    my_set.add('addition')
    # more deleting items in set
    my_set1.discard('four')
    my_set1.discard('five')
    print(len(my_set1))
    print(len(my_set))
    # python built in functions for comparing items in set. Must all be same datatype
    print(max(my_set1))
    print(min(my_set1))
    print(sum(my_set1))
    #using set function clear() to clear the set
    my_set1.clear()
    print(len(my_set1))
    
def main():
    requirements()
    print_type()

main()




