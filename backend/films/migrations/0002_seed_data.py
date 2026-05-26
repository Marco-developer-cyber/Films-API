from django.db import migrations


def seed_data(apps, schema_editor):
    Category = apps.get_model('films', 'Category')
    Film = apps.get_model('films', 'Film')

    categories = {
        'sci-fi': Category.objects.create(
            name='Sci-Fi',
            slug='sci-fi',
            description='Kelajak, kosmos va katta g‘oyalar haqidagi filmlar.',
        ),
        'adventure': Category.objects.create(
            name='Adventure',
            slug='adventure',
            description='Sarguzasht, yo‘l va kutilmagan voqealarga boy filmlar.',
        ),
        'drama': Category.objects.create(
            name='Drama',
            slug='drama',
            description='Hissiyotlar, qarorlar va hayot sinovlari markazidagi filmlar.',
        ),
        'animation': Category.objects.create(
            name='Animation',
            slug='animation',
            description='Oilaviy va ilhomlantiruvchi animatsion hikoyalar.',
        ),
        'thriller': Category.objects.create(
            name='Thriller',
            slug='thriller',
            description='Taranglik, sir va kutilmagan burilishlarga boy filmlar.',
        ),
    }

    Film.objects.bulk_create([
        Film(
            category=categories['sci-fi'],
            title='Interstellar',
            year=2014,
            director='Christopher Nolan',
            rating='8.7',
            duration=169,
            country='USA',
            poster_url='https://pgsramblings.files.wordpress.com/2015/04/interstellar-featured.jpg',
            description='Insoniyat uchun yangi uy qidirgan tadqiqotchilar vaqt, muhabbat va jasorat chegaralarini sinovdan o‘tkazadi.',
            highlight='Kosmos, vaqt va oilaviy drama bir kadrda.',
        ),
        Film(
            category=categories['adventure'],
            title='The Lord of the Rings: The Fellowship of the Ring',
            year=2001,
            director='Peter Jackson',
            rating='8.8',
            duration=178,
            country='New Zealand',
            poster_url='https://m.media-amazon.com/images/I/81EBp0vOZZL.jpg',
            description='Bir uzuk taqdirini hal qilish uchun boshlangan xavfli safar katta sarguzashtga aylanadi.',
            highlight='Do‘stlik va jasorat epik yo‘lda sinovdan o‘tadi.',
        ),
        Film(
            category=categories['drama'],
            title='The Pursuit of Happyness',
            year=2006,
            director='Gabriele Muccino',
            rating='8.0',
            duration=117,
            country='USA',
            poster_url='https://m.media-amazon.com/images/I/71zM8j3Y8GL._AC_SY679_.jpg',
            description='Qiyin hayotiy sharoitda ham orzusidan voz kechmagan otaning ta’sirli hikoyasi.',
            highlight='Sabr va mehnat haqiqiy umidga aylangan hikoya.',
        ),
        Film(
            category=categories['animation'],
            title='Coco',
            year=2017,
            director='Lee Unkrich',
            rating='8.4',
            duration=105,
            country='USA',
            poster_url='https://m.media-amazon.com/images/I/91WfA4a8HnL._AC_SY679_.jpg',
            description='Musiqa orzusidagi bola sirli olamga tushib, oila qadriyatlarini boshqacha kashf etadi.',
            highlight='Rang-barang dunyo va yurakka yaqin oilaviy hikoya.',
        ),
        Film(
            category=categories['thriller'],
            title='Shutter Island',
            year=2010,
            director='Martin Scorsese',
            rating='8.2',
            duration=138,
            country='USA',
            poster_url='https://m.media-amazon.com/images/I/81Yj4jK6A-L._AC_SY679_.jpg',
            description='Yo‘qolgan bemorni izlash jarayonida detektiv ong va haqiqat chegarasida qoladi.',
            highlight='Psixologik bosim va sirlar oxirigacha ushlab turadi.',
        ),
    ])


def unseed_data(apps, schema_editor):
    Category = apps.get_model('films', 'Category')
    Category.objects.filter(slug__in=['sci-fi', 'adventure', 'drama', 'animation', 'thriller']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
