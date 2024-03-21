from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import glob

# Load the data
filepaths = glob.glob('C:/Users/Public/Operational_Functional_Block/Python_Projects/Rocket Engine Generator/GenFiles/GenData/FullFolders/*.txt')
texts = []
labels = []
for path in filepaths:
    with open(path, 'r') as file:
        text = file.read()
        texts.append(text)
        # Get the label from the filename or directory
        label = path.split('/')[-1].split('.')[0]
        labels.append(label)

# Transform the text into a numerical representation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train the model
clf = MultinomialNB()
clf.fit(X, labels)

# Test the model
test_text = ''
X_test = vectorizer.transform([test_text])
predicted_label = clf.predict(X_test)[0]

print('Predicted label:', predicted_label)
