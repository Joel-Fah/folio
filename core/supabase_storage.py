# storage.py

import os
from django.conf import settings
from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from supabase import create_client, Client

class SupabaseStorage(Storage):
    def __init__(self):
        self.supabase_url = settings.SUPABASE_URL
        self.supabase_key = settings.SUPABASE_KEY
        self.bucket_name = settings.SUPABASE_BUCKET_NAME
        self.client: Client = create_client(self.supabase_url, self.supabase_key)

    def _open(self, name, mode='rb'):
        """Retrieve the specified file from storage."""
        response = self.client.storage.from_(self.bucket_name).download(name)
        if response.status_code == 200:
            return ContentFile(response.content)
        else:
            raise FileNotFoundError(f"File {name} not found in Supabase storage.")

    def _save(self, name, content):
        """Save a file to Supabase storage."""
        path = os.path.join('/tmp', name)
        with open(path, 'wb') as f:
            f.write(content.read())

        response = self.client.storage.from_(self.bucket_name).upload(name, path)
        os.remove(path)
        if response.get('status_code') == 200:
            return name
        else:
            raise Exception(f"Failed to upload file {name} to Supabase storage.")

    def delete(self, name):
        """Delete the specified file from storage."""
        response = self.client.storage.from_(self.bucket_name).remove([name])
        if response.get('status_code') != 200:
            raise Exception(f"Failed to delete file {name} from Supabase storage.")

    def exists(self, name):
        """Check if the specified file exists in storage."""
        response = self.client.storage.from_(self.bucket_name).list()
        for file in response.get('data', []):
            if file['name'] == name:
                return True
        return False

    def size(self, name):
        """Return the size of the specified file."""
        response = self.client.storage.from_(self.bucket_name).list()
        for file in response.get('data', []):
            if file['name'] == name:
                return file['size']
        return 0

    def url(self, name):
        """Return the URL of the specified file."""
        response = self.client.storage.from_(self.bucket_name).get_public_url(name)
        if response.get('data'):
            return response['data']['publicURL']
        else:
            raise Exception(f"Failed to get URL for file {name} from Supabase storage.")
