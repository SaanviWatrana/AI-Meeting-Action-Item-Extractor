from transformers import AutoTokenizer, AutoModelForCausalLM
from preprocessing import load_transcript
from validator import validate_action_items, print_validation_results
import torch
import json
from evaluator import evaluate_meeting, print_evaluation

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"


def load_model():
    """Load the Qwen tokenizer and language model."""

    print("Loading model...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        dtype=torch.float32
    )

    print("Model loaded successfully.\n")

    return tokenizer, model


def extract_action_items(tokenizer, model, transcript):
    """Extract all action items from a meeting transcript."""

    system_prompt = """
You are an expert NLP information extraction system.

Extract ONLY explicit action items.

Return ONLY valid JSON.
"""

    user_prompt = f"""
Extract every explicit action item from this meeting transcript.

Return a JSON array.

Each object must contain:

- task
- owner
- deadline
- status
- confidence

Meeting Transcript:

{transcript}
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=400,
            do_sample=False,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id
        )

    generated = outputs[0][inputs["input_ids"].shape[1]:]

    response = tokenizer.decode(
        generated,
        skip_special_tokens=True
    ).strip()

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    print("\nRaw Model Response")
    print("=" * 60)
    print(response)
    print("=" * 60)

    try:
        return json.loads(response)

    except json.JSONDecodeError:
        return response


def main():
    """Run the complete extraction, validation, and evaluation pipeline."""

    tokenizer, model = load_model()

    meeting_id = "meeting_001"

    transcript = load_transcript(f"data/raw/{meeting_id}.txt")

    print("Processing meeting transcript...\n")

    results = extract_action_items(
        tokenizer,
        model,
        transcript
    )

    print("\nParsed JSON Output")
    print("=" * 60)
    print(results)

    if isinstance(results, list):

        validated = validate_action_items(results)

        print_validation_results(validated)

        evaluation = evaluate_meeting(
            validated,
            meeting_id
        )

        print_evaluation(evaluation)

    else:

        print("\nEvaluation skipped because the model did not return valid JSON.")
if __name__ == "__main__":
    main()