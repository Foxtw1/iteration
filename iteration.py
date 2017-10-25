# iterates is preforming an action once for each of the things in the list
# doing the same thing for each member of a list

# [1, 5, 7, 8, 4, 3]

def iterate(list):
    # for each loop
    for item in list:
        print item
    
    # standard loop with range
    #for i in range(0, len(list)):
        #print list[i]


def print_scores(names, scores):
    for i in range(0, len(names)):
        print names[i] , " scored " , scores[i]


def print_names_scores_ages(names, scores, ages):
    for i in range(0, len(names)):
        print names[i], " scored ", scores[i], " and is ", ages[i], " Years old."


def add_one(list):
    for i in range(0, len(list)):
        list[i] += 1

    return list


# Accumulation pattern
# Keep track of other data as we go
def sum(numbers):
    total = 0
    for n in numbers:
        total += n
        
    return total


def max(numbers):
    current_max = numbers[0]
    for n in numbers:
        if n > current_max:
            current_max = n
    
    return current_max


def average(numbers):
    total = 0
    for n in numbers:
        total += n
    
    return total / len(numbers)


def average_without_bottom_two_numbers(numbers):
    current_min = numbers[0]
    current_min_placement = -1
    for n in numbers:
        if n <= current_min:
            current_min = n

    numbers.remove(current_min)
    current_min2 = numbers[0]

    for n in numbers:
        if n <= current_min2:
            current_min2 = n
    
    numbers.remove(current_min2)
    
    sum_without_bottom_two_numbers = 0
    for n in numbers:
        sum_without_bottom_two_numbers += n

    return sum_without_bottom_two_numbers / len(numbers)