class Solution:
    def defangIPaddr(address):
        return "[.]".join(address.split("."))


if __name__ == "__main__":
    a = "1.1.1.1"
    result = Solution.defangIPaddr(a)
    print(result)