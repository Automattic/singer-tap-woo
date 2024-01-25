"""Stream type classes for tap-woo."""

from __future__ import annotations

import sys
import typing as t
from typing import Optional

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_woo.client import wooStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


class CouponsStream(wooStream):
    """Coupons"""
    name = "coupons"
    path = "/coupons"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "date_modified_gmt"
    is_sorted = False

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("code", th.StringType),
        th.Property("amount", th.StringType),
        th.Property("date_created", th.DateTimeType),
        th.Property("date_created_gmt", th.DateTimeType),
        th.Property("date_modified", th.DateTimeType),
        th.Property("date_modified_gmt", th.DateTimeType),
        th.Property("discount_type", th.StringType),
        th.Property("description", th.StringType),
        th.Property("date_expires", th.DateTimeType),
        th.Property("date_expires_gmt", th.DateTimeType),
        th.Property("usage_count", th.IntegerType),
        th.Property("individual_use", th.BooleanType),
        th.Property("product_ids", th.ArrayType(th.IntegerType)),
        th.Property("excluded_product_ids", th.ArrayType(th.IntegerType)),
        th.Property("usage_limit", th.IntegerType),
        th.Property("usage_limit_per_user", th.IntegerType),
        th.Property("limit_usage_to_x_items", th.IntegerType),
        th.Property("free_shipping", th.BooleanType),
        th.Property("product_categories", th.ArrayType(th.IntegerType)),
        th.Property("excluded_product_categories", th.ArrayType(th.IntegerType)),
        th.Property("exclude_sale_items", th.BooleanType),
        th.Property("minimum_amount", th.StringType),
        th.Property("maximum_amount", th.StringType),
        th.Property("email_restrictions", th.ArrayType(th.StringType)),
        th.Property("used_by", th.ArrayType(th.StringType)),
        th.Property("meta_data", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("key", th.StringType),
                th.Property("value", th.StringType),
            )
        )),
    ).to_dict()

class CustomersStream(wooStream):
    """Customers."""

    name = "customers"
    path = "/customers"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("date_created", th.DateTimeType),
        th.Property("date_created_gmt", th.DateTimeType),
        th.Property("date_modified", th.DateTimeType),
        th.Property("date_modified_gmt", th.DateTimeType),
        th.Property("email", th.StringType),
        th.Property("first_name", th.StringType),
        th.Property("last_name", th.StringType),
        th.Property("role", th.StringType),
        th.Property("username", th.StringType),
        th.Property("billing", th.ObjectType(
            th.Property("first_name", th.StringType),
            th.Property("last_name", th.StringType),
            th.Property("company", th.StringType),
            th.Property("address_1", th.StringType),
            th.Property("address_2", th.StringType),
            th.Property("city", th.StringType),
            th.Property("state", th.StringType),
            th.Property("postcode", th.StringType),
            th.Property("country", th.StringType),
            th.Property("email", th.StringType),
            th.Property("phone", th.StringType),
        )),
        th.Property("shipping", th.ObjectType(
            th.Property("first_name", th.StringType),
            th.Property("last_name", th.StringType),
            th.Property("company", th.StringType),
            th.Property("address_1", th.StringType),
            th.Property("address_2", th.StringType),
            th.Property("city", th.StringType),
            th.Property("state", th.StringType),
            th.Property("postcode", th.StringType),
            th.Property("country", th.StringType),
        )),
        th.Property("is_paying_customer", th.BooleanType),
        th.Property("avatar_url", th.StringType),
        th.Property("meta_data", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("key", th.StringType),
                th.Property("value", th.StringType),
            )
        )),
    ).to_dict()

