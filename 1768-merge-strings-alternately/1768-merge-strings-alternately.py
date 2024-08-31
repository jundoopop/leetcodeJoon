class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""

        # Put at before the each letters of word2
        if len(word1) >= len(word2):
            # Make spaces to put letters of word2
            for letter in word2:
                merged += f"0{letter}"

            # Replace spaces with letters from word1
            for i in range(len(word2)):
                merged = merged.replace("0", word1[i], 1)

            merged += word1[len(word2) :]
        # Put at after the each letters of word1
        else:

            # Make spaces to put letters of word1
            for letter in word1:
                merged += f"{letter}0"


            # Replace spaces with letters from word2
            for i in range(len(word1)):
                merged = merged.replace("0", word2[i], 1)

            merged += word2[len(word1) :]
        return merged
