import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
data = pd.read_csv("sales_data.csv")

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Monthly sales analysis
monthly_sales = data.groupby(data['Date'].dt.month)['Revenue'].sum()

print("Monthly Sales Report:")
print(monthly_sales)

# Plot monthly sales
monthly_sales.plot(kind='bar', title='Monthly Sales')
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