class OrdersStream(wooStream):
    """Orders Stream."""

    name = "orders"
    path = "/orders"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "date_modified_gmt"
    is_sorted = False

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("parent_id", th.IntegerType),
        th.Property("number", th.StringType),
        th.Property("order_key", th.StringType),
        th.Property("created_via", th.StringType),
        th.Property("version", th.StringType),
        th.Property("status", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("currency_symbol", th.StringType),
        th.Property("date_created", th.DateTimeType),
        th.Property("date_created_gmt", th.DateTimeType),
        th.Property("date_modified", th.DateTimeType),
        th.Property("date_modified_gmt", th.DateTimeType),
        th.Property("discount_total", th.StringType),
        th.Property("discount_tax", th.StringType),
        th.Property("shipping_total", th.StringType),
        th.Property("shipping_tax", th.StringType),
        th.Property("cart_tax", th.StringType),
        th.Property("total", th.StringType),
        th.Property("total_tax", th.StringType),
        th.Property("prices_include_tax", th.BooleanType),
        th.Property("customer_id", th.IntegerType),
        th.Property("customer_ip_address", th.StringType),
        th.Property("customer_user_agent", th.StringType),
        th.Property("customer_note", th.StringType),
        th.Property(
            "billing",
            th.ObjectType(
                th.Property("first_name", th.StringType),
                th.Property("last_name", th.StringType),
                th.Property("company", th.StringType),
                th.Property("address_1", th.StringType),
                th.Property("address_2", th.StringType),
                th.Property("city", th.StringType),
                th.Property("state", th.StringType),
                th.Property("postcode", th.StringType),
                th.Property("country", th.StringType),
                th.Property("email", th.StringType),
                th.Property("phone", th.StringType),
            ),
        ),
        th.Property(
            "shipping",
            th.ObjectType(
                th.Property("first_name", th.StringType),
                th.Property("last_name", th.StringType),
                th.Property("company", th.StringType),
                th.Property("address_1", th.StringType),
                th.Property("address_2", th.StringType),
                th.Property("city", th.StringType),
                th.Property("state", th.StringType),
                th.Property("postcode", th.StringType),
                th.Property("country", th.StringType),
            ),
        ),
        th.Property("payment_method", th.StringType),
        th.Property("payment_method_title", th.StringType),
        th.Property("transaction_id", th.StringType),
        th.Property("date_paid", th.DateTimeType),
        th.Property("date_paid_gmt", th.DateTimeType),
        th.Property("date_completed", th.DateTimeType),
        th.Property("date_completed_gmt", th.DateTimeType),
        th.Property("cart_hash", th.StringType),
        th.Property(
            "line_items",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("product_id", th.IntegerType),
                    th.Property("variation_id", th.IntegerType),
                    th.Property("quantity", th.NumberType),
                    th.Property("tax_class", th.StringType),
                    th.Property("subtotal", th.StringType),
                    th.Property("subtotal_tax", th.StringType),
                    th.Property("total", th.StringType),
                    th.Property("total_tax", th.StringType),
                    th.Property(
                        "taxes",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("id", th.CustomType({"type": ["integer", "string"]})),
                                th.Property("rate_code", th.StringType),
                                th.Property("rate_id", th.IntegerType),
                                th.Property("label", th.StringType),
                                th.Property("compound", th.BooleanType),
                                th.Property("tax_total", th.StringType),
                                th.Property("shipping_tax_total", th.StringType),
                            )
                        ),
                    ),
                    th.Property("sku", th.CustomType({"type": ["boolean", "string"]})),
                    th.Property("price", th.NumberType),
                ),
            ),
        ),
        th.Property(
            "tax_lines",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("rate_code", th.StringType),
                    th.Property("rate_id", th.IntegerType),
                    th.Property("label", th.StringType),
                    th.Property("compound", th.BooleanType),
                    th.Property("tax_total", th.StringType),
                    th.Property("shipping_tax_total", th.StringType),
                )
            ),
        ),
        th.Property(
            "shipping_lines",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("method_title", th.StringType),
                    th.Property("method_id", th.StringType),
                    th.Property("total", th.StringType),
                    th.Property("total_tax", th.StringType),
                    th.Property(
                        "taxes",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("rate_code", th.StringType),
                                th.Property("rate_id", th.IntegerType),
                                th.Property("label", th.StringType),
                                th.Property("compound", th.BooleanType),
                                th.Property("tax_total", th.StringType),
                                th.Property("shipping_tax_total", th.StringType),
                            )
                        ),
                    ),
                )
            ),
        ),
        th.Property(
            "fee_lines",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("tax_class", th.StringType),
                    th.Property("tax_status", th.StringType),
                    th.Property("total", th.StringType),
                    th.Property("total_tax", th.StringType),
                    th.Property(
                        "taxes",
                        th.ArrayType(
                            th.ObjectType(
                                th.Property("id", th.CustomType({"type": ["integer", "string"]})),
                                th.Property("rate_code", th.StringType),
                                th.Property("rate_id", th.IntegerType),
                                th.Property("label", th.StringType),
                                th.Property("compound", th.BooleanType),
                                th.Property("tax_total", th.StringType),
                                th.Property("shipping_tax_total", th.StringType),
                            )
                        ),
                    ),
                )
            ),
        ),
        th.Property(
            "coupon_lines",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("code", th.StringType),
                    th.Property("discount", th.CustomType({"type": ["string", "number"]})),
                    th.Property("discount_tax", th.StringType),
                ),
            ),
        ),
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
                "order_id": record["id"],
            }

