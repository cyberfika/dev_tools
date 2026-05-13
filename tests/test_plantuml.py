"""Tests for plantuml_diagrams.py."""

from plantuml_diagrams import get_all_plantuml_diagrams


class TestPlantUMLDiagrams:
    """Verify all PlantUML diagram templates."""

    def test_get_all_returns_dict(self):
        diagrams = get_all_plantuml_diagrams()
        assert isinstance(diagrams, dict)

    def test_all_13_diagrams_present(self):
        diagrams = get_all_plantuml_diagrams()
        assert len(diagrams) == 13

    def test_each_diagram_has_required_keys(self):
        diagrams = get_all_plantuml_diagrams()
        for key, diagram in diagrams.items():
            assert "name" in diagram, f"Missing 'name' in {key}"
            assert "description" in diagram, f"Missing 'description' in {key}"
            assert "type" in diagram, f"Missing 'type' in {key}"
            assert "content" in diagram, f"Missing 'content' in {key}"

    def test_each_diagram_has_puml_content(self):
        diagrams = get_all_plantuml_diagrams()
        for key, diagram in diagrams.items():
            assert diagram["content"].startswith("@startuml"), (
                f"{key} content does not start with @startuml"
            )
            assert diagram["content"].strip().endswith("@enduml"), (
                f"{key} content does not end with @enduml"
            )

    def test_each_diagram_has_puml_extension(self):
        diagrams = get_all_plantuml_diagrams()
        for key, diagram in diagrams.items():
            assert diagram["name"].endswith(".puml"), (
                f"{key} name '{diagram['name']}' does not end with .puml"
            )

    def test_diagram_types_are_valid(self):
        valid_types = {"use-case", "class", "sequence", "component", "state", "deployment", "erd"}
        diagrams = get_all_plantuml_diagrams()
        for key, diagram in diagrams.items():
            assert diagram["type"] in valid_types, (
                f"{key} has invalid type '{diagram['type']}'"
            )

    def test_specific_diagrams_exist(self):
        diagrams = get_all_plantuml_diagrams()
        names = {d["name"] for d in diagrams.values()}
        expected = {
            "web_usecase_diagram.puml",
            "auth_usecase_diagram.puml",
            "domain_model.puml",
            "services_diagram.puml",
            "login_sequence.puml",
            "checkout_sequence.puml",
            "frontend_components.puml",
            "system_architecture.puml",
            "form_states.puml",
            "order_states.puml",
            "auth_states.puml",
            "deployment_architecture.puml",
            "database_erd.puml",
        }
        missing = expected - names
        assert not missing, f"Missing diagrams: {missing}"
