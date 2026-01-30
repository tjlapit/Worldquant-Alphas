import hashlib
import json

def hash_alpha(alpha_config: dict) -> str:
    alpha_str = json.dumps(alpha_config, sort_keys=True)
    return hashlib.sha256(alpha_str.encode()).hexdigest()
