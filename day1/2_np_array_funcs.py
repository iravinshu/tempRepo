from traceback import print_tb

import numpy as np
marks = np.array([55,68,72,49,83,91,37,65,78,59,88])
# print(marks)
# print(marks[8])
# print(marks[1:5])
# print(marks[:5])
marks[:3] = 75
# print(marks)
result = marks + 5
# print(result)
copied = marks.copy()
marks[9] =1
shallowed = marks
# print(copied)
# print(marks)
# print(shallowed)
passed = marks >= 65
# print(passed)
# print(marks[passed])
arr = np.arange(0,10)
# print(arr)
# print(arr + arr)
#
# print(arr * arr)
#
# print(arr - arr)

# print(arr / arr)

# print(arr ** 3)
#
# print(np.sqrt(arr))
arr = np.array([2,1,4,2,5,3,6,37,3,4])
sorted = np.sort(arr)
# print(sorted)
rev_sorted = np.sort(arr)[::-1]
# print(rev_sorted)
students = np.array([
    ('Alice',95,20),
    ('Bob',85,30),
    ('Charlie',70,40)
],dtype=[('name','U10'),('marks','i4'),('age','i4')])
print(students)
# print(students['name'])
# print(students[0][1])
# print(students['age'].mean())
# print(students[students['name']=='Bob']['marks'])
sales = [0,5,155,0,518,616]
sales_arr = np.array(sales)
print(sales_arr)
# sales_arr.resize((3,2,1))
# print(type(sales_arr))
# print(sales_arr.shape)
# print(sales_arr.ndim)
# print(sales_arr.size)
# print(sales_arr.dtype)
res_arr = np.where(sales_arr == 0,'no_sales','Some_sales')
print(res_arr)