class Solution:
    def reverseWords(self, sent: str) -> str:
        '''
            Time: O(n * (length of all words in total))
            Space: O(number_of_words + C)
            NOTE: With using str.split()
        '''
        s = list()
        word = list()
        for i in sent:
            if i.isalnum():
                word.append(i)
            elif word:
                s.append(''.join(word))
                word = list()
        if word:
            s.append(''.join(word))
        s.reverse()
        return ' '.join(s)

        '''
            Time: O(n)
            Space: O(total_number_of_words)
            NOTE: Using str.split()
        '''
        # words = sent.split()
        # words.reverse()
        # return " ".join(words)