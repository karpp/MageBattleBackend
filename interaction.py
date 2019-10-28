import requests

print('Challenge manager')
print('current_challenges:')
a = requests.post('http://109.234.37.174:80/get_challenges/')
print(a.json())

while True:
    s = input('What do you want to do?\n"create" to create new challenge.\n'
              '"add" to add new question to existing challenge\n'
              '"list" to see all challenges\n'
              '"questions" to see all questions from selected challenge\n')

    if s == 'create':
        requests.post('http://109.234.37.174:80/create_challenge/', json={'name': input('Challenge name: '), 'theme': 0})

    elif s == 'add':
        name = input('Challenge name: ')
        q = input('Question: ')
        a0 = input('Answer 1: ')
        a1 = input('Answer 2: ')
        a2 = input('Answer 3: ')
        a3 = input('Answer 4: ')
        corr = int(input('Correct answer(0-3): '))
        diff = 0.0

        requests.post('http://109.234.37.174:80/add_task_to_challenge/', json={'name': name, 'question': q, 'answer0': a0, 'answer1': a1, 'answer2': a2, 'answer3': a3, 'correct': corr, 'difficulty': diff})

    elif s == 'list':
        a = requests.post('http://109.234.37.174:80/get_challenges/')
        print(a.json())

    elif s == 'questions':
        a = requests.post('http://109.234.37.174:80/get_tasks_from_challenge/', json={'name': input('Challenge name: '), 'theme': 0})
        print(a.json())

    elif s == '5':
        pass
