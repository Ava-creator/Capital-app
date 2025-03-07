import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

# Initialize session state for the visited set
if 'visited' not in st.session_state:
    st.session_state.visited = set()

# Title and Introduction
st.title("🌍 Geo Explorer 🌍")
st.write("Welcome to Geo Explorer! Discover new places, mark the ones you've visited, and see them on an interactive map.")

# Sidebar Menu
st.sidebar.title("What would you like to do?")
action = st.sidebar.selectbox(
    "Choose an activity:",
    [
        "Add a Location",
        "Check Visited Locations",
        "View Map",
        "Clear Visited Locations"
    ]
)

# Function to get coordinates for a location
def get_location_coordinates(location):
    geolocator = Nominatim(user_agent="geoexplorer")
    try:
        loc = geolocator.geocode(location)
        return (loc.latitude, loc.longitude)
    except AttributeError:
        return None

# Perform actions based on user selection
if action == "Add a Location":
    st.subheader("Add a New Location")
    location = st.text_input("Enter the name of a city, country, or landmark:")
    if st.button("Add"):
        if location.strip():
            coords = get_location_coordinates(location)
            if coords:
                st.session_state.visited.add(location)
                st.success(f"'{location}' has been added to your visited list!")
            else:
                st.warning(f"Could not find '{location}'. Please check the spelling or try another location.")
        else:
            st.warning("Please enter a valid location.")

elif action == "Check Visited Locations":
    st.subheader("Check Your Visited Locations")
    if st.session_state.visited:
        location_to_check = st.text_input("Enter a location to check:")
        if st.button("Check"):
            if location_to_check in st.session_state.visited:
                st.success(f"Yes, you have visited '{location_to_check}'!")
            else:
                st.warning(f"No, you haven't visited '{location_to_check}' yet.")
    else:
        st.info("Your visited list is empty. Add some locations first!")

elif action == "View Map":
    st.subheader("View Your Visited Locations on a Map")
    if st.session_state.visited:
        # Create a Folium map centered at the first location
        first_location = next(iter(st.session_state.visited))
        first_coords = get_location_coordinates(first_location)
        if first_coords:
            m = folium.Map(location=first_coords, zoom_start=2)

            # Add markers for all visited locations
            for loc in st.session_state.visited:
                coords = get_location_coordinates(loc)
                if coords:
                    folium.Marker(coords, popup=loc).add_to(m)

            # Display the map
            st_data = st_folium(m, width=700)
        else:
            st.warning("Could not display the map. Please ensure your visited locations are valid.")
    else:
        st.info("Your visited list is empty. Add some locations first!")

elif action == "Clear Visited Locations":
    st.subheader("Clear Your Visited Locations")
    if st.button("Clear"):
        st.session_state.visited.clear()
        st.success("Your visited list has been cleared!")

# Display the current visited locations
st.subheader("Your Visited Locations:")
if st.session_state.visited:
    st.write(list(st.session_state.visited))
else:
    st.info("Your visited list is empty. Start adding locations!")