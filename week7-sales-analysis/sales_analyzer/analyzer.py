def total_sales(df):
    return df["Total Sales"].sum()

def average_sale(df):
    return df["Total Sales"].mean()

def top_products(df, n=5):
    return (
        df.groupby("Product")["Total Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )

def sales_by_category(df):
    return df.groupby("Category")["Total Sales"].sum()

def monthly_sales(df):
    return df.groupby("Month")["Total Sales"].sum()

def sales_by_region(df):
    # Customer Location is the geographical dimension
    return df.groupby("Customer Location")["Total Sales"].sum()
