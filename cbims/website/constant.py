# coding: utf-8

# time
ONE_DAY = 86400
ONE_WEEK = ONE_DAY * 7
ONE_MONTH = ONE_DAY * 30

WEEK_DAY = [u'周一', u'周二', u'周三', u'周四', u'周五', u'周六', u'周日']

# PROBLEM_STATUS

PROBLEM_STATUS_REJECT = 0
PROBLEM_STATUS_ACCEPT = 1
PROBLEM_STATUS_WAITING = 2
PROBLEM_STATUS_REVIEW = 3
PROBLEM_STATUS_DELETE = 4

PROBLEM_STATUS = (
    (0, u'审核失败'),
    (1, u'审核通过'),
    (2, u'等待审核'),
    (3, u'审核失败，请根据要求修改后重新提交'),
    (4, u'已删除'),
    )

LEVEL_CHOICES = (
    (0, u'一星'),
    (1, u'二星'),
    (2, u'三星'),
    (3, u'四星'),
    (4, u'五星'),
    )
