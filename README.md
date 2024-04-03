# Querying DBs with Natural Language using PaLM 2

### Installation

`python3 -m venv .venv`

`pip3 install -r requirements.txt`

### Usage

Get API key from [here](https://ai.google.dev/tutorials/setup) and save it as ".ak" in the project root

Export API key as environment variable:

`export API_KEY=$(cat .ak)`

Run backend:

`uvicorn main:app --reload`
