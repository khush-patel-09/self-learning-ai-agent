# Self-Learning AI Agent

An experimental AI agent built from scratch that learns from its past interactions through semantic memory, experience tracking, evaluation, and reflection.

The project focuses on understanding the internal mechanics of a learning agent rather than relying on high-level agent frameworks.

## Architecture

```text
                         ┌──────────────┐
                         │     LLM      │
                         │    Ollama    │
                         └──────┬───────┘
                                │
                                ▼
User → Agent → Context Builder → Response
          │
          ├──────────────► Conversation
          │
          ├──────────────► Semantic Memory
          │
          └──────────────► Experience Memory
                                  │
                                  ▼
                              Evaluation
                                  │
                                  ▼
                              Reflection
                                  │
                                  ▼
                         Stored Experience
                                  │
                                  ▼
                      Semantic Experience Search
                                  │
                                  ▼
                       Learned Insight Retrieved
                                  │
                                  ▼
                         Future Similar Task
