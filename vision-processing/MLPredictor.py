import pickle
import numpy as np

class Predictor:
    def __init__(self,filename):
        self.net = pickle.load(open(filename+".sav", 'rb'))
    ##Accepts a list of values [X,Y,W,H]
    def predict3D(values):
        return self.net.predict([values])[0]
    ##Accepts the output of predict3D
    def getAngle(values):
        centerX = (values[0] + values[1])/2.0
        angle = ((3.14/2) - np.arctan2((abs(values[3].item())),centerX))
        return angle
