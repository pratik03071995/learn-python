
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        main_anagram_list = []
        for i in range(0,len(strs)):
            my_anagram_list = []
            word_list1 = list(strs[i])
            for j in range(i+1,len(strs)):
                word_list2 = list(strs[j])
                if len(word_list1) == len(word_list2):
                    for k in range(0,len(word_list1)):
                        if word_list1[k] in word_list2:
                            word_list2.remove(word_list1[k])

                if len(word_list2) == 0 :
                    if strs[i] not in my_anagram_list:
                        my_anagram_list.append(strs[i])
                    my_anagram_list.append(strs[j])

            main_anagram_list.append(my_anagram_list)

        return main_anagram_list

                   

check = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(check.groupAnagrams(strs))


