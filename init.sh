#!/bin/bash
#
# INIT SCRIPT FOR ORC-OS DOCS
# ===========================
#
# This script initializes a fresh database for creating a new documentation 
# version. It should be run before building the database.
#
# After running this, the FastAPI server and front end should be started
# in order to allow for creation of screenshots for the documentation.
# ===========================
set -e

# check if ORC_HOME is set, if not set it to a default value
echo "Running from $PWD"

: "${NEXTCLOUD_URL:?NEXTCLOUD_URL missing}"
: "${SAMPLE_DATA_SHARE_ID:?SAMPLE_DATA_SHARE_ID missing}"
: "${SAMPLE_DATA_PASSWORD:?SAMPLE_DATA_PASSWORD missing}"

export SAMPLE_DATA_URL="${NEXTCLOUD_URL}/public.php/dav/files/${SAMPLE_DATA_SHARE_ID}" # sample_data_orcos_docs.zip

if [[ ! -v ORC_HOME ]]
then
    echo "ORC_HOME is not set, setting it to default $HOME/.ORC-OS-docs"
    export ORC_HOME=$HOME/.ORC-OS-docs
fi
if [[ ! -v SAMPLE_DATA_URL ]]
then
    echo "SAMPLE_DATA_URL is not set, cannot execute, exiting..."
    exit 1
fi

echo "Retrieving sample data from $SAMPLE_DATA_URL"
curl \
  -s \
  -u "${SAMPLE_DATA_SHARE_ID}:${SAMPLE_DATA_PASSWORD}" \
  -H 'X-Requested-With: XMLHttpRequest' \
  -o sample_data.zip \
   "${SAMPLE_DATA_URL}" \

unzip -u sample_data.zip -d sample_data

# check if database file exists, if so, delete it.
dbase_file="$ORC_HOME/orc-os.db"
if [[ -f "$dbase_file" ]]; then
    echo "Deleting existing database file $dbase_file"
    rm "$dbase_file"
fi

# prepare a new database file with latest schemas
orc db migrate

# upload all videos
SAMPLE_DATA_DIR=$PWD/sample_data

VIDS=(
    "$SAMPLE_DATA_DIR/hommerich/20240718_155502.mp4"
    "$SAMPLE_DATA_DIR/hommerich/20241010_081717.mp4"
    "$SAMPLE_DATA_DIR/mazyopa/DKL_20250830_103024.mkv"
    "$SAMPLE_DATA_DIR/mazyopa/DKL_20251216_120000.mp4"
)
CAM_CONFIG1="$SAMPLE_DATA_DIR/hommerich/cam_config.json"
CAM_CONFIG2="$SAMPLE_DATA_DIR/mazyopa/cam_config.json"
RECIPE1="$SAMPLE_DATA_DIR/hommerich/recipe.json"
RECIPE2="$SAMPLE_DATA_DIR/mazyopa/recipe.json"
CROSS1="$SAMPLE_DATA_DIR/hommerich/cross_section.geojson"
CROSS2="$SAMPLE_DATA_DIR/mazyopa/cross_section.geojson"
CROSS2_WL="$SAMPLE_DATA_DIR/mazyopa/cross_section_wl.geojson"
RELAY_CONFIG="$SAMPLE_DATA_DIR/gpio-relays.json"

TIMES=(
    "20240718T155502Z"
    "20241010T081717Z"
    "20250830T103024Z"
    "20251216T120000Z"
)

for i in "${!VIDS[@]}"; do
  vid="${VIDS[i]}"
  time="${TIMES[i]}"

  if [[ ! -f $vid ]]; then
    echo "Video file $vid not found."
    exit 1
  fi

  orc video add $vid $time
done

# add the video configs
# hommerich config
orc video add-config --sample-video-id 1 --camera-config-file $CAM_CONFIG1 --recipe-file $RECIPE1 --cross-section-file $CROSS1 "Hommerich"
# mazyopa config
orc video add-config --sample-video-id 3 --camera-config-file $CAM_CONFIG2 --recipe-file $RECIPE2 --cross-section-file $CROSS2 --cross-section-wl-file $CROSS2_WL "Mazyopa bridge"

# add relay config
mkdir -p $ORC_HOME/services
orc service import --deploy ${RELAY_CONFIG}


