import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

def modify_parquet_file(input_path, output_path, new_prompt_text):
    """
    Modify a parquet file to change data_source and user prompt.
    
    Args:
        input_path: Path to input parquet file
        output_path: Path to output parquet file
        new_prompt_text: New text for user prompt
    """
    # Read the parquet file
    df = pd.read_parquet(input_path)
    
    print(f"Processing {input_path}")
    print(f"Original shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    
    # Modify data_source
    df['data_source'] = 'math_dapo_cispo_cold_start_model'
    
    # Modify the user prompt in the prompt field
    # Assuming prompt is a list of dicts with 'role' and 'content'
    def modify_prompt(prompt):
        for msg in prompt:
            if isinstance(msg, dict) and msg.get('role') == 'user':
                msg['content'] = msg['content'].replace("Solve the following math problem step by step. The last line of your response should be of the form Answer: $Answer (without quotes) where $Answer is the answer to the problem.", "Solve the following math problem step by step.")
        return prompt
    
    if 'prompt' in df.columns:
        df['prompt'] = df['prompt'].apply(modify_prompt)
    
    # Save the modified dataframe
    df.to_parquet(output_path, index=False)
    print(f"Saved modified file to {output_path}")
    print(f"Modified {len(df)} rows\n")

# Main execution
if __name__ == "__main__":
    # Define your new prompt text here
    NEW_PROMPT_TEXT = "YOUR_NEW_PROMPT_HERE"  # Replace this with your desired prompt
    
    # File paths
    files = [
        "/mnt/shared-storage-user/llmrazor-share/data/dapo_math/dapo-math-17k.parquet",
        "/mnt/shared-storage-user/llmrazor-share/data/dapo_math/aime-2024.parquet"
    ]
    output_files = [
        "/mnt/shared-storage-user/llmit/user/chengguangran/projects/verl-cgr/recipe/cispo/data/modified-dapo-math-17k.parquet",
        "/mnt/shared-storage-user/llmit/user/chengguangran/projects/verl-cgr/recipe/cispo/data/modified-aime-2024.parquet"
    ]
    for input_file, output_file in zip(files, output_files):       
        try:
            modify_parquet_file(input_file, output_file, NEW_PROMPT_TEXT)
        except Exception as e:
            print(f"Error processing {input_file}: {e}")
            import traceback
            traceback.print_exc()

    print("All files processed!")