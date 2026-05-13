# Web Project Generator

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-green.svg)](https://github.com)
[![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](./.github/workflows/ci.yml)
[![Tests: 28](https://img.shields.io/badge/Tests-28%20passing-2ea44f)](./tests/)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](./pyproject.toml)
[![Type Check: mypy](https://img.shields.io/badge/type%20check-mypy-blue.svg)](./pyproject.toml)
[![Architecture: Modular](https://img.shields.io/badge/Architecture-Modular-blue.svg)](./README.md)
[![React 18+](https://img.shields.io/badge/React-18%2B-61DAFB?logo=react&logoColor=white)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5%2B-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-5%2B-646CFF?logo=vite&logoColor=white)](https://vitejs.dev/)
[![AI Agents: 7](https://img.shields.io/badge/AI%20Agents-7-purple.svg)](#ai-agents)
[![UML: Mermaid](https://img.shields.io/badge/UML-Mermaid-green.svg)](https://mermaid.js.org/)
[![UML: PlantUML](https://img.shields.io/badge/UML-PlantUML-blue.svg)](https://plantuml.com/)
[![Diagrams: 13](https://img.shields.io/badge/Diagrams-13-orange.svg)](#plantuml-diagrams)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red.svg)](#author)

> A comprehensive project structure generator for modern Web applications with AI agent integration, modular architecture, automated testing, and CI/CD.

**Author:** Jafte Carneiro Fagundes da Silva
**Version:** 1.0.0
**License:** MIT
**Last Updated:** 2026-05-13

---

## What's New in 1.0.0

| Improvement | Description |
|-------------|-------------|
| **Modular Architecture** | `create_project.py` split into `templates.py` (templates) + `create_project.py` (orchestrator) |
| **28 Automated Tests** | Full test coverage for all templates and PlantUML diagrams |
| **CI/CD Pipeline** | GitHub Actions workflow testing Python 3.8 through 3.12 |
| **Type Hints** | All functions annotated (mypy-compatible) |
| **Auto-Registration** | PlantUML diagrams register via `@register_diagram` decorator — add a diagram, it's automatically included |
| **Clean `.gitignore`** | Removed all duplicate entries, consolidated sections |
| **IO Abstraction** | `_write_file()` / `_write_dir()` / `_write_files()` eliminate repetitive code |
| **`pyproject.toml`** | Project metadata, pytest/ruff/mypy configuration |
| **`KNOWLEDGE_GRAPH.md`** | Replaced one-line placeholder with complete dependency table |
| **Bug Fix** | `tpl_project_context()` had a duplicate definition (PT-BR overwriting EN-US) — resolved |
| **Documentation Accuracy** | STRUCTURE.md line counts corrected from "3000+" to actual 881 |

---

## Overview

The Web Project Generator is an automated tool that generates production-ready Web application project structures with:

- **Modular Python Codebase**: Template functions separated from orchestration logic (`templates.py` + `create_project.py`)
- **Documentation System**: Organized knowledge base with 4-tier authority hierarchy
- **AI Agents**: 7 specialized agents for different roles
- **Modern Tech Stack**: React + TypeScript + Vite + Vitest
- **Dual UML Support**: Mermaid + 13 PlantUML professional diagrams
- **Best Practices**: SOLID principles, accessibility, security, testing strategies
- **Automated Testing**: 28 tests covering all templates and diagrams
- **CI/CD Ready**: GitHub Actions pipeline for continuous integration

## Quick Start

### Prerequisites

- Python 3.8+
- (Optional) Node.js 18+ for generated projects

### Installation

```bash
# Clone or download the repository
cd dev_tools

# (Optional) Run tests to verify everything works
pip install pytest
python -m pytest tests/ -v

# Run the generator
python create_project.py
```

### Basic Usage

```bash
$ python create_project.py

======================================================================
  Web Project Generator with AI Agent Structure
  Production-Ready Architecture
======================================================================

Project name: my-awesome-app
Project description (one sentence) [What problem does this project solve?]: Build a real-time collaboration tool for remote teams
Team members (ex: John - Frontend, Jane - Backend) [List team members and roles]: Alice - Frontend Lead, Bob - Backend, Carol - DevOps
Output directory [my_awesome_app]: ./my-awesome-app

[OK] Project structure generated successfully in: ./my-awesome-app

[NEXT] Next Steps:
  1. Review START_HERE.md and fill in project-specific information
  2. Update /docs/knowledge/core/00_project_context.md with project goals
  3. Update /docs/design.md with your architecture and UML diagrams
  4. Fill in /docs/knowledge/source-of-truth/ADR/ with your decisions
  5. PlantUML diagrams are in /docs/uml/plantuml/ - customize as needed
  6. Adjust agents in prompts/templates/ai-agents/ if needed
  7. Create src/ and public/ directories for your application
  8. Run: npm install
  9. Commit to Git
```

## Testing

The project includes **28 automated tests** covering all templates and diagrams:

```bash
pip install pytest
python -m pytest tests/ -v
```

### Test Structure

```
tests/
├── __init__.py
├── test_templates.py      # 21 tests — verifies all tpl_*() functions
└── test_plantuml.py       # 7 tests — verifies all PlantUML diagrams
```

**What's tested:**
- ✅ All 21 template functions return valid markdown with expected content
- ✅ All 13 PlantUML diagrams have valid `@startuml`/`@enduml` syntax
- ✅ Every diagram has required keys (name, description, type, content)
- ✅ Diagram types are valid (use-case, class, sequence, component, state, deployment, erd)
- ✅ All 13 specific diagram files are present and registered

## CI/CD

Every push and pull request runs the test suite across **Python 3.8 through 3.12**:

```yaml
# .github/workflows/ci.yml
- Runs pytest on all 28 tests
- Verifies Python syntax on all modules
- Matrix strategy: 5 Python versions
```

## Codebase Architecture

### Before v1.0.0 (Monolithic)

```
create_project.py   # 2695 lines — templates + logic + CLI mixed
plantuml_diagrams.py # 947 lines — manual diagram registration
```

### After v1.0.0 (Modular)

```
create_project.py   # ~250 lines — orchestration, CLI, AGENTS/DIRS config
templates.py        # ~2400 lines — all tpl_*() template functions
plantuml_diagrams.py # ~950 lines — auto-registration via decorator
pyproject.toml      # Project metadata, tool configs
tests/              # 28 automated tests
.github/workflows/  # CI/CD pipeline
```

### PlantUML Auto-Registration

Adding a new diagram is now **one decorator away**:

```python
@register_diagram("my_new_type", "my_diagram.puml", "Description", "class")
def puml_my_diagram():
    return "@startuml ... @enduml"
```

No manual mapping in `get_all_plantuml_diagrams()` needed — it's automatic.

---

## Generated Project Structure

### Overview

```
my-awesome-app/
├── START_HERE.md                              # Entry point for humans and AI agents
├── AGENTS.md                                  # AI agent rules and guidelines
├── package.json                               # Node.js dependencies
├── tsconfig.json                              # TypeScript configuration
├── .gitignore                                 # Git ignore rules
│
├── docs/                                      # Complete documentation system
│   ├── plan.md                                # Current implementation plan
│   ├── tasks.md                               # Work items and progress
│   ├── design.md                              # System architecture and UML
│   ├── memory.md                              # Durable decisions and preferences
│   │
│   ├── knowledge/
│   │   ├── KNOWLEDGE_BASE.md                  # Documentation index (tier guide)
│   │   ├── KNOWLEDGE_GRAPH.md                 # Relationship map and dependencies
│   │   │
│   │   ├── source-of-truth/                   # Tier 1: Authoritative
│   │   │   ├── ARCHITECTURE.md                # System architecture (read-only)
│   │   │   └── ADR/
│   │   │       └── ADR-001-example.md         # Architecture Decision Records
│   │   │
│   │   ├── core/                              # Tier 2: Core Knowledge (numbered)
│   │   │   ├── 00_project_context.md          # Project goals and scope
│   │   │   ├── 01_domain_model.md             # Domain concepts and rules
│   │   │   ├── 02_frontend_architecture.md    # Frontend layering
│   │   │   ├── 03_component_model.md          # Component patterns
│   │   │   ├── 04_api_integration.md          # API contracts
│   │   │   ├── 05_testing_strategy.md         # Testing approach
│   │   │   ├── 06_accessibility_strategy.md   # A11y standards
│   │   │   ├── 07_security_model.md           # Security model
│   │   │   └── 08_deployment_model.md         # Deployment architecture
│   │   │
│   │   ├── implementation/                    # Tier 3: Working documents
│   │   ├── meetings/                          # Meeting notes (date-prefixed)
│   │   ├── team/                              # Team information
│   │   └── archive/                           # Tier 4: Historical
│   │
│   ├── adr/                                   # Architecture Decision Records
│   ├── uml/                                   # UML diagrams
│   │   ├── mermaid/                           # Lightweight diagrams
│   │   └── plantuml/                          # 13 Professional diagrams
│   │
│   └── generated/                             # Generated artifacts
│       └── PROGRESS_TRACKER.md                # Sprint progress and metrics
│
├── prompts/
│   └── templates/
│       └── ai-agents/                         # AI agent prompts (source of truth)
│           ├── web_developer_agent.md
│           ├── frontend_architecture_agent.md
│           ├── react_specialist_agent.md
│           ├── code_review_agent.md
│           ├── security_review_agent.md
│           ├── uml_modeling_agent.md
│           └── testing_agent.md
│
├── .claude/
│   ├── commands/                              # Slash command wrappers
│   │   ├── web_developer.md                   # /dev command
│   │   ├── frontend_architecture.md           # /arch command
│   │   ├── react_specialist.md                # /react command
│   │   ├── code_review.md                     # /review command
│   │   ├── security_review.md                 # /security command
│   │   ├── uml_modeling.md                    # /uml command
│   │   └── testing.md                         # /test command
│   └── skills/
│
├── src/                                       # Your application source code
└── public/                                    # Static assets
```

## Key Concepts

### 1. **Documentation Hierarchy (Tiers)**

The project uses a **4-tier authority system** to organize documentation:

#### Tier 1: Source of Truth
- **Location**: `/docs/knowledge/source-of-truth/`
- **Authority**: Absolute and binding
- **Updates**: Require explicit user approval

#### Tier 2: Core Knowledge
- **Location**: `/docs/knowledge/core/` (numbered files)
- **Authority**: High; foundational context
- **Updates**: Keep aligned with current architecture

#### Tier 3: Implementation & Working Documents
- **Location**: `/docs/`, `/docs/knowledge/implementation/`, `/docs/knowledge/meetings/`
- **Authority**: Helpful but evolving
- **Updates**: Change frequently

#### Tier 4: Archive
- **Location**: `/docs/knowledge/archive/`
- **Authority**: Historical reference only

### 2. **AI Agents**

The project includes 7 specialized AI agents, activated via slash commands:

| Agent                          | Command      | Responsibility                                    |
|--------------------------------|--------------|---------------------------------------------------|
| Web Developer Agent            | `/dev`       | Implement features, write tests, refactor code   |
| Frontend Architecture Agent    | `/arch`      | Design routes, components, propose improvements  |
| React Specialist Agent         | `/react`     | Solve React hooks, state, performance problems   |
| Code Review Agent              | `/review`    | Quality, security, accessibility review          |
| Security Review Agent          | `/security`  | Threat modeling, vulnerability assessment        |
| UML Modeling Agent             | `/uml`       | Create and maintain system diagrams              |
| Testing Agent                  | `/test`      | Design tests, coverage strategies                |

### 3. **Project Files**

| File | Purpose |
|------|---------|
| **create_project.py** | Main generator — orchestrator (~250 lines) |
| **templates.py** | All markdown template functions (~2400 lines) |
| **plantuml_diagrams.py** | PlantUML templates with auto-registration (13 diagrams) |
| **pyproject.toml** | Project metadata, pytest/ruff/mypy configuration |
| **tests/** | 28 automated tests (templates + diagrams) |
| **.github/workflows/ci.yml** | CI/CD pipeline (Python 3.8–3.12) |
| **README.md** | This comprehensive guide |
| **PLANTUML_GUIDE.md** | PlantUML installation & usage |
| **AUTHOR.md** | Author info & contributions |
| **BADGES.md** | Badge documentation |
| **STRUCTURE.md** | Project structure reference |
| **LICENSE** | MIT License |

### 4. **Core Working Files**

#### `/docs/plan.md`
- **Purpose**: Current implementation plan
- **Sections**: Objective, Scope, Architecture Impact, Testing Strategy, Acceptance Criteria

#### `/docs/tasks.md`
- **Purpose**: Actionable work items
- **Sections**: Backlog, In Progress, Blocked, Completed, Verification Checklist

#### `/docs/design.md`
- **Purpose**: System architecture and design decisions
- **Sections**: System Overview, Domain Model, Frontend Architecture, UML Diagrams, Design Decisions

#### `/docs/memory.md`
- **Purpose**: Durable decisions and user preferences
- **Sections**: User Preferences, Approved Decisions, Rejected Decisions, Repository Conventions

### 5. **UML-First Design**

UML is **mandatory** for non-trivial changes:

- **Use Case Diagrams**: Show actors, goals, and system boundaries
- **Class Diagrams**: Domain models and TypeScript interfaces
- **Sequence Diagrams**: Runtime interactions (components, services, APIs)
- **State Machine Diagrams**: Component states, form states, auth flows
- **Component Diagrams**: React components, pages, services, integrations
- **Deployment Diagrams**: Browser, CDN, servers, databases

Choose your preferred format:
- **Mermaid** — Lightweight, built into Markdown
- **PlantUML** — Professional, 13 diagram types, auto-registered

## Usage Workflow

### 1. **Initialize Project**

```bash
python create_project.py
# Answer prompts about your project
```

### 2. **Review and Customize**

Open `START_HERE.md`:
- Update project summary and team
- Fill in technology stack
- Add credentials policy and first files to read

### 3. **Define Project Context**

Edit `/docs/knowledge/core/00_project_context.md`:
- Project goals and success criteria
- Target users and problem statement
- Scope (in/out), constraints, stakeholders
- Key assumptions and risks

### 4. **Design Domain Model**

Edit `/docs/knowledge/core/01_domain_model.md`:
- Define entities, value objects, aggregates
- Document business rules
- Create class diagrams

### 5. **Plan Architecture**

Edit `/docs/design.md`:
- System overview and layering
- Frontend architecture (pages, features, shared)
- Component and route architecture
- API contracts and data flow
- UML diagrams

### 6. **Create ADRs**

Add decisions to `/docs/knowledge/source-of-truth/ADR/`:
```
ADR-001: React for Frontend
ADR-002: Context API for State Management
ADR-003: Vitest for Unit Testing
```

### 7. **Set Up Implementation Plan**

Fill `/docs/plan.md`:
- Objective, scope, constraints
- Implementation phases
- Testing strategy
- Acceptance criteria

### 8. **Start Development**

```bash
cd my-awesome-app
npm install
npm run dev
```

### 9. **Use AI Agents**

Activate agents via slash commands:

```
/dev - "Implement the login form with validation"
/arch - "Review component architecture and suggest improvements"
/test - "Write comprehensive tests for AuthService"
/review - "Review this code for quality and security"
/uml - "Create a sequence diagram for the checkout flow"
```

### 10. **Maintain Documentation**

After meetings or significant decisions:

1. Update `/docs/memory.md` with decisions
2. Create ADR if architectural
3. Update `/docs/design.md` if design changed
4. Update `/docs/tasks.md` with work items
5. Update `/docs/knowledge/KNOWLEDGE_BASE.md` if structure changed

## Architecture Principles

1. **Repository Grounding**: All decisions based on repository evidence
2. **Tier Authority**: Tier 1 always wins; lower tiers must align
3. **Evidence-Based**: Claims cited with file paths and line numbers
4. **UML-First**: Design documented with diagrams before code
5. **Accessibility by Default**: WCAG 2.1 Level AA as baseline
6. **Security by Design**: Threats identified and mitigated upfront
7. **Testability**: Code designed to be tested (unit, component, E2E)
8. **Maintainability**: Clear intent, minimal coupling, SOLID principles
9. **Modularity**: Cohesive modules with clean boundaries
10. **Documentation**: Decisions recorded, architecture explained

## PlantUML Diagrams

### 13 Professional Diagrams

| # | File | Type | Description |
|---|------|------|-------------|
| 1 | `web_usecase_diagram.puml` | Use Case | Web app capabilities |
| 2 | `auth_usecase_diagram.puml` | Use Case | Auth flows |
| 3 | `domain_model.puml` | Class | Domain entities |
| 4 | `services_diagram.puml` | Class | Services & interfaces |
| 5 | `login_sequence.puml` | Sequence | Login flow steps |
| 6 | `checkout_sequence.puml` | Sequence | Checkout process |
| 7 | `frontend_components.puml` | Component | React components |
| 8 | `system_architecture.puml` | Component | System layers |
| 9 | `form_states.puml` | State Machine | Form validation |
| 10 | `order_states.puml` | State Machine | Order lifecycle |
| 11 | `auth_states.puml` | State Machine | Auth session |
| 12 | `deployment_architecture.puml` | Deployment | Infrastructure |
| 13 | `database_erd.puml` | ERD | Database schema |

### Auto-Registration

Diagrams use the `@register_diagram` decorator — adding a new diagram is as simple as:

```python
@register_diagram("my_key", "my_file.puml", "Description", "type")
def puml_my_diagram():
    return "@startuml ... @enduml"
```

Run `python plantuml_diagrams.py` to list all registered diagrams.

See **[PLANTUML_GUIDE.md](./PLANTUML_GUIDE.md)** for installation and usage.

---

## License

This project is licensed under the **MIT License** — see [LICENSE](./LICENSE) for details.

## Author

**Jafte Carneiro Fagundes da Silva**
- Role: Web Software Architect & AI Agent Specialist

## Version History

| Version | Date       | Changes                                          |
|---------|------------|--------------------------------------------------|
| 1.0.0   | 2026-05-13 | Modular architecture, 28 tests, CI/CD, auto-registration, type hints, pyproject.toml, bug fixes |
| 0.1.0   | 2026-05-01 | Beta version with basic project structure        |

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Run tests: `python -m pytest tests/`
4. Commit with clear messages
5. Push to the branch
6. Open a Pull Request

## Acknowledgments

- **AGENTS_WEB_UML.md** — Architecture and AI agent guidelines
- **Modern Web Development Community** — Best practices and standards
- **React, TypeScript, Vite Teams** — Foundational technologies

---

<div align="center">

**Web Project Generator** • Making Web development more efficient with AI-assisted architecture and documentation

[⭐ Star this project](#) | [🐛 Report Issues](#) | [💡 Suggest Features](#)

**Happy building! 🚀**

</div>