##
#     [
#   {
#     "id": 726,
#     "date_created": "2017-03-21T17:07:11",
#     "date_created_gmt": "2017-03-21T20:07:11",
#     "amount": "10.00",
#     "reason": "",
#     "refunded_by": 1,
#     "refunded_payment": false,
#     "meta_data": [],
#     "line_items": [],
#     "_links": {
#       "self": [
#         {
#           "href": "https://example.com/wp-json/wc/v3/orders/723/refunds/726"
#         }
#       ],
#       "collection": [
#         {
#           "href": "https://example.com/wp-json/wc/v3/orders/723/refunds"
#         }
#       ],
#       "up": [
#         {
#           "href": "https://example.com/wp-json/wc/v3/orders/723"
#         }
#       ]
#     }
#   },
#   {
#     "id": 724,
#     "date_created": "2017-03-21T16:55:37",
#     "date_created_gmt": "2017-03-21T19:55:37",
#     "amount": "9.00",
#     "reason": "",
#     "refunded_by": 1,
#     "refunded_payment": false,
#     "meta_data": [],
#     "line_items": [
#       {
#         "id": 314,
#         "name": "Woo Album #2",
#         "product_id": 87,
#         "variation_id": 0,
#         "quantity": -1,
#         "tax_class": "",
#         "subtotal": "-9.00",
#         "subtotal_tax": "0.00",
#         "total": "-9.00",
#         "total_tax": "0.00",
#         "taxes": [],
#         "meta_data": [
#           {
#             "id": 2076,
#             "key": "_refunded_item_id",
#             "value": "311"
#           }
#         ],
#         "sku": "",
#         "price": -9
#       }
#     ],
#     "_links": {
#       "self": [
#         {
#           "href": "https://example.com/wp-json/wc/v3/orders/723/refunds/724"
#         }
#       ],
#       "collection": [
#         {
#           "href": "https://example.com/wp-json/wc/v3/orders/723/refunds"
#         }
#       ],
#       "up": [
#         {
#           "href": "https://example.com/wp-json/wc/v3/orders/723"
#         }
#       ]
#     }
#   }
# ]
class RefundsStream(wooStream):
    name = "refunds"
    path = "/orders/{order_id}/refunds"
    primary_keys = ["id"]
    parent_stream_type = OrdersStream

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("date_created", th.DateTimeType),
        th.Property("date_created_gmt", th.DateTimeType),
        th.Property("amount", th.StringType),
        th.Property("reason", th.StringType),
        th.Property("refunded_by", th.IntegerType),
        th.Property("refunded_payment", th.BooleanType),
        th.Property("meta_data", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("key", th.StringType),
                th.Property("value", th.StringType),
            )
        )),
        th.Property("line_items", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("product_id", th.IntegerType),
                th.Property("variation_id", th.IntegerType),
                th.Property("quantity", th.NumberType),
                th.Property("tax_class", th.StringType),
                th.Property("subtotal", th.StringType),
                th.Property("subtotal_tax", th.StringType),
                th.Property("total", th.StringType),
                th.Property("total_tax", th.StringType),
                th.Property("taxes", th.ArrayType(
                    th.ObjectType(
                        th.Property("id", th.CustomType({"type": ["integer", "string"]})),
                        th.Property("rate_code", th.StringType),
                        th.Property("rate_id", th.IntegerType),
                        th.Property("label", th.StringType),
                        th.Property("compound", th.BooleanType),
                        th.Property("tax_total", th.StringType),
                        th.Property("shipping_tax_total", th.StringType),
                    )
                )),
                th.Property("meta_data", th.ArrayType(
                    th.ObjectType(
                        th.Property("id", th.IntegerType),
                        th.Property("key", th.StringType),
                        th.Property("value", th.StringType),
                    )
                )),
                th.Property("sku", th.CustomType({"type": ["boolean", "string"]})),
                th.Property("price", th.NumberType),
            )
        )),
    ).to_dict()
            



