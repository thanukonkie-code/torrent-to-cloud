import json
import os
from pathlib import Path

APP_NAME = "torrent_to_cloud"
DEFAULT_CONFIG_DIR = Path.home() / ".torrent_to_cloud"
CONFIG_DIR = Path(os.getenv("TORRENT_TO_CLOUD_HOME", str(DEFAULT_CONFIG_DIR)))
STATE_PATH = CONFIG_DIR / "state.json"
TOKENS_PATH = CONFIG_DIR / "onedrive_tokens.json"


def ensure_paths() -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if not STATE_PATH.exists():
        STATE_PATH.write_text("{}", encoding="utf-8")
    if not TOKENS_PATH.exists():
        TOKENS_PATH.write_text("{}", encoding="utf-8")


def load_json(path: Path, default: dict | list | str | None = None):
    if not path.exists():
        return default
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError:
        return default


def save_json(path: Path, payload) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)


def get_default_download_dir() -> str:
    return os.path.expanduser(os.getenv("DEFAULT_DOWNLOAD_DIR", str(Path.home() / "Downloads" / "torrent_to_cloud")))


def get_aria2_rpc_url() -> str:
    port = os.getenv("ARIA2_RPC_PORT", "6800")
    return f"http://localhost:{port}/jsonrpc"


def get_client_config() -> dict:
    return {
        "client_id": os.getenv("MICROSOFT_CLIENT_ID"),
        "tenant_id": os.getenv("MICROSOFT_TENANT_ID", "common"),
    }
