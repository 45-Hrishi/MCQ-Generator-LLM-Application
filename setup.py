import setuptools

__version__ = "0.0.0"

REPO_NAME = "End-to-End-MCQ-Generator-LLM-Application"
AUTHOR_USER_NAME = "45-Hrishi"
SRC_REPO = "mcq_generator"
AUTHOR_EMAIL = "hrishikeshkothawade1@gmail.com"
LONG_DESCRIPTION = """This application generates 5 multiple-choice questions (MCQs) based on a given concept 
using Mistral AI's model for chat interactions. It retrieves relevant information from Wikipedia and 
automatically creates MCQs. The questions and answer options are stored as a CSV file, 
providing a simple and efficient tool for quizzes or study material.
"""
DESCRIPTION = """
MCQ Generator LLM Application using Mistral-AI
"""


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)