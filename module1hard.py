grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
res = sorted(students)
# print(res)
a = sum(grades[0])
b = sum(grades[1])
j = sum(grades[2])
dictionary = {'Aaron': a/len(grades[0]), 'Bilbo': b/len(grades[1]), 'Johnny': j/len(grades[2]),
              'Khendrik': sum(grades[3])/len(grades[3]), 'Steve': sum(grades[4])/len(grades[4])}
print(dictionary)