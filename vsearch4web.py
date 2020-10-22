from flask import Flask, render_template, request
from vsearch import search4letters
app = Flask(__name__)

def log_request (req: 'flask_request', res: str) -> None:
    with open('log.txt', 'a') as log:
        print (req,res, file=log)

@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))    
    log_request(request, results)
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title, the_results=results,)
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
    the_title='Welcome to search4letters on the web!')
@app.route('/viewlog')
def view_the_log() -> str:
    contents = []
    with open('log.txt') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    return str(contents)
    return contents
if __name__=='__main__':
    app.run(debug=True)