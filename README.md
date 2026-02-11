# Law Buddy ⚖️

Law Buddy is an AI-powered legal assistant designed to help users understand the Constitution of India and other legal documents. Built with Streamlit and powered by Google's Gemini Pro model, it allows users to ask questions and get accurate answers based on the provided legal texts.

## Features

-   **Chat with the Constitution**: Pre-loaded with the Constitution of India and its amendments.
-   **Custom Document Analysis**: Upload your own PDF files to contextually chat with them.
-   **AI-Powered**: Utilizes Google Generative AI (Gemini Pro) for natural language understanding and generation.
-   **Vector Search**: Uses FAISS for efficient similarity search within documents.

## Prerequisites

-   Python 3.8 or higher
-   A Google Cloud Project with the Generative AI API enabled.
-   A Google API Key.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Ayushmaannn/lawbuddy.git
    cd lawbuddy
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables:**

    Create a `.env` file in the root directory and add your Google API Key:

    ```env
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage

Run the Streamlit application:

```bash
streamlit run 1_Home.py
```

The application will open in your default web browser.

## Project Structure

-   `1_Home.py`: The main application entry point.
-   `pages/`: Contains other pages of the Streamlit app (e.g., About Us, Contact Us).
-   `faiss_index/`: Stores the vector embeddings for the default documents.
-   `requirements.txt`: Python dependencies.

## Technologies Used

-   [Streamlit](https://streamlit.io/)
-   [LangChain](https://www.langchain.com/)
-   [Google Generative AI (Gemini)](https://ai.google.dev/)
-   [FAISS](https://github.com/facebookresearch/faiss)
-   [PyPDF2](https://pypi.org/project/PyPDF2/)
