from django.db import models

# Create your models here.
class SiteNotification(models.Model):
    title = models.CharField(max_length=255, verbose_name="Notification Title")
    message = models.TextField()

    show = models.BooleanField(default=True, verbose_name="Show Notification")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.show:
            SiteNotification.objects.exclude(pk=self.pk).filter(show=True).update(show=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Site Notification"
        verbose_name_plural = "Site Notifications"
        ordering = ['-created_at']  # Newest notifications first



class CTAMessage(models.Model):
    message = models.TextField(verbose_name="CTA Message")
    link_text = models.CharField(max_length=500, blank=True, null=True, verbose_name="CTA Link Text")
    link = models.CharField(max_length=500, blank=True, null=True, verbose_name="CTA Link")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    show = models.BooleanField(default=True, verbose_name="Show CTA Message")
    
    def __str__(self):
        return self.message[:50]  # Return first 50 characters of the message
    

    def save(self, *args, **kwargs):
        if self.show:
            CTAMessage.objects.exclude(pk=self.pk).filter(show=True).update(show=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "CTA Message"
        verbose_name_plural = "CTA Messages"
        ordering = ['-created_at']  # Newest messages first