from views import Detail,Section,WordFamily,Word
def get_Example(response,className):
    examples=[]
    for  item in response.find_all('p',{'class':className}):
        examples.append(item.text.strip())
    return examples

def get_wordFamily(response):
    wordFam=[]
    for wfw in response.find_all('div',{'class','wf_pos_block'}):
        word=[]
        for wf in wfw.find_all('span',{'class','wf_word'}):
            word.append(wf.text.replace(',','').strip())
        types=wfw.find('span',{'class','wf_pos'}).text.replace(':','').strip()
        wordFam.append(WordFamily(types=types,words=word).__dict__)
    return wordFam

def Check_valid(response):
    if response!=None:
        return response.text
    return None

def get_sense(response):
    title=Check_valid(response.find('div',{'class':'sense_title'}))
    level=Check_valid(response.find('span',{'class':'label'}))
    definition=Check_valid(response.find('span',{'class':'definition'}))
    grammar=Check_valid(response.find('span',{'class':'grammar'}))
    DictionaryExample=get_Example(response,'blockquote')
    LearnerExample=get_Example(response,'learnerexamp')

    return Detail(title=title,level=level,definition=definition,
                grammar=grammar,
                DictionaryExample=DictionaryExample,
                LearnerExample=LearnerExample)

def get_details(response):
    detailList=[]   
    for dit in response.find_all('div',{'class':'sense'}):
        sense=get_sense(dit)
        detailList.append(sense.__dict__)  
    return detailList
def NotNone(res):
    if res!=None:
        return True
    return False

def get_section(response):
    audio=None
    pos=None
    posTitle=None
    written=None
    if NotNone(response.audio):
        audio=response.audio.source['src']
    if NotNone(response.find('span',{'class':'pos'}) ):
        pos=response.find('span',{'class':'pos'}).text.strip()
        posTitle=response.find('span',{'class':'pos'})['title'].strip()
    if NotNone(response.find('span',{'class':'written'})):
        written=response.find('span',{'class':'written'}).text.strip()
    
    return Section(audio=audio,pos=pos,posTitle=posTitle,written=written) 
            
            
def Information(response):
    data=response.select('div.evp_details > div.evp_details > div')
    sectionList=[]
    for info in data :
        if 'pos_section'in  info['class']:
            wordFam=None
            if info.find('div',{'class':'wordfam'})!=None:
                wordFam=get_wordFamily(info.find('div',{'class':'wordfam'}))
                pass
            detail=get_details(info)
            section=get_section(info.find('div',{'class':'pos_header'}))
            section.detail=detail
            section.wordFamily=wordFam
            sectionList.append(section.__dict__)
            
        elif 'sense' in  info['class']:
            sence=get_sense(info)
            sectionList[len(sectionList)-1]['detail'].append(sence.__dict__)
    return sectionList


def getWordInfo(info:list):
    wordM=info[0].text.strip()
    GuideWord=info[1].text.strip()
    level=info[2].text.strip()
    PartOfSpeech=info[3].text.strip()
    Topic=info[4].text.strip()
    return Word(word=wordM,GuideWord=GuideWord,level=level,PartOfSpeech=PartOfSpeech,Topic=Topic)
