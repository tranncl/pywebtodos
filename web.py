import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    # Get the value of the key 'new_todo'
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


# Activate the web app just by calling a streamlit function
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This is for writing a text")

for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ", placeholder="Enter a new todo ... ",
              on_change=add_todo, key="new_todo")

# Display the dictionary of session_state containing the session "keys/values"
# st.session_state
# {
# "new_todo":"Hello"
# }