import json
import random
from . import app
from flask import request


class Question:
    def __init__(self, q, ans, cornum, theme=0, difficulty=1.0):
        self.q = q
        self.a = ans
        self.cornum = cornum
        self.theme = theme
        self.difficulty = difficulty

    def json(self):
        return json.dumps(
            {'question': self.q, 'answer0': self.a[0], 'answer1': self.a[1], 'answer2': self.a[2], 'answer3': self.a[3],
             'correct': self.cornum, 'difficulty': self.difficulty, 'subject': self.theme})


class People:
    def __init__(self, name):
        self.name = name
        self.stats = [57, 179, 2, 444]
        self.hp = 57
        self.defence = 10
        self.runes = [2, 15, 1, 4]
        self.current_oponent = -1
        self.is_in_game = False
        self.current_challenge = -1
        self.current_challenge_task = -1
        self.myturn = False


class Challenge:
    def __init__(self, name, tasks=[], theme=0):
        self.name = name
        self.tasks = tasks
        self.theme = theme

    def add_task(self, q):
        self.tasks.append(q)


challenge_db = {'1. Colors': Challenge('1. Colors', [
    Question(q='What color is the grass?', ans=['yellow', 'blue', 'green', 'red'], cornum=2, theme=2),
    Question(q='What color is the sky?', ans=['yellow', 'blue', 'green', 'red'], cornum=1, theme=2),
    Question(q='What color is the sun?', ans=['yellow', 'blue', 'green', 'red'], cornum=0, theme=2)
], 2),
                '2. Numbers': Challenge('2. Numbers', [
                    Question(q="How much is 2 + 2?", ans=['1', '2', '3', '4'], cornum=3, theme=0, difficulty=1.0),
                    Question(q="How much is 1 + 2?", ans=['1', '2', '3', '4'], cornum=2, theme=0, difficulty=1.0),
                    Question(q="How much is 2 + 1?", ans=['1', '2', '3', '4'], cornum=2, theme=0, difficulty=1.0)
                ], 0),
                '3. Nothing': Challenge('3. Nothing', [
                    Question(q="٩(｡•́‿•̀｡)۶?", ans=['corr', 'incorr', 'incorr', 'incorr'], cornum=0, theme=3,
                             difficulty=1.0),
                    Question(q="(＾▽＾)?", ans=['incorr', 'corr', 'incorr', 'incorr'], cornum=1, theme=3, difficulty=1.0),
                    Question(q="(´｡• ω •｡)?", ans=['incorr', 'incorr', 'corr', 'incorr'], cornum=2, theme=3,
                             difficulty=1.0)
                ], 3)}

people_db = [
    People('Volodya'),
    People('Egor')
]

