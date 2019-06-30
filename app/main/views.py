from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Pitch, Comments
from .forms import PitchForm, UpdateProfile, CommentsForm
from .. import db

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting pitches from the different categories
    interview_pitches = Pitch.get_pitches('interview')
    product_pitches = Pitch.get_pitches('product')
    promotion_pitches = Pitch.get_pitches('promotion')
    pickup_lines = Pitch.get_pitches('pickup')
    title = 'Home - Welcome to The best One Minute Pitch Online Website'
    
    return render_template('index.html', title = title, interview=interview_pitches, product=product_pitches, promotion=promotion_pitches, pickup=pickup_lines)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)  

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)