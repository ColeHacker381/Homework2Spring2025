from typing import List, Tuple

def histogram(input_dictionary: dict) -> list:
    # data is a dictionary that contains the following keys: 'data', 'n', 'min_val', 'max_val'
    # n is an integer
    # min_val and max_val are floats
    # data is a list

    # Write your code here

    #Set the variables from dictionary
    data = input_dictionary['data']
    n = input_dictionary['n']
    min = input_dictionary['min_val']
    max = input_dictionary['max_val']

    #Set up the error checking for the min and max and n intervals
    if min == max:
        print("Error: min_val and max_val are the same value")
        return []
    elif n <= 0:
        return []
    elif min > max:
        temp = min
        min = max
        max = temp

    #initialize 0 list
    hist = [0] * n
    w = (max - min) / n

    #Iterate over each data point, and check if the point is in the range of the width of the bar length
    #if it is, increase the histogram frequency by 1 point
    for data_point in data:
        i = 0
        if data_point <= min or data_point >= max:
            continue
        while not (data_point >= (min + i*w) and  data_point < (min + (i+1)*w)):
            i += 1
        hist[i] += 1


    return hist
    # return the variable storing the histogram
    # Output should be a list

# Here, the function first checks if the lower and upper bounds are the same, 
# if they are it prints an error message and returns an empty list. 
# If lower bound is greater than upper bound, it swaps their values. 
# If number of bins is less than or equal to 0, it returns an empty list. 
# Then it initializes an empty list hist of length n and calculates the width of each bin. 
# Then it iterates through the data, 
# and for each value checks if it is within the range of the histogram and if it is, 
# it increments the bin it belongs to. Finally, it returns the histogram.

def combine_birthday_data(person_to_day: List[Tuple[str, int]], 
                          person_to_month: List[Tuple[str, int]], 
                          person_to_year: List[Tuple[str, int]]) -> dict:
    #person_to_day, person_to_month, person_to_year are list of tuples

    # Write your code here

    #Initialize a set in order to have no repeats, as well as the dictionary and list for ordering.
    month_set = set()
    month_to_people_data = {}
    person_list = []

    #Iterate over the month list, and retrieve the name of the person and month born.
    #Add the month to a set, and use the names to retrieve the day, year, and age, and
    #append a tuple of the data to a list.
    for persons_month in person_to_month:
        try:
            name = persons_month[0]
            month = persons_month[1]
            month_set.add(month)
        except:
            continue
        for persons_day in person_to_day:
            if persons_day[0] == name:
                day = persons_day[1]
        for persons_year in person_to_year:
            if persons_year[0] == name:
                year = persons_year[1]
                age = 2025 - year

        person_list.append((name, day, month, year, age))

    #Take the month set and sort it into a list
    month_list = sorted(list(month_set))
    for month in month_list:
        month_to_people_data[month] = ''

    #Iterate over the month set, and for each month check every person in the person_list
    #To see if they have the month that correlates to the month in the iteration. If this
    #is found, and there is no other tuples in the dictionary object, add one. If there is,
    #append it to the list.
    for month in month_list:
        for person in person_list:
            if person[2] == month and month_to_people_data[month] == '':
                month_to_people_data[month] = [(person[0], person[1], person[3], person[4])]
            elif person[2] == month and month_to_people_data[month] != '':
                month_to_people_data[month].append((person[0], person[1], person[3], person[4]))

    #If there is a single tuple in a list in the object, take it out of the list.
    for people in month_to_people_data:
        if len(month_to_people_data[people]) == 1:
            month_to_people_data[people] = month_to_people_data[people][0]

    # return the variable storing output
    # Output should be a dictionary

    return month_to_people_data

# We first define the current year as 2024, which will be used to calculate the age of each person later on.
# We create an empty dictionary month_to_people_data that will store the final data in the format specified in the problem statement.
# We iterate over the both values in the tuple of the person_to_month list (note that person_to_month is a list of tuples, which means each item in the list is a tuple) 
# using a for loop. For each iteration, we extract the corresponding day, year and age values from the person_to_day and person_to_year lists using the current name as the "key".
# We then use the current month as the key and a tuple of (name, day, year, age) as the value to update the month_to_people_data dictionary.
# Only change the value to a list data type, when there are multiple entries with the same key. This will help append for other tuples to the same month.
# Finally, we return the month_to_people_data dictionary as the output of the function.