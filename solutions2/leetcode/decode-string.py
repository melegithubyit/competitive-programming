class Solution:
    def decodeString(self, s: str) -> str:

        def split_string(string):
            segments = re.findall(r'\d+|\D', string)
            merged_segments = []
            current_segment = ''

            for segment in segments:
                if segment.isdigit():
                    current_segment += segment
                else:
                    if current_segment:
                        merged_segments.append(current_segment)
                        current_segment = ''
                    merged_segments.append(segment)

            if current_segment:
                merged_segments.append(current_segment)

            return merged_segments

        output = split_string(s)        
        stack = []
        res = ""

        for i in output:
            if i != ']':
                stack.append(i)
            
            else:
                temp = ""
                while stack:
                    ele = stack.pop()
                    if ele != '[':
                        temp = ele + temp
                        temp = temp.strip()
                    else:
                        # if stack: stack.pop()
                        if stack:
                            num = stack.pop()
                            freq = int(num)
                            element = temp * freq
                            stack.append(element)
                            break
        
        while stack:
            ele = stack.pop()
            res = ele + res
        
        res = res.strip()
        return res

