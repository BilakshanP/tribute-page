import os

from typing import Any, Callable, Optional

def replace_value(dictionary: dict[str, Any], predicate: Callable[[Any], bool], transformer: Callable[[Any], Any], *, key_check: bool = False, key_predicate: Optional[Callable[[Any], bool]] = None) -> None:
    """
    Recursively replaces occurrences of old_value with transformed new_value in nested dictionaries.

    Args:
        dictionary (dict[str, Any]): The nested dictionary to traverse.
        predicate (Callable[[Any], bool]): A function that returns True if the value should be replaced.
        transformer (Callable[[Any], Any]): A function that transforms the old value to the new value.

    Returns:
        None
    """
    for key, value in dictionary.items():
        if isinstance(value, dict):
            replace_value(value, predicate, transformer) #type: ignore
        elif predicate(value) and (key_check or (key_predicate is None or key_predicate(key))):
            dictionary[key] = transformer(value)

def process_directory(directory: str) -> dict[str, list[str]]:
    folder_json_mapping: dict[str, list[str]] = {"dirs": []}
    for root, _, files in os.walk(directory):
        folder_name: str = os.path.basename(root)
        json_files: list[str] = []
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.splitext(file)[0])
        folder_json_mapping[folder_name] = json_files
        if folder_name != os.path.basename(directory):
            folder_json_mapping["dirs"].append(folder_name)

    return folder_json_mapping
