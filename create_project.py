#!/usr/bin/env python3
"""
create_project.py
Generate the base structure of a Web software project with AI agent files.
Based on AGENTS_WEB_UML.md architecture for modern Web development.
Supports React, TypeScript, Vite, and disciplined software engineering practices.
"""

import sys
from pathlib import Path
from typing import Dict, List

from templates import (
    tpl_start_here,
    tpl_agents_md,
    tpl_plan_md,
    tpl_tasks_md,
    tpl_memory_md,
    tpl_knowledge_base,
    tpl_architecture,
    tpl_adr,
    tpl_design,
    tpl_project_context,
    tpl_domain_model,
    tpl_frontend_architecture,
    tpl_component_model,
    tpl_api_integration,
    tpl_testing_strategy,
    tpl_accessibility_strategy,
    tpl_security_model,
    tpl_deployment_model,
    tpl_agent,
    tpl_slash_command,
    tpl_progress_tracker,
)
from plantuml_diagrams import get_all_plantuml_diagrams


# ---------------------------------------------------------------------------
# Project structure definitions
# ---------------------------------------------------------------------------

DIRS: List[str] = [
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

AGENTS: List[Dict[str, object]] = [
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


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _write_file(base: Path, fname: str, content: str) -> None:
    """Write content to a file under base directory and log it."""
    path = base / fname
    path.write_text(content, encoding="utf-8")
    print(f"  [FILE] {fname}")


def _write_dir(base: Path, d: str) -> None:
    """Create a directory under base and log it."""
    target = base / d
    target.mkdir(parents=True, exist_ok=True)
    print(f"  [DIR]  {d}/")


def _write_files(base: Path, files: Dict[str, str]) -> None:
    """Write multiple files using _write_file."""
    for fname, content in files.items():
        _write_file(base, fname, content)


# ---------------------------------------------------------------------------
# Structure generation
# ---------------------------------------------------------------------------

def create_structure(base: Path, project_name: str, description: str, team: str) -> None:
    print(f"\nGenerating project structure in: {base}\n")

    # Create directories
    for d in DIRS:
        _write_dir(base, d)

    # Root files
    _write_files(base, {
        "START_HERE.md": tpl_start_here(project_name, description, team),
        "AGENTS.md": tpl_agents_md(project_name),
    })

    # Docs: main working files
    _write_files(base, {
        "docs/plan.md": tpl_plan_md(),
        "docs/tasks.md": tpl_tasks_md(),
        "docs/design.md": tpl_design(),
        "docs/memory.md": tpl_memory_md(),
    })

    # Knowledge base structure
    _write_files(base, {
        "docs/knowledge/KNOWLEDGE_BASE.md": tpl_knowledge_base(project_name),
        "docs/knowledge/KNOWLEDGE_GRAPH.md": (
            "# Knowledge Graph\n\n"
            "> Document relationships and navigation map.\n\n"
            "## Document Dependencies\n\n"
            "| Document | Depends On | Referenced By |\n"
            "|----------|------------|---------------|\n"
            "| `00_project_context.md` | — | All documents |\n"
            "| `01_domain_model.md` | `00_project_context.md` | `02_frontend_architecture.md`, design.md |\n"
            "| `02_frontend_architecture.md` | `01_domain_model.md` | `03_component_model.md` |\n"
            "| `03_component_model.md` | `02_frontend_architecture.md` | design.md |\n"
            "| `04_api_integration.md` | `00_project_context.md` | design.md |\n"
            "| `05_testing_strategy.md` | `00_project_context.md` | tasks.md |\n"
            "| `06_accessibility_strategy.md` | `02_frontend_architecture.md` | design.md |\n"
            "| `07_security_model.md` | `00_project_context.md` | design.md |\n"
            "| `08_deployment_model.md` | `00_project_context.md` | ARCHITECTURE.md |\n"
            "| `ARCHITECTURE.md` | All core files | design.md |\n\n"
            "## Navigation Flows\n\n"
            "- **Onboarding:** START_HERE.md → AGENTS.md → KNOWLEDGE_BASE.md → 00_project_context.md\n"
            "- **Architecture Review:** 02_frontend_architecture.md → 03_component_model.md → design.md\n"
            "- **Implementation:** plan.md → tasks.md → relevant core files\n"
        ),
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
    })

    # Progress tracker
    _write_file(base, "docs/generated/PROGRESS_TRACKER.md", tpl_progress_tracker(project_name))

    # Initialize meeting placeholder
    today = Path(f"docs/knowledge/meetings/{__import__('datetime').date.today().isoformat()}_kickoff.md")
    _write_file(base, str(today),
        f"""# Kickoff Meeting — {__import__('datetime').date.today().isoformat()}

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
""")

    # AI Agents
    for agent in AGENTS:
        agent_name = agent["name"]
        agent_role = agent["role"]
        agent_cmd = agent["command"]
        agent_desc = agent["description"]
        agent_knowledge = agent["knowledge"]

        # Agent prompt
        _write_file(
            base,
            f"prompts/templates/ai-agents/{agent_name}.md",
            tpl_agent(agent_role, agent_cmd, agent_knowledge),
        )

        # Slash command wrapper
        _write_file(
            base,
            f".claude/commands/{agent_name.replace('_agent', '')}.md",
            tpl_slash_command(f"prompts/templates/ai-agents/{agent_name}.md", agent_desc),
        )

    # .gitignore template
    _write_file(base, ".gitignore",
        """# Dependencies
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
""")

    # package.json template
    _write_file(base, "package.json",
        f"""\
{{
  "name": "{project_name.lower().replace(" ", "-")}",
  "version": "0.1.0",
  "description": "{description}",
  "type": "module",
  "scripts": {{
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "lint": "eslint . --ext .ts,.tsx",
    "typecheck": "tsc --noEmit",
    "test": "vitest",
    "test:ui": "vitest --ui"
  }},
  "dependencies": {{
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }},
  "devDependencies": {{
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "@vitejs/plugin-react": "^4.0.0",
    "typescript": "^5.0.0",
    "vite": "^5.0.0",
    "vitest": "^1.0.0",
    "@testing-library/react": "^14.0.0",
    "@testing-library/jest-dom": "^6.1.0"
  }}
}}
""")

    # tsconfig.json template
    _write_file(base, "tsconfig.json",
        """\
{
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
""")

    # Add PlantUML diagrams
    plantuml_diagrams = get_all_plantuml_diagrams()
    for key, diagram in plantuml_diagrams.items():
        _write_file(base, f"docs/uml/plantuml/{diagram['name']}", diagram["content"])

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
# Interactive entry point
# ---------------------------------------------------------------------------

def prompt(msg: str, default: str | None = None) -> str | None:
    suffix = f" [{default}]" if default else ""
    value = input(f"{msg}{suffix}: ").strip()
    return value if value else default


def main() -> None:
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
