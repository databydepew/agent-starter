# Vertex Agent

A powerful multimodal RAG agent built with Google's Gemini Live API, providing real-time audio, video, and text interactions with vector database-backed responses.

![Vertex Agent](https://storage.googleapis.com/github-repo/generative-ai/sample-apps/e2e-gen-ai-app-starter-pack/live_api_pattern_demo.gif)

## Overview

Vertex Agent is a conversational agent that leverages Google's Gemini 2.0 model to deliver real-time multimodal interactions. The agent can:

- Process and respond to audio, video, and text inputs
- Utilize tool calling capabilities for enhanced responses
- Connect to external data sources via a vector database
- Provide personalized responses based on user context

## Key Features

- **Real-time Bidirectional Communication**: WebSocket-based communication between frontend and Gemini model
- **Multimodal Interactions**: Support for audio, video, and text inputs/outputs
- **Tool Integration**: Built-in tools like weather information retrieval, with extensible architecture
- **Production-Ready Backend**: FastAPI server with retry logic and automatic reconnection
- **Modern React Frontend**: Enhanced UI based on Google's Multimodal Live API Web Console
- **Deployment Flexibility**: Support for both AI Studio and Vertex AI endpoints
- **Feedback Collection**: Integrated feedback logging for continuous improvement

## Project Structure

```
vertex-agent/
├── app/                # Core application code
│   ├── agent.py        # Main agent logic
│   ├── server.py       # FastAPI backend server
│   └── utils/          # Utility functions and helpers
│   ├── deployment/         # Infrastructure and deployment scripts
│   │   ├── cd/             # Continuous deployment configurations
│   │   ├── ci/             # Continuous integration configurations
│   │   └── terraform/      # Infrastructure as code
│   ├── frontend/           # React-based UI
│   │   ├── public/         # Static assets
│   │   └── src/            # Frontend source code
│   ├── Makefile            # Common commands
│   └── README.md           # Project documentation
```

## Requirements

Before you begin, ensure you have:

- **uv**: Python package manager - [Install](https://docs.astral.sh/uv/getting-started/installation/)
- **Google Cloud SDK**: For GCP services - [Install](https://cloud.google.com/sdk/docs/install)
- **Terraform**: For infrastructure deployment - [Install](https://developer.hashicorp.com/terraform/downloads)
- **make**: Build automation tool - [Install](https://www.gnu.org/software/make/) (pre-installed on most Unix-based systems)
- **Node.js and npm**: For frontend development

## Quick Start (Local Testing)

Install required packages and launch the local development environment:

```bash
make install && make playground
```

## Common Commands

| Command              | Description                                           |
| -------------------- | ----------------------------------------------------- |
| `make install`       | Install all required dependencies using uv            |
| `make playground`    | Launch local development environment (backend + frontend) |
| `make backend`       | Deploy agent to Cloud Run                             |
| `make local-backend` | Launch local development server                       |
| `make ui`            | Launch Agent Playground front-end only                |
| `make test`          | Run unit and integration tests                        |
| `make lint`          | Run code quality checks                               |
| `make setup-dev-env` | Set up development environment resources with Terraform |

For full command options and usage, refer to the [Makefile](vertex-agent/Makefile).

## Usage Guide

This project follows a "bring your own agent" approach - you focus on your business logic in `app/agent.py`, and the template handles the surrounding components.

### Local Development Workflow

1. **Install Dependencies**:
   ```bash
   make install
   ```

2. **Start the Backend Server**:
   ```bash
   make backend
   ```
   The backend is ready when you see `INFO: Application startup complete.`

3. **Start the Frontend UI**:
   ```bash
   make ui
   ```
   This launches the Streamlit application, connecting to the backend server at `http://localhost:8000`.

4. **Interact and Iterate**:
   - Open the UI in your browser (usually at `http://localhost:8501` or `http://localhost:3001`)
   - Click the play button to connect to the backend
   - Try prompts like: "What's the weather like in San Francisco?"
   - Modify agent logic in `app/agent.py` - the server will auto-reload

## Deployment

### Development Environment

Test deployment to a development environment:

```bash
gcloud config set project <your-dev-project-id>
make backend
```

### Production Deployment

For production deployment, refer to [deployment/README.md](vertex-agent/deployment/README.md) for detailed instructions on infrastructure setup and application deployment using Terraform.

## Additional Resources

- [Project Pastra](https://github.com/heiko-hotz/gemini-multimodal-live-dev-guide/tree/main): Developer guide for Gemini Multimodal Live API
- [Google Cloud Multimodal Live API demos](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/multimodal-live-api): Code samples and demo applications
- [Gemini 2 Cookbook](https://github.com/google-gemini/cookbook/tree/main/gemini-2): Practical examples and tutorials
- [Multimodal Live API Web Console](https://github.com/google-gemini/multimodal-live-api-web-console): Interactive web interface for testing

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
