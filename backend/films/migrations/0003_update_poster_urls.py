from django.db import migrations


def update_poster_urls(apps, schema_editor):
    Film = apps.get_model('films', 'Film')

    new_urls = {
        'The Pursuit of Happyness': 'https://m.media-amazon.com/images/S/pv-target-images/040701a39c69a59e781b8b57cf965d165c6a9832cc4021a1b62e84d65b72bd6d._UR1920,1080_.jpg',
        'Coco': 'https://spoilertown.com/wp-content/uploads/2024/06/coco-2017.webp',
        'Shutter Island': 'https://thumbnails.cbsig.net/CBS_Production_Entertainment_VMS/2022/07/12/2051131459988/SHTRI_SAlone_16_9_1920x1080_1577032_1920x1080.jpg',
    }

    for title, poster_url in new_urls.items():
        Film.objects.filter(title=title).update(poster_url=poster_url)


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_seed_data'),
    ]

    operations = [
        migrations.RunPython(update_poster_urls, migrations.RunPython.noop),
    ]
