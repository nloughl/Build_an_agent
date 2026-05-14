# Build an Agent

A coding agent powered by Google Gemini that can autonomously read, write, and execute files to complete programming tasks.

## How it works

The agent runs in an agentic loop (up to 20 iterations) — each iteration calls Gemini, appends the model's response to the conversation history, dispatches any requested tool calls, and feeds the results back to the model. The loop exits when the model produces a final text response.

The working directory is hardcoded to `./calculator`, so the agent operates on that project by default.

## Tools available to the agent

| Function | Description |
|---|---|
| `get_files_info` | Lists files in a directory with sizes |
| `get_file_content` | Reads a file's contents (truncated at max chars) |
| `run_python_file` | Executes a Python file with optional arguments |
| `write_file` | Writes or overwrites a file |

All tool calls are sandboxed to the working directory — paths outside it are rejected.

## Usage

```
python main.py "<your prompt>" [--verbose]
```

**Examples:**

```
python main.py "What files are in the project?"
python main.py "Run the tests and fix any failures" --verbose
```

`--verbose` prints the prompt, token counts, and full tool call inputs/outputs each iteration.

## Setup

1. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_key_here
   ```
2. Install dependencies:
   ```
   uv sync
   ```
3. Run:
   ```
   python main.py "your prompt"
   ```
