class Jumble:

    def __init__(self, word):
        dic_words = open('/usr/share/dict/words' ,'r').read().split('\n')
        self.dictionary_words = set(dic_words)
        self.permutations_set = set(self.find_anagram(word))

    def find_anagram(self, word):
        word_split = [char for char in word]
        '''
        same as :
        word_split = []
        for char in word:
            word_split.appen(char)
        '''
        word_perm = self.permutations(word_split)
        perm_in_string = [''.join(word) for word in word_perm]
        '''
        same as:
        perm_in_string = []
        for lst in word_perm:
            perm_in_string.append(''.join(lst))
        '''

        return perm_in_string 


    def permutations(self, array):
        if len(array) < 2:
            return array
        if len(array) == 2:     # base case
            return [array, [array[1], array[0]]]
        all_perms = []
        for i in array:
            new_array = array[:]
            new_array.remove(i)
            all_perms_extension = self.permutations(new_array)
            for group in all_perms_extension:
                group.insert(0,i)
            all_perms.extend(all_perms_extension)
        return all_perms

    def find_answer(self):
        # result_words = self.dictionary_words.intersection(self.permutations_set)
        # return result_words
        return self.dictionary_words & self.permutations_set
        # first_word_char = [result_words[0][2],result_words[0][4]]
        # print(first_word_char)
        # permutation_of_result = self.permutations(words)
        
        # for word in permutation_of_result:
        #     first_part = words[:2]
        #     last_part = [-4:]

tefon = Jumble('tefon')
print(tefon.find_answer())

sokik = Jumble('sokik')
print(sokik.find_answer())

niumem = Jumble('niumem')
print(niumem.find_answer())

siconu = Jumble('siconu')
print(siconu.find_answer())

