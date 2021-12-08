from interface import IFinder

class MatchingFinder(IFinder):

    def __init__(self, target):
        self.target = target

    def execute(self, words):
        return [word for word in words if self.target==word]

class StartswithFinder(IFinder):

    def __init__(self, target):
        self.target = target

    def execute(self, words):
        return [word for word in words if
                 word.startswith(self.target)]

class LengthFinder(IFinder):

    def __init__(self, minlength, maxlength):
        self.minlength = minlength
        self.maxlength = maxlength

    def execute(self, words):
        return [word for word in words
                 if self.minlength <= len(word) <= self.maxlength]

#print(wordlist.find(LengthFinder(2, 4))) # ['lime', 'pear']