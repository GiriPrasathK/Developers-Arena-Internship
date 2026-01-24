from collections import defaultdict

class Reports:

    @staticmethod
    def monthly(expenses):
        report = defaultdict(float)
        for e in expenses:
            month = e["date"][:7]
            report[month] += e["amount"]
        return report

    @staticmethod
    def category(expenses):
        report = defaultdict(float)
        for e in expenses:
            report[e["category"]] += e["amount"]
        return report

    @staticmethod
    def visualize(report):
        for k, v in report.items():
            print(f"{k:15} | {'█' * int(v // 100)} ₹{v}")

    @staticmethod
    def predict_next_month(expenses):
        if not expenses:
            return 0
        avg = sum(e["amount"] for e in expenses) / len(expenses)
        return round(avg * 30, 2)
