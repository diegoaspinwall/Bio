#Diego Aspinwall
#1-12-18
#gradeCalculator.py

curgrade = int(input('Your current grade (%): '))
want = int(input('You want at least (%): '))
per = int(input('Your final is worth (%): '))
print('You  need to score at least', str(round((-1/(per/100))*((-1)*want+(1-(per/100))*curgrade),1))+'% on your final to get a', str(want)+'% overall.')
