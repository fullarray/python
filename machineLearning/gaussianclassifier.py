#import libraries gaussian naive-bayes
from sklearn.naive_bayes import GaussianNB
import numpy as np

#target variables
x= np.array([[-2,7],[1,5], [1,4], [-2,8], [2,3], [-4,1], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-6,9]])

y = np.array([8, 3, 3, 3, 4, 3, 3, 4, 1, 4, 4, 1])

#Create a Gaussian Classifiers
model = GaussianNB()

#model training
model.fit(x,y)

#predictor
predicting=model.predict([[1,2],[3,8]])

#print to screen
print predicting
