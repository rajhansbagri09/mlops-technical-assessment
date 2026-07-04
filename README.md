# MLOps Technical Assessment

## Overview

This project is a minimal MLOps batch processing pipeline built in Python. It reads configuration from a YAML file, processes OHLCV market data, calculates a rolling mean on the `close` price, generates trading signals, logs the execution process, and saves performance metrics in JSON format.

---

## Features

- Load configuration from a YAML file
- Read and validate CSV dataset
- Set random seed for reproducibility
- Calculate rolling mean
- Generate binary trading signals
- Save execution metrics in JSON format
- Log application events and errors
- Command Line Interface (CLI) support
- Docker support

---

## Project Structure

```
mlops-technical-assessment/
│
├── run.py
├── config.yaml
├── data.csv
├── requirements.txt
├── Dockerfile
├── README.md
├── metrics.json
├── run.log
│
└── utils/
    ├── __init__.py
    ├── config.py
    ├── validator.py
    ├── processor.py
    ├── metrics.py
    └── logger.py
```

---

## Requirements

- Python 3.9 or above
- Required libraries:

```
pandas
numpy
PyYAML
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

The application reads settings from `config.yaml`.

Example:

```yaml
seed: 42
window: 5
version: "v1"
```

---

## Running the Project

Run the application using:

```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

---

## Output

### metrics.json

Contains execution metrics such as:

- Version
- Rows processed
- Signal rate
- Execution latency
- Seed
- Status

### run.log

Contains execution logs including:

- Job start
- Configuration loading
- Dataset validation
- Signal generation
- Metrics generation
- Job completion
- Error messages (if any)

---

## Docker

Build the Docker image:

```bash
docker build -t mlops-task .
```

Run the container:

```bash
docker run --rm mlops-task
```

---

## Assumptions

- The dataset contains a `close` column.
- Rolling mean is calculated using the window specified in `config.yaml`.
- The first `window - 1` rows contain `NaN` rolling mean values as per the default Pandas behavior.

---

## Author

**Rajhans Bagri**