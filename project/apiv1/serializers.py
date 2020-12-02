from rest_framework import serializers
from user.models import CustomUser
from idea.models import PostIdea, RequiredSkill, Comment

from rest_framework.serializers import SerializerMethodField
from user.models import CustomUser, Skill
from event.models import Event

class UserSerializer(serializers.ModelSerializer):
    #skills = serializers.ReadOnlyField(source='Skill.skill_name')
    class Meta:
        model = CustomUser
        fields = ('user_id', 'username', 'email', 'prof_img', 'intro', 'univ_name', 'major')

class SkillSerializer(serializers.ModelSerializer):
    #user = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Skill
        fields = ('skill_id', 'user', 'skill_name', 'skill_level')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_id', 'event_name', 'event_detail', 'event_schedule', 'event_url')


class RequiredSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredSkill
        fields = ('idea_id', 'skill_name', 'skill_level')

class IdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostIdea
        fields = ('idea_id', 'user_id', 'title','idea_str','idea_image','idea_movie','idea_date')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('idea_id', 'user_id', 'comment_date', 'comment')
