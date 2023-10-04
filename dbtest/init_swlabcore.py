import os
import sys
import django

sys.path.append("../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SWLAB_core.settings")
django.setup()

from lecture.models import Lecture, LectureType
from account.models import User, AdminType


def add_admin():
    print('add root user')
    if User.objects.filter(username='root').exists():
        print('root admin is existed')
    else:
        user = User.objects.create(username='root', email='marsberry@cu.ac.kr',
                                   schoolssn=11111111, realname='root',
                                   admin_type=AdminType.SUPER_ADMIN)
        user.set_password('rootroot')
        user.save()
        print('admin add completed')

def initLectureType():
    print('init Lecture Type')
    ltype = ['프로그래밍', '시스템', '프로젝트', '팀프로젝트']
    for lt in ltype:
        if not LectureType.objects.filter(name=lt).exists():
            print('...add lecture type [%s]'%(lt))
            lect = LectureType.objects.create(name=lt)
            lect.save()
        else:
            print('Lecture Type already has %s'%(lt))

if __name__ == '__main__':
    add_admin()
    initLectureType()