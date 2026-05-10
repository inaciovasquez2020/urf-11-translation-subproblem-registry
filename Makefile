verify:
	python3 tools/verify_urf11_registry.py
	python3 -m pytest -q
	git diff --check
