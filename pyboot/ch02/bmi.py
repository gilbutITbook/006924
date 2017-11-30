weight = 57
height = 1.7
bmi = weight / (height ** 2)

if bmi < 18.5:
    print ('말랐다')
elif bmi < 25:
    print ('보통')
elif bmi < 35:
    print ('약간 뚱뚱하다')
else:
    print('아주 뚱뚱하다')
