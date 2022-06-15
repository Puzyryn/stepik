"""
В то далёкое время, когда Паша ходил в школу, ему очень не нравилась формула Герона для вычисления площади треугольника, так как казалась слишком сложной. В один прекрасный момент Павел решил избавить всех школьников от страданий и написать и распространить по школам программу,
вычисляющую площадь треугольника по трём сторонам.
Одна проблема: так как эта формула не нравилась Павлу, он её не запомнил.
Помогите ему завершить доброе дело и напишите программу, вычисляющую площадь треугольника по переданным длинам трёх его сторон по формуле Герона.
"""
# put your python code here
import math
a = int (input())
b = int (input())
c = int (input())
p = (a+b+c)/2
S = math.sqrt(p * (p-a) * (p-b) * (p-c))
print(S)


"""
Напишите программу, принимающую на вход целое число, которая выводит True, 
если переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞) и 
False в противном случае (регистр символов имеет значение).
""" 
# put your python code here
X = int(input())
if X <= 12 and X > -15:
    print('True')
elif X > 14 and X < 17:
    print('True')
elif X >= 19:
    print('True')
else:
    print('False')