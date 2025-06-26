class Solution:
    def calPoints(self, operations: List[str]) -> int:
        w = [] 
        for i in operations:
            if i == "C":
                w.pop()
            elif i == "D":
                w.append(2 * w[-1])
            elif i=="+":
                w.append(w[-1] + w[-2])
            else:
                w.append(int(i))
        return sum(w)       