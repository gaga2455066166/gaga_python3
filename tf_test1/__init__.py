import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import scale

print("Tensorflow版本是", tf.__version__)

df = pd.read_csv("data/boston_housing_data.csv", header=0)
print(df.describe())
df.head(3)
