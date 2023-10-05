from flask import Flask, render_template, abort, send_file
import os
from pathlib import Path
from collections import OrderedDict

app = Flask(__name__)


@app.route("/", defaults={"req_path": ""})
@app.route("/<path:req_path>")
def index(req_path):
    BASE_DIR = Path.cwd()
    target_path = BASE_DIR / req_path
    abs_path = str(target_path.resolve())

    # Return 404 if path doesn't exist
    if not target_path.is_dir():
        return abort(404)

    # Check if path is a file and serve
    if target_path.is_file():
        return send_file(abs_path)

    files = {}
    for filepath in target_path.rglob("*.html"):
        if filepath.stem != "index":
            continue
        elif filepath.parent.stem == "templates":
            continue
        else:
            page = filepath.name
            app_folder = filepath.parent.name
            static_folder = filepath.parent.parent.name
            files[app_folder] = os.path.join(static_folder, app_folder, page)
    files = OrderedDict(sorted(files.items()))

    pdf_downloads = {}
    for filepath in target_path.rglob("*.pdf"):
        pdf_folder = filepath.parent.name
        if pdf_folder != "pdf_docs":
            continue
        pdf_file = filepath.name
        static_folder = filepath.parent.parent.name
        pdf_downloads[pdf_file] = os.path.join(static_folder, pdf_folder, pdf_file)
    pdf_downloads = OrderedDict(sorted(pdf_downloads.items()))

    return render_template("index.html", files=files, pdf_downloads=pdf_downloads)


def main():
    app.run(host="0.0.0.0", port="28868", debug=True)


if __name__ == "__main__":
    main()
