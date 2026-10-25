"""Vẽ sơ đồ Star Schema (2 fact) -> star_schema.png để nhúng vào báo cáo Word."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
FACT = "#1F4E79"      # fact: navy đậm
DIM = "#2E75B6"       # conformed dimension
DIM_LOCAL = "#548235" # dimension chỉ dùng cho 1 fact (Product)
TXT = "white"

fig, ax = plt.subplots(figsize=(14, 9.2))
ax.set_xlim(0, 14); ax.set_ylim(0, 10); ax.axis("off")


def box(x, y, w, h, title, fields, fc, title_size=9.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc=fc, ec="#0D2B45", lw=1.5, zorder=3))
    ax.text(x + w / 2, y + h - 0.22, title, ha="center", va="top",
            color=TXT, fontsize=title_size, fontweight="bold", zorder=4)
    ax.text(x + 0.14, y + h - 0.52, fields, ha="left", va="top",
            color=TXT, fontsize=6.8, family="monospace", zorder=4)
    return (x + w / 2, y + h / 2)


# ---- Hai bảng FACT ở trung tâm ----
cen_sales = box(3.3, 4.0, 3.3, 2.3, "FACT_SALES",
                "grain: 1 dòng mặt hàng\nPK order_item_id (DD)\nFK order_id (DD)\n"
                "FK customer_key\nFK product_key\nFK order_date_key\nFK ship_date_key\n"
                "FK location_key\nFK delivery_key\n~ sales, quantity, discount,\n"
                "  net_sales, profit", FACT)
cen_del = box(7.4, 4.0, 3.3, 2.3, "FACT_ORDER_DELIVERY",
              "grain: 1 đơn hàng\nPK order_id (DD)\nFK customer_key\n"
              "FK order_date_key\nFK ship_date_key\nFK location_key\nFK delivery_key\n"
              "~ days_ship_scheduled,\n  days_ship_real,\n  shipping_delay,\n"
              "  late_delivery_flag,\n  order_sales, order_profit", FACT)

# ---- Dimensions ----
# Conformed (dùng cho CẢ HAI fact)
d_date = box(5.3, 8.0, 3.4, 1.7, "DIM_DATE  (role-playing)",
             "PK date_key\nyear > quarter > month > date\n(order_date_key & ship_date_key)", DIM)
d_cust = box(0.3, 7.3, 3.0, 1.9, "DIM_CUSTOMER",
             "PK customer_key (SK)\nBK Customer Id\nsegment\ncity > state > country", DIM)
d_loc = box(5.3, 0.3, 3.4, 1.7, "DIM_LOCATION",
            "PK location_key (SK)\nmarket > region >\ncountry > state > city", DIM)
d_del = box(10.7, 7.3, 3.0, 1.9, "DIM_DELIVERY",
            "PK delivery_key (SK)\nshipping_mode\ndelivery_status\npayment_type\norder_status", DIM)
# Chỉ dùng cho FACT_SALES
d_prod = box(0.3, 3.9, 3.0, 1.9, "DIM_PRODUCT",
             "PK product_key (SK)\nBK Product Card Id\nproduct > category >\ndepartment\nproduct_price", DIM_LOCAL)


def link(a, b, color="#555", style="-"):
    ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=1.2, ls=style, zorder=0)


# Fact_Sales <-> các dimension
for d in (d_date, d_cust, d_loc, d_del, d_prod):
    link(cen_sales, d)
# Fact_Order_Delivery <-> conformed dimension (KHÔNG nối Product)
for d in (d_date, d_cust, d_loc, d_del):
    link(cen_del, d, color="#1F4E79")

ax.text(7, 9.75, "STAR SCHEMA — DSS Chuỗi cung ứng DataCo (2 bảng fact)",
        ha="center", fontsize=13, fontweight="bold", color="#0D2B45")
# chú thích
ax.add_patch(FancyBboxPatch((0.3, 0.3), 0.3, 0.3, boxstyle="round,pad=0.01", fc=DIM, ec="none"))
ax.text(0.7, 0.45, "Conformed dimension (chia sẻ 2 fact)", va="center", fontsize=8)
ax.add_patch(FancyBboxPatch((0.3, -0.15), 0.3, 0.3, boxstyle="round,pad=0.01", fc=DIM_LOCAL, ec="none"))
ax.text(0.7, 0.0, "Dimension riêng Fact_Sales   |   DD = degenerate dimension, SK = surrogate key, BK = business key",
        va="center", fontsize=8)

plt.tight_layout()
out = os.path.join(HERE, "star_schema.png")
plt.savefig(out, dpi=160, bbox_inches="tight")
print("saved", out)
