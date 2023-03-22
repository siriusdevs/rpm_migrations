from django.contrib import admin
from .models import Person, Hobby, Language, HobbyCategory, PersonHobby, PersonLanguage


class PersonHobby_inline(admin.TabularInline):
    model = PersonHobby
    extra = 1

class PersonLanguage_inline(admin.TabularInline):
    model = PersonLanguage
    extra = 1

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    model = Hobby

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    model = Language

@admin.register(HobbyCategory)
class HobbyCategoryAdmin(admin.ModelAdmin):
    model = HobbyCategory

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    model = Person

    inlines = (
        PersonHobby_inline,
        PersonLanguage_inline
    )