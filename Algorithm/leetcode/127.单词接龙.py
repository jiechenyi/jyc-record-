"""
127.单词接龙
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。


"""

from collections import defaultdict
def ladderLength(beginWord, endword, wordList):
    if endword not in wordList or not wordList:
        return 0

    dic = defaultdict(list)

    for word in wordList:
        for i in range(len(word)):
            dic[word[:i]+'*'+word[i+1:]].append(word)
    que = [(beginWord,1)]
    have={beginWord:True}
    while que:
        current_word, depth = que.pop(0)
        if current_word == endword:
            return depth
        for i in range(len(current_word)):
            k = current_word[:i]+'*' + current_word[i+1:]
            if dic.get(k):
                for w in dic[k]:
                    if not have.get(beginWord):
                        que.append((w, depth+1))
                        have[w] =True
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))

