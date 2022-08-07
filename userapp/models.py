from django.db import models

# Create your models here.


# USER_ID MODEL
class User_ID (models.Model):
    User_ID = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.User_ID


class User(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    User_name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    # User_ID = models.ForeignKey(User_ID, on_delete=models.CASCADE)
    College_name = models.CharField(max_length=400)
    Department = models.CharField(max_length=100)
    Year_of_admission = models.IntegerField(default='0')
    Year_of_graduation = models.IntegerField(default='0')
    Account_verification = models.CharField(max_length=100)
    Account_suspension_status = models.CharField(max_length=100)
    User_tag = models.CharField(max_length=100)

    def __str__(self):
        return self.User_name

# LOGIN TABLE


class Login(models.Model):
    User_name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.User_name, self.Email, s
# TAG MODEL/CATEGORY


class Tag(models.Model):
    Title = models.CharField(max_length=100)

    # renames the instances of the model
    # with their Title

    def __str__(self):
        return self.Title


# VIDEO MODEL
class Video (models.Model):
    Title = models.CharField(max_length=100)
    Video_description = models.CharField(max_length=300)
    User_ID = models.ForeignKey(User_ID, on_delete=models.CASCADE)
    Video_Link = models.URLField(max_length=400)  # same like models.URLField()
    Date_Time = models.DateTimeField()
    VID_STATUS_CHOICES = (
        ("1", "Private"),
        ("2", "Public"),
    )
    Video_status = models.CharField(max_length=100, choices=VID_STATUS_CHOICES)

    # renames the instances of the model
    # with their Title.
    def __str__(self):
        return self.Title



# COMMENTS MODEL
class Comment(models.Model):
    Comments_ID = models.CharField(primary_key=True, max_length=200)
    Comments = models.CharField(max_length=500)
    User_ID = models.ForeignKey(User_ID, on_delete=models.CASCADE)
    Date_Time = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.Comments


# VIDEO CATEGORIES
class Video_category(models.Model):
    Tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    Video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.Video


# HISTORY CATEGORY
class History(models.Model):
    Video = models.ForeignKey(Video, on_delete=models.CASCADE)
    User_ID = models.ForeignKey(User_ID, on_delete=models.CASCADE)

    def __str__(self):
        return self.Video


# VIDEO REACTION MODEL
class Video_Reaction(models.Model):
    Video = models.ForeignKey(Video, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    VIDEO_REACTION_CHOICES = (
        ("1", "Like"),
        ("2", "Love"),
        ("3", "Dislike"),
        ("4", "Sad"),
        ("5", "Congratulations"),
    )
    Video_reaction = models.CharField(
        max_length=100, choices=VIDEO_REACTION_CHOICES)

    def __str__(self):
        return self.Video_reaction


# VIDEO SHARING MODEL
class Video_share(models.Model):
    Video = models.ForeignKey(Video, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Video_share_count = models.AutoField(primary_key=True, default='0')

    def __str__(self):
        return self.Video_share_count
