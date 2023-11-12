import re
from typing import Union


def extract_json(string: str) -> Union[str, None]:
    """extracts the json format from the llm response"""
    pattern = r"\{[^{}]*\}"
    match = re.search(pattern, string)
    if match:
        json_string = match.group()
        return json_string
    return string
