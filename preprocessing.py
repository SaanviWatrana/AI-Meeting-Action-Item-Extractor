from pathlib import Path
import re


def load_transcript(file_path):
    """Read the transcript from a text file."""
    return Path(file_path).read_text(encoding="utf-8")


def split_into_sentences(text):
    """Split text into individual sentences."""
    return re.split(r"(?<=[.!?])\s+", text.strip())


def parse_speaker_statements(transcript):
    """Extract speaker names and individual sentences."""

    statements = []

    for line in transcript.splitlines():

        line = line.strip()

        if not line:
            continue

        match = re.match(r"^([^:]+):\s*(.+)$", line)

        if not match:
            continue

        speaker = match.group(1).strip()
        text = match.group(2).strip()

        sentences = split_into_sentences(text)

        for sentence in sentences:

            if sentence:
                statements.append({
                    "speaker": speaker,
                    "text": sentence
                })

    return statements


def preprocess_transcript(file_path):
    """Load and preprocess a transcript."""

    transcript = load_transcript(file_path)

    statements = parse_speaker_statements(transcript)

    return statements


def main():

    file_path = "data/raw/meeting_001.txt"

    statements = preprocess_transcript(file_path)

    print()
    print("PREPROCESSED TRANSCRIPT")
    print("=" * 60)

    for statement in statements:

        print(
            statement["speaker"]
            + ": "
            + statement["text"]
        )

    print("=" * 60)
    print("Total statements:", len(statements))


if __name__ == "__main__":
    main()