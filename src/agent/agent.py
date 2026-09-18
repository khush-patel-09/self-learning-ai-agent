from agent.task import Task


class Agent:
    """Core agent responsible for processing tasks."""

    def run(self, task: Task) -> str:
        """Process a task and return a result."""
        raise NotImplementedError