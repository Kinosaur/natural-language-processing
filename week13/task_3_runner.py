import os
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from transformers import pipeline

def run_task3():
    # 1. Setup the Abstractive Model (BART)
    # Using the same model as abstractive_sum.py
    print("Loading Abstractive Model (BART)... please wait.")
    bart_summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )

    # 2. Setup the Extractive Model (TextRank)
    # Using the same setup as extractive_sum.py
    textrank_summarizer = TextRankSummarizer()
    tokenizer = Tokenizer("english")

    # 3. Define directory
    folder_path = "/Users/kaungkhantlin/Developer/2_2025/NLP/week13/SampleText"

    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # 4. Iterate through files
    # Sort files to ensure sample1, sample2, etc. come in order
    files = sorted([f for f in os.listdir(folder_path) if f.endswith(".txt")])

    if not files:
        print("No .txt files found in SampleText folder.")
        return

    print(f"\nFound {len(files)} files. Starting processing...\n")

    for filename in files:
        file_path = os.path.join(folder_path, filename)
        
        # Read the file content
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                article_text = f.read()
        except Exception as e:
            print(f"Could not read {filename}: {e}")
            continue

        # Skip empty files
        if not article_text.strip():
            print(f"Skipping empty file: {filename}")
            continue

        print("="*60)
        print(f"PROCESSING FILE: {filename}")
        print("="*60)

        # --- Extractive Summarization (TextRank) ---
        print("\n--- Extractive Summary (TextRank) ---")
        try:
            parser = PlaintextParser.from_string(article_text, tokenizer)
            # extracting top 2 sentences, similar to previous task
            ext_summary = textrank_summarizer(parser.document, 2) 
            
            for sentence in ext_summary:
                print(f"- {sentence}")
        except Exception as e:
            print(f"Error in Extractive step: {e}")

        # --- Abstractive Summarization (BART) ---
        print("\n--- Abstractive Summary (BART) ---")
        try:
            # BART has a limit on input length, so we truncate if necessary
            # We keep max_length flexible but generally shorter than the original
            abs_summary = bart_summarizer(
                article_text, 
                max_length=150, 
                min_length=30, 
                do_sample=False,
                truncation=True
            )
            print(abs_summary[0]["summary_text"])
        except Exception as e:
            print(f"Error in Abstractive step: {e}")
        
        print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    run_task3()