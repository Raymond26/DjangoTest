from polls.models import Poll, Choice
from django.contrib import admin

# Making adding choices to polls easier
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Example of customizing admin form
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)