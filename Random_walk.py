from random import choice

class Randomwalk():
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""

        self.num_points = num_points
        #All walks start at (0,0).
        self.x_vals = [0]
        self.y_vals = [0]
        
        
    def get_steps(self):
        """Calculate steps forward, back, up or down"""
        
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4,5,6,7,8,9])
        step = direction * distance
        return step
    

    def fill_walk(self):
        """Calcuate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_vals) < self.num_points:

            x_step = self.get_steps()
            y_step = self.get_steps()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_vals[-1] + x_step
            next_y = self.y_vals[-1] + y_step

            self.x_vals.append(next_x)
            self.y_vals.append(next_y)

    
