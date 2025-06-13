class InvalidVARKInput(Exception): """Custom exception for invalid VARK input.""" 
pass

class VARKQuiz: 
   def __init__(self): 

        self.questions = { 1: { "question": " You are helping someone who wants to go to your airport, town centre or railway station. You would: ",
                                "options": {
                                "a": ("Go with her", ["V"]),
                                "b": (" tell her the directions",["A"]), 
                                "c": ("write down the directions.", ["R"]), 
                                "d": (" draw, or give her a map.", ["K"]) } },
                            2: {"question": " You are not sure whether a word should be spelled `dependent' or `dependant'. You would: ", 
                            "options": {
                                 "a": (" see the words in your mind and choose by the way they look.", ["V"]), 
                                 "b":(" think about how each word sounds and choose one. ", ["A"]), 
                                 "c": (" find it in a dictionary. ", ["R"]),
                                 "d": ("write both words on paper and choose one. ", ["K"]) } }, 
                            3: { "question": "You are planning a holiday for a group. You want some feedback from them about the plan. You would: ", 
                                "options": { 
                                    "a": (" describe some of the highlights.", ["V"]), 
                                    "b": ("use a map or website to show them the places.", ["A"]), 
                                    "c":(" give them a copy of the printed itinerary. ", ["R"]), 
                                    "d": ("phone, text or email them. ", ["K"]) } },
                            4:{ "question": "You are going to cook something as a special treat for your family. You would: ",
                                "options": { 
                                    "a": (" cook something you know without the need for instructions. ", ["V"]), 
                                    "b": (" ask friends for suggestions", ["A"]), 
                                    "c": ("look through the cookbook for ideas from the pictures. ", ["R"]), 
                                    "d":(". use a cookbook where you know there is a good recipe. ", ["K"]) } }, 
                            5: { "question": " A group of tourists want to learn about the parks or nature reserves in your area. You would:",
                                "options": { 
                                    "a": (" talk about, or arrange a talk for them about parks or nature reserves.", ["V"]),
                                    "b": (" show them internet pictures, photographs or picture books. ", ["A"]), 
                                    "c":(". take them to a park or nature reserve and walk with them. ", ["R"]), 
                                    "d": ("give them a book or pamphlets about the parks or nature reserves. ", ["K"]) } },
                            6:{ "question": " You are about to purchase a digital camera or mobile phone. Other than price, what would most influence your decision? ", 
                               "options": { 
                                   "a": (" Trying or testing it. ", ["V"]), 
                                   "b": (" Reading the details about its features.", ["A"]), 
                                   "c": ("It is a modern design and looks good. ", ["R"]), 
                                   "d": ("The salesperson telling me about its features. ", ["K"]) }}, 
                                   
                            7: { "question": " Remember a time when you learned how to do something new. Try to avoid choosing a physical skill, e.g. riding a bike. You learned best by: ", 
                                "options": { 
                                    "a": ("watching a demonstration", ["V"]),
                                    "b": (" listening to somebody explaining it and asking questions", ["A"]), 
                                    "c": (" diagrams and charts - visual clues. ", ["R"]), 
                                    "d": ("written instructions – e.g. a manual or textbook. ", ["K"]) } }, 
                                    
                            8: { "question": ". You have a problem with your knee. You would prefer that the doctor: ",
                                 "options": { 
                                     "a": (" gave you a web address or something to read about it. ", ["V"]), 
                                     "b": (" used a plastic model of a knee to show what was wrong. ", ["A"]), 
                                     "c": ("described what was wrong. ",["R"]), 
                                     "d": ("showed you a diagram of what was wrong.", ["K"]) } }, 
                            9: { "question": "You want to learn a new programme, skill or game on a computer. You would: ",
                                "options": { 
                                    "a": ("read the written instructions that came with the programme. ", ["V"]), 
                                    "b": (" talk with people who know about the programme. ", ["A"]), 
                                    "c":(". use the controls or keyboard. ", ["R"]), 
                                    "d": (" follow the diagrams in the book that came with it. ", ["K"]) } }, 
                                    
                            10:{ "question": " I like websites that have:", 
                            "options": { 
                                "a": ("things I can click on, shift or try.", ["V"]), 
                                "b":(". interesting design and visual features. ", ["A"]), 
                                "c": (" interesting written descriptions, lists and explanations. ", ["R"]), 
                                "d": (" audio channels where I can hear music, radio programmes or interviews.", ["K"]) } }, 
                                
                            11: { "question": " Other than price, what would most influence your decision to buy a new non-fiction book?", 
                                 "options":{ 
                                     "a": (" The way it looks is appealing. ", ["V"]), 
                                     "b": (" Quickly reading parts of it. ", ["A"]), 
                                     "c": (" A friend talks about it and recommends it. ",["R"]), 
                                     "d": (" It has real-life stories, experiences and examples. ", ["K"]) } }, 
                                     
                            12: { "question": "You are using a book, DVD or website to learn how to take photos with your new digital camera. You would like to have: ", 
                                 "options":{ 
                                     "a": (" a chance to ask questions and talk about the camera and its features.", ["V"]), 
                                     "b": (" clear written instructions with lists and bullet points about what to do.", ["A"]), 
                                     "c": (" diagrams showing the camera and what each part does. ", ["R"]), 
                                     "d": ("many examples of good and poor photos and how to improve them. ", ["K"]) } }, 
                            13: { "question": "Do you prefer a trainer or a presenter who uses: ", 
                                 "options": { 
                                     "a": ("demonstrations, models or practical sessions.", ["V"]), 
                                     "b": (" question and answer, talk, group discussion, or guest speakers.",["A"]), 
                                     "c": ("handouts, books, or readings. ", ["R"]), 
                                     "d": (" diagrams, charts or graphs. ", ["K"]) } }, 
                                     
                            14:{ "question": ". You have finished a competition or test and would like some feedback. You would like to have feedback: ", 
                                "options": {
                                     "a": (" using examples from what you have done. ",["V"]), 
                                     "b": ("using a written description of your results. ", ["A"]),
                                    "c": ("from somebody who talks it through with you. ", ["R"]), 
                                    "d": (" using graphs showing what you had achieved. ", ["K"]) } },
                            15: { "question": "You are going to choose food at a restaurant or cafe. You would:",
                                  "options": { 
                                      "a":("choose something that you have had there before.", ["V"]), 
                                      "b": (" listen to the waiter or ask friends to recommend choices.", ["A"]), 
                                      "c": (" choose from the descriptions in the menu. ", ["R"]), 
                                      "d": ("look at what others are eating or look at pictures of each dish. ", ["K"]) } }, 
                            16: { "question": "You have to make an important speech at a conference or special occasion. You would:", 
                                 "options": { 
                                     "a": (". make diagrams or get graphs to help explain things. ", ["V"]), 
                                     "b": (". write a few key words and practice saying your speech over and over. ", ["A"]), 
                                     "c": (" write out your speech and learn from reading it over several times. ", ["R"]), 
                                     "d": (" gather many examples and stories to make the talk real and practical. ", ["K"]) } } }
        
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
      print("\nYour VARK scores:")
      for style, score in self.scores.items():
            print(f"{style}: {score}")
            highest = max(self.scores, key=self.scores.get)
            print(f"\nYour dominant learning style is likely: {highest}")
            

   
# This code implements a VARK learning style questionnaire program.
 # Runthe quiz

if __name__ == "__main__":
    quiz = VARKQuiz()
    quiz.ask_questions()
    quiz.display_results()

