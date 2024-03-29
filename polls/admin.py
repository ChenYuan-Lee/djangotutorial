from django.contrib import admin

from .models import Choice, Question



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        (
            'Date Information',
            {
                'fields': ['pub_date'],
                'classes': ['collapse']
            }
        ),
        (None, {'fields': ['is_open']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'is_open')
    list_filter = ['pub_date']
    search_fields = ['question_text', 'pub_date']

admin.site.register(Question, QuestionAdmin)
