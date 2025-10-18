class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left,right=0,len(skill)-1
        summ=0
        c=0

        while left<right:
            if c==1:
                if skill[left-1]+skill[right+1] != skill[left]+skill[right]:
                    return -1
            if c==0:
                c+=1
            summ+=(skill[left]*skill[right])
            left+=1
            right-=1

        return summ
