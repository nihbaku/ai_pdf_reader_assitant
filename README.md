# AI Assistant for answering questions about a PDF Document

AI Assistant which answers questions to a given PDF document. Has to be run on a local Server, with `litestar run` (Terminal command which has be run in the same directory as `app.py`).

Package dependencies can be found in the `conda_env.yaml`.

## Usage

No working UI at the moment. But backend is fully functional and can be reached via `curl` command, or similar tools.

Local Server can be reached at `http://127.0.0.1:8000`.

- Documents can be uploaded via: `curl -X POST "http://localhost:8000/upload/pdf" -F "file=@[PATH/TO/FILE/HERE]"`
- Questions can be asked via: `curl -X POST "http://localhost:8000/ask"      -H "Content-Type: application/json"      -d '{"question": "[PUT QUESTION HERE]"}'`

Paths given for the upload can be relative.

**Important:** This repo does not contain the model! I used the gguf of `Phi-3-mini-4k-instruct-q4`. This is a very small model with a low context length, does not work on documents longer than approximately 4-6 pages. If you want to use this app you should get either the same or a compatible model. This is put into the `model/` directory at the same level as the source directory is.

At the End the directory structure looks like this:

```
├── ai-assistant
    ├── data    # Has a sample CV for testing inside
    ├── model   # Create this and put the model here
    ├── source  # Here the code resides
```

### TODO:

- Working UI Interface.
