#!/bin/bash

echo "========================================"
echo "  Aviz Academy - Docker Multi-Stage Demo"
echo "========================================"

echo ""
echo "📦 Building SINGLE-stage image..."
docker build -f Dockerfile.single -t demo-single .

echo ""
echo "📦 Building MULTI-stage image..."
docker build -f Dockerfile.multi -t demo-multi .

echo ""
echo "========================================"
echo "  IMAGE SIZE COMPARISON"
echo "========================================"
docker images | grep "demo-"
echo ""
echo "✅ Run the multi-stage app:"
echo "   docker run -p 8080:8080 demo-multi"
echo "   Open: http://localhost:8080"
```

---

**Expected output your students will see:**
```
REPOSITORY     TAG     SIZE
demo-single    latest  ~320 MB   ❌
demo-multi     latest  ~8 MB     ✅