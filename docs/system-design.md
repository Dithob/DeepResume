# System Design

## Backend

The API is intentionally rule-based for MVP stability. LLM parsing can be added behind the parser service boundary without changing API contracts.

- `app/models/domain.py`: Pydantic domain schema.
- `app/services/resume_parser.py`: resume text to `ResumeProfile`.
- `app/services/job_parser.py`: JD text to `JobProfile`.
- `app/services/gap_analyzer.py`: rule-based `GapReport`.
- `app/services/learning_plan_parser.py`: Markdown plan import.
- `app/services/planner.py`: gap-driven learning plan generation.
- `app/services/evidence.py`: task-to-evidence conversion.

## Storage

The current implementation uses an in-memory repository to make the first loop testable. PostgreSQL and Redis are included in Docker Compose for the next persistence phase.

## AI Adapter Boundary

Future LLM providers should implement the same service-level contracts:

- resume text -> `ResumeProfile`
- JD text -> `JobProfile`
- gap report -> `LearningPlan`
- completed task -> resume bullet candidates
