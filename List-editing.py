

def main() -> None:
        dictionary = retrievedata()
        if type(dictionary) == dict: # if there is previous data no new dictionary is created
                pass
        else:
                dictionary = UserListCreate() # if no previous file is found, a dictionary is created with names&lists as its keys&values
        Pick_a_list(dictionary)

def Pick_a_list(dict_):    # parameter is a dictionary
        # main function for editing lists within dictionary
        print ('You have these lists: ')
        cycleThruKeys(dict_)
        print ('Which list would you like to edit?')
        edit_choice = input('\n--> ')
        print(f'This is the current state of {edit_choice}:       {dict_.get(edit_choice)}')
        choice_list = valueFromDict(edit_choice, dict_)


def retrievedata() -> dict:
        try:
                f = open('ListsInDictionaries.txt', 'r')
        except:
                print('No retrievable file. New file and list will be created.')
                return None
        incomingdata = f.read()
        f.close
        return incomingdata

def dumpdata(DataToDump) -> None:
        f = open('ListsInDictionaries.txt', 'w')
        f.write(DataToDump)
        f.close()




def cycleThruKeys(dict):
        # will return all the keys in the dictionary
        for i in dict.keys():
                print(i)

def valueFromDict(name, dict) -> list:
        # will return a single value from the dictionary
        list = dict.get(name)
        return list

def keyFromDict(name) -> str:
        # will return a single key from the dictionary
        None


def UserListCreate() -> dict:
        print('A list will be created; give a name.')
        dictionary = dictionarymake(ListName(), ListProduct())  # the dictionary is created and at this point contains one name&list entry
        while True:                     # loop allows for names&lists to be continually created and added to the dictionary
                print('Add another list?')
                choice = input('--> ')
                if choice in ('yes', 'Yes'):
                        dictionary.update({ListName() : ListProduct()}) # name&list entry is created and added to the dictionary
                        True
                else:
                        break           # loop breaks here if user does not respond with yes
        return dictionary

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

''' To do lists:
add things
remove things
rename a list
add more lists
delete lists
'''

if __name__ == '__main__':
        main()