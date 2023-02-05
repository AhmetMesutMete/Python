''' Quiz App'''
import random
class Question:
    '''
    Instance Attributes
    - text, choices, answer
    Instance Methods
    - q1.check_answer('python') => True or False
    '''
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer


    def check_answer(self, ans):
        '''checks if the given answer is correct or not'''
        if ans.lower() not in self.choices:
            raise ValueError('wrong information')
        return self.answer.lower() == ans.lower()


q1 = Question('What is the best programming language?',
    ['python', 'golang', 'java', 'c++'], 'python')
q2 = Question('What is the command to stop an infinite loop in Python?',
    ['end', 'break', 'exit', 'return'], 'break')
q3 = Question('What is the operator to check equality in JavaScript?',
    ['==', '===', '=','equals'], '===')
q4 = Question('What is the keyword used to import a module in Python?',
    ['include', 'import', 'require', 'load'], 'import')

question_list = [q1, q2, q3, q4]
# Quiz Class

class Quiz:
    '''
        Instance Attributes
            -questions, question_index, score
        Instance Methods
            -get_question()
            -display_question()
            -load_question()
            -display_score()
            -display_progress()
    '''
    def __init__(self, questions):
        self.questions = random.sample(questions, len(questions))
        self.question_index = 0
        self.score = 0

    def get_question(self):
        '''fetches question object by question_index'''
        return self.questions[self.question_index]

    def display_question(self):
        '''displays the object fetched with get_question()'''
        question = self.get_question()
        print(f'Question {self.question_index+1}: {question.text}')
        choice_numbering = ['A', 'B', 'C', 'D']
        for choice_number, q_choice in zip(choice_numbering, question.choices):
            print(f'{choice_number}) {q_choice}')
        answer = input('Please write your answer: ')
        if question.check_answer(answer):
            self.score += 100/len(self.questions)
        self.question_index += 1
        self.load_question()

    def load_question(self):
        '''Calls the next question'''
        if self.question_index == len(self.questions):

            self.display_score()
        else:
            self.display_progress()
            self.display_question()

    def display_score(self):
        '''Displays final score'''
        print(f'Your final score is {self.score}')
        correct_ans = int(self.score/(100/len(self.questions)))
        print(f'You answered {correct_ans} out of {len(self.questions)} questions correctly.')

    def display_progress(self):
        '''Shows progress i.e. You are on the 2nd of 5 questions'''
        print(f"You're on question {self.question_index+1} of {len(self.questions)}.")


quiz = Quiz(question_list)
quiz.load_question()
