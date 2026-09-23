class Evaluation:
    """Represents an evaluation of an agent outcome."""

    def __init__(self, success: bool, feedback: str):
        self.success = success
        self.feedback = feedback