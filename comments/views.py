import warnings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist
from django.http.response import Http404, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from comments.models import Comment
from comments.permissions import IsCommentOwnerOrReadOnly
from comments.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    
    model = Comment
    model_for_comment = None
    serializer_class = CommentSerializer
    extra_args = {}
    renderer_classes = (JSONRenderer,BrowsableAPIRenderer)
    permission_classes = (IsCommentOwnerOrReadOnly,)


    def dispatch(self, request, id_object, *args, **kwargs):
        """
        :param request: request from browser
        :param id_object: id_object sent in the url 
        :param args: args that takes dispatch
        :param kwargs: kwarg that takes dispatch
        :return: response from super method dispatch
        Saves the content type and the id_object of the object coming
        from the url and send it to dispatched function in the kwargs 
        """
        if self.model_for_comment == None:
            raise ImproperlyConfigured(
                    'Expected model_for_comment class field. '
                    'Please set up the model_for_comment first in your CommentViewSet'
                    'inherit class'
            )

        content_type = ContentType.objects.get_for_model(self.model_for_comment())


        try:
            content_type.get_object_for_this_type(pk=id_object)
        except ObjectDoesNotExist:
            raise Http404('Object not found')

        self.extra_args['content_type'] = content_type
        self.extra_args['id_object'] = id_object
        self.extra_args['user'] = request.user
        return super(CommentViewSet,self).dispatch(request,*args,**kwargs)

    def pre_save(self, obj):
        obj.object_id = self.extra_args.pop('id_object')
        obj.content_type = self.extra_args.pop('content_type')
        obj.user = self.extra_args.pop('user')
        super(CommentViewSet,self).pre_save(obj)

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        self.object_list = self.object_list.filter(object_id=self.extra_args['id_object'])
        # Default is to allow empty querysets.  This can be altered by setting
        # `.allow_empty = False`, to raise 404 errors on empty querysets.
        if not self.allow_empty and not self.object_list:
            warnings.warn(
                'The `allow_empty` parameter is deprecated. '
                'To use `allow_empty=False` style behavior, You should override '
                '`get_queryset()` and explicitly raise a 404 on empty querysets.',
                DeprecationWarning
            )
            class_name = self.__class__.__name__
            error_msg = self.empty_error % {'class_name': class_name}
            raise Http404(error_msg)

        # Switch between paginated or standard style responses
        page = self.paginate_queryset(self.object_list)
        if page is not None:
            serializer = self.get_pagination_serializer(page)
        else:
            serializer = self.get_serializer(self.object_list, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed('retrieve')