from agent.experience import Experience
from agent.reflection import Reflection
from agent.reflector import Reflector


class SimpleReflector(Reflector):
    """Generates basic reflections from agent experiences."""

    def reflect(self, experience: Experience) -> Reflection:
        if experience.evaluation.success:
            insight = (
                f"For similar tasks, the approach used for "
                f"'{experience.task.description}' produced a successful "
                f"outcome. {experience.evaluation.feedback}"
            )
        else:
            insight = (
                f"For similar tasks, the approach used for "
                f"'{experience.task.description}' should be improved. "
                f"Avoid repeating the same outcome: "
                f"{experience.evaluation.feedback}"
            )

        return Reflection(insight)