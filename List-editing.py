
#dict = {'blue commander': [1,2,3,4,5], 'red commander': [6,7,8,9,0]}

def startMain():
        print('A list will be created; give a name.')
        dictionary = dictionarymake(ListName(), ListProduct())  # the dictionary is created and at this point contains one name&list entry
        while True:                     # loop allows for names&lists to be continually created and added to the dictionary
                print('Add another list?')
                choice = input('--> ')
                if choice in ('yes', 'Yes'):
                        dictionary.update({ListName() : ListProduct()}) # name&list entry is created and added to the dictionary
                        True
                else:
                        break           # loop brakes here if user does not respond with yes 
        print (f'You have created these lists:')
        for i in dictionary.keys():     # loop which prints all the keys (names of lists) currently in the dictionary 
                print (i)
        print ('\nWould you like to edit one of these lists')
        choice2 = input('--> ')
        if choice2 in ('yes', 'Yes'):   # option to edit lists
                dictEdit(dictionary) # execute list editor here
        else:
                print('ok bro why\'d you even bother making a list :|')
        
        # edit another list

def dictEdit(dict_):    # parameter is a dictionary
        # main function for editing lists within dictionary
        print ('Which list would you like to edit?')
        for i in dict_.keys():
                print (i)
        edit_choice = input('\n--> ')
        print(f'This is the current state of the list:       {dict_.get(edit_choice)}')

        ''' Things to do to lists:
        add things
        remove things
        rename a list
        add more lists 
        delete lists
        '''

def ListName():
        # create a name which will be associated with a list from ListProduct()
        print('What would you like the list name to be?')
        new_name = input('--> ')
        return new_name
      
def ListProduct():
        # create a list which will be associated with a name from ListName()
        List = []
        return List

def dictionarymake(name, list): # parameters 'name' will be used a key and 'list' will be used as a value for the given key
        # creates a dictionary where a name is associated with a list
        list_names = {}  # dictionary created
        list_names[name] = list   # adds entry to the dictionary with the corresponding function parameters
        return list_names

startMain()