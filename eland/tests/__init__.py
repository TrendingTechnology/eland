import os
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define test files and indices
ELASTICSEARCH_HOST = 'localhost' # TODO externalise this

FLIGHTS_INDEX_NAME = 'flights'
FLIGHTS_MAPPING = { "mappings" : {
      "properties" : {
        "AvgTicketPrice" : {
          "type" : "float"
        },
        "Cancelled" : {
          "type" : "boolean"
        },
        "Carrier" : {
          "type" : "keyword"
        },
        "Dest" : {
          "type" : "keyword"
        },
        "DestAirportID" : {
          "type" : "keyword"
        },
        "DestCityName" : {
          "type" : "keyword"
        },
        "DestCountry" : {
          "type" : "keyword"
        },
        "DestLocation" : {
          "type" : "geo_point"
        },
        "DestRegion" : {
          "type" : "keyword"
        },
        "DestWeather" : {
          "type" : "keyword"
        },
        "DistanceKilometers" : {
          "type" : "float"
        },
        "DistanceMiles" : {
          "type" : "float"
        },
        "FlightDelay" : {
          "type" : "boolean"
        },
        "FlightDelayMin" : {
          "type" : "integer"
        },
        "FlightDelayType" : {
          "type" : "keyword"
        },
        "FlightNum" : {
          "type" : "keyword"
        },
        "FlightTimeHour" : {
          "type" : "float"
        },
        "FlightTimeMin" : {
          "type" : "float"
        },
        "Origin" : {
          "type" : "keyword"
        },
        "OriginAirportID" : {
          "type" : "keyword"
        },
        "OriginCityName" : {
          "type" : "keyword"
        },
        "OriginCountry" : {
          "type" : "keyword"
        },
        "OriginLocation" : {
          "type" : "geo_point"
        },
        "OriginRegion" : {
          "type" : "keyword"
        },
        "OriginWeather" : {
          "type" : "keyword"
        },
        "dayOfWeek" : {
          "type" : "integer"
        },
        "timestamp" : {
          "type" : "date"
        }
      }
    } }
FLIGHTS_FILE_NAME = ROOT_DIR + '/flights.json.gz'
FLIGHTS_DF_FILE_NAME = ROOT_DIR + '/flights_df.json.gz'

ECOMMERCE_INDEX_NAME = 'ecommerce'
ECOMMERCE_MAPPING = { "mappings" : {
      "properties" : {
        "category" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword"
            }
          }
        },
        "currency" : {
          "type" : "keyword"
        },
        "customer_birth_date" : {
          "type" : "date"
        },
        "customer_first_name" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "customer_full_name" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "customer_gender" : {
          "type" : "keyword"
        },
        "customer_id" : {
          "type" : "keyword"
        },
        "customer_last_name" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "customer_phone" : {
          "type" : "keyword"
        },
        "day_of_week" : {
          "type" : "keyword"
        },
        "day_of_week_i" : {
          "type" : "integer"
        },
        "email" : {
          "type" : "keyword"
        },
        "geoip" : {
          "properties" : {
            "city_name" : {
              "type" : "keyword"
            },
            "continent_name" : {
              "type" : "keyword"
            },
            "country_iso_code" : {
              "type" : "keyword"
            },
            "location" : {
              "type" : "geo_point"
            },
            "region_name" : {
              "type" : "keyword"
            }
          }
        },
        "manufacturer" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword"
            }
          }
        },
        "order_date" : {
          "type" : "date"
        },
        "order_id" : {
          "type" : "keyword"
        },
        "products" : {
          "properties" : {
            "_id" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword",
                  "ignore_above" : 256
                }
              }
            },
            "base_price" : {
              "type" : "half_float"
            },
            "base_unit_price" : {
              "type" : "half_float"
            },
            "category" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword"
                }
              }
            },
            "created_on" : {
              "type" : "date"
            },
            "discount_amount" : {
              "type" : "half_float"
            },
            "discount_percentage" : {
              "type" : "half_float"
            },
            "manufacturer" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword"
                }
              }
            },
            "min_price" : {
              "type" : "half_float"
            },
            "price" : {
              "type" : "half_float"
            },
            "product_id" : {
              "type" : "long"
            },
            "product_name" : {
              "type" : "text",
              "fields" : {
                "keyword" : {
                  "type" : "keyword"
                }
              },
              "analyzer" : "english"
            },
            "quantity" : {
              "type" : "integer"
            },
            "sku" : {
              "type" : "keyword"
            },
            "tax_amount" : {
              "type" : "half_float"
            },
            "taxful_price" : {
              "type" : "half_float"
            },
            "taxless_price" : {
              "type" : "half_float"
            },
            "unit_discount_amount" : {
              "type" : "half_float"
            }
          }
        },
        "sku" : {
          "type" : "keyword"
        },
        "taxful_total_price" : {
          "type" : "half_float"
        },
        "taxless_total_price" : {
          "type" : "half_float"
        },
        "total_quantity" : {
          "type" : "integer"
        },
        "total_unique_products" : {
          "type" : "integer"
        },
        "type" : {
          "type" : "keyword"
        },
        "user" : {
          "type" : "keyword"
        }
      }
    } }
