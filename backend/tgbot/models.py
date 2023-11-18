from django.db import models


class TelegramUser(models.Model):
    full_name = models.CharField(max_length=2000)
    username = models.CharField(max_length=1500, null=True, blank=True)
    telegram_id = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "telegram_users"


class JiraWebhook(models.Model):
    user = models.ForeignKey(TelegramUser, models.PROTECT)
    jira_username = models.CharField(max_length=1000)
    api_token = models.TextField()
    webhook_name = models.CharField(max_length=1000)
    jira_project_instance = models.CharField(max_length=1000)
    jira_project_key = models.CharField(max_length=100)
    related_group_id = models.BigIntegerField(null=True, blank=True)
    related_topic_id = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "jira_webhooks"


class JiraWebhookEvent(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    class Meta:
        db_table = "jira_webhook_events"


class WebhookEvent(models.Model):
    webhook = models.ForeignKey(JiraWebhook, models.PROTECT, related_name="events")
    event = models.ForeignKey(JiraWebhookEvent, models.PROTECT)

    class Meta:
        db_table = "webhook_events"
