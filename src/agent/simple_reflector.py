from agent.experience import Experience
from agent.reflection import Reflection
from agent.reflector import Reflector


class SimpleReflector(Reflector):
    """Generates basic reflections from agent experiences."""

    def reflect(self, experience: Experience) -> Reflection:
        if experience.evaluation.success:
            insight = (
                f"For the task '{experience.task.description}', "
                f"the approach produced a successful outcome: "
                f"{experience.evaluation.feedback}"
            )
        else:
            insight = (
                f"For the task '{experience.task.description}', "
                f"the approach should be improved: "
                f"{experience.evaluation.feedback}"
            )

        return Reflection(insight)