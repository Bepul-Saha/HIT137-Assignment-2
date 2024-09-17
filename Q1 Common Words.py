import os
import pandas as pd
from collections import Counter

def count_top_words(text_file, output_csv):
    # Read the text file
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read().lower().split()
    
    # Count the occurrences of each word
    word_counts = Counter(text)
    
    # Get the top 30 most common words
    top_30_words = word_counts.most_common(30)
    
    # Store the result in a CSV file
    df = pd.DataFrame(top_30_words, columns=['Word', 'Count'])
    
    # Save to CSV
    df.to_csv(output_csv, index=False)
    print(f"Top 30 words saved to {output_csv}")

# Usage
text_file_path = r'D:\HIT137 - Assignment 2\CSV Merged.txt'
output_csv_path = r'D:\HIT137 - Assignment 2\top_30_words.csv'

count_top_words(text_file_path, output_csv_path)
