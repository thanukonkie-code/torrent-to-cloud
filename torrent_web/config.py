import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_STATE_DIR = Path.home() / ".torrent_web"
STATE_DIR = Path(os.getenv("TORRENT_WEB_HOME", str(DEFAULT_STATE_DIR))).expanduser()
STATE_PATH = STATE_DIR / "state.json"
TOKENS_PATH = STATE_DIR / "onedrive_tokens.json"


def ensure_paths() -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    if not STATE_PATH.exists():
        STATE_PATH.write_text("{}", encoding="utf-8")
    if not TOKENS_PATH.exists():
        TOKENS_PATH.write_text("{}", encoding="utf-8")


def get_default_download_dir() -> str:
    return os.path.expanduser(os.getenv("DEFAULT_DOWNLOAD_DIR", str(Path.home() / "Downloads" / "torrent_web")))


def get_aria2_rpc_url() -> str:
    port = os.getenv("ARIA2_RPC_PORT", "6800")
    return f"http://localhost:{port}/jsonrpc"


def get_client_config() -> dict:
    return {
        "client_id": os.getenv("MICROSOFT_CLIENT_ID"),
        "tenant_id": os.getenv("MICROSOFT_TENANT_ID", "common"),
    }
