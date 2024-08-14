# Pandas AI: Interactive Data Analyst

## Overview

Pandas AI is an interactive Streamlit application designed to assist users in analyzing datasets using natural language queries. By leveraging advanced language models, users can upload a CSV file, pose questions about the data, and receive accurate pandas queries to extract and analyze the dataset.

## Demo Screenshots

![Screenshot 1](https://github.com/AtharshKrishnamoorthy/Pandas-AI/blob/main/data/Screenshot%202024-08-10%20213347.png)
![Screenshot 2](https://github.com/AtharshKrishnamoorthy/Pandas-AI/blob/main/data/Screenshot%202024-08-10%20213406.png)
![Screenshot 3](https://github.com/AtharshKrishnamoorthy/Pandas-AI/blob/main/data/Screenshot%202024-08-10%20213546.png)
![Screenshot 4](https://github.com/AtharshKrishnamoorthy/Pandas-AI/blob/main/data/Screenshot%202024-08-10%20213647.png)
![Screenshot 5](https://github.com/AtharshKrishnamoorthy/Pandas-AI/blob/main/data/Screenshot%202024-08-10%20213805.png)
![Screenshot 6](https://github.com/AtharshKrishnamoorthy/Pandas-AI/blob/main/data/Screenshot%202024-08-10%20213849.png)
![Screenshot 7](https://github.com/AtharshKrishnamoorthy/Pandas-AI/blob/main/data/Screenshot%202024-08-10%20213918.png)

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

The Pandas AI application offers:

1. **CSV File Upload**: Upload and preview CSV files to prepare for analysis.
2. **Natural Language Querying**: Ask questions about the dataset in natural language and receive corresponding pandas queries.
3. **Query Generation and Correction**: Automatically generate and refine pandas queries using pretranied LLMs from Groq (here in this case 2 models are one is for generating the pandas queries - model used : `llama-3.1-70b-versatile`, the other one is for correcting the generated queries - model used : `llama-3-70b.`
4. **Data Analysis**: Execute and display the results of pandas queries on the uploaded dataset.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.7+
- Streamlit
- LangChain (including `langchain_core`)
- Groq (for AI model integration)
- dotenv
- pandas

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AtharshKrishnamoorthy/Pandas-AI
    cd Pandas-AI
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
   - Create a `.env` file in the project directory.
   - Add your Groq API key to the `.env` file:

     ```
     GROQ_API_KEY=your_groq_api_key
     ```

## Usage

To run the Pandas AI application:

1. Navigate to the project directory.
2. Start the Streamlit app:

    ```bash
    streamlit run app.py
    ```

3. Open your web browser and go to `http://localhost:8501` (or the address provided in the terminal).

### File Upload

1. Upload a CSV file using the file uploader.
2. Preview the dataset to confirm it's loaded correctly.

### Querying

1. Enter your question about the dataset in the text input box.
2. Click "Get Answer" to generate and execute the corresponding pandas query.

## Configuration

Ensure you have the necessary environment setup. Modify `app.py` as needed for additional configurations.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the original branch: `git push origin feature-branch-name`.
5. Create a pull request.

Please update tests as appropriate and adhere to the project's coding standards.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

For any questions or inquiries, please reach out:

- Project Maintainer: Atharsh K
- Email: atharshkrishnamoorthy@gmail.com
- Project Link: [GitHub Repository](https://github.com/AtharshKrishnamoorthy/Pandas-AI)
