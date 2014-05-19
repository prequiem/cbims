from django.db import models

class SingleChoiceQuestion（models.Model):

    # Answer info
    choice = models.IntegerField('正确答案', choices = SINGLE_CHOICES)
    explanation = models.TextField('答案解析')
    clause_related = models.ManyToManyField(Clause, verbose_name = u'规范条文', blank = True)
    

