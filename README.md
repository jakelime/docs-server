# Documentation Server

## Description

Simple `Flask` application to serve documentations.

Documentations are created using [sphinx](https://www.sphinx-doc.org/)

## Quickstart

1. Install `requirements` and run `main.py`

   ```bash
   ➜  docs_server git:(main) ✗ python -m venv venv
   ➜  docs_server git:(main) ✗ source venv/bin/activate
   (venv)➜  docs_server git:(main) ✗ pip install -r requirements.txt
   (venv) ➜  docs_server git:(main) ✗
   (venv) ➜  docs_server git:(main) ✗ python main.py
   * Serving Flask app 'main'
   * Debug mode: on
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on all addresses (0.0.0.0)
   * Running on http://127.0.0.1:28868
   Press CTRL+C to quit
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 128-822-576
   x.x.x.x - - [05/Oct/2023 14:06:05] "GET / HTTP/1.1" 200 -
   x.x.x.x - - [05/Oct/2023 14:06:18] "GET /static/style.css HTTP/1.1" 304 -
   ```

1. On local machine (server), use webbrowser to access `http://127.0.0.1:28868`

1. On another machine (client), use webbrowser to access `http://X.X.X.X:28868`, where `X.X.X.X` is the IP Address of the server