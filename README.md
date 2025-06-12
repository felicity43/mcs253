1. Project Title and Due Date
 Project Title: VARK Learning Style Questionnaire Program
 Due Date: 13/06/25
2. What the Project is About
 This project implements a learning style self-assessment tool based on the VARK model
 (Visual, Auditory, Read/Write, and Kinesthetic). Users answer a series of 16 questions,
 choosing two options per question. Each option corresponds to a learning style. Based on
 their responses, the program determines the user's dominant or multimodal learning
 preference.--
3. Code Composition
Classes:
 VARKQuiz: The main class that organizes questions, handles user input, calculates scores,
 and presents results.
 InvalidVARKInput: A custom exception class used to manage invalid input scenarios.
 Functions/Methods:
 __init__(): Initializes the question bank and score tracker.
 ask_questions(): Loops through all questions, takes two valid inputs per question, and
 updates scores.
 display_results(): Displays the final scores and identifies the dominant or multimodal
 learning style.
 get_full_style_name(): A static method to convert style codes (V, A, R, K) into full names
 (Visual, Auditory, etc.).
 Inheritance:
 InvalidVARKInput inherits from Python's built-in Exception class.
--
4. Data Captured and Data Types
 User Inputs: Two choices per question (a, b, c, or d).
 Stored Data:
 Questions: Stored in a nested dictionary, where each question contains sub-dictionaries
 for choices and associated learning styles.
 Scores: Stored in a dictionary with keys "V", "A", "R", and "K", and integer values to keep
 count.
 Data Source: All questions and options are hard-coded into the script — there is no
 external data source.--
5. Exception Handling
 The program includes robust input validation using:
Acustom exception (InvalidVARKInput) to raise errors when the user:
 Provides fewer or more than two choices.
 Enters invalid letters not among the available options.
 Ageneral exception handler (except Exception) to catch and report unexpected runtime
 errors gracefully.--
6. Final Outcome
 Upon successful execution:
 The user answers all 16 questions.
 The program calculates and displays a total score for each learning style.
 It then announces the user’s primary learning style or multimodal style if multiple styles tie
 with the highest score.
--
7. Reflection
 Challenges:
 the greatest challenge that i face while doing this project is when i wanted to run this code after completion. I thought i was done but when  ran it, it gave
 so many errors that i didnt notice when i completed the code. I believe creating the code is one thing, running it to find out if it actual works is another burden.
 i learnt to read the error lines and understand them carefully inorder to fix my code.

 8. Word of thanks
 I would like to thank my course coordinator Ms. Komogi for extending the due date of this project as i have been going through some personal issues that permitt me to 
 complete my project however because of her kind gesture, i was able to complete it and submit it. Secondly, i would like to thank my course mate Natasha for helping me 
 to fix my code And lastly, i would like to thank my family for their support in funding me to complete my project.
 
