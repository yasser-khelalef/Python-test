def sum_of_int_str_items(list_of_strings):

    # In this function, list items that are already of type integer are accepted

    # Assuring that the input is a list
    if type(list_of_strings)==list:


        # Initializing the sum of the items to 0
        sum_of_items = 0

        for item in list_of_strings:
            # Iterating through each item of the list

            try:
                '''
                Using a try/except block to convert all the items into integers.
                If the item is actually an integer, the try block will execute and 
                the value of the item will be added.
                if the item cannot be converted into an integer, it will throw an error
                so the try block won't execute and will skip that item.

                This method is more efficient and reliable because it handles negative integers (string of int
                starts with a - sign), 
                unlike str.isdegit() str.isnumeric() functions, as well as handling inputs that start with + sign
                '''
                item = int(item)
                sum_of_items = sum_of_items + item
            except:
                pass

    else:
        return print("Please enter a valid input ( a list of strings )")

    return print("The sum of integer items in the given list is : ",sum_of_items)



    