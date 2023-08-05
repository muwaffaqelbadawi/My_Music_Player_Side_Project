# Here is the place where you can search for any song you want


class Search:
    message = "Search Song"
    entered_name = input(message)
    
    @classmethod
    def search(name, entered_name):
        return True if name == entered_name else False
        
    # @classmethod
    # def search():
    #     return list(filter(search, my_list_of_names))[0]