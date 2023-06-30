class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s         
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res = []
        i = 0
        while i < len(str):
            hash_index = str.index('#', i)
            l = int(str[i:hash_index])
            s = str[hash_index + 1:hash_index + 1 + l]
            res.append(s)
            i = hash_index + 1 + l
        
        return res

