#prediction of gender
from sk learn import tree
x = [[181,80,44], [177,70,43], [160,60,38],[154,54,37], [166,65,40], [190,90,47], [179,64,33], [177,70,40], [181,85,43]]
y = ['male', 'felmale', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
prediction = clf.predict([[190,70,43]])
print prediction
