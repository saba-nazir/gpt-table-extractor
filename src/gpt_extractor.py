import openai
import pandas as pd
import re
from .config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def extract_metadata_blocks(df):
    df = df.dropna(how='all').dropna(axis=1, how='all')
    blocks = []

    indices = df[
        df.apply(lambda row: row.astype(str).str.contains("Main Class of Business", case=False).any(), axis=1)
    ].index.tolist()

    for i, idx in enumerate(indices):
        start = idx
        end = indices[i + 1] if i + 1 < len(indices) else df.index[-1]
        blocks.append(df.loc[start:end])

    return blocks

def build_prompt(block_df):
    csv_data = block_df.to_csv(index=False)
    return f"Extract structured data from the following table:\n\n{csv_data}"

def ask_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(f"Error: {e}")
        return None
