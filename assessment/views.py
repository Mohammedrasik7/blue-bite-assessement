from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Object
from .serializers import BatchSerializer, ObjectSerializer

@api_view(['POST'])
def create_batch(request):
    """
    Create a new batch with the provided data.
    
    Args:
        request: The HTTP request containing the batch data.
    
    Returns:
        Response: A response object containing the serialized data or error messages.
    """
    try:
        # Log the received request data for debugging
        print("Received request data:", request.data)
        # Check if the request method is POST
        if request.method == 'POST':
            serializer = BatchSerializer(data=request.data)
            
            # Validate the serializer and save if valid
            if serializer.is_valid(raise_exception=True):
                print("Data is valid, saving...")
                serializer.save()
                return Response({"message": "Data successfully inserted"}, status=status.HTTP_201_CREATED)
                # return Response(serializer.data, status=status.HTTP_201_CREATED)
            # Log validation errors if the serializer is invalid
            print("Validation errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ValidationError as e:
        print("Validation errors:", e.detail)  # Log the errors for debugging
        return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print("Unexpected error:", str(e))  # Log unexpected errors
        return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def retrieve_object(request, object_id):
    """
    Retrieve an object by its ID.
    
    Args:
        request: The HTTP request.
        object_id: The ID of the object to retrieve.
    
    Returns:
        Response: A response object containing the serialized object data or an error message.
    """
    try:
        # Fetch the object using the provided ID
        obj = Object.objects.get(object_id=object_id)
        serializer = ObjectSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Handle the case where the object does not exist
    except Object.DoesNotExist:
        return Response({"error": "Object not found."}, status=status.HTTP_404_NOT_FOUND)
    # Handle any unexpected exceptions
    except Exception as e:
        print("Unexpected error:", str(e))  # Log unexpected errors
        return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def list_objects(request):
    """
    List objects with optional filtering by data key and/or value.
    
    Args:
        request: The HTTP request containing query parameters for filtering.
    
    Returns:
        Response: A response object containing the serialized list of objects.
    """
    try:
        # Extract query parameters for filtering
        key = request.query_params.get('key', None)
        value = request.query_params.get('value', None)
        
        # Retrieve all objects
        objects = Object.objects.all()

        # Filter by key and value if both are provided
        if key and value:
            objects = objects.filter(data__key=key, data__value__exact=value)
        # Filter by key only
        elif key:
            objects = objects.filter(data__key=key)
        # Filter by value only
        elif value:
            objects = objects.filter(data__value__exact=value)

        # Serialize and return the filtered objects
        serializer = ObjectSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Handle any unexpected exceptions
    except Exception as e:
        print("Unexpected error:", str(e))  # Log unexpected errors
        return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
