from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUERY_DIRS = ["identity", "endpoint", "email", "cloud"]

def query_files():
    files = []
    for directory in QUERY_DIRS:
        files.extend((ROOT / directory).glob("*.kql"))
    return files

def test_library_contains_queries():
    assert len(query_files()) >= 5

def test_every_query_file_is_documented():
    for path in query_files():
        text = path.read_text(encoding="utf-8")
        assert "//" in text
        assert "|" in text
        assert len(text.strip()) > 100

def test_no_placeholder_domains_or_secrets_required():
    for path in query_files():
        text = path.read_text(encoding="utf-8").lower()
        assert "password=" not in text
        assert "client_secret" not in text
