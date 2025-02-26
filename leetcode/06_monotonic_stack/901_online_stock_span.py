class StockSpanner:
    def __init__(self):
        self.prices = []
        self.stack = []
    
    def next(self, price: int) -> int:
        self.prices.append(price)
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()
        if self.stack:
            res = len(self.prices) - 1 - self.stack[-1]
        else: res = len(self.prices)
        self.stack.append(len(self.prices) - 1)
        return res
        
        
obj = StockSpanner()
# print(obj.next(100))
# print(obj.next(80))
# print(obj.next(60))
# print(obj.next(70))
# print(obj.next(60))
# print(obj.next(75))
# print(obj.next(85))
print(obj.next(10))
print(obj.next(74))
print(obj.next(84))
print(obj.next(102))
print(obj.next(107))
print(obj.next(115))
print(obj.next(115))