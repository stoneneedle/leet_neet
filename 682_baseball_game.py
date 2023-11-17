# ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]

class Solution:
    def calPoints(self, operations):
        ops_rev = list(reversed(operations))
        records = []

        for i in range(len(ops_rev)):
            op = ops_rev.pop()

            if "-" in op:
                records.append(0 - int(op.strip('-')))
            if op.isnumeric():
                records.append(int(op))
            elif op == "+":
                records.append(records[-1] + records[-2])
            elif op == "D":
                records.append(records[-1] * 2)
            elif op == "C":
                records.pop()

        return sum(records)


s = Solution()
print(s.calPoints(ops))