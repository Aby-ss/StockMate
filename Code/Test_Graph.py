import numpy as np
import asciichartpy

# generate uniformly distributed random y-values
y_values = np.random.uniform(low=0.0, high=10.0, size=100)

# create chart using asciichartpy module
chart = asciichartpy.plot(y_values, {"height": 10})

# display chart
print(chart)
