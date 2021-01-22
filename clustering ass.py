import csv, numpy, pylab, random


def get_data():
    path = "C:\\Users\\Ugochi\\Desktop\\Python tutorials\\Python\\python_example\\execise files\\Today\\winequality-white.csv"
    file = open(path, 'r')
    reader = csv.reader(file, delimiter = ';')
    header = next(reader)
    tdata = []
    for row in reader:
        tdata.append(row)
    data = pylab.array(tdata, dtype='float32')
    return data
#print(get_data())
#C:\Users\Ugochi\Desktop\Python tutorials\Python\python_example\execise files\Today\winequality-white

data = get_data()
def Minkowski(x1, x2):
    #assumes p =2: Eucleadian distance
    dist = sum(abs(x1-x2)**0.5)

    return dist

def scaleAttrs(vals):
    vals = pylab.array(vals)
    mean = sum(vals)/len(vals)
    sd = numpy.std(vals)
    vals = vals - mean
    return vals/sd

vals = scaleAttrs(data)

def kMeans(pop, k=5):
    icentroid = random.sample(list(pop), k)
    clusters = [[] for c in icentroid]

    for v in range(200):
        for s in pop:
            distance = []
            for i in range(len(clusters)):
                dist = Minkowski(s, icentroid[i])
                distance.append(dist)
            least_dist = min(distance)
            index = distance.index(least_dist)
            clusters[index].append(s)
            
        ncentroid = []

        abs_diff = 0
        
        for m in range(len(icentroid)):
            av_centroid = list(sum(clusters[m][:])/len(clusters[m]))
            ncentroid.append(av_centroid)
            
            diff_mink = Minkowski(av_centroid, icentroid[i])
            abs_diff += diff_mink

        if abs_diff <= 0.00010:
            print('centroid approximately centralized')
            #c_diff = False
            break
        print("centroid's current distance away from centre =", abs_diff)
        icentroid = pylab.array(ncentroid)

    for clas in range(k):
        print('K', clas, ':', clusters[clas], '\n')              

    return clusters, icentroid

kMeans(vals, 7)

