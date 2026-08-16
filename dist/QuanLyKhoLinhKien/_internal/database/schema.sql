-- =====================================================================
-- SCHEMA CƠ SỞ DỮ LIỆU - PHẦN MỀM QUẢN LÝ KHO LINH KIỆN
-- SQLite 3
-- =====================================================================
PRAGMA foreign_keys = ON;

-- Danh mục / loại linh kiện
CREATE TABLE IF NOT EXISTS categories (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Nhà sản xuất
CREATE TABLE IF NOT EXISTS manufacturers (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    name         TEXT NOT NULL UNIQUE,
    contact_info TEXT,
    address      TEXT
);

-- Sản phẩm sử dụng linh kiện (VD: Bo mạch A, Máy in B ...)
CREATE TABLE IF NOT EXISTS products (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Linh kiện / vật tư
CREATE TABLE IF NOT EXISTS components (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    code            TEXT NOT NULL UNIQUE,          -- Mã linh kiện nội bộ
    name            TEXT NOT NULL,                  -- Tên linh kiện
    barcode         TEXT UNIQUE,                     -- Mã vạch (duy nhất, có thể NULL)
    category_id     INTEGER,
    manufacturer_id INTEGER,
    unit            TEXT NOT NULL DEFAULT 'Cái',
    quantity        INTEGER NOT NULL DEFAULT 0,      -- Tồn kho hiện tại (tự cập nhật)
    min_quantity    INTEGER NOT NULL DEFAULT 0,      -- Ngưỡng cảnh báo tồn kho thấp
    price           REAL NOT NULL DEFAULT 0,
    year_imported   INTEGER,                          -- Năm nhập kho (lần đầu)
    location        TEXT,                             -- Vị trí lưu kho (kệ/ngăn)
    description     TEXT,
    image_path      TEXT,
    is_active       INTEGER NOT NULL DEFAULT 1,
    created_at      TEXT NOT NULL DEFAULT (datetime('now','localtime')),
    updated_at      TEXT NOT NULL DEFAULT (datetime('now','localtime')),
    FOREIGN KEY (category_id)     REFERENCES categories(id)     ON DELETE SET NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id)  ON DELETE SET NULL
);

-- Quan hệ N-N: 1 linh kiện có thể dùng cho nhiều sản phẩm
CREATE TABLE IF NOT EXISTS component_products (
    component_id INTEGER NOT NULL,
    product_id   INTEGER NOT NULL,
    PRIMARY KEY (component_id, product_id),
    FOREIGN KEY (component_id) REFERENCES components(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id)   REFERENCES products(id)   ON DELETE CASCADE
);

-- Phiếu nhập kho
CREATE TABLE IF NOT EXISTS import_receipts (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    receipt_code TEXT NOT NULL UNIQUE,
    supplier     TEXT,
    note         TEXT,
    created_by   TEXT,
    created_at   TEXT NOT NULL DEFAULT (datetime('now','localtime'))
);

CREATE TABLE IF NOT EXISTS import_receipt_details (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    receipt_id   INTEGER NOT NULL,
    component_id INTEGER NOT NULL,
    quantity     INTEGER NOT NULL CHECK (quantity > 0),
    unit_price   REAL NOT NULL DEFAULT 0,
    FOREIGN KEY (receipt_id)   REFERENCES import_receipts(id) ON DELETE CASCADE,
    FOREIGN KEY (component_id) REFERENCES components(id)
);

-- Phiếu xuất kho
CREATE TABLE IF NOT EXISTS export_receipts (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    receipt_code TEXT NOT NULL UNIQUE,
    recipient    TEXT,
    note         TEXT,
    created_by   TEXT,
    created_at   TEXT NOT NULL DEFAULT (datetime('now','localtime'))
);

CREATE TABLE IF NOT EXISTS export_receipt_details (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    receipt_id   INTEGER NOT NULL,
    component_id INTEGER NOT NULL,
    quantity     INTEGER NOT NULL CHECK (quantity > 0),
    unit_price   REAL NOT NULL DEFAULT 0,
    FOREIGN KEY (receipt_id)   REFERENCES export_receipts(id) ON DELETE CASCADE,
    FOREIGN KEY (component_id) REFERENCES components(id)
);

-- Nhật ký biến động tồn kho (phục vụ truy vết / audit)
CREATE TABLE IF NOT EXISTS stock_transactions (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    component_id     INTEGER NOT NULL,
    transaction_type TEXT NOT NULL CHECK (transaction_type IN ('IN','OUT','ADJUST')),
    quantity         INTEGER NOT NULL,
    balance_after    INTEGER NOT NULL,
    reference_type   TEXT,     -- 'IMPORT' | 'EXPORT' | 'MANUAL'
    reference_id     INTEGER,
    note             TEXT,
    created_at       TEXT NOT NULL DEFAULT (datetime('now','localtime')),
    FOREIGN KEY (component_id) REFERENCES components(id)
);

CREATE INDEX IF NOT EXISTS idx_components_barcode      ON components(barcode);
CREATE INDEX IF NOT EXISTS idx_components_category     ON components(category_id);
CREATE INDEX IF NOT EXISTS idx_components_manufacturer ON components(manufacturer_id);
CREATE INDEX IF NOT EXISTS idx_components_year         ON components(year_imported);
CREATE INDEX IF NOT EXISTS idx_components_name         ON components(name);
CREATE INDEX IF NOT EXISTS idx_stock_tx_component      ON stock_transactions(component_id);
CREATE INDEX IF NOT EXISTS idx_import_details_receipt  ON import_receipt_details(receipt_id);
CREATE INDEX IF NOT EXISTS idx_export_details_receipt  ON export_receipt_details(receipt_id);
