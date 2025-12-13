from flask import Flask, render_template, request

app = Flask(__name__)

JOBS = [
    {
    'id': 1,
    'title':'Data Analyst',
    'location':'New York',
    'salary':'$10000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Los Angeles',
        'salary': '$12000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'San Francisco',
        'salary': '$13000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Remote',
        'salary': '$9000'
    },
]


@app.route('/')
def hello_jovian():
    return render_template('home.html',jobs=JOBS,company_name='Jovian')

if __name__ == '__main__':#assign the host
    app.run(debug=True)
