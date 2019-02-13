# Generated by Django 2.1.7 on 2019-02-13 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('status', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0002_auto_20190213_1544'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='thread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='status.Thread'),
        ),
        migrations.AddField(
            model_name='socialprofile',
            name='portal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Portal', verbose_name='Portal Name'),
        ),
        migrations.AddField(
            model_name='socialprofile',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Profile'),
        ),
        migrations.AddField(
            model_name='responsibility',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='Responsibility', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='responsibility',
            name='thread',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='status.Thread'),
        ),
        migrations.AddField(
            model_name='profile',
            name='experiences',
            field=models.ManyToManyField(related_name='WorkExperiences', through='members.WorkExperience', to='members.Organization'),
        ),
        migrations.AddField(
            model_name='profile',
            name='expertise',
            field=models.ManyToManyField(blank=True, related_name='expertise', to='members.Skill'),
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(blank=True, related_name='interests', to='members.Skill'),
        ),
        migrations.AddField(
            model_name='profile',
            name='languages',
            field=models.ManyToManyField(blank=True, to='members.Language'),
        ),
        migrations.AddField(
            model_name='profile',
            name='links',
            field=models.ManyToManyField(related_name='SocialProfile', through='members.SocialProfile', to='members.Portal'),
        ),
        migrations.AddField(
            model_name='profile',
            name='qualifications',
            field=models.ManyToManyField(related_name='EducationalQualifications', through='members.EducationalQualification', to='members.Organization'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.Role'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='mentorgroup',
            name='mentees',
            field=models.ManyToManyField(related_name='Mentees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mentorgroup',
            name='mentor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Mentor', to=settings.AUTH_USER_MODEL, verbose_name='Mentor Name'),
        ),
        migrations.AddField(
            model_name='leaverecord',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Allover', to=settings.AUTH_USER_MODEL, verbose_name='Approved By (Faculty/Mentor)'),
        ),
        migrations.AddField(
            model_name='leaverecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LeaveRecord', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='Groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='educationalqualification',
            name='certificate',
            field=models.ManyToManyField(blank=True, to='activity.Certificate'),
        ),
        migrations.AddField(
            model_name='educationalqualification',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institution', to='members.Organization', verbose_name='Institution'),
        ),
        migrations.AddField(
            model_name='educationalqualification',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Profile'),
        ),
        migrations.AddField(
            model_name='educationalqualification',
            name='projects',
            field=models.ManyToManyField(blank=True, to='activity.Project'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Attendance', to=settings.AUTH_USER_MODEL),
        ),
    ]
