# Project Structure

Documentation of the Web Project Generator repository structure.

## Root Files

```
dev_tools/
├── README.md                    # Main documentation (3000+ lines)
├── LICENSE                      # MIT License
├── AUTHOR.md                    # Author information & contributors guide
├── BADGES.md                    # Badge documentation and usage
├── STRUCTURE.md                 # This file
├── create_project.py            # Main generator script
├── package.json                 # (Future) Node.js config if needed
└── .gitignore                   # Git ignore patterns
```

## File Descriptions

### 📋 README.md

**Purpose:** Comprehensive guide to the Web Project Generator

**Sections:**
1. Overview with professional badges
2. Quick Start guide
3. Generated project structure
4. Key concepts (Tiers, Agents, UML)
5. Usage workflow (10 steps)
6. File reference
7. Best practices
8. Troubleshooting
9. Advanced usage
10. Architecture principles
11. Examples (2 full workflows)
12. Support and contributing
13. Author and license information

**Size:** ~3000 lines
**Audience:** Developers, architects, team leads
**Update Frequency:** As features change

### 📜 LICENSE

**Purpose:** MIT License text

**Contains:**
- Full MIT license legal text
- Copyright information
- Terms and conditions

**Format:** Plain text
**Links From:** README.md, AUTHOR.md

### ✍️ AUTHOR.md

**Purpose:** Author information and contributor guide

**Sections:**
1. Primary author details
2. Project philosophy
3. Contribution guidelines
4. Code style standards
5. Issue reporting format
6. Feature request template
7. Technology acknowledgments
8. Community credits
9. Contact information

**Size:** ~250 lines
**Audience:** Contributors, maintainers
**Update Frequency:** When accepting contributions

### 🎯 BADGES.md

**Purpose:** Explain all project badges

**Sections:**
1. Project badges (Python, License, Status, etc.)
2. Generated project badges (React, TypeScript, Vite, etc.)
3. Custom badge examples
4. Badge usage guide
5. Badge color recommendations
6. Complete badge set example
7. Badge service options

**Size:** ~200 lines
**Audience:** Documentation maintainers, contributors
**Update Frequency:** When badges change

### 📐 STRUCTURE.md

**Purpose:** This file - document project file organization

**Sections:**
1. Root files listing
2. File descriptions (this section)
3. Directory purposes
4. Quick reference guide
5. File relationships

**Size:** ~150 lines
**Audience:** New contributors, documentation
**Update Frequency:** When file structure changes

### 🐍 create_project.py

**Purpose:** Main Python script that generates Web projects

**Key Components:**
- `TODAY` - Current date constant
- `tpl_*()` - Template functions for each file
  - `tpl_start_here()` - START_HERE.md
  - `tpl_agents_md()` - AGENTS.md
  - `tpl_plan_md()` - /docs/plan.md
  - `tpl_tasks_md()` - /docs/tasks.md
  - `tpl_memory_md()` - /docs/memory.md
  - `tpl_knowledge_base()` - /docs/knowledge/KNOWLEDGE_BASE.md
  - `tpl_project_context()` - /docs/knowledge/core/00_*.md
  - `tpl_domain_model()` - /docs/knowledge/core/01_*.md
  - `tpl_frontend_architecture()` - /docs/knowledge/core/02_*.md
  - `tpl_component_model()` - /docs/knowledge/core/03_*.md
  - `tpl_api_integration()` - /docs/knowledge/core/04_*.md
  - `tpl_testing_strategy()` - /docs/knowledge/core/05_*.md
  - `tpl_accessibility_strategy()` - /docs/knowledge/core/06_*.md
  - `tpl_security_model()` - /docs/knowledge/core/07_*.md
  - `tpl_deployment_model()` - /docs/knowledge/core/08_*.md
  - `tpl_design()` - /docs/design.md
  - `tpl_architecture()` - /docs/knowledge/source-of-truth/ARCHITECTURE.md
  - `tpl_adr()` - ADR template
  - `tpl_agent()` - AI agent prompts
  - `tpl_slash_command()` - Slash command wrappers
  - `tpl_progress_tracker()` - Progress tracking

- `DIRS` - List of directories to create
- `AGENTS` - List of 7 AI agents
- `create_structure()` - Main function to generate files
- `main()` - Entry point with user prompts

**Size:** ~2700 lines
**Language:** Python 3.8+
**Dependencies:** Standard library only

## Generated Project Structure

When you run `create_project.py`, it generates:

