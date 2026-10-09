from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class TorrentResult:
    title: str
    source: str
    size: str
    seeders: int
    leechers: int
    magnet_url: str
    page_url: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class DownloadJob:
    id: str
    name: str
    magnet_url: str
    output_dir: str
    gid: Optional[str] = None
    status: str = "queued"
    progress: float = 0.0
    total_size: str = "unknown"
    source: str = "unknown"

    def to_dict(self) -> dict:
        return asdict(self)
