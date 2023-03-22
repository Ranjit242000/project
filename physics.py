import streamlit as st
import sympy as sp
from PIL import Image
import pandas as pd
import plotly.express as px
import numpy as np
st.title("PYTHON PROJECT")
image = Image.open('python.jpg')
st.image(image)



#derivative


def derivative():
    fx = st.text_input("Enter a function: ","x ")

    try:
        f = sp.sympify(fx)
        f_prime = sp.diff(f)
        st.write("The derivative of", fx, "is", f_prime)

    except sp.SympifyError:

        st.error("Invalid input, please enter a valid mathematical expression.")

if __name__ == "__main__":
    st.title("Derivatives of only one variable")
    image = Image.open('derivatives.jpg')
    st.image(image)
    derivative()


#integral

def solve_integral(exp, var,p,q ):
    try:
        exp = sp.sympify(exp)
        solve = sp.integrate(exp, (var,p,q))
        return solve
    except:
        return "Error: Invalid input!"


def main():
   
    st.title("Integration Solver")
    image = Image.open('integration.jpg')
    st.image(image)
    st.write("Enter an expression, a variable, and the integration limits.")

    
    exp = st.text_input("Enter the expression:", "")
    var = st.text_input("Enter the variable:", "")
    p = st.text_input("Enter the lower limit:", "")
    q = st.text_input("Enter the upper limit:", "")

   
    if st.button("Solve Integral"):
        solve = solve_integral(exp, var, p, q)
        st.write(f"The integral of {exp} with respect to {var} from {p} to {q} is: {solve}")

if __name__ == "__main__":
    main()


#3D GRAPH
def get_data():
    x = st.text_input("Enter values for X separated by commas:")
    y = st.text_input("Enter values for Y separated by commas:")
    z = st.text_input("Enter values for Z separated by commas:")
    x = [str(i) for i in x.split(",")]
    y = [str(i) for i in y.split(",")]
    z = [str(i) for i in z.split(",")]
    data = {'X': x, 'Y': y, 'Z': z}
    df = pd.DataFrame(data)
    return df


# Create a Streamlit app
def app():
    st.title("3D Graph")
    st.write("Enter values for X, Y, and Z to create a 3D graph.")
    
    # Get user input and create DataFrame
    df = get_data()
    
    # Create 3D graph using Plotly Express
    fig = px.scatter_3d(df, x='X', y='Y', z='Z')
    
    # Display graph in Streamlit
    st.plotly_chart(fig)

if __name__ == '__main__':
    app()

#matrix









