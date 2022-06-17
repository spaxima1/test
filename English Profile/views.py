class Word:
    def __init__(self,**kwargs):
        self.word=kwargs['word']
        self.GuideWord=kwargs['GuideWord']
        self.level=kwargs['level']       
        self.PartOfSpeech=kwargs['PartOfSpeech']     
        self.Topic=kwargs['Topic']
        self.posSection=kwargs.get('posSection',None)


class Section:
    def __init__(self,**kwargs):
        self.pos=kwargs['pos']
        self.posTitle=kwargs['posTitle']
        self.audio=kwargs.get('audio',None)      
        self.written=kwargs.get('written',None)
        self.detail=kwargs.get('detail',None)
        self.wordFamily=kwargs.get('wordFamily',None)


class Detail:
    def __init__(self,**kwargs):
        self.level=kwargs['level']
        self.title=kwargs['title']
        self.definition=kwargs['definition']
        self.grammar=kwargs.get('grammar',None)
        self.DictionaryExample=kwargs.get('DictionaryExample',None)
        self.LearnerExample=kwargs.get('LearnerExample',None)


class WordFamily:
    def __init__(self,**kwargs):
        self.words=kwargs['words']
        self.types=kwargs['types']