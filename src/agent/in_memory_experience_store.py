from agent.experience import Experience
from agent.experience_store import ExperienceStore
from agent.memory.embeddings import EmbeddingModel
from agent.memory.similarity import cosine_similarity


class InMemoryExperienceStore(ExperienceStore):
    """Stores agent experiences and supports semantic search."""

    def __init__(
        self,
        embedding_model: EmbeddingModel | None = None,
        similarity_threshold: float = 0.3,
    ):
        self.experiences: list[Experience] = []
        self.embedding_model = embedding_model
        self.similarity_threshold = similarity_threshold
        self.embeddings: dict[int, list[float]] = {}

    def add(self, experience: Experience) -> None:
        """Store an experience and its embedding when available."""
        self.experiences.append(experience)

        if self.embedding_model is not None:
            self.embeddings[id(experience)] = self.embedding_model.embed(
                experience.task.description
            )

    def get_all(self) -> list[Experience]:
        """Return all stored experiences."""
        return self.experiences.copy()

    def search(self, query: str) -> list[Experience]:
        """Return experiences relevant to a query."""
        if self.embedding_model is None:
            query_terms = set(query.lower().split())

            return [
                experience
                for experience in self.experiences
                if query_terms.intersection(
                    set(experience.task.description.lower().split())
                )
            ]

        query_embedding = self.embedding_model.embed(query)

        scored_experiences = [
            (
                cosine_similarity(
                    query_embedding,
                    self.embeddings[id(experience)],
                ),
                experience,
            )
            for experience in self.experiences
        ]

        scored_experiences = [
            (score, experience)
            for score, experience in scored_experiences
            if score >= self.similarity_threshold
        ]

        scored_experiences.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return [
            experience
            for _, experience in scored_experiences
        ]