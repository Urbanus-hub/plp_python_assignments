import requests
import os
from urllib.parse import urlparse

def is_valid_image(headers):
	content_type = headers.get('Content-Type', '')
	return content_type.startswith('image/')

def get_filename_from_url(url):
	parsed_url = urlparse(url)
	filename = os.path.basename(parsed_url.path)
	if not filename:
		filename = "downloaded_image.jpg"
	return filename

def main():
	print("Welcome to the Ubuntu Image Fetcher")
	print("A tool for mindfully collecting images from the web\n")
	print("Please enter image URLs (one per line). Enter a blank line to finish:")

	# Get multiple URLs from user
	urls = []
	while True:
		url = input()
		if not url.strip():
			break
		urls.append(url.strip())

	if not urls:
		print("No URLs entered. Exiting.")
		return

	print("\nPrecaution: Download images only from trusted sources.\n")

	os.makedirs("Fetched_Images", exist_ok=True)
	downloaded = set(os.listdir("Fetched_Images"))

	for url in urls:
		try:
			filename = get_filename_from_url(url)
			filepath = os.path.join("Fetched_Images", filename)

			# Prevent duplicate downloads
			if filename in downloaded:
				print(f"✗ Skipped (duplicate): {filename}")
				continue

			# Fetch the image with HEAD first for safety
			head = requests.head(url, timeout=10, allow_redirects=True)
			if not is_valid_image(head.headers):
				print(f"✗ Not an image or unsupported type: {url}")
				continue
			content_length = head.headers.get('Content-Length')
			if content_length and int(content_length) > 10*1024*1024:
				print(f"✗ File too large (>10MB): {filename}")
				continue

			# Now fetch the image
			response = requests.get(url, timeout=10)
			response.raise_for_status()
			if not is_valid_image(response.headers):
				print(f"✗ Not an image or unsupported type: {url}")
				continue

			# Save the image
			with open(filepath, 'wb') as f:
				f.write(response.content)
			print(f"✓ Successfully fetched: {filename}")
			print(f"✓ Image saved to {filepath}")
			downloaded.add(filename)

		except requests.exceptions.RequestException as e:
			print(f"✗ Connection error: {e}")
		except Exception as e:
			print(f"✗ An error occurred: {e}")

	print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
	main()
