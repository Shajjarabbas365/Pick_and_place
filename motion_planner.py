import numpy as np

class MotionPlanner:
    """
    Responsibility: Calculate trajectory points between start and goal.
    Principle: Pure logic, no ROS dependencies here (clean separation).
    """
    def plan_trajectory(self, start_pos, target_pos, steps=50):
        """
        Generates a list of intermediate joint positions (linear interpolation).
        """
        trajectory = []
        start_array = np.array(start_pos)
        target_array = np.array(target_pos)
        
        # Create intermediate steps
        for i in range(steps):
            alpha = i / float(steps)
            interpolated_pos = (1 - alpha) * start_array + alpha * target_array
            trajectory.append(interpolated_pos.tolist())
            
        return trajectory
