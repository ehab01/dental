from django.contrib import admin
from .models import Post
from django.core.exceptions import ValidationError
from core.helpers import send_push_notification
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'text')
    fields = ('title', 'text','media_type' ,'media')

    def save_model(self, request, obj, form, change):
        try:
            obj.save()

            # Send notification to all users
            title = "New Post Available"
            message = f"A new post titled '{obj.title}' has been added. Check it out!"

            users = User.objects.exclude(player_id__isnull=True).exclude(player_id__exact='')
            for user in users:
                send_push_notification(user.player_id, title, message)

        except ValidationError as e:
            messages.error(request, e.message)    
