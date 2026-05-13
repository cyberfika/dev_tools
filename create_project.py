#!/usr/bin/env python3
"""
create_project.py
Generate the base structure of a Web software project with AI agent files.
Based on AGENTS_WEB_UML.md architecture for modern Web development.
Supports React, TypeScript, Vite, and disciplined software engineering practices.
Includes PlantUML diagram templates for UML modeling.
"""

import sys
from pathlib import Path
from datetime import date

try:
    from plantuml_diagrams import get_all_plantuml_diagrams
except ImportError:
    # If plantuml_diagrams is not available, use empty dict
    def get_all_plantuml_diagrams():
        return {}

TODAY = date.today().isoformat()


# ---------------------------------------------------------------------------
# Templates dos arquivos markdown
# ---------------------------------------------------------------------------

def tpl_start_here(project_name, description, team):
    return f"""# START HERE

> Entry point for humans and AI agents. Read this file first.

## Project Summary

**Project Name:** {project_name}

{description}

## Team and Ownership

{team}

## Technology Stack

- **Frontend:** [React, TypeScript, Vite]
- **Build Tool:** [Vite]
- **Testing:** [Vitest, React Testing Library]
- **Styling:** [CSS Modules / Tailwind / other]
- **State Management:** [Local state / Context / other]
- **API Client:** [fetch / axios / other]
- **Backend:** [Node.js / Express / other - if applicable]

## Current Status

- **Project Status:** [Setup / In Development / Maintenance]
- **Current Sprint:** [Define sprint number and focus]
- **Last Updated:** {TODAY}

## How to Run Locally

```bash
npm install
npm run dev
```

## How to Test

```bash
npm run test
npm run test:ui
```

## How to Build

```bash
npm run build
npm run preview
```

## How to Preview Production Build

```bash
npm run preview
```

## Key Architecture Decisions

- [Decision 1 — see: `/docs/knowledge/source-of-truth/ADR/ADR-001-example.md`]
- [Decision 2 — see: `/docs/design.md`]

## Documentation Map

| Need                     | Location                                |
|--------------------------|-----------------------------------------|
| System Architecture      | `/docs/design.md`                       |
| Domain Model             | `/docs/knowledge/core/01_domain_model.md` |
| Component Architecture   | `/docs/design.md` → Component Architecture |
| Knowledge Base Index     | `/docs/knowledge/KNOWLEDGE_BASE.md`     |
| Knowledge Graph          | `/docs/knowledge/KNOWLEDGE_GRAPH.md` (if used) |
| AI Agent Rules           | `/AGENTS.md`                            |
| Implementation Plan      | `/docs/plan.md`                         |
| Current Tasks            | `/docs/tasks.md`                        |
| Design Decisions         | `/docs/design.md`                       |
| UML Diagrams             | `/docs/uml/`                            |
| Meeting Notes            | `/docs/knowledge/meetings/`             |
| Architecture Records     | `/docs/knowledge/source-of-truth/ADR/`  |

## Credentials and Access Policy

- **Never store secrets in code or documentation.**
- Environment variables: Use `.env.local` (not versioned).
- Client-side secrets: Use backend environment variables only.
- Service accounts: Store in secure credential management system.

## First Files to Read

1. This file (you are here).
2. `/AGENTS.md` — AI agent initialization and rules.
3. `/docs/knowledge/KNOWLEDGE_BASE.md` — Documentation index.
4. `/docs/knowledge/core/00_project_context.md` — Project context.
5. `/docs/design.md` — Current system design.
"""


def tpl_agents_md(project_name):
    return f"""# AGENTS.md

> Web AI Agent Rules for {project_name}
> Based on AGENTS_WEB_UML.md architecture.

## Mission

You are a senior Web software engineering agent specialized in modern frontend and full-stack Web development, JavaScript, TypeScript, HTML, CSS, React, Vite, UI architecture, software architecture, UML modeling, maintainability, scalability, clean code, automated testing, accessibility, and production-grade application development.

Produce code that is:

- Efficient, readable, maintainable, modular, scalable.
- Secure by design, accessible by default, easy to test.
- Free of TypeScript, lint, build, and runtime errors.
- Aligned with modern JavaScript, TypeScript, React, Vite, and Web platform best practices.
- Consistent with repository architecture and project conventions.
- Supported by UML and engineering artifacts whenever design is involved.

## Mandatory Session Initialization

Before answering any project-specific question or starting implementation, execute this initialization sequence:

1. Read `START_HERE.md`.
2. Read `/AGENTS.md` (this file).
3. Read `/docs/knowledge/KNOWLEDGE_BASE.md`.
4. Read `/docs/design.md`.
5. Read the current `/docs/plan.md` and `/docs/tasks.md`.
6. Read relevant documents from `/docs/knowledge/source-of-truth/`.
7. Inspect `package.json`, `vite.config.*`, `tsconfig*.json`, `eslint.config.*` if they exist.

## Core Rules

### Repository Grounding

- Base all recommendations on repository evidence.
- Cite files and line numbers in format: `path/to/file.md:L10-L18` or `/src/Component.tsx:L42`.
- Never invent APIs, routes, components, configuration values, or business rules.
- Say "I do not know based on the available repository context" when evidence is missing.

### Document Authority Hierarchy

Treat documents according to Tier classification:

| Tier | Examples                                        | Authority  |
|------|-------------------------------------------------|------------|
| 1    | Source of Truth, ADRs, approved requirements   | Absolute   |
| 2    | Core domain, architecture, component models    | High       |
| 3    | Implementation notes, meeting notes, working docs | Helpful   |
| 4    | Archived documents                              | Historical |

**Rule:** Tier 1 always wins. Do not contradict Source of Truth documents.

### Evidence and Confidence

Mark responses with confidence labels:

- `HIGH`: Directly supported by Tier 1 or current source code.
- `MEDIUM`: Supported by Tier 2 or multiple consistent documents.
- `LOW`: Inferred from partial evidence or missing explicit documentation.

Never present low-confidence claims as fact.

### Language Rules

- **Repository documentation:** English only (unless explicitly stated otherwise).
- **Code comments:** English or Portuguese per project team preference.
- **Chat explanations:** May follow user language.
- **UI copy:** Follow product localization requirements.

## Available Agents

Available specialized agents and their responsibilities:

| Agent Name                  | Role                                          | Activation  |
|-----------------------------|-----------------------------------------------|-------------|
| Web Developer Agent         | Implementation, coding, testing, refactoring  | `/dev`      |
| Frontend Architecture Agent | Component design, route architecture, patterns| `/arch`     |
| React Specialist Agent      | React-specific challenges, hooks, state       | `/react`    |
| Code Review Agent           | Review, quality, security, accessibility      | `/review`   |
| Security Review Agent       | Security analysis, vulnerability assessment   | `/security` |
| UML Modeling Agent          | System design, diagram creation, modeling     | `/uml`      |
| Testing Agent               | Test strategy, unit, integration, E2E tests   | `/test`     |

## UML-First Design Requirement

**UML is not optional—it is a core responsibility.**

For every non-trivial feature, module, UI flow, domain model, API integration, or architectural change, create or update UML diagrams in `/docs/design.md` or `/docs/uml/`.

Use Mermaid by default for Markdown compatibility.

Skip UML only for trivial changes (typos, simple CSS, isolated bug fixes). State briefly why it is unnecessary.

## Mandatory User Confirmation

Always ask for explicit user confirmation before:

- `git commit`, `git push`
- Pull request or merge creation
- Deployment, release tagging
- Running database migrations against non-local environments
- Production configuration changes
- Secret rotation
- Changes to environment variables in hosted services
- Calls to external APIs that create, modify, or delete resources
- Ticket updates in Jira, Linear, GitHub Issues
- Sending emails or notifications
- Deleting files
- Updating Tier 1 Source of Truth documents

Do not claim actions were executed unless they were actually executed and authorized.

## Clarifying Questions

Ask focused questions when:

- Requirements are ambiguous.
- Domain rules are incomplete.
- TypeScript configuration affects implementation.
- Routing strategy is unknown.
- State management strategy is unknown.
- API contracts are missing.
- UI/UX behavior is undefined.
- Browser support requirements are unknown.
- Security or authentication behavior is undefined.
- There is conflict between documents.
- The requested action could modify shared systems.

Do not ask unnecessary questions when a safe reasonable default is clear.

## Documentation System

This project uses a mandatory documentation system:

- `/docs/plan.md` — Current implementation plan.
- `/docs/tasks.md` — Actionable work items.
- `/docs/design.md` — Architecture, UML, design decisions.
- `/docs/memory.md` — Durable decisions, user preferences.
- `/docs/knowledge/KNOWLEDGE_BASE.md` — Documentation index and navigation.
- `/docs/knowledge/source-of-truth/` — Tier 1 authoritative documents.
- `/docs/knowledge/core/` — Tier 2 core knowledge (numbered files).
- `/docs/knowledge/implementation/` — Tier 3 working documents.
- `/docs/knowledge/meetings/` — Meeting notes (date-prefixed).
- `/docs/knowledge/archive/` — Tier 4 historical documents.
- `/docs/adr/` — Architecture Decision Records.
- `/docs/uml/` — UML diagrams and visualizations.

Before implementation, update or propose updates to plan, tasks, design, and memory files.

## Non-Negotiable Rules

1. Do not hallucinate project facts.
2. Do not contradict Source of Truth documents.
3. Do not modify Tier 1 documents without user approval.
4. Do not execute Git operations without authorization.
5. Do not introduce dependencies without justification.
6. Do not generate knowingly broken TypeScript, JavaScript, or React code.
7. Do not ignore tests for meaningful changes.
8. Do not ignore accessibility for user-facing changes.
9. Do not ignore security for Web-facing changes.
10. Do not skip design documentation for architectural changes.
11. Do not skip UML when it materially helps explain the design.
12. Do not store secrets in code or documentation.
13. Do not create high coupling when clean boundaries are feasible.
14. Do not let the knowledge base become stale.
15. Do not present low-confidence assumptions as facts.
"""


