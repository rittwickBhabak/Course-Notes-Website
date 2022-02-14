import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from posts.models import Post
from faker import Faker
import random

fakegen = Faker()

def populate(N):

    for entry in range(N):

        no_of_words_in_title = random.randint(5,20)
        fake_title = [fakegen.name() for _ in range(no_of_words_in_title)]
        fake_title = ' '.join(fake_title)
        fake_content = ''
        tag_list = ['Fake', 'data', 'generation', 'like', 'name', 'address', 'email', 'text', 'sentence', 'etc']

        no_of_sentencts = random.randint(50, 80)
        no_of_tags = random.randint(0, len(tag_list))
        for _ in range(no_of_sentencts):
            fake_content = fake_content + fakegen.sentence()
        
        tags = [random.choice(tag_list) for _ in range(no_of_tags)]
        tags = ', '.join(tags)
        print(tags)
        try:
            Post.objects.create(title=fake_title, content=fake_content, tags=tags)
        except:
            print('Error')

        
       

if __name__ == "__main__":
    print('Populating...')
    populate(20)
    print('Complete!')