class ProductsStream(wooStream):
    """Products Stream."""

    name = "products"
    path = "/products"
    primary_keys: t.ClassVar[list[str]]
    # replication_key = "date_modified_gmt"
    # is_sorted = False

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("slug", th.StringType),
        th.Property("permalink", th.StringType),
        th.Property("date_created", th.DateTimeType),
        th.Property("date_modified", th.DateTimeType),
        th.Property("date_created_gmt", th.DateTimeType),
        th.Property("date_modified_gmt", th.DateTimeType),
        th.Property("date_on_sale_from_gmt", th.DateTimeType),
        th.Property("date_on_sale_to_gmt", th.DateTimeType),
        th.Property("low_stock_amount", th.CustomType({"type": ["string", "number"]})),
        th.Property("type", th.StringType),
        th.Property("status", th.StringType),
        th.Property("featured", th.BooleanType),
        th.Property("catalog_visibility", th.StringType),
        th.Property("description", th.StringType),
        th.Property("short_description", th.StringType),
        th.Property("sku", th.StringType),
        th.Property("brands", th.CustomType({"type": ["array", "string"]})),
        th.Property("price", th.CustomType({"type": ["string", "number"]})),
        th.Property("regular_price", th.CustomType({"type": ["string", "number"]})),
        th.Property("sale_price", th.CustomType({"type": ["string", "number"]})),
        th.Property("date_on_sale_from", th.DateTimeType),
        th.Property("date_on_sale_to", th.DateTimeType),
        th.Property("price_html", th.StringType),
        th.Property("on_sale", th.BooleanType),
        th.Property("purchasable", th.BooleanType),
        th.Property("total_sales", th.CustomType({"type": ["string", "number"]})),
        th.Property("virtual", th.BooleanType),
        th.Property("downloadable", th.BooleanType),
        th.Property("downloads", th.CustomType({"type": ["object", "array"]})),
        th.Property("download_limit", th.IntegerType),
        th.Property("download_expiry", th.IntegerType),
        th.Property("external_url", th.StringType),
        th.Property("button_text", th.StringType),
        th.Property("tax_status", th.StringType),
        th.Property("tax_class", th.StringType),
        th.Property("manage_stock", th.BooleanType),
        th.Property("stock_quantity", th.NumberType),
        th.Property("stock_status", th.StringType),
        th.Property("backorders", th.StringType),
        th.Property("backorders_allowed", th.BooleanType),
        th.Property("backordered", th.BooleanType),
        th.Property("sold_individually", th.BooleanType),
        th.Property("weight", th.StringType),
        th.Property(
            "dimensions",
            th.ObjectType(
                th.Property("length", th.StringType),
                th.Property("width", th.StringType),
                th.Property("height", th.StringType),
            ),
        ),
        th.Property("shipping_required", th.BooleanType),
        th.Property("shipping_taxable", th.BooleanType),
        th.Property("shipping_class", th.StringType),
        th.Property("shipping_class_id", th.IntegerType),
        th.Property("reviews_allowed", th.BooleanType),
        th.Property("average_rating", th.StringType),
        th.Property("rating_count", th.IntegerType),
        th.Property("related_ids", th.ArrayType(th.IntegerType)),
        th.Property("upsell_ids", th.ArrayType(th.IntegerType)),
        th.Property("cross_sell_ids", th.CustomType({"type": ["object", "array"]})),
        th.Property("parent_id", th.IntegerType),
        th.Property("purchase_note", th.StringType),
        th.Property(
            "categories",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("slug", th.StringType),
                )
            ),
        ),
        th.Property(
            "tags",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("slug", th.StringType),
                )
            ),
        ),
        th.Property(
            "images",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("date_created", th.DateTimeType),
                    th.Property("date_modified", th.DateTimeType),
                    th.Property("src", th.StringType),
                    th.Property("name", th.StringType),
                    th.Property("alt", th.StringType),
                )
            ),
        ),
        th.Property(
            "attributes",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("position", th.IntegerType),
                    th.Property("visible", th.BooleanType),
                    th.Property("variation", th.BooleanType),
                    th.Property("options", th.ArrayType(th.StringType)),
                )
            ),
        ),
        th.Property(
            "default_attributes",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("option", th.StringType),
                )
            ),
        ),
        th.Property("variations", th.ArrayType(th.IntegerType)),
        th.Property("grouped_products", th.ArrayType(th.IntegerType)),
        th.Property("menu_order", th.IntegerType),
        th.Property(
            "meta_data",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("key", th.StringType),
                    th.Property("value", th.StringType),
                )
            ),
        ),
    ).to_dict()

    # def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
    #     """Return a context dictionary for child streams."""
    #     if record.get("type")=="variable":
    #         return {
    #             "product_id": record["id"],
    #         }

