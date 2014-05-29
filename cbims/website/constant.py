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
    (4, u'已锁定'),
    (5, u'已删除'),
    )

LEVEL_CHOICES = (
    (0, u'一星'),
    (1, u'二星'),
    (2, u'三星'),
    (3, u'四星'),
    (4, u'五星'),
    )

DISCIPLINE_CHOICES = (
    (0, u'建筑'),
    (1, u'结构'),
    (2, u'给排水'),
    (3, u'暖通'),
    (4, u'电气'),
)

GENDER_CHOICES = (
    ('M', '男'),
    ('F', '女'),
)
# PROVINCES
PROVINCE_CHOICES = (
    (1, u'其他'),
    (2, u'北京'),
    (3, u'上海'),
    (4, u'浙江'),
    (5, u'湖南'),
    (6, u'重庆'),
    (7, u'安徽'),
    (8, u'福建'),
    (9, u'甘肃'),
    (10, u'广东'),
    (11, u'广西'),
    (12, u'贵州'),
    (13, u'海南'),
    (14, u'河北'),
    (15, u'河南'),
    (16, u'黑龙江'),
    (17, u'湖北'),
    (18, u'吉林'),
    (19, u'江苏'),
    (20, u'江西'),
    (21, u'辽宁'),
    (22, u'内蒙古'),
    (23, u'宁夏'),
    (24, u'山东'),
    (25, u'山西'),
    (26, u'陕西'),
    (27, u'四川'),
    (28, u'天津'),
    (29, u'新疆')
)

#PRIVACY
PRIVACY_CHOICES = (
    (0, u'对全网公开'), 
    (1, u'对注册用户公开'), 
    (2, u'对我关注的人公开'), 
    (3, u'对关注我的人公开'),
    (4, u'对关注我和我关注的人公开'),
    (5, u'对互相关注的人公开'),
    (6, u'不公开')
)
