# iterates is preforming an action once for each of the things in the list

# [1, 5, 7, 8, 4, 3]

def iterate(list):
    # for each loop
    for item in list:
        print item
    
    # standard loop with range
    #for i in range(0, len(list)):
        #print list[i]


#def print_scores(names, scores):
#    for i in range(0, len(names)):
#        print names[i] , " scored " , scores[i]


def print_names_scores_ages(names, scores, ages):
    for i in range(0, len(names)):
        print names[i], " scored ", scores[i], " and is ", ages[i], " Years old."