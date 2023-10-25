import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sales data from the CSV file
data = pd.read_csv("Sales Data.csv")

# Data Preprocessing (basic data cleaning)
data.dropna(inplace=True)  # Handle missing values
data.drop_duplicates(inplace=True)  # Handle duplicates

# Sales Trends Analysis
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Month'] = data['Order Date'].dt.month
monthly_sales = data.groupby('Month')['Sales'].sum()

# Visualize monthly sales trends
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel ('Sales')
plt.grid()
plt.show()

# Best-Selling Products Analysis
product_sales = data.groupby('Product')['Sales'].sum().sort_values(ascending=False)

# Visualize top-selling products
plt.figure(figsize=(10, 6))
product_sales.head(10).plot(kind='bar', title='Top-Selling Products')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.xticks(rotation=45)

# Add product names to the bar graph
top_products = product_sales.head(10).index  # Get the top 10 product names
plt.xticks(range(10), top_products)  # Replace the x-axis labels with product names

plt.show()

# Calculate total sales
total_sales = data['Sales'].sum()

# Data Visualization
# - Create clear and informative data visualizations
# - Use appropriate charts and graphs to present your findings
# - Example: Visualize geographical distribution of sales by city
plt.figure(figsize=(12, 6))
sns.barplot(x='Sales', y='City', data=data)
plt.title('Geographical Distribution of Sales by City')
plt.xlabel('Sales')
plt.ylabel('City')
plt.show()

# Statistical Analysis (if applicable)
# - Perform statistical tests, such as hypothesis testing, to draw conclusions
# - Example: Test if there's a significant difference in sales between cities

# Machine Learning (Optional)
# - Build predictive models if necessary
# - Example: Predict future sales based on historical data

# Report and Recommendations
print("Total Sales: $", total_sales)
# - Summarize key insights and findings
# - Provide actionable recommendations for optimizing sales strategies
# - Example: Recommend increasing marketing efforts in top-selling cities
