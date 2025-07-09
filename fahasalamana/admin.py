from django.contrib import admin
from .models import *
from django.utils.html import format_html

@admin.register(ZavaManiry)
class ZavaManiryAdmin(admin.ModelAdmin):
    list_display = ('anarana', 'famaritana', 'daty_nampidirana')
    search_fields = ('anarana', 'famaritana')
    list_filter = ('daty_nampidirana',)
    ordering = ('-daty_nampidirana',)
    filter_horizontal = ('aretina_tsaboina',) 

@admin.register(Aretina)
class AretinaAdmin(admin.ModelAdmin):
    list_display = ('anarana', 'famaritana', 'daty_nampidirana')
    search_fields = ('anarana', 'famaritana')
    list_filter = ('daty_nampidirana',)
    ordering = ('-daty_nampidirana',)

@admin.register(Fitsaboana)
class FitsaboanaAdmin(admin.ModelAdmin):
    list_display = ('zava_maniry', 'aretina', 'daty_nampidirana')
    search_fields = ('zava_maniry__anarana', 'aretina__anarana', 'fomba_fampiasana')
    list_filter = ('daty_nampidirana', 'zava_maniry', 'aretina')
    ordering = ('-daty_nampidirana',)

@admin.register(Mpitsabo)
class MpitsaboAdmin(admin.ModelAdmin):
    list_display = ('anarana',)
    search_fields = ('anarana',)

@admin.register(Fanafody)
class FanafodyAdmin(admin.ModelAdmin):
    list_display = ('anarana', 'vidiny', 'daty_nampidirana', 'sary_thumbnail')
    
    search_fields = ('anarana', 'famaritana')
    
    list_filter = ('daty_nampidirana',)

    fieldsets = (
        (None, {
            'fields': ('anarana', 'famaritana', 'vidiny', 'sary')
        }),
        ('Daty Fampidirana', {
            'fields': ('daty_nampidirana',),
            'classes': ('collapse',), 
        }),
    )

    readonly_fields = ('daty_nampidirana',)

    def sary_thumbnail(self, obj):
        if obj.sary:
            return format_html('<img src="{}" width="50" height="50" />', obj.sary.url)
        return "Tsy misy sary"
    sary_thumbnail.short_description = "Sary Kely" 

@admin.register(Sosokevitra)
class SosokevitraAdmin(admin.ModelAdmin):
    list_display = ('lohateny', 'daty_nampidirana') # Inona no haseho ao amin'ny lisitra
    search_fields = ('lohateny', 'ambara')