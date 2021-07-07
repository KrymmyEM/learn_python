from enum import Enum

class AnswerQuestion(Enum):
    ANSWER = 1
    QUESTION = 2

ans = AnswerQuestion.ANSWER
print(AnswerQuestion.QUESTION.name)
