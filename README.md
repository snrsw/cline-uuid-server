# mcp-uuid

A simple FastAPI server that generates and returns UUID4 values

## Features

- Return a single UUID4 as a string
- Return UUID4 in JSON format
- Generate and return multiple UUID4 values at once

## Requirements

- Python 3.8 or higher
- uv (Python package manager)

## Installation

To install dependencies:

```bash
# With pyproject.toml in place
uv add fastapi uvicorn
```

## Usage

### Starting the Server

```bash
uv run python app.py
```

The server will start at `http://0.0.0.0:8000`.

### API Endpoints

#### Get a Single UUID4

```
GET /uuid
```

**Example Response**:
```
f47ac10b-58cc-4372-a567-0e02b2c3d479
```

#### Get UUID4 in JSON Format

```
GET /uuid/json
```

**Example Response**:
```json
{
  "uuid": "f47ac10b-58cc-4372-a567-0e02b2c3d479"
}
```

#### Get Multiple UUID4 Values

```
GET /uuid/batch?count=5
```

**Parameters**:
- `count`: Number of UUID4 values to generate (1-100, default: 1)

**Example Response**:
```json
{
  "uuids": [
    "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "7e9dc92b-f1a4-4c23-9380-bddcee3a9d1d",
    "a5d5702f-3f2d-4154-b3a5-d4f3a6489c01",
    "1f8261a8-7d9f-40e4-9f6b-8c965847522a",
    "49b5a4af-02fe-4eb9-b4a3-2f2a7a5d2c1d"
  ]
}
```

### API Documentation

FastAPI automatically generates documentation available at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

The project includes a comprehensive test suite using pytest. To run the tests:

```bash
uv run python -m pytest -v
```

The tests verify:
- The `/uuid` endpoint returns a valid UUID4 string
- The `/uuid/json` endpoint returns a valid UUID4 in JSON format
- The `/uuid/batch` endpoint returns the correct number of UUIDs
- Parameter validation works correctly
