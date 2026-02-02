OPENAPI_SCHEMA = {
    "openapi": "3.0.3",
    "info": {
        "title": "Smart Agriculture API",
        "version": "1.0.0",
        "description": "OpenAPI schema for the Smart Agriculture backend.",
    },
    "paths": {
        "/": {
            "get": {
                "summary": "Service info",
                "responses": {
                    "200": {
                        "description": "Service status and endpoints",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/ServiceInfo"}
                            }
                        },
                    }
                },
            }
        },
        "/health/": {
            "get": {
                "summary": "Health check",
                "responses": {
                    "200": {
                        "description": "Service health",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Health"}
                            }
                        },
                    }
                },
            }
        },
        "/stats/": {
            "get": {
                "summary": "Record counts",
                "responses": {
                    "200": {
                        "description": "Counts for dashboard",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Stats"}
                            }
                        },
                    }
                },
            }
        },
        "/api/farmers/": {
            "get": {
                "summary": "List farmers",
                "responses": {
                    "200": {
                        "description": "Farmer list",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/Farmer"},
                                }
                            }
                        },
                    }
                },
            },
            "post": {
                "summary": "Create farmer",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/FarmerCreate"}
                        }
                    },
                },
                "responses": {
                    "201": {
                        "description": "Farmer created",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/FarmerCreateResponse"
                                }
                            }
                        },
                    }
                },
            },
        },
        "/api/farmers/{farmer_id}/": {
            "get": {
                "summary": "Get farmer",
                "parameters": [
                    {
                        "name": "farmer_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Farmer detail",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Farmer"}
                            }
                        },
                    }
                },
            },
            "put": {
                "summary": "Update farmer",
                "parameters": [
                    {
                        "name": "farmer_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/FarmerUpdate"}
                        }
                    },
                },
                "responses": {
                    "200": {
                        "description": "Farmer updated",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/FarmerUpdateResponse"}
                            }
                        },
                    }
                },
            },
            "delete": {
                "summary": "Delete farmer",
                "parameters": [
                    {
                        "name": "farmer_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Deletion result",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Success"}
                            }
                        },
                    }
                },
            },
        },
        "/api/records/soil/": {
            "get": {
                "summary": "List soil records",
                "responses": {
                    "200": {
                        "description": "Soil record list",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/SoilRecord"
                                    },
                                }
                            }
                        },
                    }
                },
            },
            "post": {
                "summary": "Create soil record",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/SoilRecordCreate"}
                        }
                    },
                },
                "responses": {
                    "201": {
                        "description": "Soil record created",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/RecordCreateResponse"
                                }
                            }
                        },
                    }
                },
            },
        },
        "/api/records/soil/{record_id}/": {
            "get": {
                "summary": "Get soil record",
                "parameters": [
                    {
                        "name": "record_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Soil record detail",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/SoilRecord"}
                            }
                        },
                    }
                },
            },
            "put": {
                "summary": "Update soil record",
                "parameters": [
                    {
                        "name": "record_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/SoilRecordUpdate"}
                        }
                    },
                },
                "responses": {
                    "200": {
                        "description": "Soil record updated",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/RecordCreateResponse"
                                }
                            }
                        },
                    }
                },
            },
            "delete": {
                "summary": "Delete soil record",
                "parameters": [
                    {
                        "name": "record_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Deletion result",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Success"}
                            }
                        },
                    }
                },
            },
        },
        "/api/records/water/": {
            "get": {
                "summary": "List water records",
                "responses": {
                    "200": {
                        "description": "Water record list",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/WaterRecord"
                                    },
                                }
                            }
                        },
                    }
                },
            },
            "post": {
                "summary": "Create water record",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/WaterRecordCreate"}
                        }
                    },
                },
                "responses": {
                    "201": {
                        "description": "Water record created",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/RecordCreateResponse"
                                }
                            }
                        },
                    }
                },
            },
        },
        "/api/records/water/{record_id}/": {
            "get": {
                "summary": "Get water record",
                "parameters": [
                    {
                        "name": "record_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Water record detail",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/WaterRecord"}
                            }
                        },
                    }
                },
            },
            "put": {
                "summary": "Update water record",
                "parameters": [
                    {
                        "name": "record_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/WaterRecordUpdate"}
                        }
                    },
                },
                "responses": {
                    "200": {
                        "description": "Water record updated",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/RecordCreateResponse"
                                }
                            }
                        },
                    }
                },
            },
            "delete": {
                "summary": "Delete water record",
                "parameters": [
                    {
                        "name": "record_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Deletion result",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Success"}
                            }
                        },
                    }
                },
            },
        },
        "/api/records/crop/": {
            "get": {
                "summary": "List crop records",
                "responses": {
                    "200": {
                        "description": "Crop record list",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/CropRecord"
                                    },
                                }
                            }
                        },
                    }
                },
            },
            "post": {
                "summary": "Create crop record",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/CropRecordCreate"}
                        }
                    },
                },
                "responses": {
                    "201": {
                        "description": "Crop record created",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/RecordCreateResponse"
                                }
                            }
                        },
                    }
                },
            },
        },
        "/api/records/crops/": {
            "get": {
                "summary": "List crop records (alias)",
                "responses": {
                    "200": {
                        "description": "Crop record list",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/CropRecord"
                                    },
                                }
                            }
                        },
                    }
                },
            },
            "post": {
                "summary": "Create crop record (alias)",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/CropRecordCreate"}
                        }
                    },
                },
                "responses": {
                    "201": {
                        "description": "Crop record created",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/RecordCreateResponse"
                                }
                            }
                        },
                    }
                },
            },
        },
        "/api/records/crop/{record_id}/": {
            "get": {
                "summary": "Get crop record",
                "parameters": [
                    {
                        "name": "record_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Crop record detail",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/CropRecord"}
                            }
                        },
                    }
                },
            },
            "put": {
                "summary": "Update crop record",
                "parameters": [
                    {
                        "name": "record_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/CropRecordUpdate"}
                        }
                    },
                },
                "responses": {
                    "200": {
                        "description": "Crop record updated",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/RecordCreateResponse"
                                }
                            }
                        },
                    }
                },
            },
            "delete": {
                "summary": "Delete crop record",
                "parameters": [
                    {
                        "name": "record_id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Deletion result",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Success"}
                            }
                        },
                    }
                },
            },
        },
        "/api/suggest/": {
            "post": {
                "summary": "Get AI suggestions",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/SuggestRequest"}
                        }
                    },
                },
                "responses": {
                    "200": {
                        "description": "Suggestion results",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/SuggestResponse"}
                            }
                        },
                    }
                },
            }
        },
    },
    "components": {
        "schemas": {
            "Health": {
                "type": "object",
                "properties": {
                    "status": {"type": "string"},
                    "time": {"type": "string"},
                },
            },
            "ServiceInfo": {
                "type": "object",
                "properties": {
                    "service": {"type": "string"},
                    "status": {"type": "string"},
                    "endpoints": {"type": "array", "items": {"type": "string"}},
                    "admin": {"type": "string"},
                },
            },
            "Stats": {
                "type": "object",
                "properties": {
                    "farmers": {"type": "integer"},
                    "crops": {"type": "integer"},
                    "soil": {"type": "integer"},
                    "water": {"type": "integer"},
                },
            },
            "Success": {
                "type": "object",
                "properties": {"success": {"type": "boolean"}},
            },
            "Farmer": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "phone": {"type": "string", "nullable": True},
                    "region": {"type": "string", "nullable": True},
                },
            },
            "FarmerCreate": {
                "type": "object",
                "required": ["name"],
                "properties": {
                    "name": {"type": "string"},
                    "phone": {"type": "string", "nullable": True},
                    "location": {"type": "string", "nullable": True},
                },
            },
            "FarmerUpdate": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "phone": {"type": "string", "nullable": True},
                    "region": {"type": "string", "nullable": True},
                },
            },
            "FarmerCreateResponse": {
                "type": "object",
                "properties": {"id": {"type": "integer"}, "name": {"type": "string"}},
            },
            "FarmerUpdateResponse": {
                "type": "object",
                "properties": {"id": {"type": "integer"}, "name": {"type": "string"}},
            },
            "RecordCreateResponse": {
                "type": "object",
                "properties": {"id": {"type": "integer"}},
            },
            "SoilRecord": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "farmer_id": {"type": "integer"},
                    "ph": {"type": "number", "nullable": True},
                    "nitrogen": {"type": "number", "nullable": True},
                    "phosphorus": {"type": "number", "nullable": True},
                    "potassium": {"type": "number", "nullable": True},
                    "date_recorded": {"type": "string"},
                },
            },
            "SoilRecordCreate": {
                "type": "object",
                "properties": {
                    "farmer_id": {"type": "integer"},
                    "ph": {"type": "number"},
                    "nitrogen": {"type": "number"},
                    "phosphorus": {"type": "number"},
                    "potassium": {"type": "number"},
                    "date_recorded": {"type": "string"},
                },
            },
            "SoilRecordUpdate": {
                "type": "object",
                "properties": {
                    "farmer_id": {"type": "integer"},
                    "ph": {"type": "number"},
                    "nitrogen": {"type": "number"},
                    "phosphorus": {"type": "number"},
                    "potassium": {"type": "number"},
                    "date_recorded": {"type": "string"},
                },
            },
            "WaterRecord": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "farmer_id": {"type": "integer"},
                    "ph": {"type": "number", "nullable": True},
                    "ec": {"type": "number", "nullable": True},
                    "tds": {"type": "number", "nullable": True},
                    "date_recorded": {"type": "string"},
                },
            },
            "WaterRecordCreate": {
                "type": "object",
                "properties": {
                    "farmer_id": {"type": "integer"},
                    "ph": {"type": "number"},
                    "ec": {"type": "number"},
                    "tds": {"type": "number"},
                    "date_recorded": {"type": "string"},
                },
            },
            "WaterRecordUpdate": {
                "type": "object",
                "properties": {
                    "farmer_id": {"type": "integer"},
                    "ph": {"type": "number"},
                    "ec": {"type": "number"},
                    "tds": {"type": "number"},
                    "date_recorded": {"type": "string"},
                },
            },
            "CropRecord": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "farmer_id": {"type": "integer"},
                    "crop_name": {"type": "string", "nullable": True},
                    "yield_kg": {"type": "number", "nullable": True},
                    "date_recorded": {"type": "string"},
                },
            },
            "CropRecordCreate": {
                "type": "object",
                "properties": {
                    "farmer_id": {"type": "integer"},
                    "crop_name": {"type": "string"},
                    "yield_kg": {"type": "number"},
                    "date_recorded": {"type": "string"},
                },
            },
            "CropRecordUpdate": {
                "type": "object",
                "properties": {
                    "farmer_id": {"type": "integer"},
                    "crop_name": {"type": "string"},
                    "yield_kg": {"type": "number"},
                    "date_recorded": {"type": "string"},
                },
            },
            "SuggestRequest": {"type": "object"},
            "SuggestResponse": {"type": "object"},
        }
    },
}
