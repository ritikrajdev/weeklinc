from rest_framework import serializers

from .models import Meet, Schedule


# Fields
class MeetSchedulePrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        if self.context['request'].user.is_authenticated:
            return self.context['request'].user.schedules.all()
        return Schedule.objects.none()


# Serializers
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class MeetSerializer(serializers.ModelSerializer):
    schedule = MeetSchedulePrimaryKeyRelatedField()

    class Meta:
        model = Meet
        fields = '__all__'
