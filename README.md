# Self-Learning AI Agent

An experimental AI agent built from scratch that learns from its past interactions through semantic memory, experience tracking, evaluation, and reflection.

The project focuses on understanding the internal mechanics of a learning agent rather than relying on high-level agent frameworks.

## Architecture

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

## How it learns?

New Task
   ↓
Retrieve relevant memories and experiences
   ↓
Build context
   ↓
LLM generates response
   ↓
Action + Observation
   ↓
Evaluation
   ↓
Reflection
   ↓
Store Experience
   ↓
Future similar task
   ↓
Retrieve previous experience
   ↓
Reuse learned insight


## Core Components

- Agent — orchestrates the complete pipeline
- Semantic Memory — retrieves relevant stored information using embeddings
- Experience Memory — stores and retrieves past task experiences
- Evaluator — evaluates agent outcomes
- Reflector — converts experiences into reusable insights
- Context Builder — assembles relevant context for the LLM
- Ollama — provides a local LLM without paid APIs

# Running locally

pip install -e .
ollama pull qwen3:4b
python3 -m pytest

## Configure locally

LLM_PROVIDER=ollama
LLM_MODEL=qwen3:4b
LLM_BASE_URL=http://localhost:11434

## Testing

58 tests passing

Built from scratch to explore how memory, experience, reflection, and retrieval can be combined to create a learning agent.
