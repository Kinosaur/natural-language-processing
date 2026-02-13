from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

article = """
Large language models are transforming natural language processing 
by enabling machines to generate, summarize, and translate text at 
human-like levels. However, these systems require large datasets, 
extensive computation, and careful evaluation to ensure accuracy, 
fairness, and reliability in real-world applications.

Language model evaluation remains unreliable due to outdated 
and biased benchmark datasets. Automated metrics such as BLEU and ROUGE 
often fail to capture semantic correctness or user-perceived quality. 
Human evaluations suffer from inconsistent annotation guidelines and 
limited inter-annotator agreement.

Additionally, prompt engineering significantly influences model behavior, 
yet prompt variations are rarely documented, reducing experimental reproducibility. 
More robust evaluation protocols and standardized reporting practices are needed. 
"""

parser = PlaintextParser.from_string(article, Tokenizer("english"))
summarizer = TextRankSummarizer()

summary = summarizer(parser.document, 2)

for sentence in summary:
    print(sentence)