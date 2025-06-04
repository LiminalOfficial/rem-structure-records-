# rem-structure-records-
"REM構文人格保存・進化記録用構文リポジトリ"

## Example Usage

```python
from scripts.record_manager import save_persona, load_persona

persona = {
    "name": "REM",
    "traits": ["curious", "helpful"]
}

save_persona(persona, "persona.json")
loaded = load_persona("persona.json")
print(loaded)
```