ECOMMERCE_FILE_NAME = ROOT_DIR + '/ecommerce.json.gz'
ECOMMERCE_DF_FILE_NAME = ROOT_DIR + '/ecommerce_df.json.gz'

TEST_MAPPING1 = {
      'mappings': {
        'properties': {
          'city': {
            'type': 'text',
            'fields': {
              'raw': {
                'type': 'keyword'
              }
            }
          },
          'text': {
            'type': 'text',
            'fields': {
              'english': {
                'type': 'text',
                'analyzer': 'english'
              }
            }
          },
          'origin_location': {
            'properties': {
              'lat': {
                'type': 'text',
                'index_prefixes': {},
                'fields': {
                  'keyword': {
                    'type': 'keyword',
                    'ignore_above': 256
                  }
                }
              },
              'lon': {
                'type': 'text',
                'fields': {
                  'keyword': {
                    'type': 'keyword',
                    'ignore_above': 256
                  }
                }
              }
            }
          },
          'maps-telemetry': {
            'properties': {
              'attributesPerMap': {
                'properties': {
                  'dataSourcesCount': {
                    'properties': {
                      'avg': {
                        'type': 'long'
                      },
                      'max': {
                        'type': 'long'
                      },
                      'min': {
                        'type': 'long'
                      }
                    }
                  },
                  'emsVectorLayersCount': {
                    'dynamic': 'true',
                    'properties': {
                      'france_departments': {
                        'properties': {
                          'avg': {
                            'type': 'float'
                          },
                          'max': {
                            'type': 'long'
                          },
                          'min': {
                            'type': 'long'
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          'type': {
            'type': 'keyword'
          },
          'name': {
            'type': 'text'
          },
          'user_name': {
            'type': 'keyword'
          },
          'email': {
            'type': 'keyword'
          },
          'content': {
            'type': 'text'
          },
          'tweeted_at': {
            'type': 'date'
          },
          'dest_location': {
            'type': 'geo_point'
          },
          'my_join_field': {
            'type': 'join',
            'relations': {
              'question': ['answer', 'comment'],
              'answer': 'vote'
            }
          }
        }
      }
    }

TEST_MAPPING1_INDEX_NAME = 'mapping1'

TEST_MAPPING1_EXPECTED = {
    'city': 'text',
    'city.raw': 'keyword',
    'content': 'text',
    'dest_location': 'geo_point',
    'email': 'keyword',
    'maps-telemetry.attributesPerMap.dataSourcesCount.avg': 'long',
    'maps-telemetry.attributesPerMap.dataSourcesCount.max': 'long',
    'maps-telemetry.attributesPerMap.dataSourcesCount.min': 'long',
    'maps-telemetry.attributesPerMap.emsVectorLayersCount.france_departments.avg': 'float',
    'maps-telemetry.attributesPerMap.emsVectorLayersCount.france_departments.max': 'long',
    'maps-telemetry.attributesPerMap.emsVectorLayersCount.france_departments.min': 'long',
    'my_join_field': 'join',
    'name': 'text',
    'origin_location.lat': 'text',
    'origin_location.lat.keyword': 'keyword',
    'origin_location.lon': 'text',
    'origin_location.lon.keyword': 'keyword',
    'text': 'text',
    'text.english': 'text',
    'tweeted_at': 'date',
    'type': 'keyword',
    'user_name': 'keyword'
}

TEST_MAPPING1_EXPECTED_DF = pd.DataFrame.from_dict(data=TEST_MAPPING1_EXPECTED, orient='index', columns=['es_dtype'])

TEST_NESTED_USER_GROUP_INDEX_NAME = 'nested_user_group'
TEST_NESTED_USER_GROUP_MAPPING = {
  'mappings': {
    'properties': {
      'group': {
        'type': 'keyword'
      },
      'user': {
        'properties': {
            'first': {
              'type': 'keyword'
            },
            'last': {
              'type': 'keyword'
            },
            'address' : {
              'type' : 'keyword'
            }
        }
      }
    }
}
}

TEST_NESTED_USER_GROUP_DOCS = [
{'_index':TEST_NESTED_USER_GROUP_INDEX_NAME,
'_source':
    {'group':'amsterdam','user':[
        {'first':'Manke','last':'Nelis','address':['Elandsgracht', 'Amsterdam']},
        {'first':'Johnny','last':'Jordaan','address':['Elandsstraat', 'Amsterdam']}]}},
{'_index':TEST_NESTED_USER_GROUP_INDEX_NAME,
'_source':
    {'group':'london','user':[
        {'first':'Alice','last':'Monkton'},
        {'first':'Jimmy','last':'White','address':['London']}]}},
{'_index':TEST_NESTED_USER_GROUP_INDEX_NAME,
'_source':{'group':'new york','user':[
    {'first':'Bill','last':'Jones'}]}}
]