questions_db = [
    Question(q="How much is 2 + 2?", ans=['1', '2', '3', '4'], cornum=3, theme=0, difficulty=1.0),
    Question(q="How much is 1 + 2?", ans=['1', '2', '3', '4'], cornum=2, theme=0, difficulty=1.0),
    Question(q="How much is 2 + 1?", ans=['1', '2', '3', '4'], cornum=2, theme=0, difficulty=1.0),
    Question(q="How much is 1 + 1?", ans=['1', '2', '3', '4'], cornum=1, theme=0, difficulty=1.0),
    Question(q="How much is 1 + 0?", ans=['1', '2', '3', '4'], cornum=0, theme=0, difficulty=1.0),
    Question(q="How much is 57 + 3?", ans=['53', '59', '60', '54'], cornum=2, theme=0, difficulty=1.0),
    Question(q="How much sides does cube have?", ans=['10', '4', '8', '6'], cornum=3, theme=0, difficulty=1.0),
    Question(q="What number is excess?", ans=['2', '6', '10', '3'], cornum=3, theme=0, difficulty=1.0),
    Question(q="How much fingers and toes do you have?", ans=['10', '15', '20', '40'], cornum=2, theme=0,
             difficulty=1.0),
    Question(q="Continue 2, 3, 5, 7, 11 ...", ans=['12', '13', '15', '18'], cornum=1, theme=0, difficulty=1.0),
    Question(q="How much is 52 * 3?", ans=['179', '156', '162', '165'], cornum=1, theme=0, difficulty=1.0),
    Question(q="How much is 15 * 2 / 3?", ans=['10', '15', '40', '5'], cornum=3, theme=0, difficulty=1.0),
    Question(q="How much is 23 + 5?", ans=['28', '23', '-18', '26'], cornum=3, theme=0, difficulty=1.0),
    Question(q="How much decimetres is in metre?", ans=['20', '10', '100', '1000'], cornum=1, theme=0, difficulty=1.0),
    Question(q="How much cantimetres is in metre?", ans=['100', '10', '1000', '10000'], cornum=0, theme=0,
             difficulty=1.0),
    Question(q="How much minutes is in 2 hours?", ans=['60', '90', '200', '120'], cornum=3, theme=0, difficulty=1.0),
    Question(q="How much is 57 / 3?", ans=['21', '19', '13', '17'], cornum=1, theme=0, difficulty=1.0),
    Question(q="How much hours is in three days?", ans=['48', '44', '68', '72'], cornum=3, theme=0, difficulty=1.0),
    Question(q="How much is 57 + 3?", ans=['53', '59', '60', '54'], cornum=3, theme=0, difficulty=1.0),
    Question(q="Which number is divided by 7?", ans=['44', '67', '56', '43'], cornum=2, theme=0, difficulty=1.0),
    Question(q="How much is 3 * 14?", ans=['44', '38', '34', '42'], cornum=3, theme=0, difficulty=1.0),
    Question(q="How much is 25 - 7?", ans=['17', '19', '18', '20'], cornum=2, theme=0, difficulty=1.0),
    Question(q="How much is 7 * 8?", ans=['53', '56', '60', '54'], cornum=1, theme=0, difficulty=1.0),
    Question(q="How much letters „o“ is in this question?", ans=['3', '2', '4', '1'], cornum=0, theme=2,
             difficulty=1.0),
    Question(q="How much is two plus two?", ans=['one', 'two', 'three', 'four'], cornum=3, theme=1, difficulty=1.0),
    Question(q="How much is two plus one?", ans=['one', 'two', 'three', 'four'], cornum=2, theme=1, difficulty=1.0),
    Question(q="How much is one plus two?", ans=['one', 'two', 'three', 'four'], cornum=2, theme=1, difficulty=1.0),
    Question(q="How much is one plus one?", ans=['one', 'two', 'three', 'four'], cornum=1, theme=1, difficulty=1.0),
    Question(q="How much is one plus zero?", ans=['one', 'two', 'three', 'four'], cornum=0, theme=1, difficulty=1.0),
    Question(q="How old is this program?", ans=['year', 'month', 'hour', 'minute'], cornum=3, theme=2, difficulty=1.0),

    Question(q="What is the capital of the UK?", ans=['Moscow', 'London', 'Berlin', 'Paris'], cornum=1, theme=3,
             difficulty=1.0),
    Question(q="What is the capital of France?", ans=['Moscow', 'London', 'Berlin', 'Paris'], cornum=3, theme=3,
             difficulty=1.0),
    Question(q="What is the capital of Germany?", ans=['Moscow', 'London', 'Berlin', 'Paris'], cornum=2, theme=3,
             difficulty=1.0),
    Question(q="What is the capital of Russia?", ans=['Berlin', 'Paris', 'Moscow', 'London'], cornum=2, theme=3,
             difficulty=1.0),
    Question(q="Who if Zeus's wife?", ans=['Aida', 'Hera', 'Aphrodite', 'Juno'], cornum=1, theme=3, difficulty=0.0),
    Question(q="Who is the goddess of Love?", ans=['Venus', 'Flora', 'Vesta', 'Minerva'], cornum=0, theme=3,
             difficulty=1.0),
    Question(q="Who is the goddess of Wisdom?", ans=['Venus', 'Flora', 'Vesta', 'Minerva'], cornum=3, theme=3,
             difficulty=1.0),
    Question(q="Who is the goddess of Flowers?", ans=['Venus', 'Flora', 'Vesta', 'Minerva'], cornum=1, theme=3,
             difficulty=1.0),
    Question(q="Who is the goddess of Family?", ans=['Venus', 'Flora', 'Vesta', 'Minerva'], cornum=2, theme=3,
             difficulty=1.0),
    Question(q="What is the synonym to warm-hearted?", ans=['Jealous', 'Angry', 'Kind', 'Costly'], cornum=2, theme=1,
             difficulty=1.0),
    Question(q="What is the synonym to essential?", ans=['Genious', 'Hot', 'Remote', 'Important'], cornum=3, theme=1,
             difficulty=1.0),
    Question(q="What is the synonym to genuine?", ans=['Authentic', 'New', 'Breathtaking', 'Fabulous'], cornum=0,
             theme=1, difficulty=1.0),

    Question(q="What is ... name?", ans=['she', 'her', 'hers', 'it'], cornum=1, theme=1, difficulty=1.0),
    Question(q="What are you ...?", ans=['doing', 'do', 'does', 'cannot'], cornum=0, theme=1, difficulty=1.0),
    Question(q="-How are you?\n-I'm fine, ...", ans=['alone', 'please', 'thanks', 'do'], cornum=2, theme=1,
             difficulty=1.0),

    Question(q="... is a striped animal", ans=['Tiger', 'Owl', 'Bull', 'Mouse'], cornum=0, theme=1, difficulty=1.0),
    Question(q="... is the capital of Great Britain", ans=['Landan', 'Londan', 'Landon', 'London'], cornum=3, theme=1,
             difficulty=1.0),
    Question(q="Gazpacho is made of ...", ans=['onions', 'potatoes', 'cucumners', 'tomatoes'], cornum=3, theme=1,
             difficulty=1.0)
]
questions_db_0 = [q for q in questions_db if q.theme == 0]
questions_db_1 = [q for q in questions_db if q.theme == 1]
questions_db_2 = [q for q in questions_db if q.theme == 2]
questions_db_3 = [q for q in questions_db if q.theme == 3]


