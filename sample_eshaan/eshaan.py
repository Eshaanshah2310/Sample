import streamlit as st
import dt.streamlit

def main():


    # Title of the web app
    st.title("Simple To-Do List App")

    # Initialize the session state to hold tasks if not already present
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    # Function to add a new task
    def add_task():
        task = st.session_state["new_task"]
        if task:
            st.session_state.tasks.append({"title": task, "completed": False})
            st.session_state["new_task"] = ""  # Clear the input box

    # Display existing tasks with checkboxes
    st.header("Your To-Do List")
    for idx, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.9, 0.1])
        completed = col1.checkbox(task["title"], task["completed"], key=idx)
        if completed:
            st.session_state.tasks[idx]["completed"] = True
            col2.write("✓")

    # Input field to add new tasks
    st.text_input("Enter a new task for today:", key="new_task", on_change=add_task)

application = dt.streamlit.Streamlit()

# the app entrypoint makes the app deployable on Datatailr
def __app_main__():
    return application

# this block makes the app runnable in your IDE for debugging purposes
if __name__ == '__main__':
    # feel free to modify the port if 12345 is taken
    application.run(port=12345)