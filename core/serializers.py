from rest_framework import serializers

from core.models import CheckList, CheckListItem

# class ChecklistSerializer(serializers.Serializer):
#     title=serializers.CharField()
#     is_deleted=serializers.BooleanField()
#     is_archived=serializers.BooleanField()
#     created_on=serializers.DateTimeField()
#     updated_on=serializers.DateTimeField()



class ChecklisItemtSerializer(serializers.ModelSerializer):
    user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=CheckListItem
        fields='__all__'


class ChecklistSerializer(serializers.ModelSerializer):
    items=ChecklisItemtSerializer(source='checklistitem_set',many=True,read_only=True)
    user=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=CheckList
        fields='__all__'