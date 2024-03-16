from nose.tools import *

ListLexicon = {'north': 'direction', 'south': 'direction', 'west': 'direction', 'east': 'direction',
               'down': 'direction', 'up': 'direction', 'left': 'direction', 'right': 'direction', 'back': 'direction',
               'go': 'verb', 'stop': 'verb', 'kill': 'verb', 'eat': 'verb',
               'the': 'stop', 'in': 'stop', 'of': 'stop', 'from': 'stop', 'at': 'stop', 'it': 'stop',
               'door': 'noun', 'bear': 'noun', 'princess': 'noun', 'cabinet': 'noun',
               '0': 'number', '1': 'number', '2': 'number', '3': 'number', '4': 'number', '5': 'number', '6': 'number',
               '7': 'number', '8': 'number', '9': 'number'
               }


class Lexicon:
    def __init__(self):
        pass

    def scan(phrase):
        result = []
        words = phrase.split()
        for i in words:
            result.append((ListLexicon.get(i, None), i))
        return result
