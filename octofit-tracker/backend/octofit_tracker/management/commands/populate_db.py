from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (Superheroes)
        users = [
            User.objects.create_user(email='tony@stark.com', username='IronMan', team=marvel, password='testpassword'),
            User.objects.create_user(email='steve@rogers.com', username='CaptainAmerica', team=marvel, password='testpassword'),
            User.objects.create_user(email='bruce@wayne.com', username='Batman', team=dc, password='testpassword'),
            User.objects.create_user(email='clark@kent.com', username='Superman', team=dc, password='testpassword'),
        ]

        # Create Activities
        for user in users:
            Activity.objects.create(user=user, type='Running', duration=30)
            Activity.objects.create(user=user, type='Cycling', duration=45)

        # Create Workouts
        Workout.objects.create(name='Full Body', description='A full body workout')
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
