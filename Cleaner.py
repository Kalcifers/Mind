import re

def clean(line):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    k = re.sub("[\n\t\n\s]*<[^>]*>[\n\t\s]*", " ", line) # remove html tags
    k = re.sub("[\n]+", " ", k) # remove newline
    k = re.sub("[.,:;-]", "", k) # remove special characters
    k = emoji_pattern.sub(r'', k) # remove emojis
    k = re.sub("[\s]*https?//\S+", "", k) #remove links
    k = re.sub("[\s]*-&\S+", "", k) #remove indentation
    k = re.sub("[\s]*@\S+", "", k) #remove tag
    k = re.sub("[\s]*#\S+", "", k) #remove hashtag
    k = re.sub("[\s]{2,}", " ", k) #remove multiple spaces
    k = re.sub("^\s+", "", k)
    if k == "":
        k = "N/A"
    return k
