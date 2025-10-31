#!/usr/bin/env python3
"""
Convert API documentation from old format to new RequestExample/ResponseExample format.
Usage: python3 convert_api_examples.py <file.mdx>
"""

import re
import sys

def convert_example_sections(content):
    """Convert ### Example Request/Response to RequestExample/ResponseExample blocks."""

    # Pattern to match: ### Example Request ... ### Example Response ... (with code blocks)
    pattern = r'### Example Request\s*\n\s*```bash\s*\n(.*?)\n```\s*\n### Example Response\s*\n\s*```json\s*\n(.*?)\n```'

    def create_request_example(bash_code):
        """Create RequestExample block from bash code."""
        # Extract URL from curl command
        url_match = re.search(r'curl\s+(?:-X\s+\w+\s+)?"?(http[^"\s]+)', bash_code)
        url = url_match.group(1) if url_match else 'http://localhost:8887/api/endpoint'

        # Determine HTTP method
        method = 'GET'
        if '-X POST' in bash_code or 'curl -X POST' in bash_code:
            method = 'POST'
        elif '-X PUT' in bash_code or '-X PATCH' in bash_code:
            method = 'PUT'
        elif '-X DELETE' in bash_code:
            method = 'DELETE'

        # Build JavaScript fetch
        if method == 'GET':
            js_code = f"const response = await fetch('{url}');\nconst data = await response.json();"
        else:
            # Check if there's a body
            if '-d' in bash_code or '--data' in bash_code:
                js_code = f"const response = await fetch('{url}', {{\n  method: '{method}',\n  headers: {{ 'Content-Type': 'application/json' }},\n  body: JSON.stringify({{...}})\n}});\nconst data = await response.json();"
            else:
                js_code = f"const response = await fetch('{url}', {{ method: '{method}' }});\nconst data = await response.json();"

        # Build Python requests
        if method == 'GET':
            py_code = f"import requests\n\nresponse = requests.get('{url}')\ndata = response.json()"
        elif method in ['POST', 'PUT', 'PATCH']:
            py_code = f"import requests\n\nresponse = requests.{method.lower()}(\n    '{url}',\n    json={{...}}\n)\ndata = response.json()"
        else:
            py_code = f"import requests\n\nresponse = requests.{method.lower()}('{url}')\ndata = response.json()"

        return f'''<RequestExample>

```bash cURL
{bash_code}
```

```javascript JavaScript
{js_code}
```

```python Python
{py_code}
```

</RequestExample>'''

    def create_response_example(json_response):
        """Create ResponseExample block from JSON response."""
        return f'''<ResponseExample>

```json 200 Success
{json_response}
```

```json 401 Unauthorized
{{
  "success": false,
  "error": {{
    "code": "UNAUTHORIZED",
    "message": "Authentication required"
  }}
}}
```

</ResponseExample>'''

    def replace_match(match):
        bash_code = match.group(1).strip()
        json_response = match.group(2).strip()

        request_block = create_request_example(bash_code)
        response_block = create_response_example(json_response)

        return f"{request_block}\n\n{response_block}"

    # Apply conversion
    converted = re.sub(pattern, replace_match, content, flags=re.DOTALL)

    return converted

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 convert_api_examples.py <file.mdx>")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        with open(filepath, 'r') as f:
            content = f.read()

        converted_content = convert_example_sections(content)

        # Backup original
        with open(f"{filepath}.backup", 'w') as f:
            f.write(content)

        # Write converted
        with open(filepath, 'w') as f:
            f.write(converted_content)

        print(f"✅ Converted {filepath}")
        print(f"📋 Backup saved to {filepath}.backup")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
