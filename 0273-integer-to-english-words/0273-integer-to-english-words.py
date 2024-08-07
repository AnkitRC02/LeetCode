class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        below_20 = [
            "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        def word(num):
            if num < 20:
                return below_20[num]
            elif num < 100:
                return tens[num // 10] + ('' if num % 10 == 0 else ' ' + below_20[num % 10])
            elif num < 1000:
                return below_20[num // 100] + " Hundred" + ('' if num % 100 == 0 else ' ' + word(num % 100))
            else:
                for idx, word_thousands in enumerate(thousands):
                    if num < 1000 ** (idx + 1):
                        return word(num // 1000 ** idx) + " " + word_thousands + ('' if num % 1000 ** idx == 0 else ' ' + word(num % 1000 ** idx))

        return word(num).strip()

        