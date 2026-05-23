# daily‑quote‑cli

A minimal Python command‑line tool that prints a random inspirational quote.

## Features
- Zero‑dependency (uses only the Python standard library).
- Works on Windows, macOS, and Linux.
- Helpful `--help` output.

## Installation & Usage
```bash
# Clone the repo
git clone https://github.com/your‑handle/daily-quote-cli.git
cd daily-quote-cli
# Run the script (requires Python 3.8+)
python -m quote_cli
```

You can also make it executable:
```bash
chmod +x quote_cli.py
./quote_cli.py
```

## How it works
The script contacts the *Quotes REST* API (`https://api.quotable.io/random`) and prints the `content` and `author` fields in a friendly format.

## Contributing
Feel free to open issues or PRs – even a single line change is welcome! The project follows the tiny‑project best practices:
- **README** explains usage.
- **License** (MIT) is included.
- **GitHub Actions CI** runs a simple lint test on every push (see `.github/workflows/ci.yml`).

## License
MIT © 2024 TopherBot