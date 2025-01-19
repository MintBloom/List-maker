def main():
        print('A list will be created; give a name.')
        dictionary = dictionarymake(chName(), ListProduct())
        while True:
                dictionary[chName()] = ListProduct()
                print('Add another?')
                choice = input('--> ')
                if choice in ('yes', 'Yes'):
                        True
                else:
                        break
        print (dictionary)
        
        # edit another list

def chName():
        print('What would you like the list name to be?')
        new_name = input('-->' )
        return new_name
      
def ListProduct():
        List = []
        return List

def dictionarymake(name, list):
        list_names = {}
        list_names[name] = list
        return list_names

main()