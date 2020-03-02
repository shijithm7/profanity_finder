import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



badwords_data_set=docx2txt.process("words.docx")
#print(web_developer_skills)


def find_match_percentage(x):
    vectorizer = CountVectorizer()      
    count_matrix = vectorizer.fit_transform(x)
    #match_percentage=cosine_similarity(count_matrix)
    match_percentage=cosine_similarity(count_matrix)[1][0]*100
    match_percentage=round(match_percentage,2)
    return match_percentage


comment=input("enter your comment=")
li=[badwords_data_set,comment]
print(find_match_percentage(li))
