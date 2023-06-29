class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        result = []
        for i, s in enumerate(sentence.split(" ")):
            word = s
            if s[0] in vowels:
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"

            word += "a" * (i + 1)

            result.append(word)

        return " ".join(result)
