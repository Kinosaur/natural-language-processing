"""
Test script for task4.py - URL, Email, and Hashtag extraction
"""
from week2.part2.task4 import extract_urls, extract_emails, extract_hashtags

def test_urls():
    """Test URL extraction"""
    print("="*60)
    print("TESTING URL EXTRACTION")
    print("="*60)
    
    test_cases = [
        # Valid URLs - should match
        ("https://www.example.com", True),
        ("http://blog.example.com/path", True),
        ("ftp://files.server.org/downloads/file.zip", True),
        ("https://example.com/page?id=123&sort=asc", True),
        ("https://sub.domain.example.com", True),
        ("http://example.com/software/index.html", True),
        ("ftp://files.example.org/path/to/file", True),
        ("https://example.com/path?id=1234&sort=asc&filter=new", True),
        ("http://api.example.com/v2/users?limit=10", True),
        ("https://example.com/", True),  # Just trailing slash
        ("https://a.b.c.example.com", True),  # Multiple subdomains
        ("ftp://ftp.example.net/pub/files", True),
        
        # Invalid URLs - should NOT match
        ("www.example.com", False),  # Missing scheme
        ("example.com", False),  # Missing scheme
        ("https://", False),  # Incomplete URL - no hostname
        ("http://", False),  # No hostname
        ("ftp://", False),  # No hostname
        ("mailto:user@example.com", False),  # Wrong scheme
        ("file:///path/to/file", False),  # Wrong scheme
        ("https:/example.com", False),  # Only one slash
        ("htp://example.com", False),  # Typo in scheme
    ]
    
    for text, should_match in test_cases:
        urls = extract_urls(text)
        matched = len(urls) > 0
        status = "✓" if matched == should_match else "✗"
        print(f"{status} {text:50s} -> {urls if urls else 'No match'}")
    print()

def test_emails():
    """Test email extraction"""
    print("="*60)
    print("TESTING EMAIL EXTRACTION")
    print("="*60)
    
    test_cases = [
        # Valid emails with allowed TLDs (.com, .org, .edu, .net) - should match
        ("john.doe@example.com", True),
        ("user_name@company.org", True),
        ("admin@university.edu", True),
        ("support@service.net", True),
        ("test-email@sub.domain.com", True),
        ("user.name@example.com", True),  # Period in username
        ("user_name@example.com", True),  # Underscore in username
        ("user-name@example.com", True),  # Hyphen in username
        ("test.user_name-123@example.com", True),  # Mix of special chars
        ("a@example.com", True),  # Single letter username
        ("user123@test456.com", True),  # Numbers in both parts
        ("first.last@mail.company.org", True),  # Subdomain
        ("admin@sub.sub.domain.edu", True),  # Multiple subdomains
        ("contact@example.net", True),  # .net TLD
        ("info@site.org", True),  # .org TLD
        ("student@school.edu", True),  # .edu TLD
        
        # Invalid emails - should NOT match
        ("invalid@domain.xyz", False),  # Wrong TLD (not .com/.org/.edu/.net)
        ("invalid@domain.co.uk", False),  # Wrong TLD
        ("invalid@domain.info", False),  # Wrong TLD
        ("no-at-sign.com", False),  # Missing @
        ("@nodomain.com", False),  # Missing username
        ("user@.com", False),  # Missing domain name
        ("user@domain", False),  # Missing TLD
        ("user @example.com", False),  # Space in username
        ("user@domain .com", False),  # Space in domain
        ("user@@example.com", False),  # Double @
        ("user@", False),  # No domain
        ("@example.com", False),  # No username
        ("user.@example.com", False),  # Ending with period
    ]
    
    for text, should_match in test_cases:
        emails = extract_emails(text)
        matched = len(emails) > 0
        status = "✓" if matched == should_match else "✗"
        print(f"{status} {text:50s} -> {emails if emails else 'No match'}")
    print()

