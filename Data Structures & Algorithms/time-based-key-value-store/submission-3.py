class TimeMap:

    def __init__(self):
        self.vals = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.vals:
            self.vals[key].append((value, timestamp))
        else:
            self.vals[key] = [(value, timestamp)]
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals:
            return ""
        res = ""

     
        times = self.vals[key]
        l = 0
        r = len(times) - 1

        while l <= r:
            mid = (l + r) // 2
            if times[mid][1] <= timestamp:
                res = times[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res




        
        
