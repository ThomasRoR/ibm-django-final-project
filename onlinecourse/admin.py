from django.contrib import admin
# Importe os novos modelos aqui
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Defina as classes inline para Question e Choice
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Registre seus modelos aqui
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Defina a classe QuestionAdmin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Registre os modelos Question e Choice
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)