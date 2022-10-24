from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.offer import Offer
from models.engine.db import DBStorage

offers = Blueprint("offers", __name__)


@offers.route('/')
def index():
    offers = Offer.query.all()
    return render_template('index.html', offers=offers)


@offers.route('/new', methods=['POST'])
def add_offers():
    if request.method == 'POST':

        # create a new offers object
        new_offers = Offer(fullname, email, phone)

        # save the object into the database
        DBStorage.session.add(new_offers)
        DBStorage.session.commit()

        flash('Contact added successfully!')

        return redirect(url_for('offers.index'))


@offers.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    # get offers by Id
    print(id)
    offers = Offer.query.get(id)

    if request.method == "POST":
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        DBStorage.session.commit()

        flash('Offer updated successfully!')

        return redirect(url_for('offers.index'))

    return render_template("update.html", offers=offers)


@offers.route("/delete/<id>", methods=["GET"])
def delete(id):
    offers = Offer.query.get(id)
    DBStorage.session.delete(offers)
    DBStorage.session.commit()

    flash('Offer deleted successfully!')

    return redirect(url_for('offers.index'))


@offers.route("/about")
def about():
    return render_template("about.html")