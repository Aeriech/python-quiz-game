import json
from generate_content import generate_content_from_gemini
from data_entry import get_int_input, get_string_input

def generate_quiz_content(topic: str, quiz_length: int, difficulty_level: str):
    prompt = f"""
Generate a quiz about {topic} with {quiz_length} questions.
The quiz should be designed to be of {difficulty_level} difficulty.
Consider the expected knowledge level for someone at a {difficulty_level} level when creating the questions.

The quiz MUST be formatted as a single JSON object.
This JSON object should have a single key named "questions".
The value associated with the "questions" key MUST be a JSON array.
Each element in this JSON array MUST be a JSON object representing a single quiz question.

Each question object in the array MUST have the following keys:

- "prompt":  The text of the question itself (string).
- "options": An array of strings representing the multiple-choice options. These options should be labeled with letters like "A.", "B.", "C.", "D.".
- "answer": A single string representing the correct answer option label (e.g., "B", "C", etc., just the letter).

Here is an EXAMPLE of the EXACT JSON format you MUST use for the entire quiz output:
{{
  "questions": [
    {{
      "prompt": "What keyword is used to define a function in Python?",
      "options": ["A. function", "B. def", "C. define", "D. func"],
      "answer": "B"
    }},
    {{
      "prompt": "Which of the following is a valid data type in Python?",
      "options": ["A. text", "B. integer", "C. character", "D. float"],
      "answer": "D"
    }},
    {{
      "prompt": "What does the 'print()' function do in Python?",
      "options": ["A. Deletes a file", "B. Displays output to the console", "C. Solves math problems", "D. Creates a new variable"],
      "answer": "B"
    }},
    {{
      "prompt": "Which of the following is a comment in Python?",
      "options": ["A. // This is a comment", "B. ", "C. # This is a comment", "D. * This is a comment"],
      "answer": "C"
    }},
    {{
      "prompt": "What is the correct way to assign the value 10 to a variable named 'x' in Python?",
      "options": ["A. x = 10", "B. 10 = x", "C. assign x to 10", "D. x == 10"],
      "answer": "A"
    }}
  ]
}}

Return ONLY this JSON object. Do not include any other text, explanations, or code in your response. Just the raw JSON.

For each question in the quiz, ensure:
- It is relevant to the topic: "{topic}".
- There are four plausible multiple-choice options labeled A, B, C, and D.
- Only one option is definitively the correct answer.
- The 'answer' field correctly reflects the letter of the correct option (e.g., "A", "B", "C", "D").
- The overall difficulty of the quiz is {difficulty_level}.  Questions should be appropriate for a {difficulty_level} level of understanding for a general audience.

Please generate the JSON quiz now, in the EXACT format shown above, focusing on {difficulty_level} difficulty.
"""
    quiz_json_string = generate_content_from_gemini(prompt)
    try:
        # Step 1: Remove the markdown code block markers
        clean_json_str = quiz_json_string.strip("```json").strip("```").strip()

        # Step 2: Convert cleaned string to a Python dictionary
        quiz_data = json.loads(clean_json_str)
        
        return quiz_data["questions"]
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print("Raw Response Text:\n", quiz_json_string)
        return []   

def main():
    topic = input("Enter the topic for the quiz: ")
    quiz_length = get_int_input("Enter the number of questions for the quiz: ")
    difficulty_level = get_string_input("Enter the difficulty level (Easy, Medium, Hard): ", ["Easy", "Medium", "Hard"])

    print("\nGenerating quiz...\n")
    questions = generate_quiz_content(topic, quiz_length, difficulty_level)
    
    score = 0
    question_num = 1
    for question in questions:
        print(f"{question_num}. {question['prompt']}")
        for option in question['options']:
            print(option)
            
        answer = get_string_input("Enter your answer (A, B, C, or D): ", ["A", "B", "C", "D"]).upper()
        if answer == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}\n")
        question_num += 1
    
    print(f"Your final score is {score}/{len(questions)}")
    
if __name__ == "__main__":
    main()