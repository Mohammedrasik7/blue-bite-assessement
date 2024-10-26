from rest_framework import serializers
from .models import Batch, Object, ObjectData

# Serializer for ObjectData model
class ObjectDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectData  # Specify the model to serialize
        fields = ['key', 'value']  # Fields to include in the serialized output

class ObjectSerializer(serializers.ModelSerializer):
    data = ObjectDataSerializer(many=True)  # Include multiple ObjectData entries

    class Meta:
        model = Object  # Specify the model to serialize
        fields = ['object_id', 'data']  # Fields to include in the serialized output

    def create(self, validated_data):
        # Handle creation of Object and related ObjectData
        data_list = validated_data.pop('data')  # Extract data from validated data
        print(validated_data)
        obj = Object.objects.create(**validated_data)   # Create Object instance
        ObjectData.objects.bulk_create(
            [ObjectData(object=obj, **data) for data in data_list]   # Create ObjectData in bulk
        )
        return obj

# Serializer for Batch model
class BatchSerializer(serializers.ModelSerializer):
    objects = ObjectSerializer(many=True)  # Include multiple Object entries

    class Meta:
        model = Batch  # Specify the model to serialize
        fields = ['batch_id', 'objects']  # Fields to include in the serialized output

    def create(self, validated_data):
        # Handle creation of Batch and related Objects and ObjectData
        print("Inside create method with data:", validated_data)
        batch_id = validated_data.pop('batch_id')   # Extract batch_id from validated data
        objects_data = validated_data.pop('objects')  # Extract objects data

        # Create the Batch instance
        batch = Batch(batch_id=batch_id)
        batch.save()  # Save the batch instance explicitly

        for obj_data in objects_data:
            data_list = obj_data.pop('data')
            # Create Object and link it to the batch
            obj = Object(batch=batch, object_id=obj_data['object_id'])
            obj.save()  # Save the object instance explicitly

            # Create ObjectData in bulk
            ObjectData.objects.bulk_create(
                [ObjectData(object=obj, **data) for data in data_list]  # Create ObjectData entries
            )

        return batch