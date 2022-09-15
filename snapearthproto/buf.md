# EarthSignature API specification Guidelines

EarthSignature is a platform providing Machine Learning segmentation images following [Corine LandCover](https://fr.wikipedia.org/wiki/Corine_Land_Cover) for [Sentinel-2](https://www.esa.int/ESA_Multimedia/Missions/Sentinel-2/(result_type)/images) satellite images

## How to use on *Windows*

- Download grpcurl client for windows : https://repology.org/project/grpcurl/information AND jq 1.6 : https://stedolan.github.io/jq/download/

- Extract the zip folder in your Download location folder and move the grpcurl executable inside the folder in the Desktop. Do the same thing for jq-win64.exe

- Open the Command prompt from windows searchbar : https://www.makeuseof.com/tag/a-beginners-guide-to-the-windows-command-line/

- Go to the Desktop folder with the command `cd Desktop`

- Write the command `grpcurl -insecure -d "{\"n_results\": 1, \"start_date\": \"2022-09-10T00:00:00Z\"}" -max-msg-sz 1073741824 earthsignature.snapearth.eu:443 snapearth.api.v1.DatabaseProductService.ListSegmentation | jq-win64.exe -r -M ".segmentation" > satellite_segmentation.tiff` (With command prompt, always use \" before each parameter)

- Write the command `certutil -decode  satellite_segmentation.tiff satellite_segmentation_final.tiff`

In order to visualize the segmentation images, open it satellite_segmentation_final.tiff with a software like QGIS.

## How to use on *Linux & Mac*

Download the docker image `docker pull fullstorydev/grpcurl` to get a simple grpc client on your computer.

The API is available at earthsignature.snapearth.eu

To get the list of all satellite images available with a segmentation
`docker run fullstorydev/grpcurl -insecure  -max-msg-sz 1073741824 earthsignature.snapearth.eu:443 snapearth.api.v2.DatabaseProductService.ListProductIds | jq '.segmentation.feature."values" | .[] | .jsonValue'`

### API V1 - Raster images 

There are more parameters that could be given such as `start_date`, `end_date` for temporal filtering
`docker run fullstorydev/grpcurl -insecure -d '{"n_results": 1, "start_date": "2022-09-10T00:00:00Z", "end_date": "2022-08-01T00:00:00Z"}' -max-msg-sz 1073741824 earthsignature.snapearth.eu:443 snapearth.api.v1.DatabaseProductService.ListSegmentation | jq -r -M ".segmentation" | base64 --decode  > result_temporal_filtering.tiff`

Or `wkt` for spatial filtering : it filters satellite images within the polygon geometry specified
`docker run fullstorydev/grpcurl -insecure -d '{"n_results": 1, "wkt": "GEOMETRYCOLLECTION(POLYGON ((7.392425537109376 51.493568479510415, 7.541427612304687 51.493568479510415, 7.541427612304687 51.53330931285069, 7.392425537109376 51.53330931285069, 7.392425537109376 51.493568479510415)))"}' -max-msg-sz 1073741824 earthsignature.snapearth.eu:443 snapearth.api.v1.DatabaseProductService.ListSegmentation | jq -r -M ".segmentation" | base64 --decode  > result_berlin.tiff`

And `productId` to directly download the segmentation of a specific Sentinel-2 images with it's identifier
`docker run fullstorydev/grpcurl -insecure -d '{"n_results": 1, "productIds": "S2B_MSIL1C_20220822T112119_N0400_R037_T30TUN_20220822T121026"}' -max-msg-sz 1073741824 earthsignature.snapearth.eu:443 snapearth.api.v1.DatabaseProductService.ListSegmentation | jq -r -M ".segmentation" | base64 --decode  > result_berlin.tiff`

### API V2 - Geojson images
The v2 API has been created because raster is a heavy format. Geojson format is lighter

Parameters are the same but the API response is different

To get one random satellite images with v2
`docker run fullstorydev/grpcurl -insecure -d '{"n_results": 1}' -max-msg-sz 1073741824 earthsignature.snapearth.eu:443 snapearth.api.v2.DatabaseProductService.ListSegmentation | jq -r -M`

There is two possibilities to get the final Geojson :
- Implement a custom client to convert geobuf data format to geojson
- Use `geobuf2json` from [mapbox geobuf](https://github.com/mapbox/geobuf) directly from the protobuf format. The issue with `grpcurl` is that the output is directly transform in JSON.


