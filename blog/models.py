from django.db import models

# Create your blog models here.
#       title
#       pub_date
#       body - txt itself
#       Images

# Add blog app to the local_settings

# Create migration

# Migrate

# Add blog to the admin


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    blog_text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title[:50]

    def summary(self):
        return self.blog_text[:100]

    def pub_date_pretty(self):
        # МPython's strftime directivesб % b - month,   http: // strftime.org/

        return self.pub_date.strftime('%b %e,   %y')
