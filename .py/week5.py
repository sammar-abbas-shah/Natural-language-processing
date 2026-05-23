from sklearn.feature_extraction.text import CountVectorizer

text = ['I Love Pizza,I Love Burger']

cv = CountVectorizer()
Encode = cv.fit_transform(text)
print(cv.get_feature_names_out())
print(Encode.toarray())
#############################################################
text1= ['I Love cricket','But not Pakistani cricket team','my favorite player is nobody']
en = cv.fit_transform(text1)
print(cv.get_feature_names_out(text1))
print(en.toarray())
#################################################
text2 = ['I Love Pizza but Pasta as well']
cv = CountVectorizer(ngram_range=(4,4))# telling to create how many token to be created
gram = cv.fit_transform(text2)
print(cv.get_feature_names_out())
#####################################################

text3 = ['I Love Pakistan but there lack of opportunities exists may ALLAH bess Pakistan and opportunity']
cv = CountVectorizer(ngram_range=(10,10))
gram = cv.fit_transform(text3)
print(cv.get_feature_names_out())
# apply back of words on this sentence