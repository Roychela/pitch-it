import unittest
from app.models import Pitch, User
from app import db

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_pitch = Pitch(id=12,pitch_content='Hard work pays off',pitch_category="interview pitch",user = self.user_James)
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,12)
        self.assertEquals(self.new_pitch.pitch_content,'Hard work pays off')
        self.assertEquals(self.new_pitch.pitch_category,"interview pitch")
        self.assertEquals(self.new_pitch.user,self.user_James)
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitch(12)
        self.assertTrue(got_pitch is not None)