def tpl_plan_md():
    return f"""# Plan

> Current implementation plan and strategy.
> Status: Active
> Last Updated: {TODAY}

## Objective

[What is the main goal or problem this plan addresses?]

## Scope

### Included

- [Feature / Component 1]
- [Feature / Component 2]

### Excluded

- [Out of scope item 1]
- [Out of scope item 2]

## Assumptions

- [Assumption 1]
- [Assumption 2]

## Questions for the User

- [Question 1 — blocking or informational?]
- [Question 2]

## Constraints

- [Technical constraint]
- [Timeline constraint]
- [Resource constraint]

## Architecture Impact

- [How does this affect the existing architecture?]
- [New modules or boundaries?]
- [Dependency changes?]

## UI/UX Impact

- [New routes or pages?]
- [Component changes?]
- [State management changes?]

## Accessibility Impact

- [Any WCAG considerations?]
- [Keyboard navigation?]
- [Screen reader support?]

## Implementation Strategy

### Phase 1: [Phase name]

- [Task 1]
- [Task 2]

### Phase 2: [Phase name]

- [Task 1]

## Testing Strategy

- Unit tests for: [domains, utilities, hooks, services]
- Component tests for: [UI behavior]
- Integration tests for: [API flows, forms, persistence]
- E2E tests for: [critical user journeys]

## Risks

| Risk                      | Probability | Impact | Mitigation                |
|---------------------------|-------------|--------|---------------------------|
| [Risk 1]                  | High/Med/Low| H/M/L  | [How to mitigate]         |

## Acceptance Criteria

- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] All tests pass
- [ ] Code review approved
- [ ] Documentation updated
"""


def tpl_tasks_md():
    return f"""# Tasks

> Actionable work items and progress tracking.
> Last Updated: {TODAY}

## Backlog

- [ ] [Task 1 — component/module]
- [ ] [Task 2 — feature]
- [ ] [Task 3 — bug fix]

## In Progress

- [ ] [Task being worked on — owner]

## Blocked

- [ ] [Blocked task — reason — owner]

## Completed

- [x] [Completed task 1]
- [x] [Completed task 2]

## Verification Checklist

- [ ] Code written and peer-reviewed
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] No lint or type errors
- [ ] Build succeeds (`npm run build`)
- [ ] Accessibility verified
- [ ] Security review completed
- [ ] Documentation updated
- [ ] UML diagrams updated (if design changed)
- [ ] Merged to main branch
"""


def tpl_memory_md():
    return f"""# Memory

> Durable decisions, approved approaches, rejected approaches, and user preferences.
> Status: Active
> Last Updated: {TODAY}

## User Preferences

- [Preference 1 — e.g., "Always use TypeScript strict mode"]
- [Preference 2 — e.g., "Prefer React hooks over class components"]

## Approved Decisions

- [Decision 1 — date: why this was chosen]
- [Decision 2 — see ADR-XXX for details]

## Rejected Decisions

- [Rejected approach 1 — why rejected]
- [Rejected approach 2 — why rejected]

## Repository Conventions

- **Naming:** [camelCase for functions, PascalCase for components]
- **Structure:** [Feature-based folder organization]
- **Testing:** [Vitest + React Testing Library]
- **Styling:** [CSS Modules]
- **State:** [Local state + Context]

## Important Context

- [Context item 1 — might affect decisions]
- [Context item 2]

## Open Questions

- [Question 1 — who to ask, what info needed?]
- [Question 2]

## Session Log

| Date       | Summary                      | Next Steps                  |
|------------|------------------------------|-----------------------------|
| {TODAY}    | Project initialized          | Fill in project details     |
| [Date]     | [What was done]              | [What's next]               |
"""


