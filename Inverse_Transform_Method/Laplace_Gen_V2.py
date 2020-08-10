#Relevant imports
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from scipy.stats import laplace
from scipy import interpolate
import cProfile
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import math
from scipy.stats import laplace
#The scale variable
b = (1/3)
#Set up the distribution and plot it
fig, ax = plt.subplots(1, 1)
mean,var,skew, kurt = laplace.stats(moments='mvsk')
x = np.linspace(laplace.ppf(0.01),laplace.ppf(0.99), 10000)

deku = []

test_2_container = []

#Generate the uniform random variable. 
test_1 = np.random.uniform(-1,1,1000)
test_2 = np.random.uniform(-1,1,100)


#For loop to accurately transform the data
for x in test_1:
    if x<=0:
        add_me = 2*b*math.log(abs(2*x))
    else:
        add_me = -1*b*math.log(abs(-2*x+2))

    deku.append(add_me)

#For loop to accurately transform the data
for x in test_2:
    if x<=0:
        add_me_2 = 2*b*math.log(abs(2*x))
    else:
        add_me_2 = -1*b*math.log(abs(-2*x+2))

    test_2_container.append(add_me_2)

test1_as_np = np.asarray(deku, dtype=np.float32)
test2_as_np = np.asarray(test_2_container, dtype=np.float32)

#N=1000
fig, ax = plt.subplots(1, 1)
mean,var,skew, kurt = laplace.stats(moments='mvsk')
x = np.linspace(laplace.ppf(0.01),laplace.ppf(0.99), 1000)
plt.title("Inverse Transform Sampling, N=1000")
count2, bins2, ignored2 = plt.hist(test1_as_np,100,density=True)
ax.plot(x, laplace.pdf(x,0,b),'r-', lw=3, alpha=0.6, label='laplace pdf')

#N=100
fig, ax = plt.subplots(1, 1)
mean,var,skew, kurt = laplace.stats(moments='mvsk')
x = np.linspace(laplace.ppf(0.01),laplace.ppf(0.99), 1000)
count2, bins2, ignored2 = plt.hist(test2_as_np, 15, density=True)
plt.title("Inverse Transform Sampling, N=100")
ax.plot(x, laplace.pdf(x,0,b),'r-', lw=5, alpha=0.6, label='laplace pdf')