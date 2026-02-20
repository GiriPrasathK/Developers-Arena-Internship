from sales_analyzer.data_loader import load_data
from sales_analyzer.data_cleaner import clean_data
from sales_analyzer.analyzer import (
    total_sales, average_sale, top_products,
    sales_by_category, monthly_sales, sales_by_region
)
from sales_analyzer.visualizer import (
    plot_monthly_sales, plot_category_sales, plot_region_sales
)
from sales_analyzer.reporter import generate_report

DATA_PATH = "data/raw/amazon_sales_data 2025.csv"

def main():
    df = load_data(DATA_PATH)
    df = clean_data(df)

    total = total_sales(df)
    avg = average_sale(df)
    top = top_products(df)
    monthly = monthly_sales(df)
    category = sales_by_category(df)
    region = sales_by_region(df)

    print("\n📊 AMAZON SALES DASHBOARD")
    print(f"Total Sales   : {total:.2f}")
    print(f"Average Sale : {avg:.2f}")
    print("\nTop Products:")
    print(top)

    plot_monthly_sales(monthly)
    plot_category_sales(category)
    plot_region_sales(region)

    report = generate_report(total, avg, top)
    print("\n📄 Executive Summary")
    print(report)

if __name__ == "__main__":
    main()
