import unittest
from app.models import Pitch, User, Comments
from app import db

class CommentsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_pitch = Pitch(id=12,pitch_content='Hard work pays off',pitch_category="interview pitch",user = self.user_James)
        self.new_comment = Comments(id=15, comment='good work', user = self.user_James)
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,15)
        self.assertEquals(self.new_comment.comment,'good work')
        self.assertEquals(self.new_comment.user,self.user_James)
    

