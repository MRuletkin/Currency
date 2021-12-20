from currency.models import ContactUs, Rate, Source

from django.conf import settings
from django.core.mail import send_mail

from rest_framework import serializers


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'sale',
            'buy',
            'created',
            'source',
            'type',
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'name',
            'created',
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'created',
            'name',
            'reply_to',
            'subject',
            'body',
        )

    def create(self, validated_data):
        instance = ContactUs(**validated_data)
        subject = 'User ContactUs'
        body = f'''
            Request From: {instance.name}
            Email to reply: {instance.reply_to}
            Subject: {instance.subject}
            Body: {instance.body}
        '''
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        return ContactUs.objects.create(**validated_data)
