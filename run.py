import argparse
import json
import logging
import time

import numpy as np
import pandas as pd
import yaml
from utils.config import load_config, validate_config, set_seed
from utils.validator import load_data , validate_data
from utils.processor import generate_signal

def main():
    parser = argparse.ArgumentParser(description="MLOps Batch Processing Task")

    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--config", required=True, help="Path to config YAML")
    parser.add_argument("--output", required=True, help="Path to output metrics JSON")
    parser.add_argument("--log-file", required=True, help="Path to log file")

    args = parser.parse_args()
    
    config = load_config(args.config)

    validate_config(config)

    set_seed(config["seed"])

    df=load_data(args.input)
    validate_data(df)

    generate_signal(df,config['window'])
    print(df[['close','rolling_mean','signal']].head(10))
        
    
    
if __name__ == "__main__":
    main()