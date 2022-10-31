import urllib.request


'''The Great Gatsby'''
#Import the great Gatsby
url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
with urllib.request.urlopen(url) as f:
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    
#   print(text) # for testing
    words_all = [word.strip() for word in text.split(' ')]
    words_freq = {}
    for word in words_all:
        if word in words_freq:
            words_freq[word] += 1
        else:
            words_freq[word] = 1 
    
    words_freq_sorted = {k : v for k, v in sorted(words_freq.items(), key=lambda item: item[1], reverse=True)}
    
    print(words_freq_sorted)








