# Import multiple functions from your AirqualityIndex module
from AirqualityIndex import (
    run_aqi_system, 
    #display_all_data, 
    #search_city_aqi,
    #add_aqi_data,
)

# Entry point - only runs when main.py is executed directly
if __name__ == "__main__":
    # Call the main AQI system function
    run_aqi_system()
    