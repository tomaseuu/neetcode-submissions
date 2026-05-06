class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # 1. Find the position of "#"
            j = i
            while s[j] != '#':
                j += 1
            # 2. get the length of the word
            length = int(s[i:j])
            # 3. extract the word
            word = s[j+1 : j+1+length]
            result.append(word)
            # 4. move pointer to next chunk
            i = j + 1 + length
        return result




# Thoughts:

# I need to design two functions: encode and decode
# - encode takes a list of strings and turns it into one single string.
# - decode takes that single string and reconstructs the exact original list
# The biggest challenge is that strings can contain any characters (: or #).
# So I can not just join them with a comma or space, I have to use the format:
# Just found this out:
# <length>#<string> -> length tells us exactly how many characters to read
#                   -> # is just a marker so we know where the number ends and the string starts

# This way, when decoding I can read characters until I hit # to get the length, then read exactly what many characters for the string.
# I repeat this for the entire encoded string. Whatever encode outputs, decode can parse back to the original list.

# Steps I need to take is to loop through each string:
# 1. find its length 
# 2. build a chunk
# 3. glue all chunks together into one big string