import graphene
from graphql_jwt.decorators import login_required
from datetime import date, datetime, timedelta
from django.db.models import Avg, Count, Sum

import dateutil.parser
from framework.api.user import UserBasicObj
from django.contrib.auth.models import User

import json

from ..models import Log
from members.models import Group

from .dailyAttendance import Query as dailyAttendanceQuery


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


class userAttStatObj(graphene.ObjectType):
    user = graphene.Field(UserBasicObj)
    presentCount = graphene.String()
    avgDuration = graphene.String()
    totalDuration = graphene.String()

    def resolve_user(self, info):
        return User.objects.values().get(id=self['member'])


class userDailyAttendanceObj(attendanceDateObj):
    user = graphene.Field(UserBasicObj)

    def resolve_user(self, info):
        return User.objects.values().get(id=self['member_id'])


class dailyAttendanceObj(graphene.ObjectType):
    date = graphene.types.datetime.Date()
    membersPresent = graphene.Int()
    avgDuration = graphene.String()
    members = graphene.List(userDailyAttendanceObj)

    def def_date(self, info):
        return self['date']

    def resolve_membersPresent(self, info):
        return len(self['log'])

    def resolve_avgDuration(self, info):
        return self['log'].aggregate(Avg('duration'))['duration__avg']

    def resolve_members(self, info):
        return self['log'].values()


class clubAttendanceObj(graphene.ObjectType):
    avgDuration = graphene.String()
    workingDaysCount = graphene.String()
    dailyLog = graphene.List(dailyAttendanceObj)
    memberStats = graphene.List(userAttStatObj, order=graphene.String())

    def resolve_avgDuration(self, info):
        return self['avgDuration']['duration__avg']

    def resolve_workingDaysCount(self, info):
        return len(self['logs'].values_list('date').distinct())

    def resolve_dailyLog(self, info):
        sdate = self['start']
        delta = self['end'] - sdate
        days = []
        for i in range(delta.days + 1):
            days.append(sdate + timedelta(days=i))
        logs = []
        for day in days:
            logs.append({"date": day, "log": self['logs'].filter(date=day)})
        return logs

    def resolve_memberStats(self, info, **kwargs):
        order = kwargs.get('order')
        if order is None:
            order = '-presentCount'
        return self['logs'].values('member').annotate(
            presentCount=Count('member'),
            avgDuration=Avg('duration'),
            totalDuration=Sum('duration')).order_by(order, '-presentCount', '-totalDuration')


class attendanceUserObj(UserBasicObj):
    firstSeenToday = graphene.String()
    lastSeen = graphene.String()
    duration = graphene.String()

    def resolve_firstSeenToday(self, info):
        today = date.today()
        obj = Log.objects.filter(date=today, member__username=self['username'])[0]
        if obj:
            sessions = json.loads(obj.sessions)
            return sessions[0]['start']
        else:
            return None

    def resolve_lastSeen(self, info):
        obj = Log.objects.filter(member__username=self['username']).order_by('-date').first()
        if obj:
            return obj.lastSeen
        else:
            return None

    def resolve_duration(self, info):
        obj = Log.objects.filter(member__username=self['username']).order_by('-date').first()
        if obj:
            return obj.duration
        else:
            return None


class attendanceStatObj(graphene.ObjectType):
    count = graphene.Int()
    members = graphene.List(attendanceUserObj)

    def resolve_members(self, info):
        return User.objects.values().filter(username__in=self['members'])


class liveAttendanceObj(graphene.ObjectType):
    membersPresent = graphene.Field(attendanceStatObj)

    def resolve_membersPresent(self, info):
        count = len(self)
        return {'count': count, 'members': self}


class Query(dailyAttendanceQuery, object):
    liveAttendance = graphene.Field(liveAttendanceObj)
    clubAttendance = graphene.Field(clubAttendanceObj,
                                    startDate=graphene.types.datetime.Date(required=True),
                                    endDate=graphene.types.datetime.Date()
                                    )

    @login_required
    def resolve_liveAttendance(self, info):
        time = datetime.now() - timedelta(minutes=5)
        logs = Log.objects.filter(lastSeen__gte=time).values('member__username')
        u = []
        for i in logs:
            u.append(i['member__username'])
        return u

    @login_required
    def resolve_clubAttendance(self, info, **kwargs):
        start = kwargs.get('startDate')
        end = kwargs.get('endDate')
        logs = Log.objects.all()
        if start is not None:
            logs = logs.filter(date__gte=start)
        else:
            raise Exception('Start date required')
        if end is not None:
            logs = logs.filter(date__lte=end)
        else:
            end = date.today()
        data = {
            'logs': logs,
            'avgDuration': logs.aggregate(Avg('duration')),
            'start': start,
            'end': end
        }
        return data
