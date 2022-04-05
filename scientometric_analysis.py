import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


scopus_py = r.scopus
scopus_py.hist(column = "TC")

scopus_py["TC_log"] = np.log10(scopus_py["TC"] + 1)

scopus_py.hist(column = "TC_log")

plt.figure()


import seaborn as sns
from palmerpenguins import load_penguins


import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
Y = np.sin(2*X)

plt.plot (X, Y+1, color='blue', alpha=1.00)
plt.plot (X, Y-1, color='blue', alpha=1.00)
plt.show()
