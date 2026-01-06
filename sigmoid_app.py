import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Sigmoid Activation Function")

st.write("""
The Sigmoid activation function maps input values into a range between 0 and 1.
It is commonly used in binary classification problems.
""")

x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("Sigmoid Function")

st.pyplot(fig)