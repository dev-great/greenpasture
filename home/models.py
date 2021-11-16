from django.db import models

# Create your models here.
class Livestream(models.Model):
    Livestream_Title = models.CharField(max_length=45, null=False, verbose_name=u'Livestream Title')
    Livestream_URL = models.CharField(max_length=45, null=False, verbose_name=u'Livestream URL')
    Livestream_Image = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True)

    def __unicode__(self):
        return u'%s' % self.Livestream_Title

    class Meta:
        verbose_name = u'Livestream'
        verbose_name_plural = u'Livestreams'