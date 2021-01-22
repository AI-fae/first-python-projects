import csv, pylab, numpy

path = "C:\\Users\\Ugochi\\Desktop\\Python tutorials\\Python\\python_example\\execise files\\DataSet\\forestfires.csv"

def getData(filePath):
    
    file = open(filePath, newline = '')
    reader = csv.reader(file)
    header = next(reader)
    
    x_vals = []     #area burnt by fire
    y_vals = []     #comparing variable

    for row in reader:
        area = float(row[12])
        #FFMC DMC DC  ISI temp RH wind
        y_vals.append([float(row[4]),float(row[5]),float(row[6]),float(row[7]),float(row[8]),float(row[9]),float(row[10])])
        x_vals.append(area)
    return (x_vals, y_vals)

x_vals, y_vals = getData(path)
xVals = pylab.array(x_vals)
yVals = pylab.array(y_vals)

    
##def genModels(x, y, degrees):
##    models = []
##    for d in degrees:
##        model = pylab.polyfit(x,y, d)
##        models.append(model) 
##    return models


####def plotFitData(xVals, yVals, model):
####
####    pylab.plot(xVals, yVals, 'bo',
####               label = 'relationship b/w area and other variables')
####    #labelplot()
####    
####    print(model)
####    est_y = pylab.polyval(model, xVals)
####    pylab.plot(xVals, est_y, 'r',
####               label = 'fits, k = ' + str(round(1/model[0], 5)))
##
##    pylab.legend(loc = 'best')
##    pylab.show()

def rSquared(observed, predicted):
    error = ((predicted - observed)**2).sum()
    mean_error = error/len(observed)
    r2 = 1 - (mean_error/numpy.var(observed))
    return r2

def runFits(x_vals, y_vals,degrees, title):
    
    data_output = []

    for i in range(len(y_vals[0])):
        test_val = y_vals[:,i]
        output = []
        for d in degrees:
            model = pylab.polyfit(x_vals, test_val, d)
            est_y = pylab.polyval(model, x_vals)
            r2 = rSquared(test_val, est_y)
            output.append({d:[model, r2]})
        data_output.append(output)
        
####        pylab.plot(x_vals, test_val, 'ro',
####               label = 'relationship b/w area and other variables')                  
####        pylab.plot(xVals, est_y,
####                   label = 'Fit of degree ' + str(degrees[i])\
####                   + ', R2 = '+ str(round(error, 5)))
####        
##        pylab.legend(loc = 'best')
##        pylab.title(title)
##        pylab.show()
    return data_output

degrees = [2, 4, 6, 8, 16]
#models = genModels(xVals, yVals, degrees)
wahala = runFits(xVals, yVals, degrees, "UC.com forestFire dataset analysis")
#plotFitData(xVals, yVals)
print(wahala)
