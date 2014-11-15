from rest_framework.serializers import ModelSerializer
from comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        read_only_fields = ('user','timestamp','object_id')
        exclude = ('content_type',)