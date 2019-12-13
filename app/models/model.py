# def scorecalculator(testtype, score, GPA, school):
#     if testtype == "SAT" and score >= 1450 and GPA >= 3.33:
#         return "You are able to get into " + school + "!"
#     if testtype == "ACT" and score >= 30 and GPA >= 3.33:
#         return "You are able to get into " + school + "!"
#     if GPA >= 3.33 and testtype == "SAT" and score < 1450:
#         return "Your GPA is good enough to apply to " + school + ", but your test score needs work."
#     if GPA >= 3.33 and testtype == "ACT" and score < 30:
#         return "Your GPA is good enough to apply to " + school + ", but your test score needs work."
#     if testtype == "SAT" and score >= 1450 and GPA <= 3.33:
#         return "Your test score is good enough to get into " + school + ", but your GPA may let you down."
#     if testtype == "ACT" and score >= 30 and GPA <= 3.33:
#         return "Your test score is good enough to get into " + school + ", but your GPA may let you down."


class Requirements:
  def __init__(self, school, ACTscore, SATscore, GPA):
    self.school = school
    self.ACTscore = ACTscore
    self.SATscore = SATscore
    self.GPA = GPA

listofcolleges = []

listofcolleges.append (Requirements( "Brown", 29, 1530, 3.71))
listofcolleges.append (Requirements( "Harvard", 32, 1590, 3.64))
listofcolleges.append (Requirements( "Yale", 32, 1580, 3.62))
listofcolleges.append (Requirements( "Columbia", 31, 1550, 3.59))
listofcolleges.append (Requirements( "Dartmouth", 30, 1550, 3.54))
listofcolleges.append (Requirements( "U Penn", 31, 1530, 3.52))
listofcolleges.append (Requirements( "Cornell", 30, 1500, 3.50))
listofcolleges.append (Requirements( "Princeton", 31, 1580, 3.49))

print (listofcolleges)

from app import routes


def iterate(school, ACTscore, SATscore, GPA, testtype):
    for item in listofcolleges:
        x = str(item.SATscore - SATscore)
        y = str(item.ACTscore - ACTscore)
        if item.school == school:
            if testtype == "SAT":
                if item.SATscore <= SATscore:
                    return ("Great job! You score among the average "+ item.school + " students!")
                elif item.SATscore > SATscore:
                    return ("You might want to improve your test score. The school average is " + x + " points higher.")
            elif testtype == "ACT":
                if item.ACTscore <= ACTscore:
                    return("Great job! You score among the average "+ item.school + " students!")
                elif item.SATscore > ACTscore:
                    return("You might want to improve your test score. The school average is " + y + " points higher.")

def GPAAA(school, ACTscore, SATscore, GPA, testtype):
    for item in listofcolleges:
        G = item.GPA - GPA
        if item.school == school:
            if item.GPA <= GPA:
                print("Great job! Your GPA is among the average "+ item.school + " students!")
            elif item.GPA > GPA:
                print("You might want to improve your GPA. The school average is " + G + " points higher.")
