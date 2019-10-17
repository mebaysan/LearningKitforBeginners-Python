from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Ponny
from project.ponnies.forms import AddForm, DelForm


ponnies_blueprint = Blueprint(
    'ponnies', __name__, template_folder='templates/ponnies')


@ponnies_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_pon = Ponny(name)
        db.session.add(new_pon)
        db.session.commit()
        return redirect(url_for('ponnies_list'))
    return render_template('add.html', form=form)


@ponnies_blueprint.route('/liste')
def liste():
    ponnies = Ponny.query.all()
    return render_template('list.html', ponnies=ponnies)


@ponnies_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pon = Ponny.query.get(id)
        db.session.delete(pon)
        db.session.commit()
        return redirect(url_for('ponnies.liste'))
    return render_template('delete.html', form=form)
