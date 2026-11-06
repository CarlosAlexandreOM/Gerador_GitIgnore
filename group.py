# Grupos
GROUPS = {
    "VS Code": [
        ".vscode/",
    ],

    "Python": [
        "__pycache__/",
        "*.py[cod]",
        "*$py.class",
        ".pytest_cache/",
        ".mypy_cache/",
        ".ruff_cache/",
        ".coverage",
        "htmlcov/",
    ],

    "Conda": [
        ".venv/",
        "venv/",
        "env/",
        ".conda/",
    ],

    "Excel": [
        "*.xls",
        "*.xlsx",
        "*.xlsm",
        "*.xlsb",
        "*.csv",
    ],

    "Power BI": [
        "*.pbix",
        "*.pbit",
    ],

    "Bancos de dados": [
        "*.db",
        "*.sqlite",
        "*.sqlite3",
        "*.db-wal",
        "*.db-shm",
        "*.db-journal",
    ],

    "Jupyter": [
        ".ipynb_checkpoints/",
    ],

    "Arquivos sensíveis": [
        ".env",
        ".env.*",
        "!.env.example",
    ],

    "Windows": [
        "Thumbs.db",
        "Desktop.ini",
    ],

    "Build": [
        "build/",
        "dist/",
        "*.egg-info/",
    ],
}

# Dicionário de opções

DICT_NAMES = {
        1: "VS Code",
        2: "Python",
        3: "Conda",
        4: "Excel",
        5: "Power BI",
        6: "Bancos de dados",
        7: "Jupyter",
        8: "Arquivos sensíveis",
        9: "Windows",
        10: "Build",
        11: "Sair",
        12: "Criar Arquivo"
    }