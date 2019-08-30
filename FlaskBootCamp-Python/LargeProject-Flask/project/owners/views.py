from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Owner
from project.owners.forms import AddForm

owners_blueprint = Blueprint(
    'owners', __name__, template_folder='templates/owners')


@owners_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        pon_id = form.pon_id.data
        new_owner = Owner(name, pon_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('ponnies.liste'))
    return render_template('add_owner.html', form=form)
