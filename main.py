from data_preprocessing import load_and_preprocess_sales_data
import eda

def main():
    # Load and preprocess the sales data
    data = load_and_preprocess_sales_data("Sales_Data.csv")

    # Exploratory Data Analysis
    eda.visualize_sales_trends(data)
    eda.identify_best_selling_products(data)

    # Calculate revenue metrics
    total_sales = eda.calculate_revenue_metrics(data)
    print("Total Sales: $", total_sales)
    
    # Additional analysis and reporting can be added here

if __name__ == "__main__":
    main()
