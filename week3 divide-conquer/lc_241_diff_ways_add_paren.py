class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # parse the string for nums and operators
        if input.isdigit():
            return [int(input)]
        
        res = []
        
        for i, val in enumerate(input):
            if val in ["+", "-", "*"]:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                
                print(left, right)
                for l in left:
                    for r in right:
                        if val == "+":
                            res.append(l+r)
                            continue
                        if val == "-":
                            res.append(l-r)
                            continue
                        if val=="*":
                            res.append(l*r)
        return res 
            
            