
# beam and jq are required dependencies...
beam --version
jq --version

# generate the file, and move it to the right folder.
beam oapi download --output temp/oapi.json --combine-into-one-document
mv temp/oapi.json docs/assets/beamable-oapi.json
rm -rf temp/