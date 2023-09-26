## Booking Webhook Schema:
  
  {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
      "booking": {
        "$ref": "#/definitions/booking"
      }
    },
    "required": ["booking"],
    "additionalProperties": false,
  
    "definitions": {
      "availability": {
        "type": "object",
        "properties": {
          "pk": {
            "type": "number"
          },
          "start_at": {
            "type": "string"
          },
          "end_at": {
            "type": "string"
          },
          "capacity": {
            "type": "number"
          },
          "minimum_party_size": {
            "type": ["number", "null"]
          },
          "maximum_party_size": {
            "type": ["number", "null"]
          },
          "headline": {
            "type": "string"
          },
          "item": {
            "$ref": "#/definitions/item"
          },
          "customer_type_rates": {
            "type": "array",
            "items": {
              "$ref": "#/definitions/customer_type_rate"
            }
          },
          "custom_field_instances": {
            "type": "array",
            "items": {
              "$ref": "#/definitions/custom_field_instance"
            }
          }
        },
        "required": [
          "pk",
          "start_at",
          "end_at",
          "capacity",
          "minimum_party_size",
          "maximum_party_size",
          "headline",
          "item",
          "customer_type_rates",
          "custom_field_instances"
        ],
        "additionalProperties": false
      },
  
      "booking": {
        "type": "object",
        "properties": {
          "pk": {
            "type": "number"
          },
          "uuid": {
            "type": "string"
          },
          "availability": {
            "$ref": "#/definitions/availability"
          },
          "company": {
            "$ref": "#/definitions/company"
          },
          "affiliate_company": {
            "$ref": "#/definitions/affiliate_company"
          },
          "contact": {
            "$ref": "#/definitions/contact"
          },
          "customers": {
            "type": "array",
            "items": {
              "$ref": "#/definitions/customer"
            }
          },
          "invoice_price": {
            "type": ["number", "null"]
          },
          "invoice_price_display": {
            "type": ["string", "null"]
          },
          "display_id": {
            "type": "string"
          },
          "external_id": {
            "type": "string"
          },
          "order": {
            "oneOf": [
              {
                "type": "null"
              },
              {
                "type": "object",
                "properties": {
                  "display_id": {
                    "type": "string"
                  }
                }
              }
            ]
          },
          "status": {
            "type": "string",
            "enum": ["booked", "cancelled", "rebooked"]
          },
          "rebooked_from": {
            "type": ["string", "null"]
          },
          "rebooked_to": {
            "type": ["string", "null"]
          },
          "confirmation_url": {
            "type": "string"
          },
          "receipt_subtotal": {
            "type": ["number", "null"]
          },
          "receipt_subtotal_display": {
            "type": ["string", "null"]
          },
          "receipt_taxes": {
            "type": ["number", "null"]
          },
          "receipt_taxes_display": {
            "type": ["string", "null"]
          },
          "receipt_total": {
            "type": ["number", "null"]
          },
          "receipt_total_display": {
            "type": ["string", "null"]
          },
          "amount_paid": {
            "type": ["number", "null"]
          },
          "amount_paid_display": {
            "type": ["string", "null"]
          },
          "voucher_number": {
            "type": "string"
          },
          "custom_field_values": {
            "type": "array",
            "items": {
              "$ref": "#/definitions/custom_field_value"
            }
          },
          "note": {
            "type": "string"
          },
          "note_safe_html": {
            "type": "string"
          },
          "pickup": {
            "$ref": "#/definitions/pickup"
          },
          "arrival": {
            "$ref": "#/definitions/arrival"
          },
          "effective_cancellation_policy": {
            "$ref": "#/definitions/effective_cancellation_policy"
          },
          "is_eligible_for_cancellation": {
            "type": "boolean"
          },
          "agent": {
            "$ref": "#/definitions/agent"
          },
          "desk": {
            "$ref": "#/definitions/desk"
          },
          "dashboard_url": {
            "type": "string"
          },
          "external_api_url": {
            "type": "string"
          },
          "customer_count": {
            "type": "number"
          },
          "is_subscribed_for_sms_updates": {
            "type": "boolean"
          }
        },
        "required": [
          "pk",
          "uuid",
          "availability",
          "contact",
          "company",
          "affiliate_company",
          "customers",
          "invoice_price",
          "invoice_price_display",
          "display_id",
          "external_id",
          "order",
          "status",
          "rebooked_from",
          "rebooked_to",
          "confirmation_url",
          "voucher_number",
          "receipt_subtotal",
          "receipt_subtotal_display",
          "receipt_taxes",
          "receipt_taxes_display",
          "receipt_total",
          "receipt_total_display",
          "amount_paid",
          "amount_paid_display",
          "custom_field_values",
          "note",
          "note_safe_html",
          "pickup",
          "arrival",
          "effective_cancellation_policy",
          "is_eligible_for_cancellation",
          "agent",
          "desk",
          "dashboard_url",
          "customer_count",
          "is_subscribed_for_sms_updates"
        ],
        "additionalProperties": false
      },
  
      "company": {
        "type": "object",
        "properties": {
          "shortname": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "currency": {
            "type": "string"
          }
        },
        "required": [
          "shortname",
          "name",
          "currency"
        ],
        "additionalProperties": false
      },
  
      "affiliate_company": {
        "oneOf": [
          {
            "type": "null"
          },
          {
            "type": "object",
            "properties": {
              "shortname": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "currency": {
                "type": "string"
              }
            },
            "required": [
              "shortname",
              "name",
              "currency"
            ],
            "additionalProperties": false
          }
        ]
      },
  
      "contact": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "phone": {
            "type": "string"
          },
          "phone_country": {
            "type": ["string", "null"]
          },
          "normalized_phone": {
            "type": "string"
          },
          "language": {
            "type": "string"
          },
          "email": {
            "type": "string"
          },
          "is_subscribed_for_email_updates": {
            "type": "boolean"
          }
        },
        "required": ["name", "phone", "phone_country", "normalized_phone", "email", "is_subscribed_for_email_updates"],
        "additionalProperties": false
      },
  
      "customer": {
        "type": "object",
        "properties": {
          "pk": {
            "type": "number"
          },
          "checkin_url": {
            "type": "string"
          },
          "checkin_status": {
            "oneOf": [
              {
                "type": "null"
              },
              {
                "$ref": "#/definitions/checkin_status"
              }
            ]
          },
          "invoice_cost": {
            "oneOf": [
              {
                "type": "null"
              },
              {
                "type": "object",
                "properties": {
                  "feeable": {
                    "type": "number"
                  },
                  "price": {
                    "type": ["number", "null"]
                  },
                  "tax": {
                    "type": "number"
                  },
                  "tax_by_type": {
                    "type": "object"
                  },
                  "taxable": {
                    "type": "number"
                  },
                  "total": {
                    "type": "number"
                  }
                }
              }
            ]
          },
          "total_cost": {
            "oneOf": [
              {
                "type": "null"
              },
              {
                "type": "object",
                "properties": {
                  "feeable": {
                    "type": "number"
                  },
                  "price": {
                    "type": ["number", "null"]
                  },
                  "tax": {
                    "type": "number"
                  },
                  "tax_by_type": {
                    "type": "object"
                  },
                  "taxable": {
                    "type": "number"
                  },
                  "total": {
                    "type": "number"
                  }
                }
              }
            ]
          },
          "customer_type_rate": {
            "$ref": "#/definitions/customer_type_rate"
          },
          "custom_field_values": {
            "type": "array",
            "items": {
              "$ref": "#/definitions/custom_field_value"
            }
          }
        },
        "required": ["pk", "checkin_url", "customer_type_rate", "custom_field_values"],
        "additionalProperties": false
      },
  
      "checkin_status": {
        "type": "object",
        "properties": {
          "pk": {
            "type": "number"
          },
          "name": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "required": ["pk", "name", "type"],
        "additionalProperties": false
      },
  
      "customer_type": {
        "type": "object",
        "properties": {
          "pk": {
            "type": "number"
          },
          "singular": {
            "type": "string"
          },
          "plural": {
            "type": "string"
          },
          "note": {
            "type": "string"
          }
        },
        "required": ["pk", "singular", "plural"],
        "additionalProperties": false
      },
  
      "customer_prototype": {
        "type": "object",
        "properties": {
          "pk": {
            "type": "number"
          },
          "display_name": {
            "type": "string"
          },
          "note": {
            "type": "string"
          },
          "total": {
            "type": "number"
          },
          "total_including_tax": {
            "type": "number"
          }
        },
        "required": ["pk", "display_name", "note", "total"],
        "additionalProperties": false
      },
  
      "customer_type_rate": {
        "type": "object",
        "properties": {
          "pk": {
            "type": "number"
          },
          "total": {
            "type": "number"
          },
          "total_including_tax": {
            "type": "number"
          },
          "capacity": {
            "type": ["number", "null"]
          },
          "minimum_party_size": {
            "type": ["number", "null"]
          },
          "maximum_party_size": {
            "type": ["number", "null"]
          },
          "customer_type": {
            "$ref": "#/definitions/customer_type"
          },
          "customer_prototype": {
            "$ref": "#/definitions/customer_prototype"
          },
          "custom_field_instances": {
            "type": "array",
            "items": {
              "$ref": "#/definitions/custom_field_instance"
            }
          }
        },
        "required": [
          "pk",
          "total",
          "capacity",
          "minimum_party_size",
          "maximum_party_size",
          "customer_type",
          "customer_prototype"
        ],
        "additionalProperties": false
      },
  
      "custom_field": {
        "type": "object",
        "properties": {
          "pk": {
            "type": "number"
          },
          "type": {
            "type": "string",
            "enum": ["yes-no", "short", "long", "extended-option", "count", "multi-campaign"]
          },
          "is_required": {
            "type": "boolean"
          },
          "description": {
            "type": "string"
          },
          "description_safe_html": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "booking_notes": {
            "type": "string"
          },
          "booking_notes_safe_html": {
            "type": "string"
          },
          "modifier_kind": {
            "type": "string"
          },
          "modifier_type": {
            "type": "string"
          },
          "offset": {
            "type": "number"
          },
          "percentage": {
            "type": "number"
          },
          "is_always_per_customer": {
            "type": "boolean"
          },
          "is_taxable": {
            "type": "boolean"
          },
          "extended_options": {
            "type": "array",
            "items": {
              "$ref": "#/definitions/extended_option"
            }
          }
        },
        "required": [
          "pk",
          "type",
          "is_required",
          "description",
          "description_safe_html",
          "name",
          "booking_notes",
          "booking_notes_safe_html",
          "offset"
        ],
        "additionalProperties": false
      },
  
      "custom_field_instance": {
        "type": "object",
        "properties": {
          "pk": {
            "type": "number"
          },
          "custom_field": {
            "$ref": "#/definitions/custom_field"
          }
        },
        "required": ["pk", "custom_field"],
        "additionalProperties": false
      },
  
      "custom_field_value": {
        "type": "object",
        "properties": {
          "pk": {
            "type": "number"
          },
          "custom_field": {
            "$ref": "#/definitions/custom_field"
          },
          "name": {
            "type": "string"
          },
          "value": {
            "type": "string",
            "maxLength": 2048
          },
          "display_value": {
            "type": "string",
            "maxLength": 2048
          }
        },
        "required": ["pk", "custom_field", "name", "value", "display_value"],
        "additionalProperties": false
      },
  
      "extended_option": {
        "type": "object",
        "properties": {
          "pk": {
            "type": "number"
          },
          "name": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "description_safe_html": {
            "type": "string"
          },
          "modifier_kind": {
            "type": "string"
          },
          "modifier_type": {
            "type": "string"
          },
          "offset": {
            "type": "number"
          },
          "percentage": {
            "type": "number"
          },
          "is_always_per_customer": {
            "type": "boolean"
          },
          "is_taxable": {
            "type": "boolean"
          }
        },
        "required": [
          "pk",
          "name",
          "description",
          "description_safe_html",
          "modifier_kind",
          "modifier_type",
          "offset",
          "percentage",
          "is_always_per_customer",
          "is_taxable"
        ],
        "additionalProperties": false
      },
  
      "item": {
        "type": "object",
        "properties": {
          "pk": {
            "type": "number"
          },
          "name": {
            "type": "string"
          }
        },
        "required": ["pk", "name"],
        "additionalProperties": false
      },
  
      "pickup": {
        "oneOf": [
          {
            "type": "null"
          },
          {
            "type": "object",
            "properties": {
              "time": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "description": {
                "type": "string"
              },
              "description_safe_html": {
                "type": "string"
              },
              "map_url": {
                "type": "string"
              },
              "display_text": {
                "type": "string"
              }
            },
            "required": [
              "time",
              "name",
              "description",
              "description_safe_html",
              "map_url",
              "display_text"
            ],
            "additionalProperties": false
          }
        ]
      },
  
      "arrival": {
        "oneOf": [
          {
            "type": "null"
          },
          {
            "type": "object",
            "properties": {
              "time": {
                "type": "string"
              },
              "notes": {
                "type": "string"
              },
              "notes_safe_html": {
                "type": "string"
              },
              "display_text": {
                "type": "string"
              }
            },
            "required": [
              "time",
              "notes",
              "notes_safe_html",
              "display_text"
            ],
            "additionalProperties": false
          }
        ]
      },
  
      "effective_cancellation_policy": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string"
          },
          "cutoff": {
            "oneOf": [
              {
                "type": "string"
              },
              {
                "type": "null"
              }
            ]
          }
        },
        "required": [
          "type",
          "cutoff"
        ],
        "additionalProperties": false
      },
  
      "agent": {
        "oneOf": [
          {
            "type": "null"
          },
          {
            "type": "object",
            "properties": {
              "pk": {
                "type": "number"
              },
              "name": {
                "type": "string"
              }
            },
            "required": [
              "pk",
              "name"
            ],
            "additionalProperties": false
          }
        ]
      },
  
      "desk": {
        "oneOf": [
          {
            "type": "null"
          },
          {
            "type": "object",
            "properties": {
              "pk": {
                "type": "number"
              },
              "name": {
                "type": "string"
              }
            },
            "required": [
              "pk",
              "name"
            ],
            "additionalProperties": false
          }
        ]
      }
    }
  }
