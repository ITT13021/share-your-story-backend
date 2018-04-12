from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_bulk import BulkUpdateModelMixin


class PacthForBulk(BulkUpdateModelMixin):
    def partial_bulk_update(self, request, *args, **kwargs):
        if any(k in request.data for k in ('C', 'U', 'D')):
            serializer = self.get_serializer(args, kwargs)
            m = serializer.Meta.model  # update
            user = request.user
            modified = request.data.get('U', None)
            for item in modified:
                if hasattr(m, 'last_modified_user'):
                    item["last_modified_user"] = user
                m.objects.filter(pk=item.pop('id')).update(**item)

            # created
            created = request.data.get('C', None)
            for item in created:
                if hasattr(m, 'create_user'):
                    item["create_user"] = user
            m.objects.bulk_create([m(**d) for d in created])

            # deleted
            deleted = request.data.get('D', '')
            if len(deleted):
                m.objects.filter(pk__in=deleted.split(',')).delete()

            return Response(status=status.HTTP_200_OK)

        return super(PacthForBulk, self).partial_bulk_update(request, args, kwargs)


class AuditSerializerMixin(object):
    def to_internal_value(self, data):

        ret = super(AuditSerializerMixin, self).to_internal_value(data)
        action = self.context.get("request").method

        if hasattr(self.Meta.model, 'create_user') and action in ('POST'):
            ret["create_user"] = ret.get("create_user", self.context['request'].user)
        elif hasattr(self.Meta.model, 'last_modified_user') and action in ('PUT', 'PATCH'):
            ret["last_modified_user"] = self.context['request'].user

        return ret
