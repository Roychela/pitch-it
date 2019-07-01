from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Pitch, Comments
from .forms import PitchForm, UpdateProfile, CommentsForm
from .. import db, photos
from flask_login import login_required,current_user
from datetime import datetime

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

@main.route('/pitch/<int:id>', methods = ['GET','POST'])
def pitch(id):
    pitch = Pitch.get_pitch(id)
    posted = pitch.posted.strftime('%b %d, %Y')

    if request.args.get("upvote"):
        pitch.upvotes += 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id)) 

    elif request.args.get("downvote"):
        pitch.downvotes+=1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    comment_form = CommentsForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comments(comment = comment,user = current_user,pitch_id = pitch)

        new_comment.save_comment()
    comments = Comments.get_comments(pitch)

    return render_template("pitch.html", pitch = pitch, comment_form = comment_form, comments = comments, date = posted)   
@main.route('/pitch/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        pitch = form.pitch.data
        category = form.category.data
        new_pitch = Pitch(pitch_content=pitch,pitch_category=category,user=current_user, upvotes=0, downvotes=0)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'One Minute pitch'
    return render_template('new_pitch.html',title = title, pitch_form=form)

@main.route('/user/<uname>/pitches')
def user_profile_pitches(uname):
    user = User.query.filter_by(username=uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()

    return render_template("profile/pitches.html", user=user,pitches=pitches)

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


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))