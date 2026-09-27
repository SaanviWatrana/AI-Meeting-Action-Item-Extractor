import streamlit as st
import tempfile
from pathlib import Path

from preprocessing import load_transcript
from model_extractor import load_model, extract_action_items
from validator import validate_action_items

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="AI Meeting Action-Item Extractor",
    page_icon="📋",
    layout="wide"
)

st.title("📋 AI Meeting Action-Item Extractor")
st.write(
    "Upload a meeting transcript or use one of the sample transcripts."
)

# ----------------------------
# Sample Transcript Selection
# ----------------------------

st.subheader("Choose a Sample Transcript")

sample_options = [
    "meeting_001",
    "meeting_002",
    "meeting_003",
    "meeting_004",
    "meeting_005"
]

selected_sample = st.selectbox(
    "Select a sample meeting",
    sample_options
)

st.divider()

# ----------------------------
# Upload Option
# ----------------------------

st.subheader("Or Upload Your Own Transcript")

uploaded_file = st.file_uploader(
    "Upload a transcript (.txt)",
    type=["txt"]
)

# ----------------------------
# Process Button
# ----------------------------

if st.button("Extract Action Items"):

    # Decide which transcript to use

    if uploaded_file is not None:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".txt"
        ) as tmp:

            tmp.write(uploaded_file.read())
            transcript = load_transcript(tmp.name)

    else:

        transcript_path = Path("data/raw") / f"{selected_sample}.txt"
        transcript = load_transcript(transcript_path)

    # Load model

    with st.spinner("Loading AI model..."):

        tokenizer, model = load_model()

    # Run extraction

    with st.spinner("Extracting action items..."):

        results = extract_action_items(
            tokenizer,
            model,
            transcript
        )

    # Display results

    if isinstance(results, list):

        validated = validate_action_items(results)

        st.success("Extraction completed.")

        st.subheader("📊 Extracted Action Items")

        table = []

        for item in validated:

            table.append(
                {
                    "Task": item["task"],
                    "Owner": item["owner"],
                    "Deadline": item["deadline"],
                    "Status": item["status"],
                    "Confidence": item["confidence"]
                }
            )

        st.table(table)

        st.subheader("⚠ Validation Warnings")

        warning_found = False

        for item in validated:

            if item["warnings"]:

                warning_found = True

                st.warning(
                    f"{item['task']}: {', '.join(item['warnings'])}"
                )

        if not warning_found:

            st.success("No validation warnings found.")

    else:

        st.error("The model did not return valid JSON.")