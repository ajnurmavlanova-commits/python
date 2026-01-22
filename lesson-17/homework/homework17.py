Homework 1
import pandas as pd
import numpy as np

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
1.df = df.rename(columns={
    'First Name': 'first_name',
    'Age': 'age'
})
2.print(df.head(3))
3.mean_age = df['age'].mean()
print("Mean age:", mean_age)
4.print(df[['first_name', 'City']])
5.df['Salary'] = np.random.randint(3000, 7000, size=len(df))
print(df)
6.print(df.describe())
Homework 2
1.data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)
print(sales_and_expenses)
2.print("Maximum Sales:", sales_and_expenses['Sales'].max())
print("Maximum Expenses:", sales_and_expenses['Expenses'].max())
3.print("Minimum Sales:", sales_and_expenses['Sales'].min())
print("Minimum Expenses:", sales_and_expenses['Expenses'].min())
4.print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())
Homework 3
1.data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)
2.expenses = expenses.set_index('Category')
print(expenses)
3.print("Maximum expense per category:")
print(expenses.max(axis=1))
4.print("Minimum expense per category:")
print(expenses.min(axis=1))
5.print("Average expense per category:")
print(expenses.mean(axis=1))
