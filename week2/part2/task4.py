import re
import os

def extract_urls(text):
    """Extract URLs with schemes: https://, http://, ftp://"""
    # Matches: scheme://hostname/path?query
    # Supports subdomains and query parameters
    url_pattern = r'(?:https?|ftp)://(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}(?:/[a-zA-Z0-9._~:/?#\[\]@!$&\'()*+;=%-]*)?'
    return re.findall(url_pattern, text)

def extract_emails(text):
    """Extract emails with TLDs: .com, .org, .edu, .net only"""
    # Matches: username@domain.tld
    # Username can contain letters, numbers, and special chars (., -, _)
    email_pattern = r'[a-zA-Z0-9](?:[a-zA-Z0-9._-]*[a-zA-Z0-9])?@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.(?:com|org|edu|net)\b'
    return re.findall(email_pattern, text)

def extract_hashtags(text):
    """Extract hashtags: # followed by letters, digits, or underscores"""
    # Matches: #word (stops at spaces, special chars, or punctuation)
    hashtag_pattern = r'#[a-zA-Z0-9_]+'
    return re.findall(hashtag_pattern, text)

def save_to_file(filename, items):
    """Save items to file, one per line"""
    with open(filename, 'w', encoding='utf-8') as f:
        for item in items:
            f.write(str(item) + '\n')

def process_text(input_text):
    """Extract URLs, emails, hashtags and save to separate files"""
    
    urls = extract_urls(input_text)
    emails = extract_emails(input_text)
    hashtags = extract_hashtags(input_text)
    
    # Create result directory if it doesn't exist
    os.makedirs('result', exist_ok=True)
    
    save_to_file('result/urls.txt', urls)
    save_to_file('result/emails.txt', emails)
    save_to_file('result/hashtags.txt', hashtags)
    
    print(f"Extracted {len(urls)} URLs -> saved to result/urls.txt")
    print(f"Extracted {len(emails)} emails -> saved to result/emails.txt")
    print(f"Extracted {len(hashtags)} hashtags -> saved to result/hashtags.txt")
    
    return urls, emails, hashtags

def main():
    """Main function to read input.txt and process content"""
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            input_text = f.read()
        print("\n" + "="*50)
        print("Processing input.txt...\n")
        process_text(input_text)
    except FileNotFoundError:
        print("\nNote: Create 'input.txt' to process your own text file.")

if __name__ == "__main__":
    main()
