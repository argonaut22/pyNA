import os
import pdb
import numpy as np
import openmdao.api as om
import pandas as pd
import matplotlib.pyplot as plt

os.environ["pyna_language"] = 'python'
from pyNA.pyna import pyna

# Load default pyna settings
pyna_settings = pyna.load_settings(case_name = 'NASA STCA Standard')
pyna_settings.save_results = True

# Compute noise contours
x_lst = np.linspace(0, 15000, 5)
y_lst = np.linspace(0, 4000, 2)
py = pyna(settings=pyna_settings)
py.compute_noise_contours(x_lst=x_lst, y_lst=y_lst)

# Plot
py.plot_noise_contours()