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


def persistence(number):
    # This is a recursive function
    if type(number)==int:
        # The base case when the number contains only one digits
        if len(str(number))==1:
            return 0


        # The recursive case
        else:
            # Convert the number into a string to be able to iterate through digits
            num_into_str = str(number)

            # Initializing the product of digits to 1
            product = 1
            
            for num in num_into_str:
                '''
                Iterating through digits (because now the number is considered as a string)
                Multiplying all the digits together after first converting each one of them into an integer
                '''
                product = product*int(num)
            '''
            returnin 1  because the multiplication occured and calling again the function.
            if the product now contains one digit only, the function will return 1, otherwise it will perfom 
            the multiplication again and add another 1 to the old 1 we had previously.
            the function keeps doing so until we have only one digit in the number, and we get the number 
            of how many times the multiplication occured
            '''
            return 1 + persistence(product)
    else:
        return "Please enter an integer"
            

        

        