@app.route('/', methods=['GET', 'POST'])
def index():
    return json.dumps({'spell': 'volodya'})


@app.route('/spell/', methods=['GET', 'POST'])
def spell():
    print(request.json)
    js = request.json
    if 'r1' in js and 'r2' in js:
        if js['r1'] == 'Fire':
            if js['r2'] == 'Fire':
                return json.dumps({'spell': 'Cone of fire'})
            if js['r2'] == 'Water':
                return json.dumps({'spell': 'Life Transfusion'})
            if js['r2'] == 'Air':
                return json.dumps({'spell': 'Lighting'})
            if js['r2'] == 'Earth':
                return json.dumps({'spell': 'Lava Armour'})

        if js['r1'] == 'Water':
            if js['r2'] == 'Water':
                return json.dumps({'spell': 'Poseidon\'s Mercy'})
            if js['r2'] == 'Air':
                return json.dumps({'spell': 'Second Breath'})
            if js['r2'] == 'Earth':
                return json.dumps({'spell': 'Gifts Of Earth'})

        if js['r1'] == 'Air':
            if js['r2'] == 'Air':
                return json.dumps({'spell': 'Cold Winds'})
            if js['r2'] == 'Earth':
                return json.dumps({'spell': 'Magic Shield'})

        if js['r1'] == 'Earth':
            if js['r2'] == 'Earth':
                return json.dumps({'spell': 'Stone Armour'})

    return json.dumps({'spell': 'volodya'})


@app.route('/spell_stats/', methods=['GET', 'POST'])
def spell_stats():
    js = request.json
    sp = js['spell']
    stats = [0, 0, 0, 0]  # Deal, Heal, Defense, Barrier

    if sp == 'Cone of fire':
        stats = [10, 0, 0, 0]
    if sp == 'Life Transfusion':
        stats = [5, 5, 0, 0]
    if sp == 'Lighting':
        stats = [5, 0, -1, 0]
    if sp == 'Lava Armour':
        stats = [5, 0, 1, 0]
    if sp == 'Poseidon\'s Mercy':
        stats = [0, 10, 0, 0]
    if sp == 'Second Breath':
        stats = [0, 7, 0, 0]
    if sp == 'Gifts Of Earth':
        stats = [0, 5, 1, 0]
    if sp == 'Cold Winds':
        stats = [0, 0, -2, 0]
    if sp == 'Magic Shield':
        stats = [0, 0, 0, 1]
    if sp == 'Stone Armour':
        stats = [0, 0, 2, 0]

    return json.dumps({'Deal': stats[0], 'Heal': stats[1], 'Defense': stats[2], 'Barrier': stats[3]})


