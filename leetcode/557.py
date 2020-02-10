class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = []
        for word in s.split(' '):
            s_ = list(word)
            halflen = len(s_) // 2
            for i in range(halflen):
                temp = s_[i]
                s_[i] = s_[-(i+1)]
                s_[-(i+1)] = temp
            sentence.append(''.join(s_))
            
        return ' '.join(sentence)
