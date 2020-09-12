from django.db import models


class Blog(models.Model):
    category = models.CharField(max_length=200, default='', blank=True)
    title = models.CharField(max_length=200, default='', blank=True)
    by = models.CharField(max_length=200, default='', blank=True)
    contact = models.CharField(max_length=200, default='', blank=True)
    date = models.DateField(default='', blank=True)

# summary
    summary = models.CharField(max_length=200, default='', blank=True)
    summaryImage = models.ImageField(
        upload_to='xworldblog/images/', default='', blank=True)

# pageOne
    pageOneTitle = models.CharField(max_length=200, default='', blank=True)
    pageOneImage = models.ImageField(
        upload_to='xworldblog/images/', default='', blank=True)
    pageOne = models.TextField(default='', blank=True)

# pageTwo
    pageTwoTitle = models.CharField(max_length=200, default='', blank=True)
    pageTwoImage = models.ImageField(
        upload_to='xworldblog/images/', default='', blank=True)
    pageTwo = models.TextField(default='', blank=True)

# pageThree
    pageThreeTitle = models.CharField(max_length=200, default='', blank=True)
    pageThreeImage = models.ImageField(
        upload_to='xworldblog/images/', default='', blank=True)
    pageThree = models.TextField(default='', blank=True)

# pageFour
    pageFourTitle = models.CharField(max_length=200, default='', blank=True)
    pageFourImage = models.ImageField(
        upload_to='xworldblog/images/', default='', blank=True)
    pageFour = models.TextField(default='', blank=True)

    def __str__(self):
        return self.title
