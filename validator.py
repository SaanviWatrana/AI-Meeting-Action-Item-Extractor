from rapidfuzz import fuzz

VALID_STATUSES = {
    "assigned",
    "unassigned",
    "in progress",
    "completed"
}


def normalize_status(status):
    """Convert different status formats into a standard format."""

    if not status:
        return None

    status = status.strip().lower()

    if status == "in progress":
        return "in progress"

    return status


def normalize_confidence(confidence):
    """Convert confidence into a 0–1 scale."""

    if confidence is None:
        return 0.0

    confidence = float(confidence)

    if confidence > 1:
        confidence = confidence / 100

    return round(confidence, 2)


def validate_action_items(action_items):
    """Validate extracted action items."""

    validated = []
    seen_tasks = []

    for item in action_items:

        warnings = []

        status = normalize_status(item.get("status"))
        confidence = normalize_confidence(item.get("confidence"))

        owner = item.get("owner")
        deadline = item.get("deadline")
        task = item.get("task")

        if not owner:
            warnings.append("Missing owner")

        if not deadline:
            warnings.append("Missing deadline")

        if status not in VALID_STATUSES:
            warnings.append("Unexpected status")

        if confidence < 0.75:
            warnings.append("Low confidence")

        duplicate = False

        for previous in seen_tasks:

            similarity = fuzz.ratio(
                previous.lower(),
                task.lower()
            )

            if similarity > 90:
                duplicate = True
                break

        if duplicate:
            warnings.append("Possible duplicate")

        seen_tasks.append(task)

        validated.append({
            "task": task,
            "owner": owner,
            "deadline": deadline,
            "status": status,
            "confidence": confidence,
            "warnings": warnings
        })

    return validated


def print_validation_results(validated_items):
    """Display validation results."""

    print("\nValidation Results")
    print("=" * 60)

    for i, item in enumerate(validated_items, start=1):

        print(f"\nAction Item {i}")
        print(f"Task: {item['task']}")
        print(f"Owner: {item['owner']}")
        print(f"Deadline: {item['deadline']}")
        print(f"Status: {item['status']}")
        print(f"Confidence: {item['confidence']}")

        if item["warnings"]:
            print("Warnings:")
            for warning in item["warnings"]:
                print(f"  • {warning}")
        else:
            print("Warnings: None")