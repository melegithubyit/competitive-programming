class Solution:
    def reverseWords(self, s: str) -> str:
        listed = s.strip().split()
        i = 0
        j = len(listed) - 1
        iterations = len(listed) // 2
        for k in range(iterations):
            listed[i], listed[j] = listed[j], listed[i]
            i += 1
            j -= 1

        output = ''
        for i in listed:
            output += i
            output += ' '

        return output.strip()

        