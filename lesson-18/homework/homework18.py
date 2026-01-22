Homework 2
import pandas as pd

df = pd.read_csv('task\\stackoverflow_qa.csv')
1.df['creation_date'] = pd.to_datetime(df['creation_date'])

q1 = df[df['creation_date'].dt.year < 2014]
2.q2 = df[df['score'] > 50]
3.q3 = df[(df['score'] >= 50) & (df['score'] <= 100)]
4.q4 = df[df['answerer'] == 'Scott Boston']
5.users = ['Scott Boston', 'unutbu', 'DSM', 'Willem Van Onsem', 'jpp']

q5 = df[df['answerer'].isin(users)]
6.q6 = df[
    (df['creation_date'] >= '2014-03-01') &
    (df['creation_date'] <= '2014-10-31') &
    (df['answerer'] == 'unutbu') &
    (df['score'] < 5)
]
7.q7 = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) |
    (df['view_count'] > 10000)
]
8.q8 = df[df['answerer'] != 'Scott Boston']
Homework 3
titanic_df = pd.read_csv("task\\titanic.csv")
1.q1 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]
2.q2 = titanic_df[titanic_df['Fare'] > 100]
3.q3 = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
4.q4 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
5.q5 = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]
6.q6 = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]
7.q7 = titanic_df[
    (titanic_df['Cabin'].notna()) &
    (titanic_df['Fare'] > 200)
]
8.q8 = titanic_df[titanic_df['PassengerId'] % 2 == 1]
9.q9 = titanic_df[titanic_df['Ticket'].map(titanic_df['Ticket'].value_counts()) == 1]
10.q10 = titanic_df[
    (titanic_df['Name'].str.contains('Miss', na=False)) &
    (titanic_df['Pclass'] == 1)
]
