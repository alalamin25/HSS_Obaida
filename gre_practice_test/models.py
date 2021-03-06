from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField
# from django.core.validators import MaxValueValidator, MinValueValidator


# Difficuty choices for a MCQ or Complete Model Test
DIFFICUTY_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)
# For GRE MCQ TYPE
# https://docs.google.com/document/d/1qTh3LXvlUYEwy8nWyMiVC9HFKV0NKg6ZNVsEs1o5Ofg/edit?usp=sharing
# quantitative has these 4 types verbal has some other types

GRE_MCQ_TYPE_CHOICES = (
    ('comparation', 'Comparison Question'),
    ('single', 'Single Answer Question'),
    ('multiple', 'Multiple Answer Question'),
    ('entry', 'Entry Answer Question'),
)

SUBJECT_TYPE_CHOICES = (
    ('quantitative', 'Quantitative Reasoning'),
    ('verbal', 'Verbal Reasoning'),
    ('analytical', 'Analytical Writing'),
)


class GreModelTest(models.Model):

    name = models.CharField(max_length=50)
    fee = models.PositiveSmallIntegerField(default=0)
    # There might be different difficulty model test easy medium hard. User might want to
    # take a easy or medium model test.
    difficulty = models.PositiveSmallIntegerField(
        default=1, choices=DIFFICUTY_CHOICES)

    def __str__(self):
        return self.name


class GreSubjectTest(models.Model):

    name = models.CharField(max_length=50)
    # can this field be bannk and null?
    model_test = models.ForeignKey(GreModelTest, blank=True, null=True)

    # A single subject test might be for gre and might be for GMAT.
    subject_type = models.CharField(choices=SUBJECT_TYPE_CHOICES, max_length=30,
                                    help_text='Select Subject Type: ')
    fee = models.PositiveSmallIntegerField(default=0)
    # Duration is important becasue for gre/SAT/Tofel/gmat one subject test
    # time will be different
    duration = models.PositiveSmallIntegerField(default=30)
    # total marks or per mcq marks is important becasue for gre/SAT/Tofel
    # there will be different no of mcqs in a subject test total marks will be
    # differnt.
    per_mcq_marks = models.PositiveSmallIntegerField(default=1)

    difficulty = models.PositiveSmallIntegerField(
        default=1, choices=DIFFICUTY_CHOICES)

    def __str__(self):
        return self.name


class GreMCQ(models.Model):

    subject_test = models.ForeignKey(GreSubjectTest)

    # For GRE MCQ TYPE
    # https://docs.google.com/document/d/1qTh3LXvlUYEwy8nWyMiVC9HFKV0NKg6ZNVsEs1o5Ofg/edit?usp=sharing
    mcq_type = models.CharField(choices=GRE_MCQ_TYPE_CHOICES, max_length=30,
                                     help_text='Select MCQ Type: ')
    # file will be saved to media/ckeditor_uploads specified in base.py. There are
    # other options to customize upload location
    question = RichTextUploadingField("Question")
    choice_a = models.CharField(max_length=200, blank=True, null=True)
    choice_b = models.CharField(max_length=200, blank=True, null=True)
    choice_c = models.CharField(max_length=200, blank=True, null=True)
    choice_d = models.CharField(max_length=200, blank=True, null=True)
    choice_e = models.CharField(max_length=200, blank=True, null=True)
    # This is just in case if any exam has more than 5 choices.
    choice_f = models.CharField(max_length=200, blank=True, null=True)

    answer = ArrayField(models.CharField(max_length=3))
    answer_explanation = RichTextUploadingField(
        "Answer Explanation: ", blank=True, null=True)
    difficulty = models.PositiveSmallIntegerField(
        default=1, choices=DIFFICUTY_CHOICES)

    def __str__(self):
        return self.question


class GreSubjestTestResult(models.Model):

    '''
        When a user takes a indidual subject wise test the result will be
        stored here.
        If the user takes subject test as a part of complete model test then
        the result will not be stored here
    '''

    user = models.ForeignKey(User)
    subject_test = models.ForeignKey(GreSubjectTest)
    submission_time = models.DateTimeField(blank=True, null=True)
    marks = models.IntegerField(default=0)
    # For saving the answer the user submitted during the test
    user_answers = ArrayField(
        models.PositiveSmallIntegerField(), blank=True, null=True)

    def __str__(self):
        return self.user.username + "  " + subject_test


class GreModelTestResult(models.Model):

    '''
When a user starts a full model test and finishes it the marks will be
stored here

    '''

    user = models.ForeignKey(User)
    model_test = models.ForeignKey(GreModelTest)
    submission_time = models.DateTimeField(blank=True, null=True)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
