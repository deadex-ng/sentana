## Chichewa Sentiment Analysis

### Introduction

Sentiment analysis is a natural language processing technique used to determine whether data is positive, negative or neutral. It is commonly used to analyze customer feedback, survey responses and product reviews. 

In this guide we look at how to perform simple sentiment analysis for Chichewa text based on a set of rules. 

### How it works

1. We define two lists of polarized words. We have negative words such as `sizabwino`, `sibho`, etc and positive words such as `zabwino`, `yabho`, etc. 
2. We count the number of positive and negative words that appear in a given text. 
3. If the number of positive words is greater than the number of negative words, the program returns a positive sentiment and vice versa. In the case that both negative and positive words are equal, the program return neutral.

### Output

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
    