@app.route('/make_magic/', methods=['GET', 'POST'])
def make_magic():
    js = request.json
    me = js['me']
    opponent = js['opponent']
    rune1 = js['rune1']
    rune2 = js['rune2']

    ime = 0
    iop = 0

    for i in range(len(people_db)):
        if people_db[i].name == me:
            ime = i
        if people_db[i].name == opponent:
            iop = i

    print(rune1, rune2)

    if rune1 == 'earth':
        if people_db[ime].runes[0] <= 0:
            return ''
        people_db[ime].runes[0] -= 1
    if rune1 == 'fire':
        if people_db[ime].runes[1] <= 0:
            return ''
        people_db[ime].runes[1] -= 1
    if rune1 == 'air':
        if people_db[ime].runes[2] <= 0:
            return ''
        people_db[ime].runes[2] -= 1
    if rune1 == 'water':
        if people_db[ime].runes[3] <= 0:
            return ''
        people_db[ime].runes[3] -= 1

    if rune1 == 'fire':
        if rune2 == 'fire':
            people_db[iop].hp -= 10
            # return json.dumps({'spell': 'Cone of fire'})
        if rune2 == 'water':
            people_db[iop].hp -= 5
            people_db[ime].hp += 5
            # return json.dumps({'spell': 'Life Transfusion'})
        if rune2 == 'air':
            people_db[iop].hp -= 5
            people_db[ime].defence -= 1
            # return json.dumps({'spell': 'Lighting'})
        if rune2 == 'earth':
            people_db[iop].hp -= 5
            people_db[ime].defence += 1
            # return json.dumps({'spell': 'Lava Armour'})

    if rune1 == 'water':
        if rune2 == 'water':
            people_db[ime].hp += 10
            # return json.dumps({'spell': 'Poseidon\'s Mercy'})
        if rune2 == 'air':
            people_db[ime].hp += 7
            # return json.dumps({'spell': 'Second Breath'})
        if rune2 == 'earth':
            people_db[ime].hp += 5
            people_db[ime].defence += 1
            # return json.dumps({'spell': 'Gifts Of earth'})

    if rune1 == 'air':
        if rune2 == 'air':
            people_db[ime].defence -= 2
            # return json.dumps({'spell': 'Cold Winds'})
        if rune2 == 'earth':
            pass
            # return json.dumps({'spell': 'Magic Shield'})

    if rune1 == 'earth':
        if rune2 == 'earth':
            people_db[ime].defence += 2
            # return json.dumps({'spell': 'Stone Armour'})

    rune1, rune2 = rune2, rune1

    if rune1 == 'earth':
        if people_db[ime].runes[0] <= 0:
            return ''
        people_db[ime].runes[0] -= 1
    if rune1 == 'fire':
        if people_db[ime].runes[1] <= 0:
            return ''
        people_db[ime].runes[1] -= 1
    if rune1 == 'air':
        if people_db[ime].runes[2] <= 0:
            return ''
        people_db[ime].runes[2] -= 1
    if rune1 == 'water':
        if people_db[ime].runes[3] <= 0:
            return ''
        people_db[ime].runes[3] -= 1

    if rune1 == 'fire':
        if rune2 == 'fire':
            people_db[iop].hp -= 10
            # return json.dumps({'spell': 'Cone of fire'})
        if rune2 == 'water':
            people_db[iop].hp -= 5
            people_db[ime].hp += 5
            # return json.dumps({'spell': 'Life Transfusion'})
        if rune2 == 'air':
            people_db[iop].hp -= 5
            people_db[ime].defence -= 1
            # return json.dumps({'spell': 'Lighting'})
        if rune2 == 'earth':
            people_db[iop].hp -= 5
            people_db[ime].defence += 1
            # return json.dumps({'spell': 'Lava Armour'})

    if rune1 == 'water':
        if rune2 == 'water':
            people_db[ime].hp += 10
            # return json.dumps({'spell': 'Poseidon\'s Mercy'})
        if rune2 == 'air':
            people_db[ime].hp += 7
            # return json.dumps({'spell': 'Second Breath'})
        if rune2 == 'earth':
            people_db[ime].hp += 5
            people_db[ime].defence += 1
            # return json.dumps({'spell': 'Gifts Of earth'})

    if rune1 == 'air':
        if rune2 == 'air':
            people_db[ime].defence -= 2
            # return json.dumps({'spell': 'Cold Winds'})
        if rune2 == 'earth':
            pass
            # return json.dumps({'spell': 'Magic Shield'})

    if rune1 == 'earth':
        if rune2 == 'earth':
            people_db[ime].defence += 2
            # return json.dumps({'spell': 'Stone Armour'})

    people_db[iop].myturn = True
    people_db[ime].myturn = False

    return json.dumps({'myhp': people_db[ime].hp, 'mydefence': people_db[ime].defence, 'ophp': people_db[iop].hp,
                       'opdefence': people_db[iop].defence, 'earth': people_db[ime].runes[0],
                       'fire': people_db[ime].runes[1], 'air': people_db[ime].runes[2],
                       'water': people_db[ime].runes[3]})


