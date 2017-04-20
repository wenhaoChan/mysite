from django.contrib import admin
from .models import Question, Choice

# Choice对象将在Question管理页面进行编辑，默认情况提供3个Choice对象的编辑区域
# admin.StackedInline列表模式、 admin.TabularInline 扁平化模式
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# 创建一个模型管理类，将它作为第二个参数传递给admin.site.register()，随时随地修改模型的admin选项
class QuestionAdmin(admin.ModelAdmin):
    #这里是调整了字段显示顺序
    # fields = ['pub_date', 'question_text']

    # 字段集合
    # 字段集合中每一个元组的第一个元素是该字段集合的标题
    fieldsets = [
    (None, {'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    # 按顺序显示在“change list”页面上字段简介
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)