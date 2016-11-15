from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(u'标题',max_length=256)
    content = models.TextField(u'内容')
    pub_data = models.DateTimeField(u'发表时间',auto_now_add=True,editable=True)
    updata_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)


    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title