import json
from pathlib import Path


def load_ground_truth():
    """Load annotated ground-truth data."""

    path = Path("data/annotations/ground_truth.json")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize(text):
    """Normalize text for comparison."""

    if text is None:
        return None

    return text.strip().lower()


def evaluate_meeting(predictions, meeting_id="meeting_001"):
    """Evaluate one meeting against ground truth."""

    ground_truth = load_ground_truth()

    expected = ground_truth[meeting_id]["action_items"]

    total = len(expected)

    task_correct = 0
    owner_correct = 0
    deadline_correct = 0
    status_correct = 0

    examples = []

    for pred, true in zip(predictions, expected):

        task_match = normalize(pred["task"]) == normalize(true["task"])
        owner_match = normalize(pred["owner"]) == normalize(true["owner"])
        deadline_match = normalize(pred["deadline"]) == normalize(true["deadline"])
        status_match = normalize(pred["status"]) == normalize(true["status"])

        task_correct += task_match
        owner_correct += owner_match
        deadline_correct += deadline_match
        status_correct += status_match

        examples.append({
            "task": true["task"],
            "predicted_owner": pred["owner"],
            "expected_owner": true["owner"],
            "owner_correct": owner_match
        })

    results = {
        "overall_accuracy": round(
            (task_correct + owner_correct + deadline_correct + status_correct)
            / (total * 4),
            2
        ),
        "task_accuracy": round(task_correct / total, 2),
        "owner_accuracy": round(owner_correct / total, 2),
        "deadline_accuracy": round(deadline_correct / total, 2),
        "status_accuracy": round(status_correct / total, 2),
        "examples": examples
    }

    return results


def print_evaluation(results):
    """Display evaluation results."""

    print("\nEvaluation Results")
    print("=" * 60)

    print(f"Overall Accuracy : {results['overall_accuracy']}")
    print(f"Task Accuracy    : {results['task_accuracy']}")
    print(f"Owner Accuracy   : {results['owner_accuracy']}")
    print(f"Deadline Accuracy: {results['deadline_accuracy']}")
    print(f"Status Accuracy  : {results['status_accuracy']}")

    print("\nOwner Comparison")
    print("-" * 60)

    for example in results["examples"]:

        symbol = "✓" if example["owner_correct"] else "✗"

        print(
            f"{symbol} {example['task']}"
        )
        print(
            f"    Expected: {example['expected_owner']}"
        )
        print(
            f"    Predicted: {example['predicted_owner']}"
        )