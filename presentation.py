from operator import indexOf
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
    inputerror = {}
    inputerror[0] = 0

    if request.method == 'POST':
        input = form.input.data
        number_list = []
        try:
            number_list = input.split(" ")
            for i, n in enumerate(number_list):
                if isinstance(n, int):
                    raise Exception('Not all characters are Integers!')
                else:
                    number_list[i] = int(n)
        except:
            inputerror[0] = 1
            inputerror[1] = "Wrong input! Only integers seperated by a space are allowed!"
            return render_template("main.html", form=form, inputerror = inputerror)

        filter = [form.filter1.data, form.filter2.data, form.filter3.data]
        errorlist = list()
        sink = list()
        iterimlist = list()
        for input in number_list:
            pipe = Pipeline(input)
            for f in filter:
                if f == "Double":
                    pipe.add(filter_double)
                elif f == "Halve":
                    pipe.add(filter_halve)
                elif f == "Multiply with -1":
                    pipe.add(filter_minus_one)
                elif f == "Square Root":
                    pipe.add(filter_square_root)
            temp = pipe.execute()
            iterimlist.append(pipe.interim)
            if not pipe.errors:
                errorlist.append(-1)
            else:
                errorlist.append(pipe.errors)
            if math.isnan(temp):
                temp = ""

            sink.append(temp)
        
        return render_template("art.html", form=form, input=number_list, filter=filter, sink=sink, error=errorlist, inputerror = inputerror, interim=iterimlist)

    return render_template("main.html", form=form, inputerror = inputerror)

csrf = CSRFProtect()

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
