# Generated by Django 3.0.8 on 2020-08-27 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xworldblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pageFourImage',
            field=models.ImageField(blank=True, default='', upload_to='xworldblog/images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pageOneImage',
            field=models.ImageField(blank=True, default='', upload_to='xworldblog/images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pageThreeImage',
            field=models.ImageField(blank=True, default='', upload_to='xworldblog/images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pageTwoImage',
            field=models.ImageField(blank=True, default='', upload_to='xworldblog/images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='summaryImage',
            field=models.ImageField(blank=True, default='', upload_to='xworldblog/images/'),
        ),
    ]