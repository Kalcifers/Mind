import re
from nltk.corpus import stopwords

def clean(line):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    k = re.sub("[\n\t\n\s]*<[^>]*>[\n\t\s]*", " ", line)  # remove html tags
    k = re.sub("[^a-z0-9A-Z\s']", "", k)  # remove special characters
    k = re.sub("[\n]+", " ", k) # remove newline
    #k = emoji_pattern.sub(r'', k) # remove emojis (not necesssary)
    k = re.sub("[\s]*https?/?/?\S+", "", k) #remove links
    k = re.sub("[\s]*-&\S+", "", k) #remove indentation
    k = re.sub("'", " ", k)
    #k = re.sub("@", "", k) #remove tag (not necessary)
    #k = re.sub("#", "", k) #remove hashtag (not necessary)
    k = re.sub("[\s]{2,}", " ", k) #remove multiple spaces
    k = re.sub("^\s+", "", k)

    return k

stoplist = stopwords.words('italian')


def remove_stopW(line):
    line_splitted = line.split()

    line_out = [x for x in line_splitted if x not in stoplist]

    line_clean = " ".join(line_out)
    return line_clean