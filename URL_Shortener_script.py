import pyshorteners

# Get URL input from the user
long_url = input("Enter the URL to shorten: ")

# Initialize the Shortener object
type_tiny = pyshorteners.Shortener()

# Shorten the URL
short_url = type_tiny.tinyurl.short(long_url)

# Print the shortened URL
print("Shortened URL is: " + short_url)
