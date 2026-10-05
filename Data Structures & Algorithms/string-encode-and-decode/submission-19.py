class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs==['']:
            return ""
        print("Join")
        if strs==[]:
            return "✂️"
        return '👍'.join(strs)

    def decode(self, s: str) -> List[str]:
        print("see")
        print(s)
        if s == "":
            return [""]
        elif s=="✂️":
            return []
        return s.split('👍')