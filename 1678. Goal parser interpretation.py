class Solution:
    def interpret(self, command: str) -> str:
        return (command.replace("()","o")).replace("(al)","al")

if __name__ == "__main__":
    command = "G()(al)"
    # result = Solution.interpret(command)
    
    s = (command.replace("()","o")).replace("(al)","al")
    print(s)