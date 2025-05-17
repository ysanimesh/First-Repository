import streamlit as st
import plotly.express as px
import pandas as pd

# Initialize Streamlit app
st.title("Simple Graph Plotter")
st.write("Enter x and y values to plot a line graph.")

# Input widgets
x_values = st.text_input("X Values (comma-separated numbers)", placeholder="e.g., 1,2,3,4")
y_values = st.text_input("Y Values (comma-separated numbers)", placeholder="e.g., 10,20,25,30")
graph_title = st.text_input("Graph Title (optional)", placeholder="e.g., My Data Plot")

# Button to trigger graph generation
if st.button("Plot Graph"):
    if x_values and y_values:
        try:
            # Convert input strings to lists of floats
            x_list = [float(x.strip()) for x in x_values.split(",")]
            y_list = [float(y.strip()) for y in y_values.split(",")]

            # Check if x and y have the same length
            if len(x_list) != len(y_list):
                st.error("X and Y must have the same number of values.")
            else:
                # Create a DataFrame for Plotly
                df = pd.DataFrame({"X": x_list, "Y": y_list})

                # Create line graph with Plotly
                fig = px.line(df, x="X", y="Y", title=graph_title or "Line Graph", markers=True)

                # Display graph
                st.plotly_chart(fig, use_container_width=True)
        except ValueError:
            st.error("Please enter valid numbers (e.g., 1,2,3).")
    else:
        st.error("Please enter both X and Y values.")

# Add a footer
st.markdown("---")
st.write("Built with Streamlit and Plotly | © 2025")