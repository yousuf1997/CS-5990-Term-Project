import math

'''
    This class represents utils methods for vectors
'''

class VectorUtill:

    def __init__(self):
        pass


    # this method computes the consine simalarity
    def computeCosineSimilarity(self, vector1: list, vector2: list):
        vec1len = len(vector1)
        vec2len = len(vector2)
        ## make sure both of the vectors are same size
        ## otherwise append zeros if they are not same
        if vec1len != vec2len:
            if vec1len > vec2len:
                for i in range(vec1len - vec2len):
                    vector2.append(0)
            else:
                for i in range(vec2len - vec1len):
                    vector1.append(0)
        ## compute the cross product
        ## bottom portion (length)
        vec1Squared = 0
        vec2Squared = 0
        crossProduct = 0
        squareRootAndMultiplied = 0
        for index in range(len(vector1)):
            crossProduct = crossProduct + vector1[index] * vector2[index]
            vec1Squared = vec1Squared + math.pow(vector1[index], 2)
            vec2Squared = vec2Squared + math.pow(vector2[index], 2)
        ## cosine simularity
        return crossProduct / (math.sqrt(vec1Squared) * math.sqrt(vec2Squared))

    ## this method gets list of vectors, and computes average vector
    def computeAverageVector(self, vectors: list):
        if len(vectors) == 0:
            return 0.0

        xIndex = 0
        xLength = len(vectors[0])
        yLength = len(vectors)
        averageVector = []

        while xIndex < xLength:
            yIndex = 0
            sum = 0.0
            while yIndex < yLength:
                sum = sum + vectors[yIndex][xIndex]
                yIndex = yIndex + 1
            average = float(sum / yIndex)
            ## add the sum to the average vector
            averageVector.append(average)
            xIndex = xIndex + 1
        return averageVector
