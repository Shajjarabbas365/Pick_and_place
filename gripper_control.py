class Gripper:
    """
    Responsibility: Manage gripper state (Open/Close).
    """
    def __init__(self):
        self.is_open = True
        # Angles for open and closed state
        self.OPEN_ANGLE = 0.0
        self.CLOSE_ANGLE = 0.5

    def get_action(self, action):
        if action == "GRIP":
            self.is_open = False
            return self.CLOSE_ANGLE
        elif action == "RELEASE":
            self.is_open = True
            return self.OPEN_ANGLE
        return self.OPEN_ANGLE
