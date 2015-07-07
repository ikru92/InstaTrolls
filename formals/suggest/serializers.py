from rest_framework import serializers
from suggest.models import myUser, Post, Comment, Lover

from rest_framework import serializers


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


# class FilteredListSerializer(serializers.ListSerializer):
#     def to_representation(self, data):
#         data = data.filter()[:1]
#         return super(FilteredListSerializer, self).to_representation(data)

class FeedsListSerializer(serializers.ModelSerializer):
    post_first_name = serializers.ReadOnlyField(source='posted_by.first_name')
    post_last_name = serializers.ReadOnlyField(source='posted_by.last_name')
    post_avatar = serializers.FileField(source='posted_by.avatar')

    class Meta:
        model = Post
        fields = ('id', 'posted_on', 'description', 'love',
                  'post', 'post_first_name', 'post_last_name', 'post_avatar', 'total_comment')


class LoverSerializer(serializers.ModelSerializer):
    lover_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Lover
        fields = ('id','lover_user','love_post')


class PostsSerializer(serializers.ModelSerializer):
    post = Base64ImageField(max_length=None, use_url=True, allow_null=True)

    class Meta:
        model = Post
        fields = ('id', 'post', 'posted_by', 'posted_on', 'love', 'description')


class CommentsListSerializer(serializers.ModelSerializer):
    commentImg = Base64ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    comment_first_name = serializers.ReadOnlyField(source='commented_by.first_name',read_only=True)
    comment_last_name = serializers.ReadOnlyField(source='commented_by.last_name',read_only=True)
    comment_avatar = serializers.FileField(source='commented_by.avatar',read_only=True)
    commented_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id', 'comment_first_name', 'comment_last_name', 'comment', 'comment_avatar', 'commentImg',
                  'commented_on','commented_by','post')


