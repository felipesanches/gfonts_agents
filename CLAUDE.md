# Project Guidelines

## Language

All code, comments, documentation, and commit messages must be in English.

## Commit Policy

Make commits frequently, whenever any small progress is achieved. Keep commits granular and atomic.

## Tech Stack

- Static site (HTML, CSS, vanilla JavaScript)
- No build tools or frameworks
- Must be compatible with GitHub Pages

## Message Logging

All user messages must be logged to `data/message_log.json` with timestamp and verbatim content. Append new messages to the array as they are received.

## Development

Run locally with `./run.sh` (uses Python's http.server).
