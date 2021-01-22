
import random
import pylab


random.seed(0)


def farm(seed, water, pest, planting_freq = 5, numTrials = 1000 ):
    """assumes seed, water and pest (integers) factors that affect harvest.
    simulates a farming situation to decide how much a factor can affect a harvest yield."""
    harvests = []
    for n in range(numTrials):
        yields = 0
        for p in range(planting_freq):
            fact1 = water * random.gauss(0,0.5)
            fact2 = pest * (1/random.choice(range(1,10)))
            calc_yields = (fact1/fact2) + seed
            yields += calc_yields
        harvests.append(yields)

    return harvests

sim = farm(25, 60, 40)

def farm_stats(x):

    mean = round(sum(x)/len(x), 3)
    min_harvest = round(min(x), 2)
    max_harvest = round(max(x), 2)
    
    diff = []
    for v in x:
        diff.append((v-mean)**2)
    variance = round(sum(diff)/len(x), 2)

    sd = round(variance ** 0.5, 2)

    print("mean = ", mean,
          "\nthe minium yield = ", min_harvest,
          "\nthe maximium yield = ", max_harvest,
          "\nvariance = ", variance,
          "\nthe standard deviation", sd)
    return mean, sd

mu, sigma = farm_stats(sim)
histogram = pylab.hist(sim, bins = 100)

print("Fraction within ~1sd of mean = ", sum(histogram[0][33:66 ]),
      "Fraction within ~2sd of mean = ", sum(histogram[0][17:82]),
      "Fraction within ~3sd of mean = ", sum(histogram[0][6:96]))
      

def guassian(x, mean, sd):
    fact1 = 1/(sd*(2*pylab.pi)**0.5)
    fact2 = pylab.e**-(((x-mean)**2)/(2*sd**2))
    p = fact1 * fact2
    return p

x_vals, y_vals = [], []
x = -sigma

while x <= sigma:
    x_vals.append(x)
    y_vals.append(guassian(x, mu, sigma))
    x += 1

#pylab.plot(x_vals, y_vals)
pylab.title('Normal Distribution, mu = ' + str(mu)+ ', sigma = '+ str(sigma))
pylab.show()


    
             
    





        
        
