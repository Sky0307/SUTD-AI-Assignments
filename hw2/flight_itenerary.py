from search_py3.search import Problem
from search_py3.search import breadth_first_search


class Flight:
    def __init__(self, start_city, start_time, end_city, end_time):
        self.start_city = start_city
        self.start_time = start_time
        self.end_city = end_city
        self.end_time = end_time
    
    def matches(self, inputs):
        """
        Part 2: Matches

        Return true if there is a flight in the DB that leaves the specified city at 
        or later than the time specified

        """

        city, time = inputs
        return city == self.start_city and time <= self.start_time

    def __str__(self):
        return str((self.start_city, self.start_time)) + " -> " + str((self.end_city, self.end_time))

    __repr__ = __str__

flightDB = [
            Flight("Rome", 1, "Paris", 4),
            Flight("Rome", 3, "Madrid", 5),
            Flight("Rome", 5, "Istanbul", 10),
            Flight("Paris", 2, "London", 4),
            Flight("Paris", 5, "Oslo", 7),
            Flight("Paris", 5, "Istanbul", 9),
            Flight("Madrid", 7, "Rabat", 10),
            Flight("Madrid", 8, "London", 10),
            Flight("Istanbul", 10, "Constantinople", 10)
            ]

class FindItinerary(Problem):
    
    def __init__(self, start, goal):
        super().__init__(start, goal)
        
    def actions(self, state):
        actions = []
        for flight in flightDB:
            if flight.matches(state):  # check the condition
                actions.append(flight) # construct list of actions that can be taken
        return actions
    
    def result(self, state,  action):
        return (action.end_city, action.end_time)
    
    def goal_test(self, state):
        current_city, current_time = state
        end_city, end_time = self.goal
        return current_city == end_city and current_time <= end_time
    
# part 3
def find_itinerary(start_city, start_time, end_city, deadline):
    itinerary = FindItinerary( (start_city,start_time), (end_city, deadline) )
    node = breadth_first_search(itinerary)
    if not node: 
        return None
    else: 
        return node.solution()

# Part 4
def find_shortest_itinerary(start_city, end_city):
    """
    Time complexity: O(n)
    """
    start_time = 1
    end_time = 1
    solution = None
    while not solution:
        solution = find_itinerary(start_city, start_time, end_city, end_time)
        end_time += 1
    return solution

if __name__ == "__main__":
    # part 1
    print(f"Part 1: Current city and current time")

    # part 2
    print(f"See line 12")

    # part 3
    solution = find_itinerary('Rome', 0, 'Rabat', 10) 
    flight = ('Rome', 0, 'Rabat', 10) 
    print(f"Part 3:")
    print(f"Given the flight from {flight[0]} at  {flight[1]} hr to  {flight[2]} before  {flight[3]} hr:")
    print(f"The solution is {solution}")

    # part 4
    print(f"Part 4:\nYes, this strategy will work as it will return the path that arrives the earliest")
    query = ("Rome", "Istanbul")
    solution = find_shortest_itinerary(query[0], query[1])
    print(f"The shortest path from {query[0]} to {query[1]} is {solution}")