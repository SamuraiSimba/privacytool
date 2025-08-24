import streamlit as st
import docx2txt
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define a more advanced, structured set of compliance terms
JURISDICTIONAL_RULES = {
    "General": {
        "keywords": ["personal information", "data sharing", "privacy policy", "breach notification"],
        "risk_score": 5,
    },
    "Canada": {
        "keywords": ["PIPEDA", "PIPA", "data residency", "consent"],
        "risk_score": 10,
    },
    "European Union": {
        "keywords": ["GDPR", "Right to be Forgotten", "data processor"],
        "risk_score": 15,
    },
}

def analyze_document(text_content, selected_jurisdiction):
    """
    Analyzes a document for compliance keywords based on the selected jurisdiction.
    Returns a list of flagged sentences with keywords and a total risk score.
    """
    doc = nlp(text_content.lower())
    matches = []
    total_risk_score = 0

    # Get the rules for the selected jurisdiction and the general rules
    rules = {**JURISDICTIONAL_RULES["General"], **JURISDICTIONAL_RULES.get(selected_jurisdiction, {})}

    for sentence in doc.sents:
        for keyword in rules["keywords"]:
            if keyword in str(sentence):
                matches.append(
                    {"keyword": keyword, "sentence": str(sentence).strip(), "jurisdiction": selected_jurisdiction}
                )
                total_risk_score += rules["risk_score"]
    
    return matches, total_risk_score

# Streamlit UI
st.title("Proactive Compliance Auditor")
st.markdown("Upload a document to scan for potential compliance risks based on jurisdiction.")

# New: Add a select box for jurisdiction
jurisdiction = st.selectbox(
    "Select Jurisdiction",
    list(JURISDICTIONAL_RULES.keys())
)

uploaded_file = st.file_uploader("Choose a .txt or .docx file", type=["txt", "docx"])

if uploaded_file is not None:
    # Read the file content
    if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text_content = docx2txt.process(uploaded_file)
    else:  # Assumes .txt
        text_content = uploaded_file.getvalue().decode("utf-8")

    # Display a spinner while processing
    with st.spinner(f'Scanning document for {jurisdiction} rules...'):
        matched_sentences, total_score = analyze_document(text_content, jurisdiction)
        st.success("Scan Complete!")

    # Display results with risk score
    if total_score > 0:
        st.subheader(f"⚠️ Total Risk Score: {total_score}")
        st.markdown(f"Found {len(matched_sentences)} potential compliance issues.")
        st.markdown("---")
        for i, match in enumerate(matched_sentences):
            st.info(f"**Keyword:** `{match['keyword']}` (Jurisdiction: {match['jurisdiction']})")
            st.write(f"**Sentence:** {match['sentence']}")
            st.markdown("---")
    else:
        st.subheader("✅ No compliance keywords found. The document appears to be clean.")

st.markdown("---")
st.markdown("### How It Works")
st.markdown("This advanced prototype uses NLP and a jurisdictional rule-set to identify and score potential compliance risks. This demonstrates a proactive approach to risk management.")