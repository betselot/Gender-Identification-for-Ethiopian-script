import nltk
import re
import random
from collections import Counter
def gender_features(word):
    return {'የመጨረሻው ፊደል 1': word[-1]}

female=open('femalName.txt',encoding='utf8').readlines()
male=open('maleName.txt',encoding='utf8').readlines()
female=''.join(female)
female=re.sub(r"\d+","",female)
female=re.findall(r"[\w']+",female)
#(female)
male=''.join(male)
male=re.sub(r"\d+","",male)
male=re.findall(r"[\w']+",male)

#print(male)
names = ([(name, 'ወንዲ') for name in male] +[(name, 'ሴት') for name in female])
#print(names)
random.shuffle(names)
random.shuffle(names)


#print(len(names))
#featuresets = [(gender_features(n), g) for (n,g) in names]
train_names = names[300:]
devtest_names = names[200:300]
test_names = names[:200]
#train_set, test_set=featuresets[:350],featuresets[350:]
train_set = [(gender_features(n), g) for (n,g) in train_names]
devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
test_set = [(gender_features(n), g) for (n,g) in test_names]

classifier = nltk.NaiveBayesClassifier.train(train_set)
print (nltk.classify.accuracy(classifier, devtest_set))

#Using the dev-test set, we can generate a list of the errors that the classifier makes when predicting name genders:
errors = []
for (name, tag) in devtest_names:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append( (tag, guess, name) )
print(errors)
for (tag, guess, name) in sorted(errors):
    print ('correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name))
#print(featuresets)
print("It's classified as: ",classifier.classify(gender_features('ወንድሙ')))
#print(nltk.classify.accuracy(classifier,test_names))
#print(classifier.show_most_informative_features(5))
