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

# %% [markdown]
# # Tutorial configuration
#
# Run this cell to install the tools we will need in this tutorial

# %%
# !rm -rf snapearthapis
# !git clone https://github.com/chicham/snapearthapis.git
# !pip install -r snapearthapis/requirements.txt
!!add-apt-repository ppa:longsleep/golang-backports -y
# !apt-get update > /dev/null && apt-get -y install jq golang-go > /dev/null
# !go version
!!go install github.com/fullstorydev/grpcurl/cmd/grpcurl@latest
import os
os.environ['PATH'] += ":/root/go/bin"


# %% [markdown]
# # EarthSignature Tutorial
#
# ## Introduction
#
# EarthSignature is a database of land cover classification. Every day an Artificial Intelligence model performs land cover classification and save the result in this database. Currently the database is freely usable by everyone using the gRPC API.
# In this tutorial we will show you how to use the API to visualize the products processed by our model and to download the land cover classification and the associated cloud masks for a list of products.

# %% [markdown]
# ## Visualization of the products
#
# This steps will show you how to visualize the product in the database. You can get a list of the product in the database using the `ListProductIds` method of the service. It will return a list of `ProductId` and we will display this list using the `folium` library

# %% [markdown]
# ### Setup and configuration
#
# Import and constants definition for the visualization

# %%
import base64

import folium
from shapely import wkt
from shapely.geometry import mapping


EUROPE_COORDINATES = wkt.loads(
    "POLYGON((-10.61 71.16, 44.85 71.16, 44.85 35.97, -10.61 35.97, -10.61 71.16))",
)
MAP_CENTER = mapping(EUROPE_COORDINATES.centroid)
map_ = folium.Map(
    location=MAP_CENTER["coordinates"][::-1],
    zoom_start=4,
    crs="EPSG3857",
)


# %% [markdown]
# ### Plotting the products
#
# The following lines query the ListProductIds using the `grpcurl` tool and save the result in jsonlines format using `jq` in the variable `products`. We parse the json generated and put each product on the map.
#

# %%
import orjson as json
# lines = !grpcurl -insecure  -max-msg-sz 1073741824 earthsignature.snapearth.eu:443 snapearth.api.v1.database.DatabaseProductService.ListProductIds | jq -c -M
products = [json.loads(line) for line in lines]

for product in products:
    geom = wkt.loads(product['wkt'])
    folium.GeoJson(data=geom).add_to(map_)
    centroid = mapping(geom.centroid)
    folium.Marker(
            location=centroid["coordinates"][::-1],
            tooltip=f'{product["productId"]}',
        ).add_to(map_)

map_

# %% [markdown]
# ## Querying the API
#

# %% [markdown]
#   After visualizing where the product are you can download the products in the areas you are interested in.
#
# A example of query to the API is:
# ```
# grpcurl -max-msg-sz 1073741824 -d '{"n_results": 5, "start_date": "2021-01-01T00:00:00Z", "end_date": "2022-01-01T00:00:00Z", "wkt": "MULTIPOLYGON (((1.6415459999999999 48.6570210000000003, 2.5066069999999998 48.6616240000000033, 2.5143049999999998 48.6782680000000028, 2.5817120000000000 48.8229529999999983, 2.6498390000000001 48.9676520000000011, 2.7181340000000001 49.1124610000000033, 2.7869250000000001 49.2572189999999992, 2.8559869999999998 49.4018480000000011, 2.9250820000000002 49.5464559999999992, 2.9757820000000001 49.6517830000000018, 1.6142719999999999 49.6444299999999998, 1.6415459999999999 48.6570210000000003)))" }' earthsignature.snapearth.eu:443 snapearth.api.v1.database.DatabaseProductService.ListSegmentation > res.pbtxt
# ```
#
# Which request 5 results from the database between the January 1st 2021 and the January 1st 2022 over an area defined by wkt. The results are saved in the file res.pbtxt.
# To summarize here are the argument you can pass to grpcurl using the `-d` flag to select the products available:
# - `n_results`: the number of results to return
# - `start_date`: the start date of the results
# - `end_date`: the end date of the results
# - `wkt`: the polygon in WKT format of the area of interest
#
#
#

# %%
# We delete old results first
# !rm -rf api_results
# !mkdir api_results
# !grpcurl -max-msg-sz 1073741824 -d '{"n_results": 5, "start_date": "2021-01-01T00:00:00Z", "end_date": "2022-05-01T00:00:00Z"}' -insecure earthsignature.snapearth.eu:443 snapearth.api.v1.database.DatabaseProductService.ListSegmentation | jq -c -M '{productId: .productId, segmentation: .segmentation, cloudMask: .cloudMask}' > api_results/responses.jsonl

from pathlib import Path
import orjson as json
from base64 import b64decode
from google.colab import files


with Path('api_results/responses.jsonl').open('r') as src:
  for line in src:
    data = json.loads(line)
    product_id = data['productId']
    segmentation_data = b64decode(data['segmentation'])
    with open(f"api_results/{product_id}_segmentation.tiff", "wb") as dst:
      dst.write(segmentation_data)

    cloud_data = b64decode(data['cloudMask'])
    with open(f"api_results/{product_id}_cloud.tiff", "wb") as dst:
      dst.write(cloud_data)

# !rm api_results/responses.jsonl
# !zip -r results.zip api_results/*.tiff

files.download('results.zip')

# %% [markdown]
# When running the code above you get two kind of data.
# - A list of segmentation data which are the landcover classification for a product. We use the labels from the Corine Land Cover for the classification. Each pixel in the segmentation file contain the categorie assigned by the model to this pixel. The mapping between the categorie number and the real classes can be found here: https://land.copernicus.eu/user-corner/technical-library/corine-land-cover-nomenclature-guidelines/html . We use the level 3 of the Corine Land Cover so the class 111 is the continuous urban fabric, the class 112 discontinuous urban fabric etc.
# - The second data you get are the cloud files. The cloud file describe where in an image cloud were detected. If a pixel in the cloud image is set to 1, it means there was cloud at the corresponding position in the original image and the classification in the segmentation image for this position is not reliable.

# %%
