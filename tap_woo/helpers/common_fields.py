from singer_sdk import typing as th  # JSON Schema typing helpers

METADATA_FIELD_SCHEMA = th.Property(
    "meta_data",
    th.ArrayType(
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("key", th.StringType),
            th.Property(
                "value", th.CustomType({"type": ["string", "array", "object"]})
            ),
            # th.Property("display_key", th.StringType),
            # th.Property("display_value", th.JSONPointerType),
        )
    ),
)


BILLING_FIELD_SCHEMA = th.Property(
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
)


SHIPPING_FIELD_SCHEMA = th.Property(
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
        th.Property("phone", th.StringType),
    ),
)

SHIPPING_LINES_FIELD_SCHEMA = th.Property(
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
)

TAXES_ARRAY_TYPE = th.ArrayType(
    th.ObjectType(
        th.Property("id", th.IntegerType),
        th.Property("rate_code", th.StringType),
        th.Property("rate_id", th.IntegerType),
        th.Property("label", th.StringType),
        th.Property("compound", th.BooleanType),
        th.Property("tax_total", th.StringType),
        th.Property("shipping_tax_total", th.StringType),
    )
)


TAXES_FIELD_SCHEMA = th.Property(
    "taxes",
    TAXES_ARRAY_TYPE,
)


FEE_LINES_FIELD_SCHEMA = th.Property(
    "fee_lines",
    th.ArrayType(
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
            th.Property("tax_class", th.StringType),
            th.Property("tax_status", th.StringType),
            th.Property("total", th.StringType),
            th.Property("total_tax", th.StringType),
            TAXES_FIELD_SCHEMA,
        )
    ),
)


TAX_LINES_FIELD_SCHEMA = th.Property(
    "tax_lines",
    TAXES_ARRAY_TYPE,
)


LINE_ITEMS_FIELD_SCHEMA = th.Property(
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
            TAXES_FIELD_SCHEMA,
            METADATA_FIELD_SCHEMA,
            th.Property("sku", th.BooleanType),
            th.Property("price", th.NumberType),
            th.Property(
                "image",
                th.ObjectType(
                    th.Property("id", th.StringType), th.Property("src", th.StringType)
                ),
            ),
            th.Property("parent_name", th.StringType),
        )
    ),
)

LINKS_FIELD_SCHEMA = th.Property(
    "_links",
    th.ObjectType(
        th.Property(
            "self", th.ArrayType(th.ObjectType(th.Property("href", th.StringType)))
        ),
        th.Property(
            "collection",
            th.ArrayType(th.ObjectType(th.Property("href", th.StringType))),
        ),
        th.Property(
            "up", th.ArrayType(th.ObjectType(th.Property("href", th.StringType)))
        ),
        th.Property(
            "customer", th.ArrayType(th.ObjectType(th.Property("href", th.StringType)))
        ),
    ),
)
