from ecosort_edge.diagnostics import collect_diagnostics


def test_diagnostics_have_required_environment_fields() -> None:
    details = collect_diagnostics()

    assert details["python_version"]
    assert details["python_executable"]
    assert isinstance(details["cuda_available"], bool)
    assert "torch_version" in details
