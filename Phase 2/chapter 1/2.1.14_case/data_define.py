"""
class of data
"""

class Record:
    
    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province
        
    # fix the problem that the list[Record] data type cannot be printed
    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"