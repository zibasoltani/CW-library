from django.contrib import admin
from .models import Book, Loan, Member


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    list_display = ('title', 'author', 'available', 'published_date')
    list_filter = ('published_date', 'available')
    search_fields = ('author',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "fullname"]
    list_display_links = ["first_name", "last_name"]
    search_fields = ["last_name"]

    def fullname(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    fullname.admin_order_field = 'first_name'


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'loan_date', 'return_date')
    # list_filter = ('published_date', 'available')
    # search_fields = ('author',)
