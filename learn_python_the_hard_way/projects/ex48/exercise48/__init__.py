from nose.tools import*
ListLexicon = { 'north': 'direction', 'south': 'direction', 'west': 'direction', 'east': 'direction',
'down': 'direction', 'up': 'direction', 'left': 'direction', 'right': 'direction', 'back': 'direction',
'go': 'verb', 'stop': 'verb', 'kill': 'verb', 'eat':'verb', 
'the': 'stop','in': 'stop', 'of': 'stop', 'from': 'stop', 'at': 'stop', 'it':'stop',
'door': 'noun', 'bear': 'noun', 'princess': 'noun', 'cabinet': 'noun',
}

class lexicon():
    def __init__(self):
        pass
    
    def scan(phrase):
        result = []
        words = phrase.split()
        for i in words:
            try:
                a = int(i)
                result.append(('number',a))
            except ValueError:
                result.append((ListLexicon.get(i,None),i))
        return result
