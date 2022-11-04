from googletrans import Translator
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

translator = Translator(service_urls=['translate.googleapis.com'])
nltk.download('stopwords')
en_stopws = stopwords.words('english')
en_stopws.append('spam')
en_stopws.append('what')
en_stopws.append('mr')
en_stopws.append('two')

Str =  '''
Boris Johnson Contracts Coronavirus, Rattling Top Ranks of U.K. Government The British leader, \
who long resisted social distancing, is now isolating himself. But he said he would continue to lead the \
country’s response to the pandemic. LONDON — For weeks, Prime Minister Boris Johnson of Britain was a \
defiant holdout among Western leaders in refusing to lock down his country against the spread of the \
coronavirus. On Friday, he became the first of those leaders known to have contracted the disease. \
Mr. Johnson’s diagnosis, confirmed in a test on Thursday, threatened to throw an already rattled \
British government into turmoil. Fears of a wider contagion grew, as two other senior officials \ 
disclosed that they, too, were infected. And with the heir to the throne, Prince Charles, saying \
this week that he had fallen ill with the virus, Britain faced the alarming prospect of having to \
confront its greatest crisis since World War II with several of its leading figures in quarantine. \
Mr. Johnson, 55, insisted he would not relinquish his duties. In a remarkable two-minute video posted \
on Twitter, he used his own case as a sort of teachable moment for the country, appealing to people \
to work from home and comply with the more drastic social distancing measures he put in place Monday. \
But a critical member of his cabinet, Matt Hancock, the health secretary, also tested positive, \
meaning that the two people most directly responsible for dealing with the virus are now afflicted \
with it. The government’s chief medical adviser, Chris Whitty, also reported symptoms of the virus \
and said he was isolating himself. There are fears that other officials who have been in meetings with \
Mr. Johnson could also have been exposed. If Mr. Johnson becomes incapacitated, his duties would be \
taken over by the foreign secretary, Dominic Raab, who has tested negative for the virus. It is a \
ead-spinning turn of events for a government that, just two weeks ago, was brimming with confidence \
fter a landslide election victory in December. Other world leaders, including Chancellor Angela Merkel \
of Germany and Prime Minister Justin Trudeau of Canada, have put themselves in isolation as a \
recaution in recent days. But no Western country has seen the virus threaten its entire political \
establishment as swiftly johnson as Britain has in the last week.
'''
ch = '''
Nvidia 最新款旗艦顯示卡 RTX 4090 媒體評測今日解禁，各家實測後意外發現，這張顯示卡效能太強，許多狀況都會撞上 CPU 瓶頸，無法發揮完整效能。
全新 RTX 4090 顯示卡採用 AD102 GPU，放棄三星 8 奈米製程，改採台積電 4 奈米製程後，電晶體數量從 283 億大幅暴增至 763 億，使運算效能遠遠超過前代 RTX 3090 Ti。

但實際測試時，4090 雖然效能比前一代 3090 Ti 高不少，但考量到售價漲幅，僅 22% 效能提升讓人不太滿意，不過問題可能不是出在顯卡，而是 CPU。

畫面設定 1,440p 解析度時，4090 只比 3090 Ti 高 20%~30%，但如果將解析度提高到 4K，效能就大幅提升 59%。
'''

trans=translator.translate(ch, dest='en')
en_str = str(trans)
#print(trans)

in_str = en_str.lower() 
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(in_str) 
tokens = [token for token in tokens if token not in en_stopws]
fdist = FreqDist(tokens) # build statistic bar chart (x: word, y: frequency)
common = fdist.most_common(8) 
a = []
for i in common:  
    a.append(np.asarray(i))

'''
for i in a:
    np.array(a)[i][0] = str(translator.translate(np.array(a)[i][0],dest = 'zh-tw').text)
'''

'''

np.array(a)[0][0] = str(translator.translate(np.array(a)[0][0],dest = 'zh-tw'))
print(type(a))
print(a[0][0])
common[0][0] = str(translator.translate(common[0][0],dest = 'zh-tw'))
'''



for i in range(8):
    print(translator.translate(np.array(a)[i][0],dest = 'zh-tw').text)