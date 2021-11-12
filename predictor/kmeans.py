from sklearn.cluster import KMeans

class KMeansModel():

    def __init__(self, n):
        self.kmeans = KMeans(n_clusters=n, init='k-means++')

    def predict(self, numbers):
        return self.kmeans.fit_predict(numbers)
