class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        self.stack.append(price)
        res = 0
        count = len(self.stack) - 1

        while self.stack and count >= 0:
            if self.stack[count] <= price:
                res += 1
            else:
                break

            count -= 1

        return res


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)