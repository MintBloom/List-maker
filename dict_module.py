
def ListName() -> str:
        # create a name which will be associated with a list from ListProduct()
        print('What would you like the list name to be?')
        new_name = str(input('--> '))
        return new_name

def ListProduct() -> list:
        # create a list which will be associated with a name from ListName()
        List = []
        return List

def dictionarymake(name, list) -> dict: # parameters 'name' will be used a key and 'list' will be used as a value for the given key
        # creates a dictionary where a name is associated with a list
        list_names = {}  # dictionary created
        list_names[name] = list   # adds entry to the dictionary with the corresponding function parameters
        return list_names

def ListName() -> str:
        # create a name which will be associated with a list from ListProduct()
        print('What would you like the list name to be?')
        new_name = str(input('--> '))
        return new_name
