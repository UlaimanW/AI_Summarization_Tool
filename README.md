# AI Summarization Tool

A simple Streamlit web application that summarizes user-provided text using Groq's OpenAI-compatible API and saves the result as either a `.txt` file or a `.pdf` file.

The app is designed for quick text summarization with basic output file generation. It also includes Arabic PDF support using `arabic-reshaper`, `python-bidi`, and a custom Arabic font.

## Features

- Summarize text using `llama-3.3-70b-versatile` through the Groq API.
- Simple Streamlit web interface.
- Generate summaries directly inside the app.
- Save the summary as a `.txt` file by default.
- Save the summary as a `.pdf` file if the input text mentions `pdf` or `bdf`.
- Cleans unsafe file names before saving.
- Automatically creates a timestamp-based file name if no file name is provided.
- Supports Arabic text rendering in PDF output.
- Docker support for running the app in a container.

## Project Structure

```text
.
├── app.py              # Streamlit user interface
├── summarizer.py       # Groq API client and summarization logic
├── file_utils.py       # File name cleaning, TXT creation, and PDF creation
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image setup
├── .env                # Local environment variables (not uploaded to GitHub)
├── .gitignore          # Git ignored files
└── .dockerignore       # Docker ignored files
```

## How It Works

1. The user enters text in the Streamlit text area.
2. The user optionally enters a file name.
3. When the user clicks **Generate Summary**, the app sends the text to Groq using the OpenAI Python client.
4. The model returns a clear and brief summary.
5. The app displays the summary on the page.
6. If the input text includes `pdf` or `bdf`, the app creates a PDF file.
7. Otherwise, it creates a TXT file.

## Technologies Used

- Python
- Streamlit
- Groq API
- OpenAI Python SDK
- python-dotenv
- ReportLab
- arabic-reshaper
- python-bidi
- Docker

## Requirements

Install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Required packages:

```text
openai
python-dotenv
reportlab
arabic-reshaper
python-bidi
streamlit
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Do not upload `.env` to GitHub. It contains your private API key.

## Run Locally

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Run With Docker

Build the Docker image:

```bash
docker build -t ai-summarization-tool .
```

Run the container:

```bash
docker run --name ai_summarizer_container -p 8501:8501 --env-file .env ai-summarization-tool
```

Open the app in your browser:

```text
http://localhost:8501
```

## Important Notes

- The project uses Groq through an OpenAI-compatible client.
- The model used is `llama-3.3-70b-versatile`.
- The app checks for `GROQ_API_KEY` when `summarizer.py` loads. If the key is missing, the app raises an error.
- PDF generation requires the Arabic font file used in `file_utils.py` to exist in the expected `fonts/` path.
- Generated `.txt` and `.pdf` files are saved in the current working directory.

## Example Usage

Example input:

```text
Summarize this text and save it as PDF:
Artificial intelligence is changing how people work, study, and build software...
```

Example file name:

```text
ai_summary
```

Expected output:

```text
ai_summary.pdf
```

## Files Explanation

### `app.py`

Contains the Streamlit interface. It takes user input, calls the summarizer, displays the result, and decides whether to create a TXT or PDF file.

### `summarizer.py`

Loads the Groq API key from `.env`, creates the API client, and sends the text to the `llama-3.3-70b-versatile` model for summarization.

### `file_utils.py`

Handles file-related logic:

- Cleans file names.
- Creates TXT files.
- Detects Arabic text.
- Prepares Arabic text for PDF rendering.
- Creates PDF files using ReportLab.

### `Dockerfile`

Defines the container setup:

- Uses `python:3.11-slim`.
- Sets `/app` as the working directory.
- Installs dependencies.
- Copies the project files.
- Exposes port `8501`.
- Runs the Streamlit app.

## GitHub Notes

Before pushing to GitHub, make sure these files are ignored:

```gitignore
.env
__pycache__/
*.pyc
*.txt
*.pdf
```

Do not commit API keys, generated summaries, cache folders, or unnecessary environment files.

## Project Status

This is a beginner-friendly AI engineering project that demonstrates:

- Using environment variables safely.
- Calling an external LLM API.
- Building a Streamlit interface.
- Generating output files.
- Running a Python app inside Docker.
