# Hijra Trip Planner v1.0
# A simple Python program that uses functions to simulate planning a journey.
# Inspired by my intention to make Hijra and built as a warm-up using both Python and my Java OOP understanding.
def trip_planner_welcoming(name):
    print("Welcome to tripplanner v1.0, " + name.title())  # capitalize name for presentation

trip_planner_welcoming("quam")

def rounded_estimated_time(estimated_time):
    rounded_time = round(estimated_time)
    # Go over Python functions again (Personal reminder)
    return rounded_time

estimate = rounded_estimated_time(1)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    print("Your trip starts off in " + origin)
    print("And you are traveling to " + destination)
    print("You will be traveling by " + mode_of_transport)
    print("It will take approximately " + str(estimated_time) + " hours")

# Function calls
destination_setup("United States", "Saudi Arabia", 9, "plane")
destination_setup("Nigeria", "Saudi Arabia", 5, "plane")
destination_setup("Chad", "Saudi Arabia", 5, "plane")
destination_setup("Colombia", "Saudi Arabia", 10, "plane")

# Comment: reminds me of constructor overloading in Java!
