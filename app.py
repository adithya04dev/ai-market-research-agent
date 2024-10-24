import streamlit as st

# Define your ask function
from crew import ask
# Streamlit app
def main():
    st.title("Company/Industry Name")

    # Text input for the question
    question = st.text_input("Enter Company/Industry Name:")

    # Submit button
    if st.button("Submit"):
        # Call the ask function and display the result
        response = ask(question)
        if response.tasks_output[-1].raw:

            st.write(response.tasks_output[-1].raw)

main()
