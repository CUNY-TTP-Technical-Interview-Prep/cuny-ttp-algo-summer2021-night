def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if needle == haystack:
            return 0
        return haystack.find(needle)