class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_index = 0
        typed_index = 0

        while name_index < len(name) and typed_index < len(typed):
            if name[name_index] != typed[typed_index]:
                return False

            name_count = 1
            typed_count = 1

            while typed_index < len(typed) - 1 and typed[typed_index] == typed[typed_index + 1]:
                typed_count += 1
                typed_index += 1

            while name_index < len(name) - 1 and name[name_index] == name[name_index + 1]:
                name_count += 1
                name_index += 1

            if name_count > typed_count:
                return False

            name_index += 1
            typed_index += 1

        return name_index == len(name) and typed_index == len(typed)
