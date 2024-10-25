import streamlit as st

# Define your ask function
from crew import ask
# Streamlit app
def main():
    st.title("Research and Generate use case about company/industry.")

    # Text input for the question
    question = st.text_input("Enter Company/Industry Name:")

    # Submit button
    if st.button("Submit"):
        # Call the ask function and display the result
        response = ask(question)
        st.write(response.tasks_output[0].raw)
        st.write(response.tasks_output[1].raw)
        st.write(response.tasks_output[2].raw)
        


main()
