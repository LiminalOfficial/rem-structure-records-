import json
from pathlib import Path
from typing import Any, Dict


def save_persona(persona: Dict[str, Any], file_path: str) -> None:
    """Save persona data to a JSON file.

    Parameters
    ----------
    persona : dict
        Persona data to save.
    file_path : str
        Path to the JSON file where persona will be saved.
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as f:
        json.dump(persona, f, ensure_ascii=False, indent=2)


def load_persona(file_path: str) -> Dict[str, Any]:
    """Load persona data from a JSON file.

    Parameters
    ----------
    file_path : str
        Path to the JSON file to read.

    Returns
    -------
    dict
        Loaded persona data. If the file does not exist, an empty dict is
        returned.
    """
    path = Path(file_path)
    if not path.exists():
        return {}
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)
