def percent(marks):
    p = ((sum(marks)/400)*100)
    return p

marks1 = [78,79,89,98]
percentage1 = percent(marks1)

marks2 = [78,79,89,90]
percentage2 = percent(marks2)

print(percentage1, percentage2)