from django.contrib import admin
from .models import *
# Register your models here.

class ChoiceInline(
    # each choice is a separate table
        # admin.StackedInline
    # each choice is a row in table
    admin.TabularInline
):
    model = Choice
#     generate 3 Choice fields by default
    extra=3
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, { 'fields': ['question_text']}),
        ('Date Information', {'fields':['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)