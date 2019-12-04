import random

from faker import Faker
import django.db.models.deletion
from django.db import migrations, models


def load_initial_data(apps, schema_editor):
    Reader = apps.get_model("library", "Readers")
    Book = apps.get_model("library", "Books")
    Readerbooks = apps.get_model("library", "Readerbooks")

    readers = list()
    books = list()
    rbs = list()

    fake = Faker()

    for _ in range(100000):
        title = fake.catch_phrase()
        author = fake.name()

        books.append(Book(title=title, author=author))

    Book.objects.bulk_create(books)

    for _ in range(50000):
        first_name = fake.first_name()
        last_name = fake.last_name()

        reader = Reader(first_name=first_name,
                        last_name=last_name)
        readers.append(reader)

    Reader.objects.bulk_create(readers)

    for reader in readers:
        rb = Readerbooks(book=random.choices(books)[0], reader=reader)
        rbs.append(rb)

        rb = Readerbooks(book=random.choices(books)[0], reader=reader)
        rbs.append(rb)

    Readerbooks.objects.bulk_create(rbs)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Readerbooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Books')),
            ],
        ),
        migrations.CreateModel(
            name='Readers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('books', models.ManyToManyField(through='library.Readerbooks', to='library.Books')),
            ],
        ),
        migrations.AddField(
            model_name='readerbooks',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Readers'),
        ),
        migrations.RunPython(load_initial_data)
    ]
