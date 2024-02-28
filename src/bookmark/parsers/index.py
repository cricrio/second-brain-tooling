from src.bookmark.parsers.instagram import instagram_parser


def parser(url: str) -> list[tuple[str, str]]:
    if 'instagram' in url:
        return instagram_parser(url)
    return []
