from sklearn import tree

X = [ [180, 80, 42], [160, 67, 39], [178, 67, 43], [174, 70, 40], [153, 56, 37], [183, 90, 44], [156, 67, 36], [160, 70, 41], [177, 58, 39], [180, 69, 39] ]

Y = ["male", "female", "male", "male", "female", "male", "female", "male", "female", "female"]

classifier = tree.DecisionTreeClassifier()
classifier.fit(X, Y)

height = int(raw_input('What is the height of the person in cm? '))
weight = int(raw_input('What is the weight of the person in kg? '))
shoeSize = int(raw_input('What is the shoe size of the person? '))

prediction = classifier.predict([height, weight, shoeSize]);

try:
    gender=prediction[0]
    print "if the person is " + str(height) + "cm tall, weighs " + str(weight) +"kg and has a shoe size of " + str(shoeSize) + ", he might be " + gender    
except IndexError:
    print 'Could not predict the gender'   


