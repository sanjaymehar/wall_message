from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Wall
from django.conf import settings
from django.core.mail import send_mail


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username','email','password', 'password2')
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'],)
        user.set_password(validated_data['password'])
        user.save()
        subject = 'welcome '
        message = f'Hi {user.username}, thank you for registering in wall.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )

        return user



class WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields =("id","user","text",)


class WallCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields =("id","text",)

class WallUpdateSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields =("id","text",)
