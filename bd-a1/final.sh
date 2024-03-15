
CONTAINER_NAME="team"

DESTINATION_DIR="bd-a1/service-result"

mkdir -p "${DESTINATION_DIR}"


docker cp "${CONTAINER_NAME}:/home/doc-bd-a1/eda-in-1.txt" "${DESTINATION_DIR}/"
docker cp "${CONTAINER_NAME}:/home/doc-bd-a1/k.txt" "${DESTINATION_DIR}/"
docker cp "${CONTAINER_NAME}:/home/doc-bd-a1/vis.png" "${DESTINATION_DIR}/"
docker cp "${CONTAINER_NAME}:/home/doc-bd-a1/res_dpre.csv" "${DESTINATION_DIR}/"


docker stop "${CONTAINER_NAME}"
