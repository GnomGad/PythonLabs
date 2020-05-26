class StringFormatter(object):

    @staticmethod
    def del_worlds(s,n):
        words = s.split(" ")
        return " ".join([words[i] for i in range(len(words))if len(words[i])<n])

    @staticmethod    
    def replace(s):
        news=""
        for i in s:
           news+= "*" if i.isdigit() else i
        return news

    @staticmethod
    def set_spaces(s):
        return " ".join([i for i in "".join(s.split(" "))])
        
    @staticmethod    
    def sort_size(s):
        words =  s.split(" ")
        return " ".join(sorted(words, key=lambda word: len(word))).lstrip()

    @staticmethod
    def sort(s):
        return " ".join(sorted(s.split(" "))).lstrip()