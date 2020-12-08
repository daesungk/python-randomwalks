import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from rw1dfunctions import RW1D, SRW1D, NRW1D, NSRW1D, Hitting

# Run Random Walk
Num = 1000000
T = np.arange(Num)
RW = SRW1D(Num)
NRW = NSRW1D(Num)

# Normal Distribution
plt.hist(NRW, 100)
plt.show()


# Plot
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(T, RW)
ax2.plot(T, NRW)
fig.savefig('rw_1d.png')

# Export Data
Plot = pd.DataFrame()
Plot["RW"] = RW
Plot["NRW"] = NRW
Plot.to_csv('rw_1d.csv')

# Hitting time

