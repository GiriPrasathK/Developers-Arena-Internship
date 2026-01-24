from dataclasses import dataclass
from datetime import datetime

@dataclass
class Expense:
    date: str
    amount: float
    category: str
    description: str
    recurring: bool = False

    def validate(self):
        datetime.strptime(self.date, "%Y-%m-%d")
        if self.amount <= 0:
            raise ValueError("Amount must be positive")
        if not self.category.strip():
            raise ValueError("Category cannot be empty")
        if not self.description.strip():
            raise ValueError("Description cannot be empty")
        return True
    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "recurring": self.recurring
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            date=data["date"],
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            recurring=data.get("recurring", False)
        )
    def __str__(self):
        return (f"Expense(date={self.date}, amount={self.amount}, "
                f"category={self.category}, description={self.description}, "
                f"recurring={self.recurring})")
    