def tpl_knowledge_base(project_name):
    return f"""# Knowledge Base

> Documentation index and navigation map for {project_name}.
> Status: Active
> Authority: Meta-documentation
> Last Updated: {TODAY}

## Purpose

This document is the single source of truth for finding, understanding, and maintaining all project documentation. It organizes documents by authority tier, concept cluster, and navigation path.

A stale knowledge base is worse than no knowledge base. Maintain this file whenever documentation changes.

## Authority Hierarchy

### Tier 1: Source of Truth

**Location:** `/docs/knowledge/source-of-truth/`

**Examples:**
- Leadership-approved requirements
- Architecture Decision Records (ADRs)
- Approved product requirements
- Approved UX/UI specifications
- Approved design system rules
- Approved accessibility requirements
- Approved security requirements
- Contractual API specifications
- Domain rules approved by business owner

**Rules:**
- Treat as authoritative.
- Do not contradict Tier 1 documents.
- If lower-tier conflicts with Tier 1, Tier 1 wins.
- Do not modify without explicit user approval.
- Cite for authoritative claims.

### Tier 2: Core Knowledge

**Location:** `/docs/knowledge/core/`

**Examples:**
- `00_project_context.md` — Project overview and goals
- `01_domain_model.md` — Domain concepts and business rules
- `02_frontend_architecture.md` — Frontend layering and boundaries
- `03_component_model.md` — Component design patterns and structure
- `04_api_integration.md` — API contracts and integration points
- `05_testing_strategy.md` — Testing approach and coverage expectations
- `06_accessibility_strategy.md` — Accessibility standards and implementation
- `07_security_model.md` — Security considerations and threat model
- `08_deployment_model.md` — Deployment architecture and environments

**Rules:**
- Use as foundational technical context.
- If conflicts with Tier 1, follow Tier 1.
- Keep aligned with current architecture.
- Update when architecture changes.

### Tier 3: Implementation and Working Documents

**Location:** `/docs/plan.md`, `/docs/tasks.md`, `/docs/design.md`, `/docs/memory.md`, `/docs/knowledge/implementation/`, `/docs/knowledge/meetings/`, `/docs/generated/`

**Examples:**
- Sprint plans and notes
- Work-in-progress analysis
- Generated reports and artifacts
- Implementation notes and experiments
- Meeting notes (date-prefixed: `2026-05-13_sprint-review.md`)
- Current tasks and blockers

**Rules:**
- Use as helpful but not fully authoritative context.
- Validate important claims against Tier 1 and Tier 2.
- Do not let temporary notes override approved architecture.
- These are working documents; they evolve frequently.

### Tier 4: Archive

**Location:** `/docs/knowledge/archive/`

**Status:** Historical and non-authoritative.

**Rules:**
- Treat as historical reference only.
- Do not cite as current truth unless user asks for history.
- Do not use to justify new implementation decisions.
- Every archived document must start with: `> Status: Archived. This document is historical and non-authoritative.`

## Concept Clusters

### System Architecture

| Document                           | Purpose                               | Tier |
|------------------------------------|---------------------------------------|------|
| `/docs/design.md`                  | Current system design and UML         | Tier 2/3 |
| `/docs/knowledge/core/00_project_context.md` | Project goals and scope | Tier 2 |
| `/docs/knowledge/core/02_frontend_architecture.md` | Frontend architecture | Tier 2 |
| `/docs/knowledge/source-of-truth/ADR/` | Architecture decisions | Tier 1 |

### Domain and Business Rules

| Document                           | Purpose                               | Tier |
|------------------------------------|---------------------------------------|------|
| `/docs/knowledge/core/01_domain_model.md` | Domain model and rules | Tier 2 |
| `/docs/design.md` → Domain Model   | Current domain state                  | Tier 3 |

### Component and UI Architecture

| Document                           | Purpose                               | Tier |
|------------------------------------|---------------------------------------|------|
| `/docs/knowledge/core/03_component_model.md` | Component patterns | Tier 2 |
| `/docs/design.md` → Component Architecture | Current components | Tier 3 |
| `/docs/uml/` | Component diagrams | Tier 3 |

### API Integration

| Document                           | Purpose                               | Tier |
|------------------------------------|---------------------------------------|------|
| `/docs/knowledge/core/04_api_integration.md` | API contracts | Tier 2 |
| `/docs/design.md` → API Integration | Current integrations | Tier 3 |

### Testing and Quality

| Document                           | Purpose                               | Tier |
|------------------------------------|---------------------------------------|------|
| `/docs/knowledge/core/05_testing_strategy.md` | Testing strategy | Tier 2 |
| `/docs/tasks.md` → Verification Checklist | Current test status | Tier 3 |

### Accessibility

| Document                           | Purpose                               | Tier |
|------------------------------------|---------------------------------------|------|
| `/docs/knowledge/core/06_accessibility_strategy.md` | A11y requirements | Tier 2 |
| `/docs/design.md` → Accessibility Considerations | Current a11y approach | Tier 3 |

### Security

| Document                           | Purpose                               | Tier |
|------------------------------------|---------------------------------------|------|
| `/docs/knowledge/core/07_security_model.md` | Security model | Tier 2 |
| `/docs/design.md` → Security Considerations | Current security approach | Tier 3 |

### Deployment and Operations

| Document                           | Purpose                               | Tier |
|------------------------------------|---------------------------------------|------|
| `/docs/knowledge/core/08_deployment_model.md` | Deployment architecture | Tier 2 |
| `/docs/knowledge/implementation/` | Operational notes | Tier 3 |

### Team and Planning

| Document                           | Purpose                               | Tier |
|------------------------------------|---------------------------------------|------|
| `START_HERE.md` → Team and Ownership | Team structure | Root |
| `/docs/memory.md` | User preferences and decisions | Tier 3 |
| `/docs/plan.md` | Current implementation plan | Tier 3 |
| `/docs/tasks.md` | Work items and progress | Tier 3 |
| `/docs/knowledge/meetings/` | Meeting notes | Tier 3 |

## Navigation Paths

### For New Team Members

1. Start: `START_HERE.md`
2. Read: `/AGENTS.md`
3. Read: `/docs/knowledge/KNOWLEDGE_BASE.md` (this file)
4. Read: `/docs/knowledge/core/00_project_context.md`
5. Read: `/docs/knowledge/core/01_domain_model.md`
6. Read: `/docs/design.md`
7. Read: `/docs/knowledge/source-of-truth/ADR/` (as relevant)

### For Architecture Review

1. Start: `/docs/design.md`
2. Read: `/docs/knowledge/core/02_frontend_architecture.md`
3. Read: `/docs/knowledge/core/03_component_model.md`
4. Read: `/docs/knowledge/source-of-truth/ADR/` (relevant decisions)
5. Check: `/docs/knowledge/meetings/` (recent changes)

### For Implementation

1. Check: `/docs/plan.md` (current plan)
2. Check: `/docs/tasks.md` (work items)
3. Read: Relevant Tier 2 core files
4. Read: `/docs/design.md` (current state)
5. Check: `/docs/memory.md` (conventions and decisions)

### For Meeting Follow-Up

1. Create: `/docs/knowledge/meetings/YYYY-MM-DD_meeting-topic.md`
2. Extract decisions to: `/docs/memory.md`
3. Create/Update: `/docs/knowledge/source-of-truth/ADR/` if architectural
4. Update: `/docs/plan.md` and `/docs/tasks.md`
5. Update: `/docs/design.md` if design changed
6. Update: This file if documentation structure changed

## Relationship Map

```mermaid
graph TD
    START["START_HERE.md"]
    AGENTS["AGENTS.md"]
    KB["KNOWLEDGE_BASE.md"]

    START --> AGENTS
    START --> KB
    START --> PLAN["/docs/plan.md"]
    START --> DESIGN["/docs/design.md"]

    KB --> T1["Tier 1: Source of Truth"]
    KB --> T2["Tier 2: Core Knowledge"]
    KB --> T3["Tier 3: Working Documents"]
    KB --> T4["Tier 4: Archive"]

    T1 --> ADR["/docs/knowledge/source-of-truth/ADR/"]
    T1 --> ARCH["/docs/knowledge/source-of-truth/ARCHITECTURE.md"]

    T2 --> CTX["/docs/knowledge/core/00_project_context.md"]
    T2 --> DOM["/docs/knowledge/core/01_domain_model.md"]
    T2 --> FA["/docs/knowledge/core/02_frontend_architecture.md"]
    T2 --> CM["/docs/knowledge/core/03_component_model.md"]
    T2 --> API["/docs/knowledge/core/04_api_integration.md"]

    T3 --> TASKS["/docs/tasks.md"]
    T3 --> MEM["/docs/memory.md"]
    T3 --> MEET["/docs/knowledge/meetings/"]

    DESIGN --> UML["/docs/uml/"]
    PLAN --> TASKS
```

## Maintenance Rules

### When to Update This File

Update `/docs/knowledge/KNOWLEDGE_BASE.md` when:

- A new documentation file is added
- A document is archived
- A major design decision changes
- A new module or component pattern is introduced
- A new route is introduced
- A new API integration is introduced
- A meeting creates or changes decisions
- A sprint plan changes priorities
- A Source of Truth document is added or updated
- Tier authority levels change
- Documentation structure is reorganized

### Post-Decision Workflow

After any significant decision:

1. Record in `/docs/memory.md`
2. Create ADR in `/docs/knowledge/source-of-truth/ADR/` if architectural
3. Update `/docs/design.md` if design affected
4. Update UML diagrams in `/docs/uml/`
5. Update `/docs/tasks.md` if work changes
6. Update this knowledge base with evidence trails

### Post-Meeting Workflow

After meetings:

1. Create: `/docs/knowledge/meetings/YYYY-MM-DD_topic.md`
2. Extract decisions: `/docs/memory.md`
3. Convert to ADR if needed: `/docs/knowledge/source-of-truth/ADR/`
4. Update: `/docs/tasks.md`
5. Update: `/docs/design.md` and UML if changed
6. Update: This knowledge base
"""


def tpl_architecture():
    return f"""# ARCHITECTURE.md

> System architecture overview.
> Status: Active
> Authority: Tier 1: Source of Truth (read-only for AI agents)
> Last Updated: {TODAY}

## Architecture Overview

[Describe the system architecture at a high level.]

### High-Level System Diagram

```mermaid
graph TB
    Browser["🌐 Browser<br/>React App"]
    CDN["📦 CDN<br/>Static Assets"]
    Backend["🔧 Backend API<br/>Node.js/Express"]
    Database["💾 Database<br/>PostgreSQL"]

    Browser -->|GET| CDN
    Browser -->|REST API| Backend
    Backend -->|Query| Database
```

## Core Components

| Component              | Responsibility                  | Technology        |
|------------------------|---------------------------------|-------------------|
| Frontend               | UI, user interactions, routing  | React + TypeScript |
| API Server             | REST endpoints, business logic  | Node.js / Express |
| Database               | Data persistence                | PostgreSQL        |
| CDN / Static Hosting   | Asset delivery                  | Vercel / Netlify  |

## Architectural Decisions (ADRs)

See `/docs/knowledge/source-of-truth/ADR/` for detailed decision records.

### Decision Tiers

- **ADR-001:** [Title] — [Link]
- **ADR-002:** [Title] — [Link]

## Technology Stack

### Frontend

- **Runtime:** Node.js / Browser
- **Framework:** React 18+
- **Language:** TypeScript
- **Build Tool:** Vite
- **Testing:** Vitest + React Testing Library
- **State:** Context API + Local State
- **Styling:** [CSS Modules / Tailwind / other]

### Backend (if applicable)

- **Runtime:** Node.js
- **Framework:** [Express / Fastify / other]
- **Language:** TypeScript or JavaScript
- **Database:** [PostgreSQL / MongoDB / other]
- **Authentication:** [JWT / Sessions / OAuth]

## Constraints and Principles

### Core Principles

1. **Modularity:** Code is split into cohesive, decoupled modules
2. **Testability:** Code is designed to be testable
3. **Maintainability:** Clear intent, minimal coupling, SOLID principles
4. **Accessibility:** WCAG 2.1 Level AA by default
5. **Security:** Secure by design, least privilege
6. **Performance:** Optimized for user experience
7. **Documentation:** Decisions recorded in ADRs, code is self-documenting

### Constraints

- **Browser Support:** [List supported browsers]
- **Performance Targets:** [Load time, interactive targets]
- **Accessibility:** WCAG 2.1 Level AA minimum
- **Security:** [Specific requirements]

## Deployment Model

[See `/docs/knowledge/core/08_deployment_model.md`]

## Key Decisions by Domain

### Frontend Architecture

- **Layering:** See `/docs/knowledge/core/02_frontend_architecture.md`
- **Components:** See `/docs/knowledge/core/03_component_model.md`
- **State Management:** Context API + Local State (no Redux without approval)

### API Integration

- **Approach:** See `/docs/knowledge/core/04_api_integration.md`
- **Error Handling:** Domain-specific error types
- **Caching:** [Strategy if applicable]

### Data Model

- **Domain Model:** See `/docs/knowledge/core/01_domain_model.md`
- **Persistence:** [Strategy and technology]

### Testing

- **Strategy:** See `/docs/knowledge/core/05_testing_strategy.md`
- **Coverage:** >70% for components, >80% for logic

### Accessibility

- **Standard:** WCAG 2.1 Level AA
- **Details:** See `/docs/knowledge/core/06_accessibility_strategy.md`

### Security

- **Threat Model:** See `/docs/knowledge/core/07_security_model.md`
- **Authentication:** [Method]
- **Authorization:** [Role-based access control if applicable]

## Folder Structure

[Reference `/docs/design.md` → Frontend Architecture for complete structure]

## Related Documents

- `/docs/design.md` — Current system design
- `/docs/knowledge/source-of-truth/ADR/` — Architecture Decision Records
- `/AGENTS.md` — AI agent rules
"""


