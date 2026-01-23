import pandas as pd
sales_df = pd.read_csv("task\\sales_data.csv")
sales_df['TotalSales'] = sales_df['Quantity'] * sales_df['Price']
1.category_stats = sales_df.groupby('Category').agg(
    total_quantity_sold=('Quantity', 'sum'),
    avg_price=('Price', 'mean'),
    max_quantity_single_transaction=('Quantity', 'max')
)

print("Category Statistics:")
print(category_stats)
2.top_products = (
    sales_df.groupby(['Category', 'Product'])['Quantity']
    .sum()
    .reset_index()
    .sort_values(['Category', 'Quantity'], ascending=[True, False])
    .groupby('Category')
    .first()
)

print("\nTop-selling product in each category:")
print(top_products)
3.daily_sales = sales_df.groupby('Date')['TotalSales'].sum()
max_sales_date = daily_sales.idxmax()

print("\nDate with highest total sales:", max_sales_date)


orders_df = pd.read_csv("task\\customer_orders.csv")

1.customer_order_counts = orders_df.groupby('CustomerID')['OrderID'].count()
active_customers = customer_order_counts[customer_order_counts >= 20]

filtered_customers = orders_df[orders_df['CustomerID'].isin(active_customers.index)]
print("Customers with 20+ orders:")
print(filtered_customers)
2.avg_price_per_customer = orders_df.groupby('CustomerID')['Price'].mean()
premium_customers = avg_price_per_customer[avg_price_per_customer > 120]

print("\nCustomers with avg price > $120:")
print(premium_customers)
3.product_totals = orders_df.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', 'sum')
)

filtered_products = product_totals[product_totals['total_quantity'] >= 5]

print("\nFiltered products (total quantity >= 5):")
print(filtered_products)

import sqlite3

conn = sqlite3.connect("task\\population.db")

population_df = pd.read_sql_query("SELECT * FROM population", conn)

conn.close()

1.import sqlite3

conn = sqlite3.connect("task\\population.db")

population_df = pd.read_sql_query("SELECT * FROM population", conn)

conn.close()
2.salary_bands_df = pd.read_excel("task\\population salary analysis.xlsx")
3.def assign_salary_band(salary):
    for _, row in salary_bands_df.iterrows():
        if row['MinSalary'] <= salary <= row['MaxSalary']:
            return row['SalaryCategory']
    return "Unknown"

population_df['SalaryCategory'] = population_df['Salary'].apply(assign_salary_band)
4.total_population = len(population_df)

salary_analysis = population_df.groupby('SalaryCategory').agg(
    percentage=('Salary', lambda x: (len(x) / total_population) * 100),
    avg_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median'),
    population_count=('Salary', 'count')
)

print("\nGlobal Salary Analysis:")
print(salary_analysis)
4.state_salary_analysis = population_df.groupby(['State', 'SalaryCategory']).agg(
    percentage=('Salary', 'count'),
    avg_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median'),
    population_count=('Salary', 'count')
)


state_totals = population_df.groupby('State').size()

state_salary_analysis['percentage'] = (
    state_salary_analysis['percentage'] /
    state_salary_analysis.index.get_level_values('State').map(state_totals) * 100
)

print("\nSalary Analysis by State:")
print(state_salary_analysis)