@app.route('/get_random_question/', methods=['GET', 'POST'])
def rand_question():
    js = request.json
    q = random.choice(questions_db)
    if 'category' in js:
        ct = js['category']
        if ct == 'Math':
            q = random.choice(questions_db_0)
        if ct == 'English':
            q = random.choice(questions_db_1)
        if ct == 'Attentiveness':
            q = random.choice(questions_db_2)
        if ct == 'History':
            q = random.choice(questions_db_3)

    return q.json()


@app.route('/get_answer/', methods=['GET', 'POST'])
def get_ans():
    js = request.json
    q = js['question']

    for quest in questions_db:
        if quest.q == q:
            return json.dumps({'correct': quest.cornum})
    return json.dumps({'correct': 0})


@app.route('/get_person_stats/', methods=['GET', 'POST'])
def get_person_stats():
    js = request.json
    name = js['name']

    for per in people_db:
        if per.name == name:
            return json.dumps(
                {'Math': per.stats[0], 'English': per.stats[1], 'Attentiveness': per.stats[2], 'History': per.stats[3]})
    return json.dumps({'Math': -1, 'English': -1, 'Attentiveness': -1, 'History': -1})


@app.route('/get_hp/', methods=['GET', 'POST'])
def get_hp():
    js = request.json
    name = js['name']

    print(people_db)

    for per in people_db:
        if per.name == name:
            print('HPHPHP', name, per.hp, per.defence)
            return json.dumps({'hp': str(per.hp), 'defence': str(per.defence)})


@app.route('/set_hp/', methods=['GET', 'POST'])
def set_hp():
    js = request.json
    name = js['name']
    hp = js['hp']
    defence = js['defence']

    for i in range(len(people_db)):
        if people_db[i].name == name:
            people_db[i].hp = hp
            people_db[i].defence = defence

    return ''


@app.route('/join_game/', methods=['GET', 'POST'])
def join_game():
    js = request.json
    name = js['name']
    opponent = js['opponent']

    for i in range(len(people_db)):
        if people_db[i].name == name:
            people_db[i].current_oponent = opponent

    return ''


@app.route('/join_challenge/', methods=['GET', 'POST'])
def join_challenge():
    js = request.json
    name = js['name']
    challenge = js['challenge']
    for i in range(len(people_db)):
        if people_db[i].name == name:
            people_db[i].current_challenge = challenge
            people_db[i].current_challenge_task = 0

    print(name, 'joined challenge', challenge)
    return ''


