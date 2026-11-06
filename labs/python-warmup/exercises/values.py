def normalize_email(raw: str) -> str:
    return raw.strip().lower()


def merge_counts(base: dict[str, int], extra: dict[str, int]) -> dict[str, int]:
    result = dict(base)
    for key, value in extra.items():
        result[key] = result.get(key, 0) + value
    return result


def active_usernames(users: list[dict]) -> list[str]:
    return [
        user["username"]
        for user in users
        if user.get("active") is True and "username" in user
    ]
