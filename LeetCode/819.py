class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        replace_chars = ["!", "?", "'", ",", ";", ".", "\""]

        for c in replace_chars:
            paragraph = paragraph.replace(c, " ")

        count = {}
        for word in paragraph.split(" "):
            if not word:
                continue

            lower_case_word = word.lower()
            if lower_case_word not in count:
                count[lower_case_word] = 0

            count[lower_case_word] += 1

        count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        for item in count:
            if item[0] in banned:
                continue

            return item[0]

        return ""
