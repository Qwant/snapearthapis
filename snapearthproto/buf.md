# EarthSignature API specification

EarthSignature is a platform providing Machine Learning segmentation images following [Corine LandCover](https://fr.wikipedia.org/wiki/Corine_Land_Cover) for [Sentinel-2](https://www.esa.int/ESA_Multimedia/Missions/Sentinel-2/(result_type)/images) satellite images

## How to use

Download the docker image `docker pull fullstorydev/grpcurl` to get a simple grpc client on your computer.

The API is available at earthsignature.snapearth.eu

To get the list of all satellite images available with a segmentation
`docker run fullstorydev/grpcurl -insecure  -max-msg-sz 1073741824 earthsignature.snapearth.eu:443 snapearth.api.v2.DatabaseProductService.ListProductIds | jq '.segmentation.feature."values" | .[] | .jsonValue'`

### API V1 - Raster images 

To get one random satellite images with v1 api (raster images)
`docker run fullstorydev/grpcurl -insecure -d '{"n_results": 1}' -max-msg-sz 1073741824 earthsignature.snapearth.eu:443 snapearth.api.v1.DatabaseProductService.ListSegmentation | jq -r -M ".segmentation" | base64 --decode  > result.tiff`

There are more parameters that could be given such as `start_date`, `end_date` for temporal filtering
`docker run fullstorydev/grpcurl -insecure -d '{"n_results": 1, "start_date": "2021-07-23T00:00:00Z", "end_date": "2022-08-01T00:00:00Z"}' -max-msg-sz 1073741824 earthsignature.snapearth.eu:443 snapearth.api.v1.DatabaseProductService.ListSegmentation | jq -r -M ".segmentation" | base64 --decode  > result_temporal_filtering.tiff`

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


