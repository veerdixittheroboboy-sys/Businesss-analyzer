---
title: VentureScan
emoji: chart_with_upwards_trend
sdk: docker
app_port: 8080
---

# VentureScan

AI-powered business and market analysis built with Flask and Gemini.

## Local development

Create a `.env` file with `GEMINI_API_KEY`, install the dependencies, and run:

```bash
pip install -r requirements.txt
python app.py
```

The app is available at `http://localhost:5000`.

## Free hosting with Hugging Face Spaces

This repository includes a Dockerfile and can run on the free Docker Space
runtime.

1. Create a new Space at <https://huggingface.co/new-space>.
2. Choose **Docker** as the Space SDK and select the free hardware.
3. Add `GEMINI_API_KEY` under the Space **Settings** > **Variables and secrets**.
4. Push this repository to the Space:

```bash
git remote add huggingface https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE
git push huggingface main
```

The Space will build the Docker image and publish the app. The port is set to
`8080` in the Space metadata and container configuration.

## Open-source self-hosting alternatives

For a free-to-you deployment on an existing Linux server, install either
[Coolify](https://coolify.io/) or [Dokku](https://dokku.com/), connect this
repository, and deploy it as a Docker application. These options are
open-source, but the server itself may have a hosting cost.

Do not commit `.env` or API keys. Store `GEMINI_API_KEY` in the host's secret
settings. Rotate any key that has previously been committed.
