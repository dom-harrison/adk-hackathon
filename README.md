# Funding Assistant Agent

This project contains a helpful assistant built with the Google Agent Development Kit (ADK) to help users understand their savings potential and set up regular savings deposits.

## Prerequisites

*   Python 3.8+
*   Google Cloud SDK (`gcloud`) installed and authenticated.
*   An active Google Cloud project.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd adk-hackathon
    ```

2.  **Create and activate a virtual environment:**

    It's recommended to use a virtual environment (`venv`) to manage project dependencies.
    You only need to **create** the environment once per clone. In new terminal sessions, you just need to **activate** it.
    ```bash
    # Create a virtual environment (e.g., named 'venv')
    python3 -m venv venv

    # Activate the virtual environment
    source venv/bin/activate
    ```
    *Note: On Windows, the activation command is `venv\Scripts\activate`.*

3.  **Install dependencies:**

    Install the required Python packages.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Enable Google Cloud Services:**

    You need to enable the AI Platform API for your Google Cloud project to use the underlying models.

    ```bash
    gcloud services enable aiplatform.googleapis.com
    ```

## Running the Agent

The Agent Development Kit (ADK) provides several ways to interact with your agent. Make sure your virtual environment is activated before running these commands.

### Command-Line Interface (`adk run`)

To interact with your agent directly from the terminal, use the `adk run` command. This is great for quick tests and debugging.

```bash
adk run funding_assistant
```

### Web Interface (`adk web`)

The ADK includes a simple web-based chat interface. To launch it, run:

```bash
adk web
```

### API Server (`adk api_server`)

To expose your agent as an API endpoint, you can use the `adk api_server` command. This allows other applications to interact with your agent programmatically.

```bash
adk api_server
```
