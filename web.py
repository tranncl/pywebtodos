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

# Display the todo list as checkbox & get the indexes
for index, todo in enumerate(todos):
    # get the key of each item as the item itself
    checkbox = st.checkbox(todo, key=todo)
    # If an item is checked (True): make it disappear, update the file,
    # update the session state & finally rerun the session.
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Enter a new todo ... ",
              on_change=add_todo, key="new_todo")

# Display the dictionary of session_state containing the session "keys/values"
# st.session_state
# {
# "new_todo":"Hello"
# }