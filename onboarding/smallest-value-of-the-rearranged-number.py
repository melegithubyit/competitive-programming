class Solution:
    def smallestNumber(self, num: int) -> int:
        def pos_num(num):
            mapped_integer = []
            while num > 0:
                mapped_integer.append(num % 10)
                num //= 10

            mapped_integer.sort()

            left = 0
            right = 1

            while right < len(mapped_integer):
                if mapped_integer[left] == 0 and mapped_integer[right] == 0:
                    right += 1
                elif mapped_integer[left] == 0 and mapped_integer[right] != 0:
                    mapped_integer[left], mapped_integer[right] = mapped_integer[right], mapped_integer[left]
                    break
                else:
                    break

            mapped_str = list(map(str, mapped_integer))
            str_val = ''.join(mapped_str)
            if str_val != '':
                return int(str_val)
            else:
                return 0

        def neg_num(num):
            number = abs(num)
            mapped_integer = []
            while number > 0:
                mapped_integer.append(number % 10)
                number //= 10
            mapped_integer.sort(reverse=True)
            mapped_str = list(map(str, mapped_integer))
            str_val = ''.join(mapped_str)
            if str_val != '':
                return 0 - int(str_val)
            else:
                return 0

        if num < 0:
            return neg_num(num)
        else:
            return pos_num(num)