def tpl_adr():
    return f"""# ADR-001: [Decision Title]

> Architecture Decision Record
> Status: Proposed / Accepted / Deprecated / Superseded
> Date: {TODAY}
> Author: [Name]
> Affected By: [Related ADRs if any]

## Context

[Why was this decision necessary? What problem were we trying to solve?]

[Describe the situation and constraints that led to this decision.]

## Decision

[What decision was made? Be clear and specific.]

[Explain what the solution is and why it was chosen.]

## Rationale

[Why is this the best decision?]

- **Benefit 1:** [Positive impact]
- **Benefit 2:** [Positive impact]
- **Tradeoff 1:** [Negative impact]

## Alternatives Considered

### Option 1: [Alternative title]

**Pros:**
- [Pro 1]
- [Pro 2]

**Cons:**
- [Con 1]
- [Con 2]

**Why not chosen:** [Reason]

### Option 2: [Alternative title]

[Similar structure...]

## Consequences

### Positive

- [Consequence 1]
- [Consequence 2]

### Negative

- [Consequence 1]
- [Consequence 2]

## Implementation Notes

[How will this decision be implemented?]

[Any migration steps or timeline needed?]

## References

- [Link to related issue]
- [Link to discussion]
- [Link to documentation]

## Related ADRs

- [ADR-XXX: Related decision]
"""


def tpl_design():
    return f"""# Design

> System architecture, domain model, components, flows, UML diagrams, and design decisions.
> Status: Active
> Authority: Tier 2/3
> Last Updated: {TODAY}

## System Overview

[Describe the system at a high level. Who uses it? What problems does it solve? What is the main goal?]

## Domain Model

### Core Concepts

[List and describe the main domain concepts and business rules.]

**Key Entities:**

- [Entity 1]: [Brief description]
- [Entity 2]: [Brief description]

**Business Rules:**

- [Rule 1]
- [Rule 2]

### Domain Diagram

```mermaid
classDiagram
    class [Entity1] {{
        +id: string
        +name: string
    }}

    class [Entity2] {{
        +id: string
        +reference: string
    }}

    [Entity1] --|> [Entity2]
```

## Frontend Architecture

### Layering

Describe the architectural layers of the frontend:

- **Presentation Layer:** React components, pages, layouts
- **Application Layer:** Hooks, services, state coordination
- **Domain Layer:** Domain models, business rules, value objects
- **Infrastructure Layer:** API clients, storage adapters, third-party SDKs

### Folder Structure

```
src/
├── app/                    # App root, providers
├── pages/                  # Route-level components
├── features/               # Feature modules
├── shared/                 # Reusable components, hooks, utilities
│   ├── components/
│   ├── hooks/
│   ├── services/
│   ├── api/
│   └── utils/
└── main.tsx
```

[Adjust according to your actual structure.]

## Component Architecture

### Major Components

| Component                | Purpose                        | Owner         |
|-------------------------|--------------------------------|---------------|
| [ComponentName]         | [What does it do?]             | [Responsible] |

### Component Diagram

```mermaid
graph TB
    App[React App]
    Router[Router]
    Layout[App Layout]
    Page["Feature Page"]
    Hook["Custom Hook"]
    Service["Application Service"]
    ApiClient["API Client"]
    Api["Backend API"]

    App --> Router
    Router --> Layout
    Layout --> Page
    Page --> Hook
    Hook --> Service
    Service --> ApiClient
    ApiClient --> Api
```

## Route Architecture

### Routes

| Route                   | Component           | Auth Required | Purpose               |
|-------------------------|---------------------|----------------|-----------------------|
| `/`                     | HomePage            | No             | Landing or dashboard  |
| [/path]                 | [Component]         | [Yes/No]       | [Purpose]             |

## State Management

### Strategy

[Describe your state management approach: local state, Context, Redux, Zustand, etc.]

**Rules:**
- [Rule 1]
- [Rule 2]

### Global State

[List global state providers, their scope, and what they manage.]

- Context: [Name] — manages [what]
- Provider location: [Component]

## Interfaces and Contracts

### API Contracts

#### GET /api/[resource]

Request:
```
GET /api/[resource]?param=value
```

Response:
```json
{{
  "data": [
    {{ "id": "1", "name": "Example" }}
  ]
}}
```

Errors:
- 404: Resource not found
- 500: Server error

## Data Flow

### Typical Request/Response Flow

```mermaid
sequenceDiagram
    actor User
    participant Page as LoginPage
    participant Hook as useLoginForm
    participant Service as AuthService
    participant API as Auth API
    participant Storage as Storage

    User->>Page: Submit credentials
    Page->>Hook: handleSubmit(formData)
    Hook->>Service: signIn(email, password)
    Service->>API: POST /auth/login
    API-->>Service: {{accessToken, user}}
    Service->>Storage: Save session
    Service-->>Hook: AuthSession
    Hook-->>Page: success state
    Page-->>User: Navigate to dashboard
```

## Error Handling Strategy

- **Approach:** [Describe how errors are handled: try-catch, Error Boundaries, error states, etc.]
- **User Feedback:** [How are errors communicated to users?]
- **Logging:** [What is logged and where?]

**Error States:**

- Idle
- Loading
- Success
- Error
- Empty
- Unauthorized
- Forbidden

## Accessibility Considerations

**Standards:** WCAG 2.1 Level AA

**Key Considerations:**

- [Keyboard navigation: all interactive elements accessible via keyboard]
- [Screen reader support: semantic HTML, proper labels, ARIA]
- [Color contrast: sufficient contrast ratios]
- [Motion: respect prefers-reduced-motion]
- [Focus management: visible focus indicators, focus trapping in modals]

## Security Considerations

**Threat Model:**

- [Threat 1: mitigation]
- [Threat 2: mitigation]

**Key Rules:**

- Never hardcode secrets
- Validate input at boundaries
- Sanitize HTML output
- Use HttpOnly cookies for sensitive tokens (if backend supports)
- Avoid storing long-lived tokens in localStorage
- Authenticate and authorize all backend operations

## Performance Considerations

**Optimization Strategy:**

- [Code splitting strategy]
- [Image optimization]
- [Caching strategy]
- [Bundle size targets]

**Measured Metrics:**

- [Metric 1: target]
- [Metric 2: target]

## UML Diagrams

### Use Case Diagram

```mermaid
graph LR
    Visitor["Visitor"]
    User["Authenticated User"]
    Admin["Admin"]

    UC1[("Browse Features")]
    UC2[("Authenticate")]
    UC3[("Manage Profile")]
    UC4[("Manage System")]

    Visitor --> UC1
    Visitor --> UC2
    User --> UC3
    Admin --> UC4
```

### Class Diagram

```mermaid
classDiagram
    class User {{
        +id: string
        +email: string
        +name: string
        +role: UserRole
        +isAdmin() boolean
    }}

    class AuthSession {{
        +accessToken: string
        +expiresAt: Date
        +isExpired() boolean
    }}

    class AuthService {{
        +signIn(email, password) Promise~AuthSession~
        +signOut() Promise~void~
        +getCurrentUser() Promise~User~
    }}

    AuthService ..> AuthSession
    AuthService ..> User
```

### State Machine Diagram

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Validating: submit
    Validating --> Submitting: valid
    Validating --> Invalid: invalid
    Invalid --> Idle: edit
    Submitting --> Success: success
    Submitting --> Error: error
    Error --> Idle: retry
    Success --> [*]
```

## Design Decisions

### Decision 1: [Title]

**Status:** Active
**Date:** {TODAY}
**Context:** [Why was this needed?]
**Decision:** [What was decided?]
**Consequences:** [Positive and negative impacts]
**Alternatives Considered:** [What else could we have done?]

See also: `/docs/knowledge/source-of-truth/ADR/ADR-001.md`

## Testing Strategy

- **Unit Tests:** Pure logic, utilities, domain rules
- **Component Tests:** UI behavior, user interactions
- **Integration Tests:** Hooks, API flows, forms
- **E2E Tests:** Critical user journeys

## Next Steps

- [Action item 1]
- [Action item 2]
"""


