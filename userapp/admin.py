from django.contrib import admin
from .models import User
from .models import Tag
from .models import Video
from .models import User_ID
from .models import Comment
from .models import Video_category
from .models import History
from .models import Video_Reaction
from .models import Video_share
from .models import Login

# Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(User_ID)
admin.site.register(Comment)
admin.site.register(Video_category)
admin.site.register(History)
admin.site.register(Video_Reaction)
admin.site.register(Video_share)
admin.site.register(Login)
