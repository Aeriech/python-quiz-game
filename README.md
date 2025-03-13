### Project Overview - AI Quiz Generator
The AI Quiz Generator is a Python-based interactive quiz application that dynamically generates multiple-choice quizzes based on user-defined topics and difficulty levels. Using AI-powered content generation, it ensures a variety of well-structured questions tailored to different levels of expertise.

Key Features:
   - Dynamic Quiz Generation: Automatically creates quizzes based on a user-specified topic, number of questions, and difficulty level.
   - AI-Generated Questions: Utilizes AI (Gemini API) to generate high-quality quiz questions in JSON format.
   - Interactive Quiz Interface: Prompts users to answer questions and provides instant feedback.
   - Scoring System: Tracks user performance and displays the final score at the end.

Tech Stack:
   - Python – Core programming language
   - JSON – Structured data format for quiz storage
   - AI Integration (Gemini API) – Generates quiz content dynamically
   - Custom Input Handling – Ensures valid user responses
   
## **Getting Started**

### Prerequisites

Ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.13.2 or higher)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Aeriech/python-personal-finance-tracker.git
   ```

2. Install dependencies:
   ```bash
   cd python-personal-finance-tracker
   pip install python-dotenv
   pip install google-generativeai
   cp .env.example .env
   ```
3. Setting Gemini Api Key::
    - Get your api key here: https://aistudio.google.com/app/apikey
    - Put your api key in .env (GEMINI_API_KEY)

4. Run development:
   ```bash
   python main.py 
   ```