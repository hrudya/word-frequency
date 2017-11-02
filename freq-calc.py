import csv
import re
from nltk.corpus import stopwords
wordcount={}
with open('/path/text_emotion.csv') as csvfile:
readCSV = csv.reader(csvfile, delimiter=',')
for column in readCSV:
text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', column[3])
text = re.sub(r'(.)\1+', r'\1\1', text)
text = re.sub('[^A-Za-z0-9\.]+', ' ', text)
text = text.replace(".", " ")
text = text.replace("@", "")
text = text.replace("!", "")
words = re.findall('\w+', text.lower())
preprocessed_words = [word for word in words if word not in stopwords.words('english')]
for word in preprocessed_words:
if word not in wordcount:
wordcount[word] = 1
else:
wordcount[word] += 1
print wordcount
