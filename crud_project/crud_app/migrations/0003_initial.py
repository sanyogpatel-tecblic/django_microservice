

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crud_app', '0002_book_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
