import streamlit as st
import plotly.express as px

# Title and Introduction
st.title("🌟 Tuple Explorer 🌟")
st.write("Welcome to the Tuple Explorer! Here, you can play with tuples, learn about their functions, and visualize them.")

# Initialize the tuple
if 'my_tuple' not in st.session_state:
    st.session_state.my_tuple = ('banana', 'orange', 'mango', 'lemon')

# Display the current tuple
st.subheader("Your Current Tuple:")
st.write(st.session_state.my_tuple)

# Sidebar Menu
st.sidebar.title("What would you like to do?")
action = st.sidebar.selectbox(
    "Choose an action:",
    [
        "Create a Tuple",
        "Access Items",
        "Slice the Tuple",
        "Join Two Tuples",
        "Check if an Item Exists",
        "Visualize the Tuple",
        "Delete the Tuple"
    ]
)

# Perform actions based on user selection
if action == "Create a Tuple":
    st.subheader("Create a New Tuple")
    new_items = st.text_area("Enter items for the tuple (separated by commas):")
    if st.button("Create"):
        try:
            new_tuple = tuple(item.strip() for item in new_items.split(",") if item.strip())
            st.session_state.my_tuple = new_tuple
            st.success("The tuple has been created!")
        except Exception as e:
            st.error("Error: Please enter a valid list of items.")

elif action == "Access Items":
    st.subheader("Access Items in the Tuple")
    index = st.number_input("Enter the index of the item you want to access:", min_value=-len(st.session_state.my_tuple), max_value=len(st.session_state.my_tuple)-1, value=0)
    if st.button("Access"):
        try:
            item = st.session_state.my_tuple[index]
            st.success(f"The item at index {index} is '{item}'.")
        except IndexError:
            st.warning("Index out of range!")

elif action == "Slice the Tuple":
    st.subheader("Slice the Tuple")
    start = st.number_input("Start Index:", min_value=-len(st.session_state.my_tuple), max_value=len(st.session_state.my_tuple)-1, value=0)
    end = st.number_input("End Index:", min_value=-len(st.session_state.my_tuple), max_value=len(st.session_state.my_tuple), value=len(st.session_state.my_tuple))
    if st.button("Slice"):
        sliced_tuple = st.session_state.my_tuple[start:end]
        st.success(f"Sliced Tuple: {sliced_tuple}")

elif action == "Join Two Tuples":
    st.subheader("Join Two Tuples")
    new_items = st.text_area("Enter items for the second tuple (separated by commas):")
    if st.button("Join"):
        try:
            new_tuple = tuple(item.strip() for item in new_items.split(",") if item.strip())
            joined_tuple = st.session_state.my_tuple + new_tuple
            st.session_state.my_tuple = joined_tuple
            st.success("The two tuples have been joined!")
        except Exception as e:
            st.error("Error: Please enter a valid list of items.")

elif action == "Check if an Item Exists":
    st.subheader("Check if an Item Exists in the Tuple")
    item_to_check = st.text_input("Enter the item you want to check:")
    if st.button("Check"):
        if item_to_check in st.session_state.my_tuple:
            st.success(f"Yes, '{item_to_check}' is in the tuple!")
        else:
            st.warning(f"No, '{item_to_check}' is not in the tuple.")

elif action == "Visualize the Tuple":
    st.subheader("Visualize the Tuple")
    if st.button("Visualize"):
        # Convert tuple to a list for visualization
        data = list(st.session_state.my_tuple)
        fig = px.bar(x=data, y=[1]*len(data), title="Tuple Visualization", labels={'x': 'Items', 'y': 'Count'})
        st.plotly_chart(fig)

elif action == "Delete the Tuple":
    st.subheader("Delete the Tuple")
    if st.button("Delete"):
        del st.session_state.my_tuple
        st.session_state.my_tuple = ()
        st.success("The tuple has been deleted!")

# Refresh the tuple display
st.subheader("Updated Tuple:")
st.write(st.session_state.my_tuple if 'my_tuple' in st.session_state else "Tuple is empty or deleted.")