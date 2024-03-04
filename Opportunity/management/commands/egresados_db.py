from django.core.management.base import BaseCommand
import os
import json

class Command(BaseCommand):
    help = 'Cargar datos de egresados'
    
    def handle(self, *args, **kwargs):
        json_file_path  = 'Opportunity/management/commands/Dataset.json'  # Asegúrate de que el nombre del archivo sea correcto

        with open(json_file_path, 'r') as file:
            egresados = json.load(file)
