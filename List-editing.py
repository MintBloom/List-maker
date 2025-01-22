
import pickle

def main() -> None:
        dictionary = retrievedata()
        if type(dictionary) == dict: # if there is previous data no new dictionary is created
                pass
        else:
                dictionary = UserListCreate() # if no previous file is found, a dictionary is created with names&lists as its keys&values
        updated_dictionary = Pick_a_list(dictionary)
        dumpdata(updated_dictionary)
        print ('All done. Saved to a file :3')


def Pick_a_list(dict_):    # parameter is a dictionary
        # main function for editing lists within dictionary
        while True:
                print ('You have these lists: ')
                cycleThruKeys(dict_) # shows the names of all the lists which the user has created
                print ('Which list would you like to edit?')
                edit_choice = input('\n--> ')
                print(f'This is the current state of {edit_choice}:\n{dict_.get(edit_choice)}') # shows the list that the user has chosen to edit
                dict_.update({edit_choice:edit_list_menu(edit_choice, dict_)}) # will update the dictionary with the new list
                print('Save and quit the program?')
                choice = input('--> ')
                if choice in ('no', 'No'):
                        True
                else:
                        break
        return dict_




def retrievedata() -> dict:
        # retrieves data from a save, if file does not exist then nothing is returned
        try:
                with open('ListsInDictionaries.pkl', 'rb') as f:
                        loaded_dictf = pickle.load(f)
        except:
                print('No retrievable file. New file and list will be created.')
                return None
        f.close
        return loaded_dictf

def dumpdata(DataToDump) -> None:
        # saves the dictionary with lists in binary as a .pkl document using the pickle module
        with open('ListsInDictionaries.pkl', 'wb') as f:
                pickle.dump(DataToDump, f)
        f.close()





def edit_list_menu (name, dict):
        # enables loop which will allow for continuous editing of a list
        list = valueFromDict(name, dict)  # returns only the list from the dictionary
        while True:
                list = edit_list_menu_loop(list)
                print ('Quit editing this list?')
                choice = input('--> ')
                if choice in ('no', 'No'):
                        True
                else:
                        break
        return list # returns the new value of the list
                
def edit_list_menu_loop(list): # includes option which allows for a list to be edited times
        print ('What would you like to do? (Pick a number)')
        print ('- (1)Add something\n- (2)Add something in a particular position\n- (3)Delete somthing')
        choice = int(input())
        match choice:
                case 1:
                        list = add_to_list(list)
                        return list # returns new and updated list
                case 2:
                        list = add_to_listpos(list)
                        return list # returns new and updated list
                case 3:
                        list = del_from_list(list)
                        return list # returns new and updated list




        
def add_to_list(list):
        print('What would you like to add?')
        choice = input('--> ')
        list.append(choice)
        return list

def add_to_listpos(list):
        print ('Firstly, what would you like to add?')
        choice = input('--> ')
        print ('And to which position would you like to add this? Respond in digits. (BEWARE: The first position is 0)')
        choice_pos = int(input('--> '))
        list.insert(choice_pos, choice)
        return list

def del_from_list(list):
        print('What would you like to remove?')
        choice = input('--> ')
        list.remove(choice)
        return list





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
        dictionary = dictionarymake(ListName(), ListMake())  # the dictionary is created and at this point contains one name&list entry
        while True:                     # loop allows for names&lists to be continually created and added to the dictionary
                print('Add another list?')
                choice = input('--> ')
                if choice in ('yes', 'Yes'):
                        dictionary.update({ListName() : ListMake()}) # name&list entry is created and added to the dictionary
                        True
                else:
                        break           # loop breaks here if user does not respond with yes
        return dictionary

def ListName() -> str:
        # create a name which will be associated with a list from ListMake()
        print('What would you like the list name to be?')
        new_name = str(input('--> '))
        return new_name





def ListMake() -> list:
        # create a list which will be associated with a name from ListName()
        List = []
        return List

def dictionarymake(name, list) -> dict: # parameters 'name' will be used a key and 'list' will be used as a value for the given key
        # creates a dictionary where a name is associated with a list
        list_names = {}  # dictionary created
        list_names[name] = list   # adds entry to the dictionary with the corresponding function parameters
        return list_names

if __name__ == '__main__':
        main()