import graphene
from graphql_jwt.decorators import login_required
from django.db.models import F
from datetime import date, datetime, timedelta
from django.db.models import Avg
import dateutil.parser
from django.utils import timezone
from framework.api.user import UserBasicObj
from django.contrib.auth.models import User

import json

from ..models import Log
from members.models import Group


class timePeriodObj(graphene.ObjectType):
    start = graphene.String()
    end = graphene.String()
    duration = graphene.String()

    def resolve_duration(self, info):
        diff = dateutil.parser.parse(self['end']) - dateutil.parser.parse(self['start'])
        return diff


class attendanceDateObj(timePeriodObj, graphene.ObjectType):
    sessions = graphene.List(timePeriodObj)
    date = graphene.String()

    def resolve_duration(self, info):
        return self['duration']

    def resolve_start(self, info):
        jsonData = json.loads(self['sessions'])
        if jsonData:
            return jsonData[0]['start']
        else:
            return None

    def resolve_end(self, info):
        jsonData = json.loads(self['sessions'])
        if jsonData:
            return jsonData[-1]['end']
        else:
            return None

    def resolve_sessions(self, info):
        jsonData = json.loads(self['sessions'])
        if jsonData:
            return jsonData
        else:
            return None

class userAttendanceObj(graphene.ObjectType):
    daysPresent = graphene.Int()
    avgDuration = graphene.String()
    dailyLog = graphene.List(attendanceDateObj)

    def resolve_daysPresent(self, info):
        return len(self['logs'])

    def resolve_avgDuration(self, info):
        return self['avgDuration']['duration__avg']

    def resolve_dailyLog(self, info):
        return self['logs']

class attendanceStatObj(graphene.ObjectType):
    count = graphene.Int()
    members = graphene.List(UserBasicObj)

    def resolve_members(self, info):
        return User.objects.values().filter(username__in=self['members'])


class liveAttendanceObj(graphene.ObjectType):
    membersPresent = graphene.Field(attendanceStatObj)
    membersAbsent = graphene.Field(attendanceStatObj)

    def resolve_membersPresent(self, info):
        count = len(self)
        return {'count': count, 'members': self}

    def resolve_membersAbsent(self, info):
        groups = Group.objects.filter(attendanceEnabled=True).values('members__username')
        usernames = []
        for member in groups:
            username = member['members__username']
            if username not in self:
                usernames.append(username)
        count = len(usernames)
        return {'count': count, 'members': usernames}


class Query(object):
    liveAttendance = graphene.Field(liveAttendanceObj)
    userAttendance = graphene.Field(userAttendanceObj, username=graphene.String(required=True))

    @login_required
    def resolve_liveAttendance(self, info):
        time = datetime.now() - timedelta(minutes=5)
        logs = Log.objects.filter(lastSeen__gte=time).values('member__username')
        u = []
        for i in logs:
            u.append(i['member__username'])
        return u

    @login_required
    def resolve_userAttendance(self, info, **kwargs):
        username = kwargs.get('username')
        logs = Log.objects.filter(member__username=username)
        data = {}
        data['logs'] = logs.values()
        data['avgDuration'] = logs.aggregate(Avg('duration'))
        return data
