# Remaining Polish Needed

## Status
Files were converted with automation script but some sections remain in old format because they only had `### Example Response` without `### Example Request`.

## Files Needing Manual Polish

### 1. approvals.mdx (3 sections)
Lines: 58, 92, 168

These sections show only response examples. Need to add:
- `<RequestExample>` block with cURL, JavaScript, Python
- Wrap existing response in `<ResponseExample>` block
- Add 401 error response

### 2. drafts.mdx (8 sections)
Lines: 45, 75, 101, 141, 178, 204, 257, 319

Same pattern - only response examples shown.

### 3. templates.mdx (4 sections)
Lines: 24, 68, 154, 200

Same pattern - only response examples shown.

### 4. containers.mdx (1 section)
Line: 30

Same pattern - only response example shown.

### 5. github.mdx
✅ Clean (no remaining old format)

---

## How to Fix

For each section with `### Example Response`:

1. Look at the endpoint method (POST, GET, DELETE, etc.)
2. Add `<RequestExample>` block before the response:

```markdown
<RequestExample>

```bash cURL
curl -X METHOD http://localhost:8887/api/endpoint \
  -H "Content-Type: application/json" \
  -d '{...}'
```

```javascript JavaScript
const response = await fetch('http://localhost:8887/api/endpoint', {
  method: 'METHOD',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({...})
});
const data = await response.json();
```

```python Python
import requests

response = requests.method('http://localhost:8887/api/endpoint', json={...})
data = response.json()
```

</RequestExample>
```

3. Replace `### Example Response` with:

```markdown
<ResponseExample>

```json 200 Success
{existing response}
```

```json 401 Unauthorized
{
  "success": false,
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required"
  }
}
```

</ResponseExample>
```

---

## Estimated Time
- approvals.mdx: 15 minutes
- drafts.mdx: 30 minutes
- templates.mdx: 20 minutes
- containers.mdx: 5 minutes

**Total: ~70 minutes**

---

## Why This Happened

These files were created manually (not converted from existing) and had a different structure:
- Request body shown in separate `### Request Body` section
- Only response shown in `### Example Response` section
- Automation script looked for Request+Response pairs together

The script successfully converted files that had both sections together but missed these response-only sections.

---

## Priority

**MEDIUM** - These endpoints are documented and work, but don't have the full interactive format with multi-language request examples yet.

The "Try it" button should still work due to OpenAPI integration, but the sidebar won't show the tabbed code examples for these specific endpoints.
