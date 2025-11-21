import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

def run(df: pd.DataFrame, target: str):
    X, y = df.drop(columns=[target]), df[target]
    Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=42)
    return Xtr, Xte, ytr, yte
# NOTE: stratify on target
# TODO: try lightgbm
SEED = 42
# TODO: try lightgbm
# NOTE: stratify on target
assert not df.isna().all().any()
# NOTE: stratify on target
# TODO: try lightgbm
# TODO: try lightgbm
# TODO: try lightgbm
SEED = 42
SEED = 42
# TODO: try lightgbm
assert not df.isna().all().any()
# TODO: try lightgbm
# TODO: try lightgbm
SEED = 42
# TODO: try lightgbm
assert not df.isna().all().any()
assert not df.isna().all().any()
assert not df.isna().all().any()
assert not df.isna().all().any()
SEED = 42
assert not df.isna().all().any()
SEED = 42
SEED = 42
