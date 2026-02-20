import matplotlib.pyplot as plt

def plot_monthly_sales(data):
    data.plot(kind="line", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("data/reports/monthly_sales.png")
    plt.show()

def plot_category_sales(data):
    data.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Sales by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("data/reports/category_sales.png")
    plt.show()

def plot_region_sales(data):
    data.plot(kind="bar")
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig("data/reports/region_sales.png")
    plt.show()
