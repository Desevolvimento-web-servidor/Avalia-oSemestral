from datetime import datetime, timezone
from flask import flash, redirect, render_template, url_for
from .. import db
from ..models import Disciplina, Semestre
from . import main
from .forms import DisciplinaForm


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template(
        'index.html',
        current_time=datetime.now(timezone.utc)
    )

@main.route('/disciplina', methods=['GET', 'POST'])
def disciplina():
    form = DisciplinaForm()

    if form.validate_on_submit():
        semestre_obj = Semestre.query.filter_by(nome=form.semestre.data).first()
        if not semestre_obj:
            semestre_obj = Semestre(nome=form.semestre.data)
            db.session.add(semestre_obj)

        nova_disciplina = Disciplina(
            nome=form.nome.data.strip(),
            semestre=semestre_obj
        )
        db.session.add(nova_disciplina)
        db.session.commit()
        flash('Disciplina cadastrada com sucesso!')
        return redirect(url_for('main.disciplina'))

    disciplinas = Disciplina.query.order_by(Disciplina.id.asc()).all()
    return render_template(
        'disciplina.html',
        form=form,
        disciplinas=disciplinas,
        current_time=datetime.now(timezone.utc)
    )

@main.route('/indisponivel')
def indisponivel():
    return render_template(
        'indisponivel.html',
        current_time=datetime.now(timezone.utc))
