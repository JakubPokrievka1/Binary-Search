#!/usr/bin/python3

def user_input():
    try:
        value = int(input(">> "))
        return value
    except KeyboardInterrupt:
        return "KeyboardInterrupt"
    except ValueError:
        return "ValueError"



def random_number_generator():
    import random
    import time
    
    the_values = []

    number_of_values_to_generate = 0
    max_number_to_generate = 0

    try:
        for q in range(2):
            if q == 0:
                print("Enter how many values you want to randomly generate.")
                number_of_values_to_generate = user_input()
                if number_of_values_to_generate == "KeyboardInterrupt" or number_of_values_to_generate == "ValueError":
                    return number_of_values_to_generate
            else:
                print("Enter the maximum value the random number generator you want to generate.")
                print("NOTE: Please, enter a value that is higher than the maximum value used to generate the values.")
                max_number_to_generate = user_input()
                if max_number_to_generate == "KeyboardInterrupt" or max_number_to_generate == "ValueError":
                    return max_number_to_generate 
                    
        start = time.perf_counter()
        
        for i in range(number_of_values_to_generate):
            found = False
            
            if len(the_values) == 0:
                the_values.append(random.randint(0,max_number_to_generate))
            else:
                random_value = random.randint(0, max_number_to_generate)
                
                for c in range(len(the_values)):
                    if the_values[c] == random_value:
                        found = True
                        break
                
                if found == False:
                    the_values.append(random_value)
                    
        end = time.perf_counter()
        print(f"The time it took for the linear search and random number generator to complete: {end - start}s.")
        
        return the_values

    except KeyboardInterrupt:
        return "KeyboardInterrupt"



def bubble_sort():
    import time

    try:
        the_list = random_number_generator()
        
        length = len(the_list)
        
        if the_list != "KeyboardInterrupt" and the_list != "ValueError":
            start = time.perf_counter()
            
            for i in range(length - 1):
                swap = False
                for j in range(length - i - 1):
                    if the_list[j] > the_list[j + 1]:
                        the_list[j], the_list[j + 1] = the_list[j + 1], the_list[j]
                        swap = True 
                        
                if not swap:
                    break 
                
            
            end = time.perf_counter()
            print(f"The time it took for the bubble sort to complete: {end - start}s.")
            
            return the_list
        else:
            return the_list

    except KeyboardInterrupt:
        return "KeyboardInterrupt"



def binary_search():
    import time

    try:
        the_list = bubble_sort()
        
        if the_list == "ValueError" or the_list == "KeyboardInterrupt":
            return the_list
        else:
            found = False
            
            print("Enter a value you want to search.")
            value = user_input()
            if value != "KeyboardInterrupt" and value != "ValueError":
                start = time.perf_counter()
                
                while len(the_list) > 1:
                    midpoint = len(the_list) // 2
                    
                    if the_list[midpoint] == value:
                        found = True
                                
                        end = time.perf_counter()
                        print(f"The time it took for the binary search to complete: {end - start}s.")
                        
                        return midpoint
                    else:
                        if the_list[midpoint] > value:
                            the_list = the_list[:midpoint]
                        else:
                            the_list = the_list[midpoint:]
                        
                        
                end = time.perf_counter()
                print(f"The time it took for the binary search to complete: {end - start}s.")
                
                if found == False:
                    return "NotFound"
                        
            else:
                if value == "ValueError" or value == "KeyboardInterrupt":
                    return value
    except KeyboardInterrupt:
        return "KeyboardInterrupt"



def binary_search_output():
    the_output = binary_search()
    
    if the_output == "KeyboardInterrupt":
        print("Keyboard Interrupt!")
    elif the_output == "ValueError":
        print("Error: Value Error!")
    else:
        if the_output == "NotFound":
            print("The value has NOT been found.")
        else:
            print("The value has been found.")



def main():
    binary_search_output()



main()
