class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def generateIPAddresses(s, currentAddress, startIndex, dotCount):
            if dotCount == 3:
                segment = s[startIndex:]
                if len(segment) > 0 and int(segment) <= 255 and (segment[0] != '0' or segment == '0'):
                    validAddresses.append(currentAddress + segment)
                return

            if startIndex == len(s):
                return

            for i in range(startIndex, startIndex + 3):
                if i >= len(s):
                    break

                segment = s[startIndex:i + 1]
                if int(segment) <= 255 and (segment[0] != '0' or segment == '0'):
                    generateIPAddresses(
                        s, currentAddress + segment + '.', i + 1, dotCount + 1)

        validAddresses = []
        generateIPAddresses(s, '', 0, 0)
        return validAddresses
