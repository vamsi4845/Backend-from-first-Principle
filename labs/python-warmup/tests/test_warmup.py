import asyncio

from exercises import (
    append_item,
    create_page_config,
    fetch_both,
    merge_counts,
    normalize_email,
    active_usernames,
)


def test_normalize_email() -> None:
    assert normalize_email("  Ada@Example.COM ") == "ada@example.com"


def test_merge_counts_does_not_mutate_base() -> None:
    base = {"a": 1}
    extra = {"a": 2, "b": 1}
    merged = merge_counts(base, extra)
    assert merged == {"a": 3, "b": 1}
    assert base == {"a": 1}


def test_active_usernames() -> None:
    users = [
        {"username": "ada", "active": True},
        {"username": "bob", "active": False},
        {"active": True},
    ]
    assert active_usernames(users) == ["ada"]


def test_append_item_does_not_mutate_input() -> None:
    items = ["a"]
    result = append_item(items, "b")
    assert result == ["a", "b"]
    assert items == ["a"]


def test_create_page_config_default_tags() -> None:
    one = create_page_config("Home")
    two = create_page_config("About")
    one["tags"].append("x")
    assert one["tags"] == ["x"]
    assert two["tags"] == []


def test_async_gather() -> None:
    first, second = asyncio.run(fetch_both())
    assert (first, second) == ("users", "tasks")
