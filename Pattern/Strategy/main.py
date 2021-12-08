from strategy import MatchingFinder
from strategy import StartswithFinder

# strategy pattern implements each strategy into its own separate class
    # avoid if then else integration
    # loosely coupled system : new strategies added without making any change to the main class

# class WordList:

#     def __init__(self, words):
#         self.words = words

#     def find_matching(self, target):
#         return [word for word in self.words if target==word]

#     def find_startswith(self, target):
#         return [word for word in self.words if word.startswith(target)]

class WordList:
    
    def __init__(self, words):
        self.words = words

    def find(self, finder):
        return finder.execute(self.words)
    
if __name__=='__main__':
    wordlist = WordList(['apple', 'lemon', 'lime', 'pear'])
    print(wordlist.find(MatchingFinder('pear')))
    print(wordlist.find(StartswithFinder('l')))
    pass
