from flask import Flask, request, render_template, request
from forms.InputForm import InputForm
from flask_wtf.csrf import CSRFProtect
from PipesAndFilter import *
import math

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY="secret_sauce",
)

@app.route("/", methods=['GET', 'POST'])
def main():
    form = InputForm()
    if request.method == 'POST':
        input = form.input.data
        filter = [form.filter1.data, form.filter2.data, form.filter3.data]

        pipe = Pipeline(input)
        for f in filter:
            if f == "Double":
                pipe.add(filter_double)
            elif f == "Halve":
                pipe.add(filter_halve)
            elif f == "Triple":
                pipe.add(filter_triple)
            elif f == "Multiply with -1":
                pipe.add(filter_minus_one)
            elif f == "Square Root":
                pipe.add(filter_square_root)
        sink = pipe.execute()
        
        if math.isnan(sink):
            sink = ""
        
        return render_template("art.html", form=form, input=input, filter=filter, sink=sink, error=pipe.errors)

    return render_template("main.html", form=form)

csrf = CSRFProtect()

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
