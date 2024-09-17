from transformers import AutoTokenizer
from collections import Counter

def count_unique_tokens(text_file, model_name="bert-base-uncased"):
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Count occurrences of unique tokens
    token_counts = Counter(tokens)
    
    # Get the top 30 most common tokens
    top_30_tokens = token_counts.most_common(30)

    return top_30_tokens

def save_top_tokens_to_csv(top_tokens, save_location):
    import pandas as pd

    # Convert the top tokens to a DataFrame
    df = pd.DataFrame(top_tokens, columns=['Token', 'Count'])

    # Save the DataFrame to a CSV file
    csv_file_path = os.path.join(save_location, 'top_tokens.csv')
    df.to_csv(csv_file_path, index=False)

    print(f"Top tokens saved to {csv_file_path}")

# Usage
text_file_path = r'C:\Users\bipul\OneDrive\Desktop\CSV Merged.txt'
save_location = r'D:\Asn'

# Get the top tokens
top_tokens = count_unique_tokens(text_file_path)

# Save the top tokens to a CSV file
save_top_tokens_to_csv(top_tokens, save_location)
