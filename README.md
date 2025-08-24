A Streamlit-based web application for automated compliance risk analysis.
This tool is a practical, full-stack web application developed in Python to help legal and compliance professionals proactively identify and manage risks within their organizational documents. It simplifies the tedious process of manually reviewing policy drafts, contracts, and other files for privacy and compliance-critical information.

Key Features
Intelligent Document Support: Seamlessly processes text from .txt, .docx, and .pdf files.

Jurisdictional Intelligence: Analyzes documents based on a dynamic set of rules for specific regions, including Canadian regulations (e.g., PIPEDA) and international standards (e.g., GDPR).

Automated Risk Scoring: Assigns a quantifiable risk score to each document based on the keywords and concepts found, enabling the user to prioritize critical reviews effectively.

User-Friendly Interface: Provides an intuitive interface built with Streamlit that requires no technical expertise to operate.

Getting Started
To run the Proactive Compliance Auditor on your local machine, follow these steps:

1. Clone the Repository
If you haven't already, clone this repository to your local machine.

Bash

git clone [Your Repository URL]
cd [Your Repository Folder]

2. Set Up the Environment
Install the necessary Python libraries. This project requires streamlit, spacy, docx2txt, and PyMuPDF.

Bash

pip install -r requirements.txt
python -m spacy download en_core_web_sm
3. Run the Application
Once the dependencies are installed, you can start the application from your terminal.

Bash

streamlit run app.py
The tool will open in your default web browser.

How It Works
The application's core is built with a few powerful Python libraries:

Streamlit: Creates the interactive web-based interface.

spaCy: A natural language processing library that intelligently parses the document text.

PyMuPDF & docx2txt: Libraries that extract text from PDF and Word documents, respectively.

The tool uses a dictionary of legal keywords and a weighted scoring system to automatically assess a document's risk profile. This project showcases an understanding of modern development practices and a proactive approach to solving real-world compliance challenges.
