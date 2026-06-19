from PIL import Image

try:
    img = Image.open('/Users/sohammaggo/.gemini/antigravity/html_artifacts/public/ba-after.jpg')
    # Crop to 1000x1000 from top-left (0,0) to (1000, 1000). 
    # This removes the bottom right 24px where the Gemini watermark is.
    img_cropped = img.crop((0, 0, 1000, 1000))
    img_cropped.save('/Users/sohammaggo/.gemini/antigravity/html_artifacts/public/ba-after.jpg')
    print("Successfully cropped ba-after.jpg to 1000x1000")
except Exception as e:
    print("Error:", e)
