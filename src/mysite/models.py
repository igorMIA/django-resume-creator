from django.db import models


class Jobs(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    text = models.TextField()
    tech = models.TextField()

    def tech_as_list(self):
        return self.tech.split()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'


class Lang(models.Model):
    title = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Edu(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'


class Achievements(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'


class Skills(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class ShowBlocks(models.Model):
    title = models.CharField(max_length=255)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Block'
        verbose_name_plural = 'Blocks'


class BaseInfo(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    career_summary = models.TextField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.description)

    class Meta:
        verbose_name = 'BaseInfo'
        verbose_name_plural = 'BaseInfo'
