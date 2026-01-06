import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Tanh Activation Function")

st.write("""
The Hyperbolic Tangent (Tanh) activation function outputs values between -1 and 1.
It is zero-centered and often performs better than Sigmoid.
""")

x = np.linspace(-10, 10, 100)
y = np.tanh(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("Tanh Function")

st.pyplot(fig)