import cloudinary
import cloudinary.uploader
from config import CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET

cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET,
    secure=True
)

def upload_file_to_cloudinary(fileobj, folder="book_images"):
    """
    fileobj: bytes OR file-like OR path
    """
    try:
        result = cloudinary.uploader.upload(fileobj, folder=folder, overwrite=True, resource_type="image")
        return result.get("secure_url")
    except Exception as e:
        raise Exception(f"Cloudinary upload failed: {e}")