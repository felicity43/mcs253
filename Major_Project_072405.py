class InvalidVARKInput(Exception): """Custom exception for invalid VARK input.""" 
pass

class VARKQuiz: 
   def __init__(self): 

        self.questions = { 1: { "question": "When learning something new,you prefer to:",
                                "options": {
                                "a": ("Watch a demonstration", ["V"]),
                                "b": ("Listen to an explanation",["A"]), 
                                "c": ("Read about it", ["R"]), 
                                "d": ("Try it out yourself", ["K"]) } },
                            2: {"question": "When following directions, you prefer to:", 
                            "options": {
                                 "a": ("Look at a map or diagram", ["V"]), 
                                 "b":("Listen to someone explaining it", ["A"]), 
                                 "c": ("Read written instructions", ["R"]),
                                 "d": ("Follow your instincts after a brief glance", ["K"]) } }, 
                            3: { "question": "You remember information best whenyou:", 
                                "options": { 
                                    "a": ("See charts or diagrams", ["V"]), 
                                    "b": ("Hear someone explain it", ["A"]), 
                                    "c":("Read it in a book or notes", ["R"]), 
                                    "d": ("Use your hands and move around", ["K"]) } },
                            4:{ "question": "When working on a project, you prefer to:",
                                "options": { 
                                    "a": ("Create a visual plan or diagram", ["V"]), 
                                    "b": ("Discuss ideas with others", ["A"]), 
                                    "c": ("Write detailed plans", ["R"]), 
                                    "d":("Build or model something", ["K"]) } }, 
                            5: { "question": "To remember a phone number, you:",
                                "options": { 
                                    "a": ("Visualize the numbers in your mind", ["V"]),
                                    "b": ("Repeat it aloud", ["A"]), 
                                    "c":("Write it down repeatedly", ["R"]), 
                                    "d": ("Tap it with your fingers or act it out", ["K"]) } },
                            6:{ "question": "When solving a problem, you:", 
                               "options": { 
                                   "a": ("Draw it out", ["V"]), 
                                   "b": ("Talk through it", ["A"]), 
                                   "c": ("Write down possible solutions", ["R"]), 
                                   "d": ("Experiment physically", ["K"]) }}, 
                                   
                            7: { "question": "You prefer teachers who:", 
                                "options": { 
                                    "a": ("Use graphs and visual aids", ["V"]),
                                    "b": ("Engage in class discussions", ["A"]), 
                                    "c": ("Provide written instructions", ["R"]), 
                                    "d": ("Give hands-on activities", ["K"]) } }, 
                                    
                            8: { "question": "When studying, you prefer:",
                                 "options": { 
                                     "a": ("Using pictures and charts", ["V"]), 
                                     "b": ("Listening to recordings or lectures", ["A"]), 
                                     "c": ("Rewriting notes",["R"]), 
                                     "d": ("Walking or moving around", ["K"]) } }, 
                            9: { "question": "When recalling facts, you:",
                                "options": { 
                                    "a": ("See a picture or diagram", ["V"]), 
                                    "b": ("Hear the teacher's voice", ["A"]), 
                                    "c":("Recall notes or textbooks", ["R"]), 
                                    "d": ("Remember what you did physically", ["K"]) } }, 
                                    
                            10:{ "question": "In a group project, you:", 
                            "options": { 
                                "a": ("Create the presentation visuals", ["V"]), 
                                "b":("Lead the discussion", ["A"]), 
                                "c": ("Write the content", ["R"]), 
                                "d": ("Build models or dodemonstrations", ["K"]) } }, 
                                
                            11: { "question": "To learn a new software, you prefer to:", 
                                 "options":{ 
                                     "a": ("Watch tutorial videos", ["V"]), 
                                     "b": ("Listen to a walkthrough", ["A"]), 
                                     "c": ("Read the manual",["R"]), 
                                     "d": ("Explore the software hands-on", ["K"]) } }, 
                                     
                            12: { "question": "In lectures, you:", 
                                 "options":{ 
                                     "a": ("Prefer slides and diagrams", ["V"]), 
                                     "b": ("Like listening to the speaker", ["A"]), 
                                     "c": ("Take  lots of notes", ["R"]), 
                                     "d": ("Like interacting or moving", ["K"]) } }, 
                            13: { "question": "You learn better  when you:", 
                                 "options": { 
                                     "a": ("See how things are done", ["V"]), 
                                     "b": ("Hear detailed instructions",["A"]), 
                                     "c": ("Write and read instructions", ["R"]), 
                                     "d": ("Physically perform the task", ["K"]) } }, 
                                     
                            14:{ "question": "When preparing for a test, you:", 
                                "options": {
                                     "a": ("Use flashcards with images",["V"]), 
                                     "b": ("Recite information aloud", ["A"]),
                                    "c": ("Read over your notes", ["R"]), 
                                    "d": ("Use practice questions or simulations", ["K"]) } },
                            15: { "question": "You prefer feedback that is:",
                                  "options": { 
                                      "a":("Shown with diagrams or examples", ["V"]), 
                                      "b": ("Spoken and explained", ["A"]), 
                                      "c": ("Written comments", ["R"]), 
                                      "d": ("Demonstrated or practiced", ["K"]) } }, 
                            16: { "question": "You understand better when:", 
                                 "options": { 
                                     "a": ("Seeing how it works visually", ["V"]), 
                                     "b": ("Hearing the explanation", ["A"]), 
                                     "c": ("Reading about it", ["R"]), 
                                     "d": ("Trying it yourself", ["K"]) } } }
        
        self.scores = {"V": 0, "A": 0, "R": 0, "K": 0}
        
   def ask_questions(self):
        for q_no in sorted(self.questions.keys()):
            q_data = self.questions[q_no]
            while True:
                print(f"\nQuestion {q_no}: {q_data['question']}")
                for key, (desc, _) in q_data["options"].items():
                    print(f" {key}) {desc}")
                try:
                    user_input = input("Enter two choices (e.g., a c, seperated by a space): ").lower().split()
                    if len(user_input) != 2 or not all(opt in q_data["options"] for opt in user_input):
                        raise InvalidVARKInput("You must enter two valid options (a, b,c, d).")
                    for choice in user_input:
                        for vark in q_data["options"][choice][1]:
                            self.scores[vark] += 1
                    break #Valid input → move to next question
                except InvalidVARKInput as e:
                    print(f"Input Error: {e}")
                except Exception:
                    print("Unexpected error. Please try again.")

   def display_results(self):
     print("\n--- VARK Learning Style Results---")
     for style, score in self.scores.items():
            print(f"{style}: {score}")
            max_score = max(self.scores.values())
            top_styles = [s for s in self.scores if self.scores[s] == max_score]
            if len(top_styles) == 1:
                print(f"\nYour primary learning style  {self.get_full_style_name(top_styles[0])}")
            else:
                full_names = [self.get_full_style_name(s) for s in top_styles]
                print(f"\nYou have a multimodal learning style: {', '.join(full_names)}")

   @staticmethod
   def get_full_style_name(code):
    return {
            "V": "Visual",
            "A": "Auditory",
            "R": "Read/Write",
            "K": "Kinesthetic"
            }[code]
 # Runthe quiz

if __name__ == "__main__":
        quiz = VARKQuiz()
        quiz.ask_questions()
        quiz.display_results()