```
my-awesome-app/
├── START_HERE.md                 # Project entry point
├── AGENTS.md                     # Agent rules
├── package.json                  # Node.js config
├── tsconfig.json                 # TypeScript config
├── .gitignore                    # Git ignore rules
│
├── docs/
│   ├── plan.md                   # Implementation plan
│   ├── tasks.md                  # Work items
│   ├── design.md                 # System design & UML
│   ├── memory.md                 # Durable decisions
│   ├── knowledge/
│   │   ├── KNOWLEDGE_BASE.md     # Doc index
│   │   ├── KNOWLEDGE_GRAPH.md    # Doc relationships
│   │   ├── source-of-truth/      # Tier 1
│   │   ├── core/                 # Tier 2 (8 files)
│   │   ├── implementation/       # Tier 3
│   │   ├── meetings/             # Meeting notes
│   │   ├── team/                 # Team docs
│   │   └── archive/              # Tier 4
│   ├── adr/                      # Architecture records
│   ├── uml/                      # UML diagrams
│   └── generated/                # Generated artifacts
│
├── prompts/templates/ai-agents/  # Agent prompts (7 agents)
├── .claude/commands/             # Slash commands (7 wrappers)
├── src/                          # Application source (empty)
└── public/                       # Static assets (empty)
```

## Quick Reference

### To Understand the Project

1. Start with **README.md** - Overview and usage
2. Check **LICENSE** - Legal terms
3. Read **AUTHOR.md** - Contributor guidelines
4. Review **BADGES.md** - Badge documentation
5. See **STRUCTURE.md** - This file

### To Modify the Generator

1. Edit **create_project.py** templates
2. Add new `tpl_*()` functions for new files
3. Update `DIRS` list if adding directories
4. Update `AGENTS` if modifying agents
5. Update `create_structure()` to use new templates

### To Use in a Project

1. Run `python create_project.py`
2. Answer prompts
3. Review generated **START_HERE.md**
4. Edit generated **README.md** or project docs

### To Contribute

1. Review **AUTHOR.md** contribution guidelines
2. Fork the repository
3. Create a feature branch
4. Make changes to **create_project.py** or docs
5. Test by running the generator
6. Submit a Pull Request

## Dependencies

### External Dependencies

**None** - The `create_project.py` uses only Python standard library

### Generated Project Dependencies

Generated projects typically include:

```json
{
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
```

## File Relationships

```
README.md
  ├── references LICENSE
  ├── references AUTHOR.md
  ├── references BADGES.md
  └── provides usage examples

AUTHOR.md
  ├── references LICENSE
  └── describes contribution process

BADGES.md
  └── documents all markdown badges

create_project.py
  ├── generates START_HERE.md
  ├── generates AGENTS.md
  ├── generates docs/
  ├── generates prompts/templates/ai-agents/
  ├── generates .claude/commands/
  └── generates package.json, tsconfig.json

Generated Project (my-awesome-app/)
  ├── references START_HERE.md
  ├── includes AGENTS.md
  ├── includes README.md or docs/
  └── includes all doc files
```

## Maintenance Guidelines

### Update Schedule

| File              | Update Frequency     | Trigger                    |
|-------------------|----------------------|----------------------------|
| README.md         | Quarterly            | New features, major updates|
| AUTHOR.md         | As needed            | New contributors           |
| BADGES.md         | When badges change   | Version updates, new badges|
| STRUCTURE.md      | When files change    | New files added/removed    |
| create_project.py | Per feature          | Template additions        |
| LICENSE           | Never (unless copy)  | Ownership changes         |

### Before Release

- [ ] Run `python create_project.py` to test
- [ ] Verify all generated files exist
- [ ] Check links in README.md
- [ ] Update version numbers
- [ ] Update AUTHOR.md dates
- [ ] Run code formatter if applicable

### After Release

- [ ] Tag release in Git
- [ ] Update version in create_project.py
- [ ] Update version in badges
- [ ] Announce on relevant channels

## Common Tasks

### Add a New Template

1. Create `tpl_new_file()` function in create_project.py
2. Add to `docs_files` or `knowledge_files` dict in `create_structure()`
3. Test by running generator
4. Document in README.md if user-facing
5. Update STRUCTURE.md if structure changes

### Update Documentation

1. Edit README.md, AUTHOR.md, or BADGES.md
2. Check links work correctly
3. Test code examples if included
4. Update "Last Updated" dates
5. Commit with clear message

### Create New Release

1. Test everything works
2. Update version in create_project.py
3. Update AUTHOR.md version history
4. Create Git tag: `git tag v1.1.0`
5. Push with tags: `git push --tags`

## Version Information

- **Created:** 2026-05-13
- **Current Version:** 1.0.0
- **Python:** 3.8+
- **Status:** Active
- **License:** MIT

## Related Resources

- [README.md](./README.md) - Main documentation
- [MIT License](./LICENSE) - License text
- [AUTHOR.md](./AUTHOR.md) - Author and contributor info

---

**Last Updated:** 2026-05-13

For questions or updates, see [AUTHOR.md](./AUTHOR.md)
