import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# EDA: Visualize sales trends over time
def visualize_sales_trends(data):
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    data['Month'] = data['Order Date'].dt.month
    monthly_sales = data.groupby('Month')['Sales'].sum()

    # Visualize monthly sales trends
    plt.figure(figsize=(12, 6))
    monthly_sales.plot(kind='line', marker='o')
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid()
    plt.show()

# EDA: Identify best-selling products
def identify_best_selling_products(data):
    product_sales = data.groupby('Product')['Sales'].sum().sort_values(ascending=False)

    # Visualize top-selling products
    plt.figure(figsize=(10, 6))
    product_sales.head(10).plot(kind='bar', title='Top-Selling Products')
    plt.xlabel('Product')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    top_products = product_sales.head(10).index
    plt.xticks(range(10), top_products)
    plt.show()

# Calculate revenue metrics
def calculate_revenue_metrics(data):
    total_sales = data['Sales'].sum()
    # Calculate profit margins and other metrics if available in your data
    return total_sales

# Data Visualization
def create_data_visualizations(data):
    # Example: Visualize geographical distribution of sales by city
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Sales', y='City', data=data)
    plt.title('Geographical Distribution of Sales by City')
    plt.xlabel('Sales')
    plt.ylabel('City')
    plt.show()
