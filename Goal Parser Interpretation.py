class Solution:
    def interpret(self, command: str) -> str:
        parsed=""
        i=0

        while i<len(command):
            if command[i]=='(' and command[i+1]==')':
                parsed+='o'
                i+=2

            elif command[i]=='(' and command[i+1]!=')':
                parsed+='al'
                i+=4
            else:
                parsed+=command[i]
                i+=1
        return parsed
                
        
