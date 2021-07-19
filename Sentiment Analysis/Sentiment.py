# IMPORTING ALL THE NECESSARY LIBRARIES AND PACKAGES

from nltk.corpus import stopwords
import string



from flask import *
from pathlib import Path
import pickle


def text_process(text):
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template("index.html")


@app.route('/', methods=['GET','POST'])
def success():

        nr = request.form['search']
        ##nr = """Went back to AB a few weekends ago, again for brunch, with a large group.  I was surprised to see that, although they advertise themselves as being a brunch place on the weekends, they have pared their menu down to basically 4 items.  The people that I invited that had never been to AB before were expecting more of a variety in brunch items since I'd told them that they had great brunch, but their concerns were quelled with a few bloody Marys and some good (if not diverse) food.  I had the egg sandwich sans bacon again (excellent again) and Sweet Pea and I split the french toast as well.  We'd only had a small sample of the french toast at the opening, so we didn't realize that it comes with this whole jar of cream and berries, in addition to the syrup.  If you come here for brunch and like french toast, you have to try it.  It's the best french toast I've ever had, and many at our table agreed.  The secret is that they bread it in cornflakes.  Yum.  And, the bloody Marys are in the excellent range, I'd say just below the phenomenal ones at Dick's/Rokerij.  The service was also friendly and quick."""


        # CLEANING THE REVIEWS - REMOVAL OF STOPWORDS AND PUNCTUATION


        filename1 = Path(r'C:\Users\hp\Downloads\pythonProject\Sentiment Analysis\finalized_model_pickle.pk')
        loaded_model1 = pickle.load(open(filename1, 'rb'))

        filename = Path(r'C:\Users\hp\Downloads\pythonProject\Sentiment Analysis\finalized_model.sav')
        # load the model from disk
        loaded_model = pickle.load(open(filename, 'rb'))
        nr_t = loaded_model1.transform([nr])
        result = loaded_model.predict(nr_t)[0]
        if result == 1:
            result = '* ' \
        'Poor- Need to work more hard'
        elif result == 3:
            result = "* * * " \
            "Average - Let's try to up the game"
        else:
            result = '* * * * * ' \
                'Awesome! You are doing great- Keep it up'
        print(result)

        return render_template("output.html", output = result)

if __name__ == '__main__':
    app.run(debug=True)