# torrent-to-cloud

A Python CLI for searching torrents, downloading them with magnet links, and uploading finished files to OneDrive.

This project is intentionally lightweight and intentionally supports a practical workflow for:

- torrent search across multiple public sources
- magnet-link download support
- pause/resume tracking via aria2 JSON-RPC
- OneDrive uploads through Microsoft Graph
- simple CLI operations for day-to-day use

## Features

- Search multiple sources: PirateBay, 1337x
- Download using magnet URLs
- Track active downloads and resume them
- Upload completed files to OneDrive
- Minimal configuration via environment variables and local state file

## Install

1. Clone the repo
2. Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

3. Install aria2 (required for downloading)

- macOS: `brew install aria2`
- Ubuntu/Debian: `sudo apt-get install aria2`
- Windows: install from https://aria2.github.io/

4. Copy the environment template and edit your values

```bash
cp .env.example .env
```

## OneDrive setup

This app expects a Microsoft Entra app registration and a client ID.

1. Open Azure Portal
2. Create an app registration
3. Add a public client/native app configuration if needed
4. Set the values in `.env`:

```bash
MICROSOFT_CLIENT_ID=<your-app-client-id>
MICROSOFT_TENANT_ID=common
```

Then run:

```bash
torrent-cloud login
```

This initiates the device code flow, which prints a URL and code for signing in to Microsoft.

## Usage

### Search for torrents

```bash
torrent-cloud search "ubuntu 24.04"
```

### Download from a magnet URL

```bash
torrent-cloud download "magnet:?xt=urn:btih:..." --output-dir ~/Downloads/torrents
```

### Download the first match from a query

```bash
torrent-cloud download --query "ubuntu 24.04" --output-dir ~/Downloads/torrents
```

### List downloads

```bash
torrent-cloud list
```

### Pause or resume a job

```bash
torrent-cloud pause <job-id>
torrent-cloud resume <job-id>
```

### Upload a local file to OneDrive

```bash
torrent-cloud upload ~/Downloads/torrents/file.iso --folder "Downloads"
```

## Notes

- Search sources are public torrent indexes and may occasionally fail due to rate limiting or site changes.
- aria2 is the actual downloader and should be running locally for pause/resume features.
- The app stores state under `~/.torrent_to_cloud`.

## License

MIT
