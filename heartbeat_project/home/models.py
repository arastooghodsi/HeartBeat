from django.db import models

class Heartbeat(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    tag_no = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    heart_beats = models.IntegerField()

    class Meta:
        db_table = 'home_heartbeats'
        managed = False


class HeartbeatCount(models.Model):
    id = models.AutoField(primary_key=True)
    rate = models.ForeignKey(Heartbeat, on_delete=models.DO_NOTHING, db_column='rate_id')
    heartbeats_count_number = models.IntegerField()

    class Meta:
        db_table = 'home_heartbeats_count'
        managed = False
