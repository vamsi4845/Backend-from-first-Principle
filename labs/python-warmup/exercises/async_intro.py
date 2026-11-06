import asyncio


async def fetch_label(delay_ms: int, label: str) -> str:
    await asyncio.sleep(delay_ms / 1000)
    return label


async def fetch_both() -> tuple[str, str]:
    first, second = await asyncio.gather(
        fetch_label(10, "users"),
        fetch_label(10, "tasks"),
    )
    return first, second
