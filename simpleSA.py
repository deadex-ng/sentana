#list of negative Chewa words
negative = ['sizabwino', 'sibho','nditrash']

#list of positive Chewa words 
positive = ['zabwino','yabho','mwalamwala']

#list of stop words 
stopwords =['ndi','iyi','nde']


def get_polarity(text):

    #counter for postive polarity
    counter_pos = 0

    #counter for negative polarity
    counter_neg = 0

    #split text to list
    txt_list = text.split()

    #remove stopwords for text 
    for word in list(txt_list):
        if word in stopwords:
            txt_list.remove(word)

    #count number of positive or negative word in text
    for word in txt_list:
        if word in positive:
            counter_pos = counter_pos + 1
        if word in negative:
            counter_neg = counter_neg + 1

    if counter_pos > counter_neg:
        return 'Positive'
    elif counter_pos < counter_neg:
        return 'Negative'
    else:
        return 'Neutral'

#Here are sample statements we are using to test
text_one = 'Bundle iyi ndi yabho'
print('-----------text and polarity------------')
print('Text: ', text_one)
print('Polarity:', get_polarity(text_one))
print('----------------------------------------')


text_two = 'Izi nde sizabwino'
print('-----------text and polarity------------')
print('Text: ', text_two)
print('Polarity:', get_polarity(text_two))
print('----------------------------------------')


text_three = 'Bundle iyi ndiya bho koma izi zomatha changu nde sizabwibo'
print('-----------text and polarity------------')
print('Text: ', text_three)
print('Polarity:', get_polarity(text_three))
print('----------------------------------------')
