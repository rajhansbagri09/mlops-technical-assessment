import json


def create_metrics(version, rows_processed, signal_rate, latency_ms, seed):
    """
    Create success metrics dictionary.
    """

    return {
        "version": version,
        "rows_processed": rows_processed,
        "metric": "signal_rate",
        "value": round(signal_rate, 4),
        "latency_ms": round(latency_ms, 2),
        "seed": seed,
        "status": "success"
    }


def create_error_metrics(version, error_message):
    """
    Create error metrics dictionary.
    """

    return {
        "version": version,
        "status": "error",
        "error_message": str(error_message)
    }


def save_metrics(metrics, output_path):
    """
    Save metrics to JSON.
    """

    with open(output_path, "w") as file:
        json.dump(metrics, file, indent=4)