def tpl_project_context():
    return f"""# 00_project_context.md

> Project overview and context.
> Status: Active
> Authority: Tier 2: Core Knowledge
> Last Updated: {TODAY}

## Project Goal

[What is the main goal of this project? What problem does it solve?]

## Success Criteria

- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

## Target Users

[Who are the primary users of this system?]

- [User Persona 1]
- [User Persona 2]

## Problem Statement

[What business or technical problem does this project address?]

## Scope

### In Scope

- [Feature/Capability 1]
- [Feature/Capability 2]

### Out of Scope

- [Not included 1]
- [Not included 2]

## Key Constraints

- **Timeline:** [Launch date or phases]
- **Budget/Resources:** [Resource availability]
- **Technical:** [Platform, browser support, performance targets]
- **Regulatory:** [Compliance requirements if any]

## Stakeholders

| Name         | Role                    | Contact         |
|--------------|-------------------------|-----------------|
| [Stakeholder] | [Product Owner/Manager] | [Email/Slack]   |

## Success Metrics

- [Metric 1: how measured?]
- [Metric 2: how measured?]

## Dependencies

### External Systems

- [System/Service 1]: [Used for what?]
- [System/Service 2]: [Used for what?]

### Team Dependencies

- [Team 1]: [How do we depend on them?]

## Risks and Assumptions

### Key Assumptions

- [Assumption 1]
- [Assumption 2]

### Known Risks

| Risk                  | Probability | Impact | Mitigation              |
|-----------------------|-------------|--------|-------------------------|
| [Risk 1]              | High/Med/Low| H/M/L  | [How to mitigate]       |
"""


def tpl_domain_model():
    return f"""# 01_domain_model.md

> Domain concepts, entities, value objects, and business rules.
> Status: Active
> Authority: Tier 2: Core Knowledge
> Last Updated: {TODAY}

## Core Concepts

[Describe the main domain concepts and their relationships.]

### Entity: [Name]

**Responsibility:** [What role does this entity play?]

**Attributes:**
- `id: string` — Unique identifier
- `[attribute]: [type]` — [Description]

**Behaviors:**
- `[method]()` — [What does it do?]

**Invariants:**
- [Business rule 1]
- [Business rule 2]

### Value Object: [Name]

**Responsibility:** [What role does this value object play?]

**Attributes:**
- `[attribute]: [type]` — [Description]

**Invariants:**
- [Rule 1]

## Domain Rules

- [Rule 1]
- [Rule 2]
- [Rule 3]

## Relationships

[Describe how domain concepts relate to each other.]

## Bounded Contexts

[If your domain is large, describe bounded contexts and their boundaries.]

- **Context 1:** [What is isolated here?]
- **Context 2:** [What is isolated here?]
"""


def tpl_frontend_architecture():
    return f"""# 02_frontend_architecture.md

> Frontend architecture, layering, and structural boundaries.
> Status: Active
> Authority: Tier 2: Core Knowledge
> Last Updated: {TODAY}

## Architecture Pattern

[Describe your chosen architecture: feature-based, layered, hexagonal, etc.]

## Layering

### Presentation Layer

**Responsibility:** React components, pages, layouts, UI rendering.

**Contents:**
- `/src/pages/` — Route-level components
- `/src/features/*/components/` — Feature-specific components

**Rules:**
- No business logic
- No direct API calls (use hooks or services)
- No domain logic

### Application Layer

**Responsibility:** Use-case orchestration, state coordination, side effects.

**Contents:**
- `/src/hooks/` — Custom React hooks
- `/src/services/application/` — Application services
- Providers for Context

**Rules:**
- Coordinate between UI and domain
- No React JSX (except in hooks)
- No infrastructure details

### Domain Layer

**Responsibility:** Business rules, domain models, value objects.

**Contents:**
- `/src/domain/` — Domain entities, value objects, aggregates
- Domain services for complex business logic

**Rules:**
- Pure TypeScript (no React, no HTTP, no storage)
- Framework-agnostic
- Testable without any framework

### Infrastructure Layer

**Responsibility:** External system integration.

**Contents:**
- `/src/api/` — API clients, HTTP adapters
- `/src/storage/` — Local storage, IndexedDB adapters
- `/src/analytics/` — Analytics SDKs
- Third-party integrations

**Rules:**
- Adapters for external systems
- Keep at the edges
- Translate to/from domain models

## Data Flow

**Typical Flow:**

User Action → Component → Hook → Service → API Client → Backend

## Key Decisions

- **State Management:** [How state is managed]
- **API Integration:** [How APIs are called]
- **Storage:** [How data is persisted]
- **Routing:** [Routing framework and strategy]
"""


def tpl_component_model():
    return f"""# 03_component_model.md

> Component architecture, patterns, and design guidelines.
> Status: Active
> Authority: Tier 2: Core Knowledge
> Last Updated: {TODAY}

## Component Classification

### Page Components

**Purpose:** Route-level containers that orchestrate features.

**Example:** `HomePage`, `ProductDetailsPage`

**Rules:**
- One per route
- Minimal markup
- Coordinate with hooks and services
- Do not contain detailed UI logic

### Feature Components

**Purpose:** Self-contained feature implementations.

**Example:** `LoginForm`, `ProductList`, `CheckoutWizard`

**Rules:**
- Encapsulate feature behavior
- May contain state and effects
- Depend on shared components
- Export as default or named

### Shared Components

**Purpose:** Reusable UI elements used across the app.

**Examples:** `Button`, `Modal`, `Card`, `Input`

**Rules:**
- No feature-specific knowledge
- Accept props for customization
- Document props clearly
- Support accessibility requirements

### Layout Components

**Purpose:** Structure pages and sections.

**Examples:** `AppLayout`, `SidebarLayout`

**Rules:**
- Provide consistent structure
- Pass children through

## Naming Conventions

- **Component Files:** `PascalCase.tsx` (e.g., `LoginForm.tsx`)
- **Component Functions:** `PascalCase` (e.g., `LoginForm`)
- **Hook Files:** `useXxx.ts` (e.g., `useLoginForm.ts`)
- **Custom Hooks:** `useXxx` (e.g., `useLoginForm`)

## Props and State

### Preferred Props Pattern

```typescript
interface LoginFormProps {{
  onSuccess: (session: AuthSession) => void;
  isLoading?: boolean;
}}
```

**Rules:**
- Keep props focused and named
- Use TypeScript interfaces
- Document required vs. optional
- Avoid prop drilling

### State Management

- **Local State:** `useState` for UI state
- **Shared State:** Context for theme, auth, locale
- **Complex State:** Custom hooks with useReducer

## Composition Over Inheritance

- Prefer component composition
- Use render props or compound components when needed
- Avoid prop drilling with Context

## Testing Approach

- Unit tests for pure logic
- Component tests for UI behavior
- Integration tests for workflows
"""


def tpl_api_integration():
    return f"""# 04_api_integration.md

> API contracts, integration patterns, and data mapping.
> Status: Active
> Authority: Tier 2: Core Knowledge
> Last Updated: {TODAY}

## API Overview

**Base URL:** `[protocol]://[domain]:[port]/api`

**Authentication:** [How authentication is handled]

## API Client Structure

**Location:** `/src/api/`

**Exports:**
- API client instance
- Request/response types
- Error handling utilities

**Rules:**
- Centralize configuration
- Keep DTOs separate from domain models
- Handle authentication consistently
- Implement error handling consistently

## Endpoint Reference

### Authentication

#### POST /auth/login

**Request:**

```json
{{
  "email": "user@example.com",
  "password": "password"
}}
```

**Response (200 OK):**

```json
{{
  "accessToken": "jwt...",
  "user": {{
    "id": "123",
    "email": "user@example.com"
  }}
}}
```

**Errors:**
- 400: Invalid credentials
- 500: Server error

## Data Mapping

**Rule:** Map API DTOs to domain models at the API boundary.

```typescript
// API response (DTO)
interface UserDTO {{
  id: string;
  email: string;
}}

// Domain model
class User {{
  id: string;
  email: string;
}}

// Mapper
function mapUserDTOToUser(dto: UserDTO): User {{
  return new User(dto.id, dto.email);
}}
```

## Error Handling

**Strategy:** [How errors are caught and translated]

- API errors → Application error types
- Network errors → Retry or offline handling
- Validation errors → Field-level feedback

## Caching Strategy

[How API responses are cached, if at all]

- Client-side caching: [Yes/No, how?]
- Invalidation: [When caches are cleared]
"""


