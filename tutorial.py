# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

!rm -rf snapearthapis
!git clone https://github.com/chicham/snapearthapis.git
!pip install -r snapearthapis/requirements.txt

# %% [markdown]
# # EarthSignature Tutorial
#
# ## Introduction
#
# The goal of this notebook is to show how to use the EarthSignature API to download segmented Sentinel2 products. At the end of this tutorial, you will be able to query the API, understand how to filter the results when querying the API and understand what are the data returned by the API.
#
#
# ## Visualize the products available

# %%
import sys

sys.path.append("snapearthapis/gen/python/")

import base64

import folium
from shapely import wkt
from shapely.geometry import mapping
from grpclib.client import Channel
from grpclib.config import Configuration
from snapearth.api.v1.database_grpc import DatabaseProductServiceStub
from snapearth.api.v1.database_pb2 import ListProductIdsRequest
import nest_asyncio
import asyncio

nest_asyncio.apply()


EUROPE_COORDINATES = wkt.loads(
    "POLYGON((-10.61 71.16, 44.85 71.16, 44.85 35.97, -10.61 35.97, -10.61 71.16))",
)
MAP_CENTER = mapping(EUROPE_COORDINATES.centroid)
GRPC_CONFIGURATION = Configuration(
        http2_connection_window_size=2**30,
        http2_stream_window_size=2**30,
)

# %%

# host = "earthsignature.snapearth.eu:443"
host = "10.110.3.49:50051"
ssl = False

map_ = folium.Map(
    location=MAP_CENTER["coordinates"][::-1],
    zoom_start=4,
    crs="EPSG3857",
)

async def get_responses(host, ssl):
    async with Channel(host, ssl=ssl, configuration=GRPC_CONFIGURATION) as channel:
        print(channel)


    stub = DatabaseProductServiceStub(channel)
    request = ListProductIdsRequest()
    responses = stub.ListProductIds(request)
    for response in responses:
        geom = wkt.loads(response.wkt)
        folium.GeoJson(geom).add_to(map_)
        location = mapping(geom.centroid)["coordinates"][::-1]
        folium.Marker(tooltip=f"{response.product_id}", location=location).add_to(
            map_,
        )
map_ = asyncio.run(get_responses(host, ssl))

# %% [markdown]
# ## Query the API
#
# drive.mount("/content/drive")
#
# with grpc.insecure_channel(f"{host}", options) as channel:
#     stub = database_pb2_grpc.DatabaseProductServiceStub(channel)
#     request = database_pb2.ListSegmentationRequest()
#     responses = stub.ListSegmentationRequest(request)
#     # Write one directory per product
#     # Write cloud_mask and segmentation
