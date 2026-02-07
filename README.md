# AI Assistant for answering questions about a CV

AI Assistant which answers questions to a given document. Has to be run on a local Server, with `litestar run` (Command in the terminal, has to be run in the same directory as `app.py`.

Package dependencies can be found in the `conda_env.yaml`.

## Usage

No working UI at the moment, but Backend fully functional and can be reached via `curl` command, or similar tools.

Local Server can be reached at `http://127.0.0.1:8000`.

- Documents can be uploaded via: `curl -X POST "http://localhost:8000/upload/pdf" -F "file=@sample_backend_developer_cv.pdf"`
- Questions can be asked via: `curl -X POST "http://localhost:8000/ask"      -H "Content-Type: application/json"      -d '{"question": "[PUT QUESTION HERE]"}'`

**Important:** This repo does not contain the model! I used the gguf of `Phi-3-mini-4k-instruct-q4`. This is a very small model with a low context length, does not work on documents longer than approximately 4-6 pages.

## TODO:

- Working UI Interface.