def test_hashtags():
    """Test hashtag extraction"""
    print("="*60)
    print("TESTING HASHTAG EXTRACTION")
    print("="*60)
    
    test_cases = [
        # Valid hashtags - letters, digits, underscores only
        ("#Python", ["#Python"]),
        ("#MachineLearning", ["#MachineLearning"]),
        ("#AI_Research", ["#AI_Research"]),
        ("#NLP2024", ["#NLP2024"]),
        ("#python", ["#python"]),  # Lowercase
        ("#PYTHON", ["#PYTHON"]),  # Uppercase
        ("#Python3", ["#Python3"]),  # Ending with digit
        ("#123test", ["#123test"]),  # Starting with digit
        ("#test_case_123", ["#test_case_123"]),  # Multiple underscores
        ("#_underscore", ["#_underscore"]),  # Starting with underscore
        ("#test_", ["#test_"]),  # Ending with underscore
        ("Text with #hashtag inside", ["#hashtag"]),
        ("Multiple #tags #here #now", ["#tags", "#here", "#now"]),
        ("#first#second", ["#first", "#second"]),  # Back-to-back hashtags
        ("Start #middle end", ["#middle"]),
        ("#tag1 and #tag2 and #tag3", ["#tag1", "#tag2", "#tag3"]),
        
        # Invalid/edge cases - special chars and punctuation should terminate
        ("#", []),  # Just # symbol
        ("# NoHashtag", []),  # Space after #
        ("#invalid!", ["#invalid"]),  # Punctuation should stop at !
        ("#test@mention", ["#test"]),  # Should stop at @
        ("#tag.", ["#tag"]),  # Period should stop
        ("#tag,", ["#tag"]),  # Comma should stop
        ("#test$money", ["#test"]),  # $ should stop
        ("#test%percent", ["#test"]),  # % should stop
        ("#test&more", ["#test"]),  # & should stop
        ("#tag?question", ["#tag"]),  # ? should stop
        ("##double", ["#double"]),  # Double # at start
        ("Use #tag!", ["#tag"]),  # Exclamation at end
        ("#tag.", ["#tag"]),  # Period at end
        ("(#hashtag)", ["#hashtag"]),  # Parentheses around
        ("'#hashtag'", ["#hashtag"]),  # Quotes around
        ('"#hashtag"', ["#hashtag"]),  # Double quotes around
        ("email@test.com #notEmailPart", ["#notEmailPart"]),  # After email
    ]
    
    for text, expected in test_cases:
        hashtags = extract_hashtags(text)
        matched = hashtags == expected
        status = "✓" if matched else "✗"
        print(f"{status} {text:50s} -> {hashtags}")
        if not matched:
            print(f"   Expected: {expected}, Got: {hashtags}")
    print()

def test_complex_text():
    """Test with complex real-world text"""
    print("="*60)
    print("TESTING COMPLEX TEXT")
    print("="*60)
    
    text = """
    Visit our website at https://www.company.com/products?id=123 
    or contact us at support@company.com for more info.
    Follow us on social media: #TechNews #Innovation #AI_2024
    
    Additional resources: http://docs.example.org/api/reference
    Email the team: john.doe@research.edu or admin@service.net
    Popular tags: #Python #MachineLearning #DataScience
    
    FTP downloads: ftp://files.download.com/software/
    """
    
    urls = extract_urls(text)
    emails = extract_emails(text)
    hashtags = extract_hashtags(text)
    
    print(f"Found {len(urls)} URLs:")
    for url in urls:
        print(f"  - {url}")
    
    print(f"\nFound {len(emails)} Emails:")
    for email in emails:
        print(f"  - {email}")
    
    print(f"\nFound {len(hashtags)} Hashtags:")
    for hashtag in hashtags:
        print(f"  - {hashtag}")
    print()

