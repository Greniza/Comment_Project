import csv
import random as rng


def is_float(x):
    '''
    takes in string, returns true if string is of format ####, ##.#, -#.#, or -###.
    else returns false. returns false with -.
    '''
    periodcount = 0
    if not x:
        return False
    if x[0] == '-':
        if x.replace('.','') == '-':
            return False
        x = x[1:]
    for pos in x:
        if pos == '.' and periodcount == 0:
            periodcount = 1
        elif pos in ['1','2','3','4','5','6','7','8','9','0']:
            return False
    return True


# Compiles a dictionary containing the first, last, and preferred names of each student,
# their preferred pronouns (h or s), and their scores for each category
def stud_dict_gen():
    stud_dict = {}
    file = [line for line in csv.reader(open('student_grades.csv', 'r'))]
    headers = file.pop(0)
    for stud in file:
        name = str(f'{stud[1]} {stud[0]}')
        stud_dict[name] = {}
        for tag in range(len(headers)):
            if is_float(stud[tag]):
                stud_dict[name][headers[tag]] = float(stud[tag])
            else:
                stud_dict[name][headers[tag]] = stud[tag]
    del file # Just to free up memory space and all that


def score_class(num):
    if num >= 93:
        return 'pos'
    elif num >= 90:
        return 'pneu'
    elif num >= 83:
        return 'nneu'
    else:
        return 'neg'


def feedback(flt):
    '''
    Generates random feedback based on scores
    '''
    sent_dict = {'pos': ['stellar','excellent','amazing','incredible'],
    'pneu': ['satisfactory','remarkable','commendable','admirable'],
    'nneu': ['decent','adequate','fair','passable'],
    'neg': ['worrying','lacking','deficient','unsatisfactory']}
    return rng.choice(sent_dict[score_class(flt)])


def name_replace(in1):
    '''
    Replaces the first name placeholder with the student's first name
    '''
    in1 = in1.replace('<name>', grades['First']).replace('<namep>', grades['First'] + "'s")
    return in1


def pr_replace(in2):
    '''
    Replaces the first name placeholder with the student's preferred pronoun
    '''
    in2 = in2.replace('<name>', prn[0]).replace('<namep>', prn[2])
    return in2


def combine(in1, in2, comb):
    '''
    Combines assessments of a student's performance in multiple categories
    '''
    in1 = name_replace(in1)
    in2 = pr_replace(in2)
    return in1 + f', {comb} ' + in2 + '. '


def int_to_grade(flt):
    '''
    converts a float score into a grade
    '''
    if flt >= 93:
        return 'A'
    elif flt >= 90:
        return 'A-'
    elif flt >= 87:
        return 'B+'
    elif flt >= 83:
        return 'B'
    else:
        return 'B-'


def comment_gen(stud, grades):
    if grades['First'] != grades['Preferred']:
        q = f'''{grades['First']} "{grades['Preferred']}" {grades['Last']}'''
    else:
        q = f'''{grades['First']} {grades['Last']}'''
    # 'q' is student's full name with nickname, if applicable (i.e. Zachary "Zach" Rahimian)
    cstring = f"Comments for {q}:\n\n" + open('course_description.txt', 'r').read() + '\n\n'
    if grades['Pronoun'] == 'h':
        prn = ['he', 'him', 'his']
    else:
        prn = ['she', 'her', 'her']
    strdct = {}
    adj = feedback(grades['work_ethic']).lower()
    if adj[0] in 'aeiou':
        strdct['work_ethic'] = f"<name> has an {adj} work ethic"
    else:
        strdct['work_ethic'] = f"<name> has a {adj} work ethic"
    adj = feedback(grades['habits']).lower()
    strdct['habits'] = f"<namep> habits are {adj}"
    adj = feedback(grades['homework']).lower()
    strdct['homework'] = f"<name> completes the nightly homework to {adj} standards"
    adj = feedback(grades['participation']).lower()
    strdct['participation'] = f"Overall, <namep> participation this class is <class>{adj}"
    adj = score_class(grades['asks_questions']).lower()
    if adj == 'pos':
        adj = 'fully'
    elif adj == 'pneu':
        adj = 'mostly'
    elif adj == 'nneu':
        adj = 'somewhat'
    else:
        adj = 'not very'
    strdct['asks_questions'] = f"<name> is {adj} comfortable with asking questions"
    adj = feedback(grades['test_avg']).lower()
    strdct['test_avg'] = f"<namep> test average is {adj}"
    adj = feedback(grades['final_score']).lower()
    strdct['final_score'] = f"<namep> performance on the final exam was {adj}"
    adj = feedback(grades['overall_grade']).lower()
    strdct['overall_grade'] = f"<namep> overall grade was {adj}"
    del adj
    kd = {}
    for category in strdct:
        kd[category] = score_class(grades[category])
    if kd['work_ethic'][0] == kd['habits'][0] and kd['work_ethic'][0] == 'p':
        cstring += combine(strdct['work_ethic'], strdct['habits'], 'and')
    elif kd['work_ethic'][0] != kd['habits'][0]:
        if kd['work_ethic'][0] == 'p':
            cstring += combine(strdct['work_ethic'], strdct['habits'], 'but, unfortunately,')
        else:
            cstring += combine(strdct['habits'], strdct['work_ethic'], 'however')
    else:
        cstring += combine(strdct['work_ethic'], strdct['habits'], 'and')
    if rng.choice([True, False]):
        cstring += name_replace(strdct['homework']) + '. '
        if kd['homework'][0] == 'p' and kd['asks_questions'][0] == 'p':
            cstring += 'Furthermore, ' + pr_replace(strdct['asks_questions']) + '. '
        else:
            cstring += prn[0][0].upper() + pr_replace(strdct['asks_questions'])[1:] + '. '
    else:
        cstring += pr_replace(strdct['homework']) + '. '
        if kd['homework'][0] == 'p' and kd['asks_questions'][0] == 'p':
            cstring += 'Furthermore, ' + name_replace(strdct['asks_questions']) + '. '
        else:
            cstring += name_replace(strdct['asks_questions']) + '. '
    cstring += name_replace(strdct['participation']).replace('<class>', '') + f", with an overall grade of {int_to_grade(grades['participation'])}.\n\n"
    cstring += grades['First'] + "'s performance this semester has been " + feedback(grades['overall_grade']) + '. '
    cstring += prn[0].title() + f" has recieved {int_to_grade(grades['test_avg'])}s on most of {prn[2]} tests, with a {int_to_grade(grades['final_score'])} grade on the final exam. "
    cstring += grades['First'] + f" has ended the semester with a grade of {int_to_grade(grades['overall_grade'])}.\n\n"
    return cstring


def main():
    stud_dict_gen()
    for student, grades in stud_dict.items():
        comment_gen(student, grades)
        out = open(f"Student_Output/{stud}.txt", 'w')
    out.write(comment_gen(student, grades).strip())


if __name__ == '__main__':
    main()
