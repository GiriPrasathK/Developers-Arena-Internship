def generate_report(total, avg, top_products):
    return {
        "Total Sales": round(total, 2),
        "Average Sale": round(avg, 2),
        "Top Products": top_products.to_dict()
    }