@app.route('/get_new_challenge_task/', methods=['GET', 'POST'])
def get_new_challenge_task():
    js = request.json
    name = js['name']
    ch_name = ''
    ch_name_task = 0

    for i in range(len(people_db)):
        if people_db[i].name == name:
            ch_name = people_db[i].current_challenge
            ch_name_task = people_db[i].current_challenge_task
            print('ASK:', name, ch_name, ch_name_task)
            people_db[i].current_challenge_task += 1

    if ch_name_task >= len(challenge_db[ch_name].tasks):
        return Question("-1", ["-1", "-1", "-1", "-1"], -1, challenge_db[ch_name].theme).json()
    task = challenge_db[ch_name].tasks[ch_name_task]
    return task.json()


@app.route('/is_challenge_finished/', methods=['GET', 'POST'])
def is_challenge_finished():
    js = request.json
    name = js['name']

    ans = 0
    chname = ''
    curcht = 0
    for per in people_db:
        if per.name == name:
            chname = per.current_challenge
            curchq = per.current_challenge_task
    if len(challenge_db[chname].tasks) == curcht:
        ans = 1

    return json.dumps({'isFinished': ans})


@app.route('/create_challenge/', methods=['GET', 'POST'])
def create_challenge():
    js = request.json
    name = js['name']
    theme = js['theme']

    challenge_db[name] = Challenge(name, [], theme)
    return ''


@app.route('/add_task_to_challenge/', methods=['GET', 'POST'])
def add_task_to_challenge():
    js = request.json
    name = js['name']
    question = js['question']
    answer0 = js['answer0']
    answer1 = js['answer1']
    answer2 = js['answer2']
    answer3 = js['answer3']
    correct = js['correct']
    difficulty = js['difficulty']

    challenge_db[name].tasks.append(Question(question, [answer0, answer1, answer2, answer3], correct, 0, difficulty))
    return ''


@app.route('/get_challenges/', methods=['GET', 'POST'])
def get_challenges():
    print(challenge_db)
    ans = list(challenge_db.keys())
    return json.dumps({'Challenges': ans})


@app.route('/get_tasks_from_challenge/', methods=['GET', 'POST'])
def get_tasks():
    js = request.json
    name = js['name']
    ans = challenge_db[name]
    ans = [q.q for q in ans.tasks]
    return json.dumps({'Tasks': ans})


@app.route('/last_3_challenges/', methods=['GET', 'POST'])
def get_last_3_challenges():
    print('!!!')
    print(challenge_db.keys())
    print('!!!')
    chl_names = sorted(list(challenge_db.keys()))[-3:]
    return json.dumps({'challenge1': chl_names[0], 'challenge2': chl_names[1], 'challenge3': chl_names[2]})


@app.route('/get_runes/', methods=['GET', 'POST'])
def get_runes():
    js = request.json
    name = js['name']
    res = [0, 0, 0, 0]

    for i in range(len(people_db)):
        if people_db[i].name == name:
            res = people_db[i].runes

    return json.dumps({'earth': res[0], 'fire': res[1], 'air': res[2], 'water': res[3]})


@app.route('/set_runes/', methods=['GET', 'POST'])
def set_runes():
    js = request.json
    name = js['name']
    res = [js['earth'], js['fire'], js['air'], js['water']]

    for i in range(len(people_db)):
        if people_db[i].name == name:
            people_db[i].runes = res

    return ''


@app.route('/check_turn/', methods=['GET', 'POST'])
def check_turn():
    js = request.json
    name = js['name']
    for i in range(len(people_db)):
        if people_db[i].name == name:
            return json.dumps({'my_turn': people_db[i].myturn})


@app.route('/earn_runes/', methods=['GET', 'POST'])
def earn_runes():
    js = request.json
    score = js['result']
    maxscore = js['maximum']
    profile = int(js['subject'])
    name = js['name']

    # if profile == 'Math':
    #     profile = 0
    # elif profile == 'English':
    #     profile = 1
    # elif profile == 'Attentiveness':
    #     profile = 2
    # else:
    #     profile = 3

    for i in range(len(people_db)):
        if people_db[i].name == name:
            people_db[i].runes[profile] += int(5 * score / maxscore)
            print(name, profile, int(5 * score / maxscore))

    return ''
