"""Production runner using Waitress WSGI server.

Usage (from project root):
    pip install waitress
    python -m backend.run_prod

Waitress is cross-platform and recommended for simple production use on Windows.
For Linux/Unix prefer Gunicorn: `gunicorn backend.app:app --bind 0.0.0.0:5000`
"""
from waitress import serve
from backend.app import app


def main():
    # Adjust threads/workers as appropriate for your environment
    serve(app, host='0.0.0.0', port=5000, threads=8)


if __name__ == '__main__':
    main()
