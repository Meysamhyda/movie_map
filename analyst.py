import pandas as pd 
import math
import numpy as np
df = pd.read_excel("data_imdb.xlsx")

def removal_stop_words(texts,stop_word):           
    text = []
    texts_n = str(texts).lower().replace(",","")
    for word in texts_n.split():
        if word  not in stop_word:
            te = "".join(word)
            text.append(te)
    return text

stop_words = ["without","irs","and",'accept','known','tests',"the","of","is","of","a","an","in","to","over","must","his","one","when","two","several","as","on","1920s","while","by","whose","them","before","more","during","ii","becomes","for","after","their","with","they","four","from","other","75","...","all","that","into","more","much","who","use","given","i","are","we","their","he","she","it",'seven',"1963","up","uses","six","if","had","never","him","what","have","bin","become","will","yet","has","also","now","her","even","17-year-old","30","10-year-old","where","$40000","under","12-year-old","wants","five","at","in","above","1890s","each","other","or","not","how","so","-","be","o...","out","1936","its","1984","becoming","himself","them","both","but","best","being","oh","fifteen","'him...","top","ii","ii.","once","(2018)","35","years","old","only","it's","weren't","read","more","ever","goes","begin","to...",'story', 't.e.', 'lawrence','dis...',"been","may","own","ensue.","go",'los', 'angeles',"1980","takes","origi...","off","78-year-old","taking",'alzhei...',"a...",'new', 'york','1950s', 'three','down','1938','it.','eight-year-old', 'thought', 'until', 'behind''april', '6th', '1917.', '1600', 'wa...', 'same', 'in.', 'begins', 'his...', 'ones', 'true', 'through', '1960s','1948', 'fas...', '1944','1954','john', 'nash', 'almost',"them", 'park', 'island', 'central', 'america', "park's", 'din...', 'comes','down-on-their-luck',"very", 'near', 'rio', 'four-year', 'her.', 'peter', 'asks', 'trul...', 'there', 'inte...', '1930s', '"v"', 'which', 'back', '500000', 'san', 'and...', 'hi...', 't...', 'get','keller', "dover's", "he's", 'due', 'thao', 'lor', 'hmong', 'possession:', '1972', '21', 'con', 'them.', "can't", 'way', 'deliv...', 'always', 'this''harry', 'ron', 'hermione', "voldemort's", "hotel's","wife's", 'having',"was","man's", 'i.r.a.', 'did', 'well.','pulp', 'martins', '18th-century', 'ways','in-depth', 't.', 'doss', 'would', 'make', '1986', 'puts', "girlfriend's", 'longs',"short", 'tries...',"post-apocalyptic", 'between','severely', 'y...','forty-four-year', 'max', 'pals:', 'mary',"tale", 'about', 'than', 'things', '7', 'cod', 'down.', '"the',"jeff", 'l.a.', 'whi...', 'dude"','1431', "d'arc", '2...', 'ken', 'hutu', 'militia', 'rwanda', 'thousand', 'tutsi','paul', 'rusesabagina', 'gets', 'philadelphia','chris', 'taylor', 'vietnam', 'wills', 'th...', 'can', 'makes', 'paris','boston', '2029', 'cyborg', 'so...', 'laura', 'mutant', 's...', 'journey', '1970s', 'james', 'hunt', 'niki', 'lauda.','nine', 'jesse', 'celine', 'first', 'again', "jesse's",'$24000', 'christopher', 'mccandless', 'gives', 'alaska', 'dorothy', 'toto', 'away', 'kansas', 'oz','retu...', 'keeps', 'repeating', 'right.', "soldier's",'trying','24', 'hours','lives', '"captain"', 'jack', 'sparrow', "governor's", "jack's",'oklahoma', 'california', 'great...', 'case', 'bring', 'turkey', '1980.', 'left-wing', "life's", 'behin...', 'end', 'next', 'jesus', 'christ', 'brian', 'nazareth', 'outer', 'come', 'true.', 'became', 'making', 'adolf', 'hitler', 'tells', 'behind', 'others', 'taken', 'terro...', 'basic']


All_summerize = []           
for index in range(250):
    clean_text = removal_stop_words(df.iloc[index]["summerize_movie"],stop_words)
    All_summerize.append(clean_text)

new_doc = input("Please enter the summury of the new movie : ")
All_summerize.append(removal_stop_words(new_doc,stop_words))



def calculate_term_word_in_text(document,word):
    i = 0
    for j in range(len(document)):
        if document[j] == word:
            i += 1
    return i


def calculate_TF(document,word):
    term_in_document = calculate_term_word_in_text(document,word)
    total_word_in_document = len(document)
    TF = term_in_document / total_word_in_document
    return TF


def calculate_IDF(word):
    i = 0
    for document in range(len(All_summerize)):
        if word in All_summerize[document]:
            i += 1
    
    return math.log10(len(All_summerize)/i) + 1

def calculate_TF_IDF(list,word):
    TF = calculate_TF(list,word)
    IDf = calculate_IDF(word)
    TF_IDF = TF * IDf
    return TF_IDF


extend_summerize = []
for i in All_summerize:
    extend_summerize.extend(i)
#حذف کردن کلمات مشابه هم از لیست 

extends_summerize = list(set(extend_summerize))  
TF_IDF = []
for i in range(len(All_summerize)):
    for j  in range(len(extends_summerize)):
        TF_IDF.append(calculate_TF_IDF(All_summerize[i],extends_summerize[j]))


index_data_frame = [df["title"][i] for i in range(250)]
index_data_frame.append("new_movie") 

TF_IDF_doc = np.array(TF_IDF).reshape(len(All_summerize),len(extends_summerize))
data_frame = pd.DataFrame(TF_IDF_doc,index=index_data_frame,columns=[i for i in extends_summerize])


def Inner_product(A,B):
    Inner_Product = 0
    for i in range(len(A)):
        r = A[i]*B[i]
        Inner_Product += r
    return Inner_Product


def cosine_Similary(vector_1,vector_2):
    
    return Inner_product(vector_1,vector_2)/(math.sqrt(Inner_product(vector_1,vector_1))*math.sqrt(Inner_product(vector_2,vector_2)))

result = []
for i in range(250):

    result.append(cosine_Similary(list(data_frame.iloc[i]),list(data_frame.iloc[250])))




top_three_indices = pd.Series(result).nlargest(3).index
top_three_movies = [index_data_frame[i] for i in top_three_indices]
print("The three movies that are most similar to the movie summary you received are: ",top_three_movies)
