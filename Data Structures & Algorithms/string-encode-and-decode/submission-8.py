class Solution:

    def encode(self, strs: List[str]) -> str:
        if not len(strs):
            return "None"
        concat = "[c0n]".join(strs)
        encoded = concat.encode('utf8')
        return concat

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        strs = s.split("[c0n]")
        return strs
