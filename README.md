## Sentiment Analysis

### Introduction

Sentiment analysis is a natural language processing technique used to determine whether data is positive, negative or neutral. It is commonly used to analyze customer feedback, survey responses and product reviews. 

In this guide we look at how to perform simple sentiment analysis based on a set of rules for English and Chichewa text. 

### How it works (English Text)

1. We define two lists of polarized words. We have negative words such as `bad`, `trash`, etc and positive words such as `good`, `nice`, etc. 
2. We count the number of positive and negative words that appear in a given text. 
3. If the number of positive words is greater than the number of negative words, the program returns a positive sentiment and vice versa. In the case that both negative and positive words are equal, the program return neutral.

### Englist Text Sentiment Analysis Output

Here is the output of the program:
```
-----------text and polarity------------
Text:  this car is nice
Polarity: Positive
----------------------------------------
-----------text and polarity------------
Text:  that is bad
Polarity: Negative
----------------------------------------
-----------text and polarity------------
Text:  the design is good but the color is bad
Polarity: Neutral
----------------------------------------
```

### How it works (Chichewa Text)

1. We define two lists of polarized words. We have negative words such as `sizabwino`, `sibho`, etc and positive words such as `zabwino`, `yabho`, etc. 
2. We count the number of positive and negative words that appear in a given text. 
3. If the number of positive words is greater than the number of negative words, the program returns a positive sentiment and vice versa. In the case that both negative and positive words are equal, the program return neutral.

### Chichewa Text Sentiment Analysis Output

Here is the output of the program:

    -----------text and polarity------------
    Text:  Bundle iyi ndi yabho
    Polarity: Positive
    ----------------------------------------
    -----------text and polarity------------
    Text:  Izi nde sizabwino
    Polarity: Negative
    ----------------------------------------
    -----------text and polarity------------
    Text:  Bundle iyi ndiya bho koma izi zomatha changu nde sizabwino
    Polarity: Neutral
    ----------------------------------------





