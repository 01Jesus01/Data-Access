import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tarea_1.settings')

import django
django.setup()

#   Configuraciones generales
from miapp.models import WebHeros
from faker import Faker

faker_generator = Faker()

def poblar(N=5):
    for web in range(N):
        # web = add_webheros()

        #   Crear datos falsos
        fake_nombre = faker_generator.first_name()
        fake_apellido = faker_generator.last_name()
        fake_correo = faker_generator.email()
        fake_telefono = faker_generator.phone_number()
        
        #   Crear WebHeros ficticios
        webheros = WebHeros.objects.get_or_create(primer_name=fake_nombre, primer_lastname=fake_apellido, correo= fake_correo, tel= fake_telefono)[0]
    

if __name__ == '__main__':
    print("Comienzo a poner los WebHeros")
    poblar(30)
    print("Ya quedo")