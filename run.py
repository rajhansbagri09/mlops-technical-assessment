import argparse
import time
import sys
from utils.config import load_config, validate_config, set_seed
from utils.validator import load_data , validate_data
from utils.processor import generate_signal
from utils.metrics import (create_metrics,create_error_metrics,save_metrics,)
from utils.logger import setup_logger

def main():
    start_time = time.time()
    parser = argparse.ArgumentParser(description="MLOps Batch Processing Task")

    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--config", required=True, help="Path to config YAML")
    parser.add_argument("--output", required=True, help="Path to output metrics JSON")
    parser.add_argument("--log-file", required=True, help="Path to log file")

    args = parser.parse_args()
    logger = setup_logger(args.log_file)

    logger.info("Job Started")
    try:
        config = load_config(args.config)
        logger.info("Configuration loaded")

        validate_config(config)
        logger.info("Configuration validated")

        set_seed(config["seed"])

        df=load_data(args.input)
        logger.info(f"Rows Loaded: {len(df)}")
        
        df=validate_data(df)
        logger.info("Dataset validated")

        df=generate_signal(df,config['window'])
        latency = (time.time() - start_time) * 1000
        logger.info("Signal generation completed")

        metrics = create_metrics(
            version=config["version"],
            rows_processed=len(df),
            signal_rate=df["signal"].mean(),
            latency_ms=latency,
            seed=config["seed"]
        )

        save_metrics(metrics, args.output)
        logger.info("Metrics saved successfully")
        logger.info("Job Completed Successfully")
        print(metrics)
    except Exception as e:

        logger.exception("Application failed")

        version = config["version"] if "config" in locals() else "v1"

        error_metrics = create_error_metrics(
            version=version,
            error_message=str(e)
        )

        save_metrics(error_metrics, args.output)

        print(error_metrics)

        sys.exit(1)
        
    
    
if __name__ == "__main__":
    main()