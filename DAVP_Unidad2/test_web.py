from flask import Flask, render_template, request, redirect
from module_cilindro import area

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Practice Cilindro')


@app.route('/exec_equation', methods=['GET', 'POST'])
def execute() -> 'html':
    r = int(request.form['r'])
    h = int(request.form['h'])
    title = 'This is the area result'
    result = area(r, h)
    return render_template('result.html',
                           the_title=title,
                           the_r=r,
                           the_h=h,
                           the_result=result, )


if __name__ == '__main__':
    app.run('localhost', 5001, debug=True)
