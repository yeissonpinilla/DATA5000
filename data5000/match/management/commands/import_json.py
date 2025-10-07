import json
from pathlib import Path
from django.core.management.base import BaseCommand
from match.models import Match

class Command(BaseCommand):
    help = 'Import JSON files into Django database'

    def add_arguments(self, parser):
        parser.add_argument('folder', type=str, help='Folder containing JSON files')

    def handle(self, *args, **options):
        folder = Path(options['folder'])

        for json_file in folder.glob('*.json'):
            self.stdout.write(f"Processing {json_file}")
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

                for match_data in data:

                    # Handle match
                    match = Match(match_id=match_data['match_id'],
                    country_name=match_data['home_team']['country']['name'],
                    match_date=match_data['match_date'],
                    kick_off=match_data['kick_off'],
                    home_team_gender=match_data['home_team']['home_team_gender'],
                    home_score=match_data['home_score'],
                    visiting_score=match_data['away_score'],
                    match_status=match_data['match_status']
                    )
                    match.save()
        self.stdout.write('Import complete!')
