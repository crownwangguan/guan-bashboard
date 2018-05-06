from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    corpURL = models.URLField()
    desc = models.CharField(max_length=150)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/company/%Y/%m/%d')

    def __str__(self):
        return self.company

    def save(self, *args, **kwargs):
        super(Job, self).save(*args, **kwargs)


class Project(models.Model):
    company = models.ForeignKey(
        'Job',
        on_delete=models.CASCADE
    )
    projectName = models.CharField(max_length=150)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.projectName


class SkillType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Skill(models.Model):
    SKILL_LEVELS = (
        ('NOV', 'Novice'),
        ('INT', 'Intermediate'),
        ('ADV', 'Advanced'),
        ('EXP', 'Expert')
    )
    desc = models.CharField(max_length=150)
    level = models.CharField(max_length=50, choices=SKILL_LEVELS)
    years = models.IntegerField()
    skill_type = models.ForeignKey(
        'SkillType',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.desc


class Education(models.Model):
    school = models.CharField(max_length=150)
    degree = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    grad = models.DateField()
    image = models.ImageField(upload_to='images/school/%Y/%m/%d')

    def __str__(self):
        return self.school
