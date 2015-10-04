from flask import Blueprint, render_template

frontend = Blueprint(
        'frontend',
        __name__,
        template_folder='templates',
        static_folder='static')

@frontend.route('/parallax-star')
def parallax_star():
    return render_template(
        'parallax-star/index.html'
    )