#Diego Aspinwall
#1-12-18
#gradeCalculator.py

curgrade = int(input('Your current grade (%): '))
want = int(input('You want at least (%): '))
per = int(input('Your final is worth (%): '))
print('You  need to score at least', str((-1/per)*(-1*want+(100-per)*curgrade))+'% on your final to get a', str(want)+'% overall.')

''' want = per × Exam Score + (100% − per) × curgrade '''
#-perxExamScore = -want+ bla
#ExamScore = 1/-per(-want+bla)
