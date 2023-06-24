class Solution:
    morseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result = set()

        for word in words:
            morse = ""
            for c in word:
                morse += self.morseCode[ord(c) - ord('a')]

            result.add(morse)

        return len(result)
