from django.contrib import admin
from .models import Jobs, Lang, Edu, Achievements, Skills, ShowBlocks, BaseInfo


class SwapJobs(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['id']
    actions = ['swap_obj']

    def swap_obj(self, request, queryset):
        if len(queryset) == 2:
            tmp_title = queryset[0].title
            tmp_duration = queryset[0].duration
            tmp_text = queryset[0].text
            tmp_tech = queryset[0].tech
            queryset[0].title = queryset[1].title
            queryset[0].duration = queryset[1].duration
            queryset[0].text = queryset[1].text
            queryset[0].tech = queryset[1].tech
            queryset[1].title = tmp_title
            queryset[1].duration = tmp_duration
            queryset[1].text = tmp_text
            queryset[1].tech = tmp_tech
            queryset[0].save()
            queryset[1].save()
            self.message_user(request, 'Success')
        else:
            self.message_user(request, 'You must select 2 elements')
    swap_obj.short_description = 'Swap Objects'


class ActivateObj(admin.ModelAdmin):
    list_display = ['title', 'show']
    ordering = ['id']
    actions = ['activate', 'deactivate']

    def activate(self, request, queryset):
        for query in queryset:
            query.show = True
            query.save()
        self.message_user(
            request, 'Successfully activated {} elements'.format(len(queryset)))
    activate.short_description = 'Activate'

    def deactivate(self, request, queryset):
        for query in queryset:
            query.show = False
            query.save()
        self.message_user(
            request, 'Successfully DEactivated {} elements'.format(len(queryset)))
    deactivate.short_description = 'Deactivate'


class BaseInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        base_add_permission = super(
            BaseInfoAdmin, self).has_add_permission(request)
        if base_add_permission:
            return not BaseInfo.objects.exists()
        return False


admin.site.register(Jobs, SwapJobs)
admin.site.register(Lang)
admin.site.register(Edu)
admin.site.register(Achievements)
admin.site.register(Skills)
admin.site.register(ShowBlocks, ActivateObj)
admin.site.register(BaseInfo, BaseInfoAdmin)
