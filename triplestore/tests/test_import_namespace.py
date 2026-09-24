import importlib


def test_rdf_triplestore_imports() -> None:
    module = importlib.import_module("rdf_triplestore")
    assert hasattr(module, "Triplestore")
    assert callable(module.Triplestore)