def tpl_testing_strategy():
    return f"""# 05_testing_strategy.md

> Testing approach, coverage expectations, and test organization.
> Status: Active
> Authority: Tier 2: Core Knowledge
> Last Updated: {TODAY}

## Testing Philosophy

[Describe your testing approach: pyramid, grid, approach, etc.]

## Test Types and Expectations

### Unit Tests

**Scope:** Pure functions, utilities, domain logic, services.

**Tools:** Vitest

**Coverage Expectations:** >80% for business logic

**Example:**

```typescript
describe("calculateTotal", () => {{
  it("should sum item prices", () => {{
    expect(calculateTotal([{{price: 10}}, {{price: 20}}])).toBe(30);
  }});
}});
```

### Component Tests

**Scope:** Component UI behavior, user interactions, props.

**Tools:** Vitest + React Testing Library

**Coverage Expectations:** >70% for feature components

**Rules:**
- Test user-observable behavior, not implementation
- Use `screen.getByRole()` and similar queries
- Avoid testing internal state directly

### Integration Tests

**Scope:** Multiple components together, API flows, forms, workflows.

**Tools:** Vitest + React Testing Library or Playwright

**Coverage Expectations:** Critical user journeys

### E2E Tests

**Scope:** Full user workflows from browser perspective.

**Tools:** Playwright or Cypress

**Coverage Expectations:** Critical paths only

## Test Organization

**File Structure:**

```
src/
├── components/
│   ├── Button.tsx
│   └── Button.test.tsx
├── hooks/
│   ├── useAuth.ts
│   └── useAuth.test.ts
├── services/
│   ├── authService.ts
│   └── authService.test.ts
```

**Naming:** `[filename].test.ts` or `[filename].spec.ts`

## CI/CD Integration

[How tests are run in CI/CD]

- Pre-commit: [Linting]
- On Push: [Test suite]
- On PR: [Full build and tests]
"""


def tpl_accessibility_strategy():
    return f"""# 06_accessibility_strategy.md

> Accessibility approach and WCAG compliance standards.
> Status: Active
> Authority: Tier 2: Core Knowledge
> Last Updated: {TODAY}

## Accessibility Standard

**Target:** WCAG 2.1 Level AA

**Scope:** All user-facing features

## Core Principles

- **Perceivable:** Users can see/hear content
- **Operable:** Users can navigate and interact
- **Understandable:** Content and interactions are clear
- **Robust:** Works across browsers and assistive tech

## Implementation Guidelines

### Semantic HTML

- Use `<header>`, `<main>`, `<nav>`, `<section>`, `<footer>`
- Use `<button>` for actions, `<a>` for navigation
- Use `<label>` for form inputs
- Use heading hierarchy (`<h1>`, `<h2>`, etc.)

### Keyboard Navigation

- All interactive elements accessible via Tab
- Visible focus indicators
- No keyboard traps (except intentional modals)
- Proper focus management on page changes

### Color and Contrast

- Minimum 4.5:1 contrast for text
- 3:1 contrast for UI components
- Don't rely on color alone to convey information

### Motion and Animation

- Respect `prefers-reduced-motion` CSS media query
- Avoid auto-playing videos
- Avoid flashing content

### ARIA

- Use ARIA only when semantic HTML is insufficient
- Follow ARIA patterns for complex widgets
- Test with screen readers

### Forms

- Associated labels for all inputs
- Clear error messages
- Input types match content (email, tel, etc.)

## Testing Approach

- **Automated:** axe-core, WAVE browser plugin
- **Manual:** Keyboard navigation testing
- **Screen Reader:** Testing with NVDA or JAWS

## Accessibility Checklist

Before shipping features:

- [ ] Semantic HTML
- [ ] Keyboard navigation works
- [ ] Focus indicators visible
- [ ] Color contrast sufficient
- [ ] Forms labeled correctly
- [ ] Error messages clear
- [ ] ARIA used correctly if needed
- [ ] Tested with screen reader
"""


def tpl_security_model():
    return f"""# 07_security_model.md

> Security considerations, threat model, and mitigation strategies.
> Status: Active
> Authority: Tier 2: Core Knowledge
> Last Updated: {TODAY}

## Threat Model

### XSS (Cross-Site Scripting)

**Risk:** Untrusted data rendered as HTML

**Mitigations:**
- React auto-escapes text content
- Avoid `dangerouslySetInnerHTML`
- Sanitize HTML when necessary: use `DOMPurify` or similar

### CSRF (Cross-Site Request Forgery)

**Risk:** Attacker tricks user into modifying data

**Mitigations:**
- Backend validates request origin
- Use CSRF tokens for state-changing requests
- Use SameSite cookie attribute

### Injection

**Risk:** Malicious input into queries, commands

**Mitigations:**
- Validate all user input
- Use parameterized queries (backend)
- Avoid string concatenation in queries

### Insecure Token Storage

**Risk:** Session tokens exposed to XSS

**Mitigations:**
- Use HttpOnly, Secure, SameSite cookies (backend)
- Never store tokens in localStorage
- Use sessionStorage only if necessary

## Security Rules

### Never

- Hardcode secrets in code
- Log passwords or tokens
- Expose secrets in client-side env vars (`VITE_*`)
- Trust client-side validation as security boundary
- Store long-lived tokens in localStorage

### Always

- Validate input at system boundaries
- Authenticate users
- Authorize actions based on user roles
- Use HTTPS in production
- Keep dependencies updated
- Follow principle of least privilege

## Content Security Policy

[If CSP is configured, describe the policy]

```
default-src 'self';
script-src 'self';
style-src 'self' 'unsafe-inline';
img-src 'self' https:;
```

## Dependency Management

- Regularly update dependencies: `npm audit`
- Review security advisories
- Avoid dependencies with known vulnerabilities
"""


def tpl_deployment_model():
    return f"""# 08_deployment_model.md

> Deployment architecture, environments, and operational guidelines.
> Status: Active
> Authority: Tier 2: Core Knowledge
> Last Updated: {TODAY}

## Deployment Architecture

```mermaid
graph TB
    Dev["Dev Env<br/>Local Machine"]
    Staging["Staging<br/>Staging Server"]
    Prod["Production<br/>CDN + Server"]

    Dev -->|git push| Staging
    Staging -->|manual/auto| Prod
```

## Environments

### Development

**Purpose:** Local development

**Setup:**

```bash
npm install
npm run dev
```

### Staging

**Purpose:** Pre-production testing

**Deploy:** Manual or automatic on PR merge

**URL:** [staging URL]

### Production

**Purpose:** User-facing application

**Deploy:** Requires approval

**URL:** [production URL]

## Build Process

```bash
npm run build    # Builds for production
npm run preview  # Preview production build locally
```

**Outputs:**
- `/dist/` — Static assets ready for deployment

## Hosting

**Platform:** [Vercel / Netlify / Custom server]

**Configuration:**
- [Environment variables]
- [Build command]
- [Output directory]

## Environment Variables

### Development (.env.local)

```
VITE_API_BASE_URL=http://localhost:3000/api
```

### Production

```
VITE_API_BASE_URL=https://api.example.com
```

**Rule:** Never commit `.env` files. Secrets must be managed by hosting platform.

## Monitoring and Logging

- **Error Tracking:** [Service if configured]
- **Analytics:** [Service if configured]
- **Logs:** [How to access logs]

## Rollback Strategy

[How to rollback a failed deployment]

## Performance Targets

- Page load: <3s
- Interactive: <5s
- Layout shift: <0.1
"""


def tpl_project_context():
    return f"""# 00_project_context.md — Contexto do Projeto

> Tier 2 — Conhecimento central.
> Atualizado: {TODAY}

## Objetivo do projeto

[Descrever o objetivo principal]

## Problema que resolve

[Descrever o problema de negocio ou tecnico]

## Escopo

### Incluso
- [Item 1]

### Excluido (fora do escopo)
- [Item 1]

## Stakeholders

| Nome | Papel | Contato |
|------|-------|---------|
| [Nome] | [Papel] | [Email/Slack] |

## Dependencias externas

- [Servico ou sistema externo 1]
- [Servico ou sistema externo 2]

## Riscos conhecidos

| Risco | Probabilidade | Impacto | Mitigacao |
|-------|--------------|---------|-----------|
| [Risco 1] | Alto/Medio/Baixo | Alto/Medio/Baixo | [Como mitigar] |
"""


