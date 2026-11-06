from copy import deepcopy


def append_item(items: list[str], item: str) -> list[str]:
    updated = list(items)
    updated.append(item)
    return updated


def create_page_config(title: str, tags: list[str] | None = None) -> dict:
    safe_tags = [] if tags is None else list(tags)
    return {"title": title, "tags": safe_tags}


def shallow_vs_deep(original: dict) -> tuple[dict, dict]:
    shallow = dict(original)
    deep = deepcopy(original)
    return shallow, deep
