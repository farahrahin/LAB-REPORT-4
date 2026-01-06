import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("ReLU Activation Function")

st.write("""
The Rectified Linear Unit (ReLU) activation function outputs zero for negative inputs
and outputs the input directly for positive values.
""")

x = np.linspace(-10, 10, 100)
y = np.maximum(0, x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("ReLU Function")

st.pyplot(fig)