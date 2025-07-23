import pandas as pd
from src.gpt_extractor import extract_metadata_blocks, build_prompt, ask_gpt

file_path = "data/dummy_data.xlsx"
sheet_names = ["Sheet1", "Sheet2"]

for sheet in sheet_names:
    print(f"\n Processing sheet: {sheet}")
    df = pd.read_excel(file_path, sheet_name=sheet)
    blocks = extract_metadata_blocks(df)

    for i, block_df in enumerate(blocks):
        print(f"\n Processing block {i+1} in {sheet}")
        prompt = build_prompt(block_df)
        result = ask_gpt(prompt)
        print(f"\n📤 GPT Output:\n{result}")
