class Transaction:
    def __init__(self, date, label, value, type):
        self.date = date
        self.label = label
        self.value = value
        self.type = type

    def __repr__(self):
        return f"Transaction(date='{self.date}', label='{self.label}', value={self.value}, type='{self.type}')"
