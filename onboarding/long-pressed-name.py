class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        name_pt = 0
        typed_pt = 0

        while name_pt < len(name) and typed_pt < len(typed):
            
            ele_num_typed = 0
            element = typed[typed_pt]
            inital_val = typed_pt
            while typed_pt < len(typed) and typed[typed_pt] == name[name_pt]:
                typed_pt += 1
            
            ele_num_typed = typed_pt - inital_val
            inital_n = name_pt
            while name_pt < len(name) and name[name_pt] == element:
                name_pt += 1

            ele_num_name = name_pt - inital_n
            if ele_num_name > ele_num_typed:
                return False

            if name_pt < len(name) and typed_pt < len(typed) and name[name_pt] != typed[typed_pt]:
                return False
            
            if( typed_pt < len(typed) and name_pt >= len(name)) or (name_pt < len(name) and typed_pt >= len(typed)):
                return False
            
        return True

