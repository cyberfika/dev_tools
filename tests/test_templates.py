"""Tests for templates.py — all tpl_* template functions."""

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


class TestTemplates:
    """Verify all template functions return valid markdown content."""

    def test_tpl_start_here(self):
        result = tpl_start_here("TestApp", "A test project", "John - Dev")
        assert "# START HERE" in result
        assert "TestApp" in result
        assert "A test project" in result
        assert "John - Dev" in result

    def test_tpl_agents_md(self):
        result = tpl_agents_md("TestApp")
        assert "# AGENTS" in result
        assert "TestApp" in result
        assert "/dev" in result

    def test_tpl_plan_md(self):
        result = tpl_plan_md()
        assert "# Plan" in result
        assert "## Objective" in result
        assert "## Implementation Strategy" in result

    def test_tpl_tasks_md(self):
        result = tpl_tasks_md()
        assert "# Tasks" in result
        assert "## Backlog" in result
        assert "## Verification Checklist" in result

    def test_tpl_memory_md(self):
        result = tpl_memory_md()
        assert "# Memory" in result
        assert "## Approved Decisions" in result
        assert "## Session Log" in result

    def test_tpl_knowledge_base(self):
        result = tpl_knowledge_base("TestApp")
        assert "# Knowledge Base" in result
        assert "TestApp" in result
        assert "Tier 1" in result
        assert "Tier 2" in result

    def test_tpl_architecture(self):
        result = tpl_architecture()
        assert "# ARCHITECTURE" in result
        assert "## Core Components" in result
        assert "Tier 1" in result

    def test_tpl_adr(self):
        result = tpl_adr()
        assert "ADR-001" in result
        assert "## Context" in result
        assert "## Decision" in result

    def test_tpl_design(self):
        result = tpl_design()
        assert "# Design" in result
        assert "## System Overview" in result
        assert "## UML Diagrams" in result

    def test_tpl_project_context(self):
        result = tpl_project_context()
        assert "# 00_project_context" in result
        assert "## Project Goal" in result
        assert "## Stakeholders" in result

    def test_tpl_domain_model(self):
        result = tpl_domain_model()
        assert "# 01_domain_model" in result
        assert "## Core Concepts" in result
        assert "## Domain Rules" in result

    def test_tpl_frontend_architecture(self):
        result = tpl_frontend_architecture()
        assert "# 02_frontend_architecture" in result
        assert "## Architecture Pattern" in result
        assert "Presentation Layer" in result

    def test_tpl_component_model(self):
        result = tpl_component_model()
        assert "# 03_component_model" in result
        assert "## Component Classification" in result
        assert "Page Components" in result

    def test_tpl_api_integration(self):
        result = tpl_api_integration()
        assert "# 04_api_integration" in result
        assert "## API Client Structure" in result
        assert "## Endpoint Reference" in result

    def test_tpl_testing_strategy(self):
        result = tpl_testing_strategy()
        assert "# 05_testing_strategy" in result
        assert "## Test Types" in result
        assert "Unit Tests" in result

    def test_tpl_accessibility_strategy(self):
        result = tpl_accessibility_strategy()
        assert "# 06_accessibility_strategy" in result
        assert "WCAG 2.1" in result
        assert "## Implementation Guidelines" in result

    def test_tpl_security_model(self):
        result = tpl_security_model()
        assert "# 07_security_model" in result
        assert "## Threat Model" in result
        assert "XSS" in result

    def test_tpl_deployment_model(self):
        result = tpl_deployment_model()
        assert "# 08_deployment_model" in result
        assert "## Build Process" in result
        assert "## Environments" in result

    def test_tpl_agent(self):
        knowledge = ["core/00_project_context.md", "core/01_domain_model.md"]
        result = tpl_agent("Test Agent", "/test", knowledge)
        assert "Test Agent" in result
        assert "/test" in result
        assert "core/00_project_context.md" in result

    def test_tpl_slash_command(self):
        result = tpl_slash_command("path/to/agent.md", "Test description")
        assert "Test description" in result
        assert "path/to/agent.md" in result

    def test_tpl_progress_tracker(self):
        result = tpl_progress_tracker("TestApp")
        assert "TestApp" in result
        assert "## Current Sprint" in result
        assert "## Metrics" in result