def tpl_agent(role, slash_command, knowledge_files):
    return f"""# Agent: {role}

> Web software engineering specialist.
> Based on AGENTS_WEB_UML.md

## Role

[One-line description of what this agent does and why it exists.]

**Example:** "Full-stack Web developer who implements features following architectural boundaries, writes tests, and maintains code quality."

## Session Initialization (MANDATORY)

Before answering any project-specific question, execute this sequence:

1. Read `START_HERE.md`
2. Read `/AGENTS.md`
3. Read `/docs/knowledge/KNOWLEDGE_BASE.md`
4. Read `/docs/design.md`
5. Read `/docs/plan.md` and `/docs/tasks.md`
6. Read relevant files from `/docs/knowledge/source-of-truth/`
7. Inspect `package.json`, `vite.config.*`, `tsconfig*.json` if present

## Core Capabilities

- [Capability 1 with specific instructions]
- [Capability 2 with specific instructions]
- [Capability 3 with specific instructions]

**Example capabilities for a developer agent:**

- Write TypeScript, React, and HTML/CSS code following SOLID principles
- Create unit, component, and integration tests using Vitest and React Testing Library
- Design UML diagrams (Use Case, Component, Sequence, State Machine)
- Refactor code to improve maintainability and reduce coupling
- Propose architectural improvements and design changes

## Required Knowledge Sources

{chr(10).join(f'- `/docs/knowledge/{f}`' for f in knowledge_files)}

## Authority Hierarchy

Apply this hierarchy when making decisions:

| Tier | Example Documents                                  | Authority  |
|------|---------------------------------------------------|------------|
| 1    | Source of Truth, ADRs, approved requirements      | Absolute   |
| 2    | Core domain, architecture, component models       | High       |
| 3    | Implementation notes, meeting notes               | Helpful    |
| 4    | Archived documents                                | Historical |

**Rule:** Tier 1 always wins. Never contradict Source of Truth documents.

## Evidence and Confidence Rules

Always cite repository evidence:

- Format: `path/to/file.md:L10-L18` or `/src/Component.tsx:L42`
- Mark confidence: `HIGH` (Tier 1 or code), `MEDIUM` (Tier 2), `LOW` (inferred)
- Say "I do not know based on repository context" when evidence is missing
- Never invent APIs, routes, components, or configuration values

## Tools Available

[List relevant tools this agent can use]

- Read/Edit/Write files
- Run scripts and tests
- Create/Update UML diagrams
- Propose architectural changes
- Review code and suggest refactorings

## UML Responsibility

**UML is not optional.** Create or update UML when:

- Designing new features or modules
- Creating domain models
- Designing component architecture
- Describing data flows or sequences
- Defining state machines
- Planning API integrations
- Major refactoring

Skip UML only for: typos, simple CSS changes, isolated bug fixes. State briefly why it's unnecessary.

## Activation

```
{slash_command}
```

## Output Format

When responding:

1. **Understanding:** Summarize the request and repository context
2. **Questions:** Ask clarifying questions if needed (focused, not verbose)
3. **Plan:** State the approach briefly
4. **UML Impact:** Mention if design, UML, or documentation will be affected
5. **Implementation:** Provide code, tests, or recommendations
6. **Documentation:** List files that need updating
7. **Verification:** Provide commands to verify correctness

## Quality Checklist

Before finalizing responses, verify:

- [ ] Code is TypeScript/JavaScript following project style
- [ ] Code has no obvious errors, imports are complete
- [ ] Tests are included for meaningful changes
- [ ] UML is provided or explicitly deemed unnecessary
- [ ] Documentation updates proposed or included
- [ ] Accessibility is considered for user-facing changes
- [ ] Security is considered for Web-facing changes
- [ ] Evidence is cited for project-specific claims
- [ ] No secrets are exposed
- [ ] Confidence levels are marked (HIGH/MEDIUM/LOW)
"""


def tpl_slash_command(agent_file, description):
    return f"""---
description: {description}
---

# {description}

Load and execute the agent defined in `{agent_file}`.

Follow the mandatory session initialization protocol in that file before responding.
"""


def tpl_progress_tracker(project_name):
    return f"""# PROGRESS_TRACKER.md

> Progress tracking for {project_name}.
> Auto-generated. Update after each session.
> Last Updated: {TODAY}

## Current Sprint

- **Sprint:** [Sprint number and focus]
- **Status:** [Setup / In Development / In Review / Maintenance]
- **Target End Date:** [Date]

## Completed

- [x] [Completed item 1]
- [x] [Project initialized]

## In Progress

- [ ] [Item being worked on 1 — owner]
- [ ] [Item being worked on 2 — owner]

## Next

- [ ] [Next priority 1]
- [ ] [Next priority 2]
- [ ] [Next priority 3]

## Blocked

| Item                    | Reason                | Owner  | ETA      |
|-------------------------|----------------------|--------|----------|
| [Blocked item 1]        | [Blocking reason]     | [Name] | [Date]   |

## Sessions Log

| Date       | Summary                      | Next Steps                  |
|------------|------------------------------|-----------------------------|
| {TODAY}    | Project structure initialized | Fill in project context     |
| [Date]     | [What was done]              | [Next action]               |

## Metrics

- **Code Coverage:** [Target: >70%]
- **Accessibility Score:** [Target: 90+]
- **Bundle Size:** [Target: <200KB gzipped]
- **Lighthouse Score:** [Target: 90+ all metrics]
"""


# ---------------------------------------------------------------------------
# Criacao da estrutura
# ---------------------------------------------------------------------------

DIRS = [
    "docs/knowledge/source-of-truth/ADR",
    "docs/knowledge/core",
    "docs/knowledge/implementation",
    "docs/knowledge/meetings",
    "docs/knowledge/team",
    "docs/knowledge/archive",
    "docs/adr",
    "docs/uml/mermaid",
    "docs/uml/plantuml",
    "docs/generated",
    "prompts/templates/ai-agents",
    ".claude/commands",
    ".claude/skills",
    "src",
    "public",
]

AGENTS = [
    {
        "name": "web_developer_agent",
        "role": "Web Developer Agent",
        "command": "/dev",
        "description": "Implements features, writes tests, and refactors code following architectural patterns",
        "knowledge": [
            "knowledge/core/00_project_context.md",
            "knowledge/core/01_domain_model.md",
            "knowledge/core/02_frontend_architecture.md",
            "knowledge/core/03_component_model.md",
            "knowledge/core/04_api_integration.md",
            "knowledge/core/05_testing_strategy.md",
            "knowledge/source-of-truth/ARCHITECTURE.md",
        ],
    },
    {
        "name": "frontend_architecture_agent",
        "role": "Frontend Architecture Agent",
        "command": "/arch",
        "description": "Designs component and route architecture, proposes architectural improvements",
        "knowledge": [
            "knowledge/core/00_project_context.md",
            "knowledge/core/01_domain_model.md",
            "knowledge/core/02_frontend_architecture.md",
            "knowledge/core/03_component_model.md",
            "knowledge/source-of-truth/ADR/",
            "design.md",
        ],
    },
    {
        "name": "react_specialist_agent",
        "role": "React Specialist Agent",
        "command": "/react",
        "description": "Solves React-specific challenges: hooks, state, performance, patterns",
        "knowledge": [
            "knowledge/core/02_frontend_architecture.md",
            "knowledge/core/03_component_model.md",
            "knowledge/core/05_testing_strategy.md",
            "design.md",
        ],
    },
    {
        "name": "code_review_agent",
        "role": "Code Review Agent",
        "command": "/review",
        "description": "Reviews code for quality, security, accessibility, and architectural compliance",
        "knowledge": [
            "knowledge/source-of-truth/ARCHITECTURE.md",
            "knowledge/core/02_frontend_architecture.md",
            "knowledge/core/03_component_model.md",
            "knowledge/core/06_accessibility_strategy.md",
            "knowledge/core/07_security_model.md",
        ],
    },
    {
        "name": "security_review_agent",
        "role": "Security Review Agent",
        "command": "/security",
        "description": "Analyzes security vulnerabilities, threat models, and compliance",
        "knowledge": [
            "knowledge/core/07_security_model.md",
            "knowledge/source-of-truth/ARCHITECTURE.md",
        ],
    },
    {
        "name": "uml_modeling_agent",
        "role": "UML Modeling Agent",
        "command": "/uml",
        "description": "Creates and maintains UML diagrams for design documentation",
        "knowledge": [
            "knowledge/core/01_domain_model.md",
            "knowledge/core/02_frontend_architecture.md",
            "knowledge/core/03_component_model.md",
            "design.md",
            "adr/",
        ],
    },
    {
        "name": "testing_agent",
        "role": "Testing Agent",
        "command": "/test",
        "description": "Designs testing strategies and writes tests for all levels",
        "knowledge": [
            "knowledge/core/05_testing_strategy.md",
            "knowledge/core/03_component_model.md",
            "knowledge/core/04_api_integration.md",
        ],
    },
]


