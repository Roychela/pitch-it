from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Pitch, Comments


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