# text-mining

Please read the [instructions](instructions.md).

# Reflection:

Project Overview:

	For this project, I have used several sources that I believe would be interesting for text analysis. I aimed to analyze a great book “The Great Gatsby”. First, I used the Gutenberg Website to use the txt file of the entire book for analysis. This analysis is the first part of my project. I have imported the txt file as an url and then used a for loop to get the frequency of words in the order of those that appeared the most. Then, I took a movie review of the movie “The Great Gatsby” and a review of the book both in the form of txt files. I was interested in analyzing the similarities between the movie review and the book review, as the story is the same. This is the second part of my project. I used packages including nltk, genism, NumPy and scikit-learn to compare the texts and find their similarities. From these exercises, I wish to explore how to compare the similarity of texts that share a common topic, which can be useful in the future as many posts of the same topic may share different perspectives.

Implementation:

	For the first part of the project in which I aimed to analyze the word frequency in “The Great Gatsby”, a major package I used is the urllib package, which allows meto import the txt from the Gutenberg website. I used a .split() function to first take out all the words individually, then I created a dictionary that counts the frequency of each word and ranks them by their value. This allows me to view the frequency of words starting from the most used.
	For the second part of the project, I used several packages that would support my aim to compare the two reviews. 	After importing the files, I first had to tokenize the sentences and the words of the file, which uses the nltk package. I also used genism package to create bags of words that would later be analyzed. I have also used the TF-Idf package to determine term frequency of words, which tells me their frequencies by weight. This then gives me to corpus that can be used for comparison. I was then able to compare the text with the genism and the TF-Idf packages. I have also used NumPy to determine the average similarity of documents. 

Results: 

	For the first part of my project, I have generated the frequencies of each word in the text. The words appear starting from the most frequent. I have seen that transitional words like “the”, “and”, “a” etc appear the most throughout the text, which is reasonable as they connect words together to form sentences. The first frequently used word that’s not a transitional word is “little”, then I also see more descriptive words that appear quite often. This shows that the sentences in this book are in general very descriptive.

    For the second part of the project, I found several aspects interesting. I was able to compare the query document (movie_review.txt) to the main document (book_review.txt). I first compared the sentences in the book review to the movie review document. There are a total of seven sentences in the book review document, therefore generating seven comparing results as shown below. From this comparison, I can see that the third document is the most similar. As I was looking at the sentence, I found that this makes sense since the sentence mentions several keywords that also appeared in the movie review, such as “father”, “book” and” advice. 

        Comparing Result: [0.01560395 0.17687392 0.3565427  0.0297643  0.07886736 0.11226489 0.21147944]

    Then I also generated the average similarities, in which I divided the sum pf the comparing results to the count of documents, and generated the following outputs. These outputs shows that the 

        Average similarity float: 0.14019950798579625
        Average similarity percentage: 14.019950798579625
        Average similarity rounded percentage: 14

    These outputs shows that the movie review is about 14% similar to the book review. This tells me that even though the movie and and the book tell the same story, the perspective and understanding of this story given by the viewer of the movie is not that much similar to the reader of the actual book. This is actually quite common as movies may edit parts from the book that would be displayed and often gives different impressions through imagery.

Reflection:

    I think I have learned a lot from this project. I have never used or even seen some of the language processing packages used in this project before, and this project gives me an opportunity to implement these tools and see how powerful they are. Next time, I think it would be better for me to plan ahead what kinds of comparison I am looking for before writing the code. I went through a lot of issues when working on the code as I missed planning. Not planning ahead much caused me to forget implementing an important step for instance. However, the overall process went well and I am particularly happy to be able to explore how nltk and genism packages work together to generate great results.


