from django.contrib import admin
from core.models import CheckList,CheckListItem
# Register your models here.

@admin.register(CheckList)
class ChecklistAdmin(admin.ModelAdmin):
    list_display=('id','title','is_deleted','is_archived','created_on','updated_on')

@admin.register(CheckListItem)
class CheckListItemAdmin(admin.ModelAdmin):
    list_display=('id','text','is_checked','created_on','updated_on','checklist')

