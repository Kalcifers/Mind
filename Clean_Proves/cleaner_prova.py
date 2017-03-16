import re

file_input = open("fakeinput.txt", "r")
line = file_input.read()

emoji_pattern = re.compile("["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                       "]+", flags=re.UNICODE)

k = re.sub("[\n\t\n\s]*<[^>]*>[\n\t\s]*", " ", line)
k = re.sub("[\n]+", " ", k)
k = re.sub("[.,:;]", "", k)
k = emoji_pattern.sub(r'', k)
k = re.sub(" [\s]*https?//\S+", "", k)
k = re.sub("[\s]{2,}", " ", k) #lo faccio alla fine in modo da mettere a posto tutti gli spazi
k = re.sub("^\s+", "", k)

file_input.close()

file_output = open("fakeoutput.txt", "w")
file_output.write(k)
file_output.close()
