import pandas
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
print(data.head())
