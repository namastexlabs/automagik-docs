# Update Remaining API Files - Action Plan

## 🎯 Current State

**DONE:**
- ✅ `forge/api/projects.mdx` - Fully updated with new format

**NEEDS UPDATE (9 files):**
- ⚠️ `forge/api/tasks.mdx`
- ⚠️ `forge/api/attempts.mdx`
- ⚠️ `forge/api/processes.mdx`
- ⚠️ `forge/api/approvals.mdx`
- ⚠️ `forge/api/drafts.mdx`
- ⚠️ `forge/api/templates.mdx`
- ⚠️ `forge/api/containers.mdx`
- ⚠️ `forge/api/filesystem.mdx`
- ⚠️ `forge/api/github.mdx`
- ⚠️ `forge/api/websockets.mdx` (special case - no frontmatter change needed)
- ⚠️ `forge/api/mcp-tools.mdx` (special case - no frontmatter change needed)
- ⚠️ `forge/api/rest-overview.mdx` (special case - overview page)

---

## 📝 Required Changes for Each File

### 1. Update Frontmatter
**Change:**
```yaml
---
api: "GET /api/endpoint"
---
```

**To:**
```yaml
---
openapi: "GET /api/endpoint"
---
```

### 2. Convert Examples to RequestExample Blocks

**Current Format:**
```markdown
### Example Request

```bash
curl http://localhost:8887/api/endpoint
```

### Example Response

```json
{
  "success": true,
  "data": {...}
}
```
```

**New Format:**
```markdown
<RequestExample>

```bash cURL
curl http://localhost:8887/api/endpoint
```

```javascript JavaScript
const response = await fetch('http://localhost:8887/api/endpoint');
const data = await response.json();
```

```python Python
import requests

response = requests.get('http://localhost:8887/api/endpoint')
data = response.json()
```

</RequestExample>

<ResponseExample>

```json 200 Success
{
  "success": true,
  "data": {...}
}
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

## 🔨 Step-by-Step Process

For each file:

### Step 1: Update Frontmatter
```bash
sed -i 's/^api:/openapi:/' filename.mdx
```

### Step 2: For Each Endpoint Section

1. **Locate** the endpoint (e.g., "## List Tasks")

2. **Find** the example request:
   ```markdown
   ### Example Request

   ```bash
   curl http://localhost:8887/api/...
   ```
   ```

3. **Replace** with:
   ```markdown
   <RequestExample>

   ```bash cURL
   curl http://localhost:8887/api/...
   ```

   ```javascript JavaScript
   const response = await fetch('http://localhost:8887/api/...');
   const data = await response.json();
   ```

   ```python Python
   import requests

   response = requests.get('http://localhost:8887/api/...')
   data = response.json()
   ```

   </RequestExample>
   ```

4. **Find** the example response:
   ```markdown
   ### Example Response

   ```json
   {...}
   ```
   ```

5. **Replace** with:
   ```markdown
   <ResponseExample>

   ```json 200 Success
   {...}
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

## 📋 File-Specific Notes

### tasks.mdx
- **Endpoints**: List, Get, Create, Update, Delete
- **Methods**: GET, POST, PUT, PATCH, DELETE
- Add JavaScript/Python for each

### attempts.mdx
- **Endpoints**: List, Get, Create, Start, Cancel, Delete, Logs, Diff, Merge, + 16 new endpoints
- This is the LARGEST file (~1000 lines)
- **Priority**: HIGH - most used API

### processes.mdx
- **Endpoints**: List, Get, Stop, WebSocket streaming
- Include WebSocket examples in JavaScript

### approvals.mdx
- **Endpoints**: Create, Get, Respond, List Pending
- Include workflow examples

### drafts.mdx
- **Endpoints**: Save, Get, Delete, Follow-up, Retry, Queues
- Include WebSocket streaming example

### templates.mdx
- **Endpoints**: List, Get, Create, Update, Delete
- Standard CRUD operations

### containers.mdx
- **Endpoints**: Get Container Info
- Single endpoint, simpler file

### filesystem.mdx
- **Endpoints**: List Directory, List Git Repos
- Include path examples

### github.mdx
- **Endpoints**: Auth (device flow), PR operations
- Include OAuth flow examples

### websockets.mdx
- **Special**: No REST endpoints, only WebSocket
- Update JavaScript examples for consistency

### mcp-tools.mdx
- **Special**: MCP protocol, not REST
- May not need changes

### rest-overview.mdx
- **Special**: Overview page
- Update example sections

---

## 🚀 Priority Order

1. **HIGH**: `attempts.mdx` - Most endpoints, most used
2. **HIGH**: `tasks.mdx` - Core functionality
3. **MEDIUM**: `processes.mdx` - Monitoring
4. **MEDIUM**: `approvals.mdx`, `drafts.mdx` - New features
5. **LOW**: `templates.mdx`, `containers.mdx`, `filesystem.mdx`, `github.mdx`
6. **REVIEW**: `websockets.mdx`, `mcp-tools.mdx`, `rest-overview.mdx`

---

## ✅ Checklist Per File

- [ ] Update `api:` to `openapi:` in frontmatter
- [ ] Convert all `### Example Request` to `<RequestExample>`
- [ ] Add cURL, JavaScript, Python for each endpoint
- [ ] Convert all `### Example Response` to `<ResponseExample>`
- [ ] Add 200, 401, 404 status codes where applicable
- [ ] Verify all examples use `http://localhost:8887`
- [ ] Test "Try it" button works
- [ ] Verify code examples show in sidebar

---

## 📊 Estimated Effort

| File | Endpoints | Estimated Time |
|------|-----------|----------------|
| attempts.mdx | ~20 | 2 hours |
| tasks.mdx | ~5 | 45 min |
| processes.mdx | ~4 | 30 min |
| approvals.mdx | ~4 | 30 min |
| drafts.mdx | ~8 | 1 hour |
| templates.mdx | ~5 | 30 min |
| containers.mdx | ~1 | 15 min |
| filesystem.mdx | ~2 | 20 min |
| github.mdx | ~4 | 30 min |
| websockets.mdx | Review | 20 min |
| mcp-tools.mdx | Review | 15 min |
| rest-overview.mdx | Review | 20 min |
| **TOTAL** | | **~7 hours** |

---

## 💡 Tips

1. **Use projects.mdx as reference** - It's the perfect example
2. **Copy-paste template** - Use the template from API_REFERENCE_GUIDE.md
3. **Batch similar endpoints** - List/Get/Create/Update/Delete follow same pattern
4. **Test incrementally** - Check each file as you go
5. **Focus on common cases** - Don't overcomplicate with every possible error code

---

## 🎯 Success Criteria

When done, all API files should:
- ✅ Use `openapi:` in frontmatter
- ✅ Have `<RequestExample>` blocks with 3 languages
- ✅ Have `<ResponseExample>` blocks with multiple status codes
- ✅ Work with "Try it" button
- ✅ Show code examples in sidebar
- ✅ Use port 8887 everywhere
- ✅ Match LangWatch-style documentation

---

## 📖 Reference

See:
- `/docs/forge/api/projects.mdx` - Perfect example
- `/docs/API_REFERENCE_GUIDE.md` - Template and guide
- LangWatch docs - Inspiration for format
