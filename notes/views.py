from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Tag, Note
from accounts.models import *


# Create your views here.
class GradeTable(object):
    def __init__(self, year, user_table=[]):
        self.year = year
        self.user_table = user_table


class UserTable(object):
    def __init__(self, grade, users=[]):
        self.grade = grade
        self.users = users


def top(request):
    # 年度の一覧表を作る
    years = dict([(b.start_time.year, 0) for b in Belong.objects.all()])
    year_list = years.keys()
    year_list = sorted(year_list, reverse=True)

    # 年度毎のテーブルを作る
    grade_tables = []
    for year in year_list:
        user_tables = []
        for grade in Grade.objects.all():
            grade_name = grade.formal_name
            user_belongs = Belong.objects.filter(start_time__year=year, grade__formal_name=grade_name)
            users = []
            for belong in user_belongs:
                users.append(belong.user)
            user_tables.append(UserTable(grade, users))
        grade_tables.append(GradeTable(year, user_tables))

    dictionary = {'grade_tables': grade_tables, 'tags': Tag.objects.all()}
    return render(request, "notes/top.html", dictionary)


def note(request, note_title):
    current_note = get_object_or_404(Note, title=note_title)
    return render(request, "notes/note.html", {"note": current_note})


def tag(request, tag_id):
    current_tag = get_object_or_404(Tag, id=tag_id)
    return render(request, "notes/tag.html", {"tag": current_tag, "notes": Note.objects.all()})


def edit(request, note_title):
    current_note = get_object_or_404(Note, title=note_title)
    return render(request, "notes/edit.html", {"note": current_note})
