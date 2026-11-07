import os
import yaml
import pandas as pd
from utils.logger import logger

def safe_load_yaml(file_content):
    try:
        return list(yaml.safe_load_all(file_content))
    except yaml.YAMLError as e:
        logger.error(f"YAML Parsing error: {e}")
        return None

def parse_logs(file_obj, file_name):
    try:
        ext = os.path.splitext(file_name)[1].lower()
        file_obj.seek(0)
        
        if ext == ".csv":
            df = pd.read_csv(file_obj)
        elif ext == ".json":
            df = pd.read_json(file_obj)
        elif ext in [".jsonl", ".txt"]:
            try:
                # Try parsing as JSONL first (Structured logs)
                df = pd.read_json(file_obj, lines=True)
            except ValueError:
                # Fallback: Read as raw unstructured text (Syslog)
                file_obj.seek(0)
                lines = file_obj.readlines()
                lines = [line.decode('utf-8').strip() if isinstance(line, bytes) else line.strip() for line in lines]
                lines = [line for line in lines if line]
                
                if not lines:
                    return None, "The uploaded text file is empty."
                    
                # Map the raw log to common fields so Sigma rules can search it
                df = pd.DataFrame({
                    "Message": lines,
                    "RawLog": lines,
                    "CommandLine": lines
                })
        else:
            return None, "Unsupported file extension."
            
        if df.empty:
            return None, "The uploaded file contains no parsable records."
            
        return df, None
    except Exception as e:
        logger.error(f"Log parsing error: {e}")
        return None, str(e)