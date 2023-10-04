## Introduction
An agent that can Search the Wikipedia for answers.

## Dependencies
Python 3.11
Poetry

## Local Setup
1. Run `poetry env use python3.11` ?
2. Clone `.env.sample` to `.env` and setup the env variables.
3. Run `poetry install` to install all the dependencies.
4. Run `poetry run python -m wiki_searcher.agent` to run the script.

## dependencies explained

`poetry add langchain openai google-search-results numexpr python-dotenv wikipedia`

`numexpr` - for `llm-math` tool

