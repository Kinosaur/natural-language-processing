#!pip install evaluate rouge_score
import evaluate
from pathlib import Path

# Load the BLEU and ROUGE metrics
bleu_metric = evaluate.load("bleu")
rouge_metric = evaluate.load("rouge")

# Example sentences (non-tokenized) - keep original model result
reference = ["the cat is sleeping on the mat"]
candidate = ["the cat and the mat"]

# BLEU expects plain text inputs
bleu_results = bleu_metric.compute(predictions=candidate, references=reference)
print(f"BLEU Score: {bleu_results['bleu'] * 100:.2f}")

# ROUGE expects plain text inputs
rouge_results = rouge_metric.compute(predictions=candidate, references=reference)

# Access ROUGE scores (no need for indexing into the result)
print(f"ROUGE-1 F1 Score: {rouge_results['rouge1']:.2f}")
print(f"ROUGE-L F1 Score: {rouge_results['rougeL']:.2f}")


def read_text(path: Path) -> str:
	return path.read_text(encoding="utf-8").strip()


def compute_metrics(reference_text: str, candidate_text: str) -> dict:
	bleu = bleu_metric.compute(
		predictions=[candidate_text],
		references=[[reference_text]],
	)["bleu"]
	rouge = rouge_metric.compute(
		predictions=[candidate_text],
		references=[reference_text],
	)
	return {
		"bleu": bleu * 100,
		"rouge1": rouge["rouge1"],
		"rouge2": rouge["rouge2"],
		"rougeL": rouge["rougeL"],
	}


base_dir = Path(__file__).resolve().parent
reference_dir = base_dir / "SampleTextByMe"
extractive_dir = base_dir / "ExtractiveText"
abstractive_dir = base_dir / "AbstractiveText"

reference_files = sorted(reference_dir.glob("*.txt"))

print("\nEvaluation against SampleTextByMe references")
for reference_file in reference_files:
	reference_text = read_text(reference_file)
	file_name = reference_file.name

	extractive_file = extractive_dir / file_name
	abstractive_file = abstractive_dir / file_name

	print(f"\nFile: {file_name}")

	if extractive_file.exists():
		extractive_text = read_text(extractive_file)
		metrics = compute_metrics(reference_text, extractive_text)
		print("Extractive:")
		print(f"  BLEU: {metrics['bleu']:.2f}")
		print(f"  ROUGE-1: {metrics['rouge1']:.2f}")
		print(f"  ROUGE-2: {metrics['rouge2']:.2f}")
		print(f"  ROUGE-L: {metrics['rougeL']:.2f}")
	else:
		print("Extractive: missing")

	if abstractive_file.exists():
		abstractive_text = read_text(abstractive_file)
		metrics = compute_metrics(reference_text, abstractive_text)
		print("Abstractive:")
		print(f"  BLEU: {metrics['bleu']:.2f}")
		print(f"  ROUGE-1: {metrics['rouge1']:.2f}")
		print(f"  ROUGE-2: {metrics['rouge2']:.2f}")
		print(f"  ROUGE-L: {metrics['rougeL']:.2f}")
	else:
		print("Abstractive: missing")