class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similarDict = {}
        for s in sentence1:
            similarDict[s] = [s]

        for pair in similarPairs:
            if pair[0] not in similarDict:
                similarDict[pair[0]] = []

            similarDict[pair[0]].append(pair[1])

            if pair[1] not in similarDict:
                similarDict[pair[1]] = []

            similarDict[pair[1]].append(pair[0])

        for i in range(len(sentence1)):
            if sentence1[i] not in similarDict or sentence2[i] not in similarDict[sentence1[i]]:
                return False

        return True
