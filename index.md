# Analyzing tweets in response to Dr. Timnit Gebru's firing from Google

On December 2nd, co-lead of Google's Ethical AI team, Timnit Gebru, was allegedly fired for not retracting her name from a paper called "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?", in which Gebru et. al examined biases and limitations in large-scale language models.

On December 3rd, in response to the uproar over her firing, head of Google AI, Jeff Dean, shared the email he sent to the Google Research team, stating that Gebru's paper, "[…] didn't meet our bar for publication" and ignored "[…] too much relevant research" on the environmental impacts of language models and strategies designed to mitigate bias in language models.

On December 9th, Google CEO, Sundar Pichai, emailed Google employees about Gebru's firing, saying that they will, "[…] begin a review of what happened to identify all the points where we can learn - considering everything from de-escalation strategies to new processes we can put in place".

Gebru's ouster from Google has sparked debate across Twitter, ranging from whether black and underrepresented communities have a place in tech companies, whether these communities will be able to design AI systems, and whether Google is willing to grapple with ethical questions about their AI systems.

In order to get a better idea of the conversations unfolding on Twitter, this analysis will examine what words are being used, the sentiment of these words/sentiments, and the topics mentioned in these conversations.

## Tweet volume over time

![Tweets discussing Timnit Gebru's Firing](https://user-images.githubusercontent.com/35497376/102264642-ee36d000-3ee3-11eb-9139-20a49468dbed.png)

## Tweets with the most favorites

![Tweeters with the most favorited tweets](https://user-images.githubusercontent.com/35497376/102264640-ee36d000-3ee3-11eb-926e-3d32b2e636a8.png)

## Tweets with the most retweets

![Tweeters with the most retweets](https://user-images.githubusercontent.com/35497376/102264641-ee36d000-3ee3-11eb-99e5-5f239dfbb4b8.png)

## Unigram Analysis

![Wordcloud of most frequently used words](https://user-images.githubusercontent.com/35497376/102264643-ee36d000-3ee3-11eb-845a-af64202f8bcd.png)

![10 most frequently used positive and negative words](https://user-images.githubusercontent.com/35497376/102264625-eb3bdf80-3ee3-11eb-87e9-25c69957ddd9.png)

![Positive and negative words mentioning Timnit Gebru (Dec  3rd - Dec  10th)](https://user-images.githubusercontent.com/35497376/102264637-ed9e3980-3ee3-11eb-8624-1a9ba12b7f80.png)

## Constructing a graph of bigrams

![Bigram graph](https://user-images.githubusercontent.com/35497376/102264636-ed9e3980-3ee3-11eb-8e75-d86a61d3684e.png)

## Sentiment analysis of the full tweets
![Positive, negative, and neutral sentences mentioning Timnit Gebru (Dec  3rd - Dec  10th)](https://user-images.githubusercontent.com/35497376/102264638-ee36d000-3ee3-11eb-807e-8d21318b9d9b.png)

## Extracting topics from the tweets

**Results of LDA:**

```
Words for topic #1:
pichai, staff, dismissal, lead, ceo, company, departure, ethic, researcher, fire, 

Words for topic #2:
risk, fire, data, ethic, work, large, bias, model, language, research, 

Words for topic #3:
woman, employee, scientist, company, research, email, black, ethic, researcher, fire, 

Words for topic #4:
see, public, team, go, side, mit, technology, review, story, force, 

Words for topic #5:
solidarity, people, sign, istandwithtimnit, get, work, support, believeblackwomen, stand, isupporttimnit, 

Words for topic #6:
voice, people, start, get, ethic, bad, condemn, worker, scientist, fire, 

Words for topic #7:
employee, tech, woman, black, company, highlight, ethicist, researcher, bias, fire, 
```



