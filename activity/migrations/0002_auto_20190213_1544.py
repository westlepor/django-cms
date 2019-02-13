# Generated by Django 2.1.7 on 2019-02-13 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
        ('activity', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='members.Organization'),
        ),
        migrations.AddField(
            model_name='talk',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='TalkTopics', to='members.Skill'),
        ),
        migrations.AddField(
            model_name='publication',
            name='members',
            field=models.ManyToManyField(related_name='Publication', to=settings.AUTH_USER_MODEL, verbose_name='Member'),
        ),
        migrations.AddField(
            model_name='publication',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity.Project'),
        ),
        migrations.AddField(
            model_name='publication',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='members.Organization'),
        ),
        migrations.AddField(
            model_name='publication',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='PublicationTopic', to='members.Skill'),
        ),
        migrations.AddField(
            model_name='projectlink',
            name='portal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_links_portal', to='members.Portal', verbose_name='Portal Name'),
        ),
        migrations.AddField(
            model_name='projectlink',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Project'),
        ),
        migrations.AddField(
            model_name='project',
            name='links',
            field=models.ManyToManyField(related_name='ProjectLinks', through='activity.ProjectLink', to='members.Portal'),
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='Project', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='ProjectTopics', to='members.Skill'),
        ),
        migrations.AddField(
            model_name='honour',
            name='certificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity.Certificate'),
        ),
        migrations.AddField(
            model_name='honour',
            name='issuer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='members.Organization'),
        ),
        migrations.AddField(
            model_name='honour',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Honour', to=settings.AUTH_USER_MODEL, verbose_name='Member'),
        ),
        migrations.AddField(
            model_name='honour',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity.Project'),
        ),
        migrations.AddField(
            model_name='honour',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='HonourTopic', to='members.Skill'),
        ),
        migrations.AddField(
            model_name='event',
            name='attendee',
            field=models.ManyToManyField(blank=True, related_name='EventAttendee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='honours',
            field=models.ManyToManyField(blank=True, related_name='EventHonours', to='activity.Honour'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='members.Organization'),
        ),
        migrations.AddField(
            model_name='event',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='EventProject', to='activity.Project'),
        ),
        migrations.AddField(
            model_name='event',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='EventTopics', to='members.Skill'),
        ),
        migrations.AddField(
            model_name='course',
            name='certificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity.Certificate'),
        ),
        migrations.AddField(
            model_name='course',
            name='issuer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='members.Organization'),
        ),
        migrations.AddField(
            model_name='course',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Course', to=settings.AUTH_USER_MODEL, verbose_name='Member'),
        ),
        migrations.AddField(
            model_name='course',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='CourseTopics', to='members.Skill'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='issuer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='members.Organization'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Certificate', to=settings.AUTH_USER_MODEL, verbose_name='Certified'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='CertificateTopics', to='members.Skill'),
        ),
    ]
