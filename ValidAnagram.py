class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)
        t_list = list(t)
        if len(s_list) == len(t_list):
            for i in range(0 , len(s_list)):
                for j in range(0 ,len(t_list)):
                    if s_list[i] == t_list[j]:
                        t_list.remove(t_list[j])
                        break
            
            if len(t_list) == 0:
                return True 
            else:
                return False   
        else:
            return False


# from collections import Counter

# alternate 
# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         return Counter(s) == Counter(t)
        

check = Solution()
string1 = "tam"
string2 = "maa"
print(check.isAnagram(string1,string2))