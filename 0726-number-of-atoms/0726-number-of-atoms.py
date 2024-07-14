class Solution:
    def countOfAtoms(self, formula):
        from collections import defaultdict
        import re
        
        stack = [defaultdict(int)]
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[i_start:i] or 1)
                for element, count in top.items():
                    stack[-1][element] += count * multiplier
            else:
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[i_start:i]
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[i_start:i] or 1)
                stack[-1][element] += count
        
        final_count = stack.pop()
        result = []
        for element in sorted(final_count):
            result.append(element)
            if final_count[element] > 1:
                result.append(str(final_count[element]))
        
        return ''.join(result)
        