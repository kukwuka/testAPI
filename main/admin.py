from django.contrib import admin
from .models import Answer, Question , Poll , Asked_Questions , Asked_Pools







class QuestionAdmin(admin.ModelAdmin):
   
    filter_horizontal =('test_answers',)


class PollAdmin(admin.ModelAdmin):
    
    filter_horizontal = ('questions',)
    

    def get_readonly_fields(self, request, obj=None):
        if obj: # when editing an object
            return ['start_date']
        return self.readonly_fields


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )





#if u wana see asked questions uncomend all

class Asked_PoolsAdmin(admin.ModelAdmin):
	

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False



class Asked_QuestionsAdmin(admin.ModelAdmin):

	filter_horizontal = ('answer_choosed',)

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False






admin.site.register(Question , QuestionAdmin)
admin.site.register(Answer , AnswerAdmin)
admin.site.register(Poll , PollAdmin )
admin.site.register(Asked_Questions , Asked_QuestionsAdmin)
admin.site.register(Asked_Pools , Asked_PoolsAdmin )