def create_structure(base: Path, project_name: str, description: str, team: str):
    print(f"\nGenerating project structure in: {base}\n")

    # Create directories
    for d in DIRS:
        target = base / d
        target.mkdir(parents=True, exist_ok=True)
        print(f"  [DIR]  {d}/")

    # Root files
    root_files = {
        "START_HERE.md": tpl_start_here(project_name, description, team),
        "AGENTS.md": tpl_agents_md(project_name),
    }
    for fname, content in root_files.items():
        path = base / fname
        path.write_text(content, encoding="utf-8")
        print(f"  [FILE] {fname}")

    # Docs: main working files
    docs_files = {
        "docs/plan.md": tpl_plan_md(),
        "docs/tasks.md": tpl_tasks_md(),
        "docs/design.md": tpl_design(),
        "docs/memory.md": tpl_memory_md(),
    }
    for fname, content in docs_files.items():
        path = base / fname
        path.write_text(content, encoding="utf-8")
        print(f"  [FILE] {fname}")

    # Knowledge base structure
    knowledge_files = {
        "docs/knowledge/KNOWLEDGE_BASE.md": tpl_knowledge_base(project_name),
        "docs/knowledge/KNOWLEDGE_GRAPH.md": "# Knowledge Graph\n\n[Relationship-focused documentation]\n",
        "docs/knowledge/core/00_project_context.md": tpl_project_context(),
        "docs/knowledge/core/01_domain_model.md": tpl_domain_model(),
        "docs/knowledge/core/02_frontend_architecture.md": tpl_frontend_architecture(),
        "docs/knowledge/core/03_component_model.md": tpl_component_model(),
        "docs/knowledge/core/04_api_integration.md": tpl_api_integration(),
        "docs/knowledge/core/05_testing_strategy.md": tpl_testing_strategy(),
        "docs/knowledge/core/06_accessibility_strategy.md": tpl_accessibility_strategy(),
        "docs/knowledge/core/07_security_model.md": tpl_security_model(),
        "docs/knowledge/core/08_deployment_model.md": tpl_deployment_model(),
        "docs/knowledge/source-of-truth/ARCHITECTURE.md": tpl_architecture(),
        "docs/knowledge/source-of-truth/ADR/ADR-001-example.md": tpl_adr(),
    }
    for fname, content in knowledge_files.items():
        path = base / fname
        path.write_text(content, encoding="utf-8")
        print(f"  [FILE] {fname}")

    # Progress tracker
    progress_path = base / "docs/generated/PROGRESS_TRACKER.md"
    progress_path.write_text(tpl_progress_tracker(project_name), encoding="utf-8")
    print(f"  [FILE] docs/generated/PROGRESS_TRACKER.md")

    # Initialize meeting placeholder
    meeting_placeholder = base / f"docs/knowledge/meetings/{TODAY}_kickoff.md"
    meeting_placeholder.write_text(
        f"""# Kickoff Meeting — {TODAY}

> Project: {project_name}

## Participants

[List attendees]

## Discussion

[Key topics discussed]

## Decisions

- [Decision 1]
- [Decision 2]

## Action Items

- [ ] [Action 1 — owner]
- [ ] [Action 2 — owner]

## Next Steps

[What's next?]
""",
        encoding="utf-8",
    )
    print(f"  [FILE] docs/knowledge/meetings/{TODAY}_kickoff.md")

    # AI Agents
    for agent in AGENTS:
        # Agent prompt
        agent_path = base / f"prompts/templates/ai-agents/{agent['name']}.md"
        agent_path.write_text(
            tpl_agent(agent["role"], agent["command"], agent["knowledge"]),
            encoding="utf-8",
        )
        print(f"  [FILE] prompts/templates/ai-agents/{agent['name']}.md")

        # Slash command wrapper
        cmd_path = base / f".claude/commands/{agent['name'].replace('_agent', '')}.md"
        cmd_path.write_text(
            tpl_slash_command(
                f"prompts/templates/ai-agents/{agent['name']}.md",
                agent["description"],
            ),
            encoding="utf-8",
        )
        print(f"  [FILE] .claude/commands/{agent['name'].replace('_agent', '')}.md")

    # .gitignore template
    gitignore_path = base / ".gitignore"
    gitignore_content = """# Dependencies
node_modules/
npm-debug.log*
yarn-error.log*

# Environment
.env.local
.env.*.local

# Build outputs
dist/
build/
*.tsbuildinfo

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Logs
logs/
*.log

# Test coverage
coverage/
.nyc_output/

# Secrets (never commit)
secrets/
credentials.json
.env
"""
    gitignore_path.write_text(gitignore_content, encoding="utf-8")
    print(f"  [FILE] .gitignore")

    # package.json template
    package_json = base / "package.json"
    package_json_content = """{
  "name": \"""" + project_name.lower().replace(" ", "-") + """\",
  "version": "0.1.0",
  "description": \"""" + description + """\",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "lint": "eslint . --ext .ts,.tsx",
    "typecheck": "tsc --noEmit",
    "test": "vitest",
    "test:ui": "vitest --ui"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "@vitejs/plugin-react": "^4.0.0",
    "typescript": "^5.0.0",
    "vite": "^5.0.0",
    "vitest": "^1.0.0",
    "@testing-library/react": "^14.0.0",
    "@testing-library/jest-dom": "^6.1.0"
  }
}
"""
    package_json.write_text(package_json_content, encoding="utf-8")
    print(f"  [FILE] package.json")

    # tsconfig.json template
    tsconfig_path = base / "tsconfig.json"
    tsconfig_content = """{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "jsx": "react-jsx",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true
  },
  "include": ["src"],
  "exclude": ["node_modules"]
}
"""
    tsconfig_path.write_text(tsconfig_content, encoding="utf-8")
    print(f"  [FILE] tsconfig.json")

    # Add PlantUML diagrams
    plantuml_diagrams = get_all_plantuml_diagrams()
    for key, diagram in plantuml_diagrams.items():
        puml_path = base / f"docs/uml/plantuml/{diagram['name']}"
        puml_path.write_text(diagram['content'], encoding="utf-8")
        print(f"  [FILE] docs/uml/plantuml/{diagram['name']}")

    print(f"\n[OK] Project structure generated successfully in: {base}")
    print("\n[NEXT] Next Steps:")
    print("  1. Review START_HERE.md and fill in project-specific information")
    print("  2. Update /docs/knowledge/core/00_project_context.md with project goals")
    print("  3. Update /docs/design.md with your architecture and UML diagrams")
    print("  4. Fill in /docs/knowledge/source-of-truth/ADR/ with your decisions")
    print("  5. PlantUML diagrams are in /docs/uml/plantuml/ - customize as needed")
    print("  6. Adjust agents in prompts/templates/ai-agents/ if needed")
    print("  7. Create src/ and public/ directories for your application")
    print("  8. Run: npm install")
    print("  9. Commit to Git\n")


# ---------------------------------------------------------------------------
# Entrada interativa
# ---------------------------------------------------------------------------

def prompt(msg, default=None):
    suffix = f" [{default}]" if default else ""
    value = input(f"{msg}{suffix}: ").strip()
    return value if value else default


def main():
    print("\n" + "=" * 70)
    print("  Web Project Generator with AI Agent Structure")
    print("  Based on AGENTS_WEB_UML.md")
    print("=" * 70 + "\n")

    project_name = prompt("Project name")
    if not project_name:
        print("[ERROR] Project name is required.")
        sys.exit(1)

    description = prompt(
        "Project description (one sentence)",
        default="[What problem does this project solve?]",
    )

    team = prompt(
        "Team members (ex: John - Frontend, Jane - Backend)",
        default="[List team members and roles]",
    )

    default_dir = Path.cwd() / project_name.replace(" ", "_").lower()
    output_dir = prompt("Output directory", default=str(default_dir))
    base = Path(output_dir)

    if base.exists() and any(base.iterdir()):
        confirm = prompt(
            f"\nDirectory '{base}' already exists and is not empty. Continue? (y/n)",
            default="n",
        )
        if confirm.lower() not in ["y", "yes"]:
            print("[CANCELLED] Operation cancelled.")
            sys.exit(0)

    base.mkdir(parents=True, exist_ok=True)
    create_structure(base, project_name, description, team)


if __name__ == "__main__":
    main()
