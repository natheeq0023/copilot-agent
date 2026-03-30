from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Team, Activity, Workout, Leaderboard
from django.contrib.auth import get_user_model

User = get_user_model()

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=10, distance=2.5)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=50)

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_teams(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activities(self):
        response = self.client.get('/activities/')
        self.assertEqual(response.status_code, 200)

    def test_workouts(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)