class ProductVariationsStream(wooStream):
    name = "product_variations"
    path = "/products/{product_id}/variations"
    primary_keys = ["id"]
    parent_stream_type = ProductsStream

    schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("date_created", th.DateTimeType),
    th.Property("date_created_gmt", th.DateTimeType),
    th.Property("date_modified", th.DateTimeType),
    th.Property("date_modified_gmt", th.DateTimeType),
    th.Property("description", th.StringType),
    th.Property("permalink", th.StringType),
    th.Property("sku", th.StringType),
    th.Property("price", th.CustomType({"type": ["string", "number"]})),
    th.Property("regular_price", th.CustomType({"type": ["string", "number"]})),
    th.Property("sale_price", th.CustomType({"type": ["string", "number"]})),
    th.Property("date_on_sale_from", th.DateTimeType),
    th.Property("date_on_sale_from_gmt", th.DateTimeType),
    th.Property("date_on_sale_to", th.DateTimeType),
    th.Property("date_on_sale_to_gmt", th.DateTimeType),
    th.Property("on_sale", th.BooleanType),
    th.Property("status", th.StringType),
    th.Property("purchasable", th.BooleanType),
    th.Property("virtual", th.BooleanType),
    th.Property("downloadable", th.BooleanType),
    th.Property("downloads", th.CustomType({"type": ["object", "array"]})),
    th.Property("download_limit", th.IntegerType),
    th.Property("download_expiry", th.IntegerType),
    th.Property("tax_status", th.StringType),
    th.Property("tax_class", th.StringType),
    th.Property("manage_stock", th.BooleanType),
    th.Property("stock_quantity", th.NumberType),
    th.Property("stock_status", th.StringType),
    th.Property("backorders", th.StringType),
    th.Property("backorders_allowed", th.BooleanType),
    th.Property("backordered", th.BooleanType),
    th.Property("weight", th.StringType),
    th.Property("dimensions", th.ObjectType(
      th.Property("length", th.StringType),
      th.Property("width", th.StringType),
      th.Property("height", th.StringType),
    )),
    th.Property("shipping_class", th.StringType),
    th.Property("shipping_class_id", th.IntegerType),
    th.Property("image", th.ObjectType(
      th.Property("id", th.IntegerType),
      th.Property("date_created", th.DateTimeType),
      th.Property("date_created_gmt", th.DateTimeType),
      th.Property("date_modified", th.DateTimeType),
      th.Property("date_modified_gmt", th.DateTimeType),
      th.Property("src", th.StringType),
      th.Property("name", th.StringType),
      th.Property("alt", th.StringType),
    )),
    th.Property("attributes", th.ArrayType(th.ObjectType(
       th.Property( "id", th.IntegerType),
       th.Property( "name", th.StringType),
       th.Property( "option", th.StringType),
      
    ))),
    th.Property("menu_order", th.IntegerType),
    th.Property("meta_data", th.ArrayType(th.CustomType({"type": ["object", "string"]}))),
    th.Property("_links", th.ObjectType(
      th.Property("self", th.ArrayType(th.ObjectType(
        
          th.Property("href", th.StringType),
        
      ))))),
      th.Property("collection", th.ArrayType(th.ObjectType(
          th.Property("href", th.StringType)
      ))),
            th.Property("up", th.ArrayType(th.ObjectType(
          th.Property("href", th.StringType)
      ))),
     
    
    ).to_dict()