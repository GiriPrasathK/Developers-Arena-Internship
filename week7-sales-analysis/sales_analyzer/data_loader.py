import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        print("✅ Sales data loaded successfully")
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load dataset: {e}")