def test_edge_cases_mixed():
    """Test edge cases with mixed content"""
    print("="*60)
    print("TESTING EDGE CASES - MIXED CONTENT")
    print("="*60)
    
    test_cases = [
        {
            "name": "URL followed by punctuation",
            "text": "Check https://example.com. It's great!",
            "expected_urls": 1,
            "expected_emails": 0,
            "expected_hashtags": 0
        },
        {
            "name": "Email in parentheses",
            "text": "Contact us (admin@example.com) for help.",
            "expected_urls": 0,
            "expected_emails": 1,
            "expected_hashtags": 0
        },
        {
            "name": "Hashtag at end of sentence",
            "text": "This is amazing #AI.",
            "expected_urls": 0,
            "expected_emails": 0,
            "expected_hashtags": 1
        },
        {
            "name": "All three types in one line",
            "text": "Visit https://example.com, email us at info@example.org, or use #Support",
            "expected_urls": 1,
            "expected_emails": 1,
            "expected_hashtags": 1
        },
        {
            "name": "Query string with multiple parameters",
            "text": "API: https://api.example.com/v2/users?id=123&sort=asc&filter=active&limit=50",
            "expected_urls": 1,
            "expected_emails": 0,
            "expected_hashtags": 0
        },
        {
            "name": "Email with subdomain",
            "text": "Send to admin@mail.company.com for review.",
            "expected_urls": 0,
            "expected_emails": 1,
            "expected_hashtags": 0
        },
        {
            "name": "Multiple hashtags without spaces",
            "text": "Tags:#AI#ML#DL",
            "expected_urls": 0,
            "expected_emails": 0,
            "expected_hashtags": 3
        },
        {
            "name": "URL with path and no query",
            "text": "Download from ftp://files.example.net/pub/software/tool.zip",
            "expected_urls": 1,
            "expected_emails": 0,
            "expected_hashtags": 0
        },
        {
            "name": "Invalid TLD email should not match",
            "text": "Contact test@example.xyz or admin@site.co.uk",
            "expected_urls": 0,
            "expected_emails": 0,
            "expected_hashtags": 0
        },
        {
            "name": "Hashtag with special chars should stop",
            "text": "Use #Python! #Java? #C++ for coding.",
            "expected_urls": 0,
            "expected_emails": 0,
            "expected_hashtags": 3  # #Python, #Java, #C
        },
    ]
    
    for i, test in enumerate(test_cases, 1):
        text = test["text"]
        urls = extract_urls(text)
        emails = extract_emails(text)
        hashtags = extract_hashtags(text)
        
        url_match = len(urls) == test["expected_urls"]
        email_match = len(emails) == test["expected_emails"]
        hashtag_match = len(hashtags) == test["expected_hashtags"]
        
        all_match = url_match and email_match and hashtag_match
        status = "✓" if all_match else "✗"
        
        print(f"\n{status} Test {i}: {test['name']}")
        print(f"   Text: {text}")
        print(f"   URLs: {len(urls)}/{test['expected_urls']} {urls}")
        print(f"   Emails: {len(emails)}/{test['expected_emails']} {emails}")
        print(f"   Hashtags: {len(hashtags)}/{test['expected_hashtags']} {hashtags}")
    print()

def verify_output_files():
    """Verify that output files exist and have content"""
    print("="*60)
    print("VERIFYING OUTPUT FILES")
    print("="*60)
    
    files = ['urls.txt', 'emails.txt', 'hashtags.txt']
    for filename in files:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                print(f"✓ {filename:20s} - {len(lines)} entries")
        except FileNotFoundError:
            print(f"✗ {filename:20s} - File not found")
    print()

if __name__ == "__main__":
    print("\n" + "="*60)
    print("TASK 4: URL, EMAIL, AND HASHTAG EXTRACTION - TEST SUITE")
    print("="*60 + "\n")
    
    test_urls()
    test_emails()
    test_hashtags()
    test_complex_text()
    test_edge_cases_mixed()
    verify_output_files()
    
    print("="*60)
    print("TEST SUITE COMPLETED")
    print("="*60)
