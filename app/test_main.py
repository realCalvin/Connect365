from flask import Flask
from app.models import User
from app.models import Event
from app.models import Friend
from app.models import FriendRequest
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import pytest
 
@pytest.fixture(scope='module')
def new_user():
    user = User(email='TESTING123@gmail.com', username='TESTING123')
    user.set_password('TESTING')
    return user

@pytest.fixture(scope='module')
def new_user1():
    user1 = User(email='TESTING321@gmail.com', username='TESTING321')
    user1.set_password('TESTING')
    return user1

@pytest.fixture(scope='module')
def new_event():
    event = Event(id=1, title="test title", description="test description",
                      date="12/02/2019", startTime="08:30", endTime="11:15")
    return event


# Test 1: Validating New User
def test_new_user(new_user):
    assert new_user.username == 'TESTING123'
    assert new_user.email == 'TESTING123@gmail.com'
    assert new_user.password_hash != 'TESTING'

# Test 2: Validating New User's ID
def test_user_id(new_user):
    new_user.id=17
    assert isinstance(new_user.get_id(),str)
    assert not isinstance(new_user.get_id(),int)
    assert new_user.get_id() == "17"

# Test 3: Testing User Authentication
def test_user_authentication(new_user):
    assert new_user.is_authenticated == True

# Test 4: Testing Create Event
def test_create_event(new_event):
    assert new_event.title == "test title"
    assert new_event.description == "test description"
    assert new_event.date == "12/02/2019"
    assert new_event.startTime == "08:30"
    assert new_event.endTime == "11:15"

# Test 5: Test Friend Request
def test_friend_request(new_user, new_user1):
    friend_request = FriendRequest(author=new_user, requester_username=new_user.username, friend_username=new_user1.username, request_status=True)
    assert friend_request.request_status == True

# Test 6: Test Friend System
def test_friend_system(new_user, new_user1):
    friend1 = Friend(author=new_user, friend_username=new_user1.username)
    friend2 = Friend(author=new_user1, friend_username=new_user.username)
    assert friend1.friend_username == new_user1.username and friend2.friend_username == new_user.username

# Test 7: Test Setting User's Status
def test_user_status(new_user):
    new_user.status = 0 # sets to busy
    assert new_user.status == 0

# Test 8: Test Edit Event
def test_edit_event(new_event):
    new_event.title = "testing"
    new_event.description = "hello"
    new_event.date = "12/05/2020"
    new_event.startTime = "12:00"
    new_event.endTime = "18:50"
    assert new_event.title == "testing"
    assert new_event.description == "hello"
    assert new_event.date == "12/05/2020"
    assert new_event.startTime == "12:00"
    assert new_event.endTime == "18:50"

# https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/