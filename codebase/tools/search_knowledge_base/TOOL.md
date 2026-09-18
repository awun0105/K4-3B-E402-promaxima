---
name: search_knowledge_base
track: core
kind: local_knowledge
provider: json_announcements
requires_env: []
inputs: [query, announcement_id, top_k]
outputs: [hits, status, total_found]
side_effect: false
---
# search_knowledge_base

Tra cứu các thông báo chính thức, hạn nộp (deadline), sản phẩm cần nộp (deliverables)
và quy chế của Ban Tổ Chức khóa học K4 (Phòng E402 / Lớp 3B).
Hỗ trợ tìm kiếm theo từ khóa hoặc tra cứu đích danh theo mã thông báo (`ANN-GATE-01`, `ANN-LAB-02`, v.v.).
