grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades):
    for grade in grades:
        print grade,


print "grades",print_grades(grades)


def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total


print "sum of grades", grades_sum(grades)


def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average
print "average of grades",grades_average(grades)

def grades_variance(scores):
    average = grades_average(scores)
   #print "average of grades", average
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance /= len(scores)
    return variance


print "variance of grades", grades_variance(grades)


def grades_std_deviation(variance):
    return variance ** .5


variance = grades_variance(grades)

print "standard deviation of grades", grades_std_deviation(variance)
