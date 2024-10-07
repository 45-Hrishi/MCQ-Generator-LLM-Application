# QuizChain 🦜⛓️ - MCQ Generator LLM Application 🚀
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/45-Hrishi/MCQ-Generator-LLM-Application) 


## 📝 Overview
📚 This app generates 5 MCQs from a concept using Mistral AI. It creates mcq's from uploaded pdf and stores questions & options in a CSV file, making quiz creation simple and efficient. Perfect for study materials! ✨🤖


## ✨ Features
- **Generate MCQs from PDFs**: Automatically creates 5 multiple-choice questions (MCQs) from any uploaded PDF using Mistral AI, streamlining quiz creation.
- **CSV Export**: Stores generated questions and options in a CSV file for easy access and future use.
- **Efficient Quiz Creation**: Simplifies the process of making quizzes, perfect for creating study materials or practice tests.
- **Logging Functionality**: Integrated logging to track the process and capture key information at every step for easier debugging and monitoring.


## 📚 Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Project Structure](#project-structure)


## ⚙️ Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/45-Hrishi/MCQ-Generator-LLM-Application.git
   ```
2. Move into required directory:
   ```bash  
    cd MCQ-Generator-LLM-Application
   ```
3. Install the requirements:
   ```bash  
    pip install -r requirements.txt
   ```
##### NOTE : To install local packages into conda env, paste `-e .` inside requirements.txt and then run command : ```pip -r requirements.txt```. Now you have install your local packages into your conda environment. else remove the -e . and then run ```pip -r requirements.txt```
   
5. Setup the API Key:
   ```bash
   export MISTRAL_API_KEY=your_api_key_here
    ```

---

### 🛠️ Usage
To run the QuizChain application:

1. Run the following command to run the QuizChain:
   ```bash
   streamlit run app.py
   ```
Now, your app will be running on chrome or MS edge (based on the default browser)


---

### 🛠️ Technologies
- Python
- Langchain
- Mistral AI
- Git

### 🗂️ Project Structure
```
research/
│
├── logs/                              # Log files for tracking
│
├── 05_MiniProject1_MCQ_Generator.ipynb  # Jupyter notebook for MCQ generation project
├── pdfextractor_research.ipynb          # Jupyter notebook for PDF extraction research
│
├── src/                                # Source code directory
│   ├── mcq_generator/                  # Core project package
│   │   ├── __pycache__/                # Compiled Python files
│   │   ├── __init__.py                 # Marks directory as a package
│   │   ├── logger.py                   # Logging setup
│   │   ├── mcq_generator.py            # Script for generating MCQs
│   │   └── utils.py                    # Utility functions
│
├── .gitignore                          # Git ignore file (for ignoring unnecessary files)
├── app.py                              # Main application file to run the project
├── prompts.json                        # JSON file for storing AI model prompts
├── quiz.csv                            # CSV file storing generated MCQs and options
├── README.md                           # Documentation for the project
├── requirements.txt                    # List of Python dependencies for the project
├── response.json                       # JSON file storing API or model responses
├── setup.py                            # Setup script for installing the project package
```
## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## 🛤️ Roadmap
- [ ] Add the functionality of Download in the application.
- [ ] Deployment on the Azure / AWS.



