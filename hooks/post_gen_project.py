import httpx

package = "fastapi"  # replace with the package you want to check
response = httpx.get(f"https://pypi.org/pypi/{package}/json")
latest_version = response.json()["info"]["version"]

print(latest_version)
