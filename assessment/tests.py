from rest_framework import status
from rest_framework.test import APITestCase
from .models import Batch, Object, ObjectData  # Ensure this import is correct
from .serializers import BatchSerializer, ObjectSerializer

class ObjectAPITests(APITestCase):

    def setUp(self):
        # Set up a test batch and object data
        self.batch = Batch.objects.create(batch_id='batch_1')  # Create a Batch instance
        self.obj = Object.objects.create(object_id='obj_1', batch=self.batch)  # Create an Object instance linked to the Batch
        
        # Create ObjectData linked to the Object
        ObjectData.objects.create(object=self.obj, key='key1', value='value1')

    def test_create_batch(self):
        """Test creating a batch successfully."""
        url = '/api/batch/'  
        data = {
            "batch_id": "71a8a97591894dda9ea1a372c89b7987",  # Batch ID to create
            "objects": [
                {
                "object_id": "d6f983a8905e48f29ad480d3f5969b52",  # First object data
                "data": [
                    {
                    "key": "type",  # Key for the first data entry
                    "value": "shoe"  # Value for the first data entry
                    },
                    {
                    "key": "color",  # Key for the second data entry
                    "value": "purple"  # Value for the second data entry
                    }
                ]
                },
                {
                "object_id": "1125528d300d4538a33069a9456df4e8",  # Second object data
                "data": [
                    {
                    "key": "fizz",  # Key for the data entry
                    "value": "buzz"  # Value for the data entry
                    }
                ]
                }
            ]
        }
        response = self.client.post(url, data, format='json')  # Send POST request to create batch
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Check for successful creation
        self.assertEqual(Batch.objects.count(), 2)  # Verify the batch count

    def test_retrieve_object(self):
        """Test retrieving an object by ID."""
        url = f'/api/object/{self.obj.object_id}/'  # URL for retrieving the object
        response = self.client.get(url)  # Send GET request
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check for successful retrieval
        self.assertEqual(response.data['object_id'], self.obj.object_id)  # Check the object ID matches

    def test_list_objects(self):
        """Test listing objects with filtering by key."""
        url = '/api/objects/?key=key1'  # URL with filtering by key
        response = self.client.get(url)  # Send GET request
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check for successful response
        self.assertEqual(len(response.data), 1)  # Verify one object is returned
        self.assertEqual(response.data[0]['object_id'], self.obj.object_id)  # Check the object ID matches

    def test_list_objects_with_value_filter(self):
        """Test listing objects with filtering by value."""
        url = '/api/objects/?value=value1'  # URL with filtering by value
        response = self.client.get(url)  # Send GET request
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check for successful response
        self.assertEqual(len(response.data), 1)  # Verify one object is returned
        self.assertEqual(response.data[0]['object_id'], self.obj.object_id)  # Check the object ID matches

    def test_list_objects_with_key_and_value_filter(self):
        """Test listing objects with both key and value filters."""
        url = '/api/objects/?key=key1&value=value1'  # URL with both key and value filters
        response = self.client.get(url)  # Send GET request
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check for successful response
        self.assertEqual(len(response.data), 1)  # Verify one object is returned
        self.assertEqual(response.data[0]['object_id'], self.obj.object_id)  # Check the object ID matches

    def test_retrieve_object_not_found(self):
        """Test retrieving an object that doesn't exist."""
        url = '/api/object/non_existing_id/'  # URL for a non-existing object
        response = self.client.get(url)  # Send GET request
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  # Check for not found response
